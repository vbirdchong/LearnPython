__metaclass__ = type

class Person:

    def setName(self, name):
        self.name = name

    def getName(self, name):
        return self.name

    def greet(self):
        print "Hello, world! I'm %s." % self.name


        
foo = Person()
foo.setName('Luke Sky')
foo.greet()

boo = Person()
boo.setName('Jim Kun')
boo.greet()
