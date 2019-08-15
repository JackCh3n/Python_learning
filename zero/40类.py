class Student(object):
    """self相当于This"""
    def __init__(self, n='', a='', w=''):
        self.n = n
        self.a = a
        self.w = w
    '''一般方法都是要夹带self'''

    def speak(self):
        print(f'my name is {self.n} now age is {self.a} with is {self.w}')

    def t(self, q, w):
        print(q+'----'+w)


class StudentMin(Student):
    """类的继承"""
    def player(self):
        print('player games')
    '''方法的重写'''
    def speak(self):
        print('I am a pupil, the world is invincible')


class Skill(object):
    """docstring for ClassName"""
    def consumption(self, matter):
        print('buy the %s' % (matter))


class Baby(StudentMin, Skill):
    '''类的多继承'''
    def speak(self):
        print('wa wa wa wa ')

    def destroy(self, matter):
        print('destroy to '+matter)


a = Student('jack', 18, 20)
a.speak()
a.t('haha', 'biubiu')

b = StudentMin()
b.player()
b.speak()

c = Baby()
c.speak()
c.destroy('car')
c.consumption('cat')
