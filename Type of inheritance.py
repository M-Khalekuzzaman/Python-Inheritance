'''
 There are 3 types of inheritance
    1)Hierarchical Inheritance
     2)Multi-level Inheritance
    3)Multiople Inheritance
'''
'''
#Multi-Level Inheritance
class A :
    def display1(self):
        print("I am inside A class")

class B(A) :
    # display(1)
    def display2(self):
        print("I am inside B class")

class C(B) :
    # display(1),display(2)
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class")

ob1 = C()
ob1.display3()

'''

#Multiple Inheritance
class A :
    def display(self):
        print("I am inside A class")

class B :
    # display(1)
    def display(self):
        print("I am inside B class")

class C(A,B) :
    # display(1),display(2)
    def display(self):
        super().display()
        super().display()
        print("I am inside C ")

ob1 = C()
ob1.display()

