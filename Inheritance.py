# Inheritance is a class.whice is use to one class characture to convert to another class characture

'''
class Phone:   #  paraent class/Super class/base class

    def call(self):
        print("you can call now")

    def message(self):
        print("You can message now")


class Realme(Phone) :   #  Child class/sub class/derived class
    # call & message

    def photo(self):
        print("You can photo now")

r = Realme()
r.call()
r.message()
r.photo()
print(issubclass(Realme,Phone))

'''
class Khalekuzzaman :

    def name(self):
        print("My name is Khalekuzzaman")

    def roll(self):
        print("My roll number is 1910979158")

class Kaochar(Khalekuzzaman) :
    # name , roll
    def sesson(self):
        print("My session is  : 2018-19")

k1 = Khalekuzzaman()
k1.name()
k1.roll()

k2 = Kaochar()
k2.name()
k2.roll()
k2.sesson()
print(issubclass(Kaochar,Khalekuzzaman))