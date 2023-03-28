from dataclasses import dataclass

# using dataclass makes initialization in classes easier
@dataclass
class Person:
	f_name: str
	l_naem: str
	
	def call_name(self):
		print(self.f_name + ' ' + self.l_naem)

f=input("Enter first name: ")
l=input("Enter last name: ")
my_name=Person(f,l)
my_name.call_name()