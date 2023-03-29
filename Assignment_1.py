from dataclasses import dataclass


@dataclass
class Mountain:
	name: str
	elevation: int
	
# m_name=input("Enter mountain name: ")
# m_elevation=int(input("Enter mountain elevation: "))
m1=Mountain("Mt. Everest", 8499)
m1_string = str(m1)
print(m1_string)