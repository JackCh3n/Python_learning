import re
str = '''<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="thunder://QUFmdHA6Ly95Z2R5ODp5Z2R5OEB5ZzQ1LmR5ZHl0dC5uZXQ6ODQ2OS8lRTklOTglQjMlRTUlODUlODklRTclOTQlQjUlRTUlQkQlQjF3d3cueWdkeTguY29tLiVFNiU4MSVCNiVFNCVCQSVCQSVFNCVCQyVBMC5CRC43MjBwLiVFOSU5RiVBOSVFOCVBRiVBRCVFNCVCOCVBRCVFNSVBRCU5Ny5ta3ZaWg==" target="_self" thunderpid="" thundertype="" thunderrestitle="ftp://ygdy8:ygdy8@yg45.dydytt.net:8469/阳光电影www.ygdy8.com.恶人传.BD.720p.韩语中字.mkv" onclick="return OnDownloadClick_Simple(this,2);" oncontextmenu="ThunderNetwork_SetHref(this)" zyrjhqkt="thunder://QUFmdHA6Ly95Z2R5ODp5Z2R5OEB5ZzQ1LmR5ZHl0dC5uZXQ6ODQ2OS8lRTklOTglQjMlRTUlODUlODklRTclOTQlQjUlRTUlQkQlQjF3d3cueWdkeTguY29tLiVFNiU4MSVCNiVFNCVCQSVCQSVFNCVCQyVBMC5CRC43MjBwLiVFOSU5RiVBOSVFOCVBRiVBRCVFNCVCOCVBRCVFNSVBRCU5Ny5ta3ZaWg==">ftp://ygdy8:ygdy8@yg45.dydytt.net:8469/阳光电影www.ygdy8.com.恶人传.BD.720p.韩语中字.mkv</a></td>'''

pattern = re.compile(r'ftp+://[^s]*(avi|mpeg|rmvb|mp4|mov|flv|wmv|mkv)')
url = pattern.search(str)
print(url.group(0))