import pydantic
from typing import List

#pydantics is like dataclasses but better

class Hobby(pydantic.BaseModel):
    name:str
    is_a_team_hobby:bool

class Person(pydantic.BaseModel):
    f_name:str
    l_name:str
    hobbies:List[Hobby]

p1 = Person(f_name="John", l_name="Smith", hobbies=[Hobby(name="Football", is_a_team_hobby=True)])
print(p1)
p1_to_dict = p1.dict()
print(p1_to_dict)

#here we used 'p1_to_dict' as input parameters for initializing the object 'p2' by unpacking it using '**'
p2=(Person(**p1_to_dict))
print(p1 == p2)   