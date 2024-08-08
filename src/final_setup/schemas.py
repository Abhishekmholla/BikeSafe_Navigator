from pydantic import BaseModel, condecimal
from enum import Enum
from shapely import Polygon
from sqlalchemy import Text

# class NodeBase(BaseModel):
#     lga_name: str 
#     latitude: condecimal(max_digits=9, decimal_places=6)  
#     longitude: condecimal(max_digits=9, decimal_places=6)
#     accident_no : str 

# class Node(NodeBase):
#     node_id: int
#     class Config:
#         orm_model = True

# class SeverityEnum(str, Enum):
#     High = "high"
#     Medium = "medium"
#     Low = "low"
    
# class AccidentBase(BaseModel):
#     lga_name: str 
#     latitude: condecimal(max_digits=9, decimal_places=6)  
#     longitude: condecimal(max_digits=9, decimal_places=6)
#     severity : str


# class Accident(AccidentBase):
#     accident_no : str 
#     class Config:
#         orm_model = True

# class RouteBase(BaseModel):
#     geo_shape : str
#     type: str

# class Route(RouteBase):
#     route_id : int
#     class Config:
#         orm_model = True

# class AccidentRouteBase(BaseModel):
#     pass

# class AccidentRoute(AccidentRouteBase):
#     accident_no : str
#     route_id : int
#     class Config:
#         orm_model = True

class Melbourne_LGABase(BaseModel):
    lga_name: str 
    geometry: Text

class Melbourne_LGA(Melbourne_LGABase):
    id: int
    class Config:
        orm_model = True
        
class AccidentBase(BaseModel):
    lga_name: str 
    latitude: condecimal(max_digits=9, decimal_places=6)  
    longitude: condecimal(max_digits=9, decimal_places=6)
    severity : str
    point: Text

class Accident(AccidentBase):
    accident_no : str
    class Config:
        orm_model = True
        