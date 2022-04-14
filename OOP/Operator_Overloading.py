class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        self.n1=self.m1 + other.m1
        self.n2=self.m2 + other.m2
        self.s=Student(self.n1,self.n2)
        return self.s
    def __gt__(self,other):
        self.n1 = self.m1 + other.m1
        self.n2 = self.m2 + other.m2
        if self.n1>self.n2:
            return True
        else:
            return False
    def __str__(self):
        return f'{self.m1},{self.m2}'


s1=Student(400,80)
s2=Student(100,200)
s3=s1+s2
print(s3.m1)
print(s3.m2)
if s1>s2:
    print('Student 1 Wins')
else:
    print('Student 2 Wins')
print(s1)
print(s2)
print ('So,sum is ...')
print(s3)
