<?php

/**
 * 获取客户端IP地址
 * @param integer $type 返回类型 0 返回IP地址 1 返回IPV4地址数字
 * @param boolean $adv 是否进行高级模式获取（有可能被伪装） 
 * @return mixed
 */
function get_client_ip($type = 0) {
    $type       =  $type ? 1 : 0;
    static $ip  =   NULL;
    if ($ip !== NULL) return $ip[$type];
    # nginx 代理模式下，获取客户端真实IP
    if($_SERVER['HTTP_X_REAL_IP']){
        $ip=$_SERVER['HTTP_X_REAL_IP'];     
    # 客户端的ip
    }elseif (isset($_SERVER['HTTP_CLIENT_IP'])) {
        $ip     =   $_SERVER['HTTP_CLIENT_IP'];
    # 浏览当前页面的用户计算机的网关
    }elseif (isset($_SERVER['HTTP_X_FORWARDED_FOR'])) {
        $arr    =   explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
        $pos    =   array_search('unknown',$arr);
        if(false !== $pos) unset($arr[$pos]);
        $ip     =   trim($arr[0]);
    }elseif (isset($_SERVER['REMOTE_ADDR'])) {
    # 浏览当前页面的用户计算机的ip地址
        $ip     =   $_SERVER['REMOTE_ADDR'];
    }else{
        $ip=$_SERVER['REMOTE_ADDR'];
    }
    # IP地址合法验证
    $long = sprintf("%u",ip2long($ip));
    $ip   = $long ? array($ip, $long) : array('0.0.0.0', 0);
    return $ip[$type];
}


/**
 * 获取客户端UA
 * @return [String] [客户端UA]
 */
function get_client_ua()
{
    return empty(filter_input(INPUT_SERVER, 'HTTP_USER_AGENT'))?filter_var($_SERVER['HTTP_USER_AGENT']):filter_input(INPUT_SERVER, 'HTTP_USER_AGENT');
}


if (isset($_GET['user'])) {
    if ($_GET['user']=='nobige') {
        # 没有缓存目录便创建
        if (!file_exists(__DIR__.DIRECTORY_SEPARATOR.'history'.DIRECTORY_SEPARATOR)) {
            mkdir(__DIR__.DIRECTORY_SEPARATOR.'history');
        }
        # 缓存文件ID
        $id = filter_var($_GET['id'], FILTER_VALIDATE_INT);
        # 缓存文件路径
        $file_path = __DIR__.DIRECTORY_SEPARATOR.'history'.DIRECTORY_SEPARATOR.$id;
        # 记录用户的信息
        $data_str = date('Y-m-d H:i:s|').get_client_ip().'|'.get_client_ua().PHP_EOL;
        if (file_exists($file_path)) {
            file_put_contents($file_path, $data_str,FILE_APPEND);
            exit('1');
        }else{
            file_put_contents($file_path, $data_str);
            exit('0');
        }
    }else{
        exit('403');
    }
}else{
    exit('404');
}