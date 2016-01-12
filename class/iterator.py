__metaclass__ = type

'''
������ʵ��쳲���������
'''

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()

for f in fibs:
    if f < 50:
        print f
        #break
    else:
        break


'''
ʵ���ϣ���Ϊ������������ձ飬Pythonר�Ž��ؼ���for�����˵��������﷨�ǡ�
��forѭ���У�Python���Զ����ù�������iter()��õ��������Զ�����next()��ȡԪ�أ�
������˼��StopIteration�쳣�Ĺ���
'''

listA = [1,2,3]

it = iter(listA)
try:
    while True:
        val = it.next()
        print val
except StopIteration:
    pass

##һ��forѭ���������ü�������
for value in listA:
    print value




