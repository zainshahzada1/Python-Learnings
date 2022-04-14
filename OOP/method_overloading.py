class Student:
    def __init__(self, m1=None, m2=None,m3=None):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def sum(self,a=None,b=None,c=None):
        if a != None and b != None and c != None:
            s=a+b+c
        elif a != None and b != None:
            s = a+b
        else:
            s=a
        return s



s1 = Student(100,200)

print(s1.sum(5+10+15))

