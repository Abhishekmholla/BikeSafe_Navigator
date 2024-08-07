from pydantic import BaseModel, condecimal
from enum import Enum

class TodoBase(BaseModel):
    title : str
    description : str | None = None


class TodoCreate(TodoBase):
    pass

        
class Todo(TodoBase):
    id : int
    owner_id  : int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    pass 


class User(UserBase):
    id : int
    is_active : bool
    todos : list[Todo] = []

    class Config:
        orm_model = True

class TestBase(BaseModel):
    email: str

class Test(TestBase):
    id: int
    class Config:
        orm_model = True

class NodeBase(BaseModel):
    lga_name: str 
    latitude: condecimal(max_digits=9, decimal_places=6)  
    longitude: condecimal(max_digits=9, decimal_places=6)
    accident_no : str 

class Node(NodeBase):
    node_id: int
    class Config:
        orm_model = True

# class SeverityEnum(str, Enum):
#     High = "high"
#     Medium = "medium"
#     Low = "low"
    
class AccidentBase(BaseModel):
    lga_name: str 
    latitude: condecimal(max_digits=9, decimal_places=6)  
    longitude: condecimal(max_digits=9, decimal_places=6)
    severity : str


class Accident(AccidentBase):
    accident_no : str 
    class Config:
        orm_model = True

class RouteBase(BaseModel):
    geo_shape : str
    type: str

class Route(RouteBase):
    route_id : int
    class Config:
        orm_model = True

class AccidentRouteBase(BaseModel):
    pass

class AccidentRoute(AccidentRouteBase):
    accident_no : str
    route_id : int
    class Config:
        orm_model = True