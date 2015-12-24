__metaclass__ = type

'''
ͨ����������������
'''

class Rectangle_v1:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width,self.height = size

    def getSize(self):
        return self.width, self.height


r = Rectangle_v1()
print r.getSize()

r.setSize((11,12))
print r.getSize()


'''
ʹ��property ֮��size��ʹ�þ������������һ������
'''

class Rectangle_v2:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)

print "v2"
r2 = Rectangle_v2()
print r2.getSize()
print r2.size

r2.size = 13, 14
print r2.getSize()
print r2.size

r2.setSize((15,16))
print r2.getSize()
print r2.size
