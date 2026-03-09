'''
Abstraction:
hiding the internal implementation and showing only functionality to the end user .
Abstraction method:
if a method/function consstes of only declaration not defination then it will be called as "abstract methods"
Abstract Class:
if a class consists of at least one abstract method,it is called as "abstract class"
concrete class :
if a class with no abstract method is called concrete class

'''
from abc import ABC,abstractmethod 
class ATM(ABC): # abstract class 
    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
       pass

    @abstractmethod
    def check_bal(self):
        pass

class SBI_ATM(ATM): # concrete class
    @abstractmethod
    def generate_pin(self):
        print("generate pin")
    
    @abstractmethod
    def forget_pin(self):
       print("forget pin")

    @abstractmethod
    def check_bal(self):
        print("check bal")

