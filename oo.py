
# 简单类创建

class Hello:

    def __init__(self, name):
        self._name = name

    def sayHello(self):
        print("Hello, {0}".format(self._name))


# 继承关系

class Hi(Hello):
    def __init__(self, name):
        Hello.__init__(self, name)

    def sayHi(self):
        print("Hi, {0}".format(self._name))

h = Hello("ZhangSan")
h.sayHello()

h1 = Hi("LiSi")
h1.sayHi()
