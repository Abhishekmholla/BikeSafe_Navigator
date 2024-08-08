from sqlalchemy import Boolean, Column, ForeignKey, ForeignKeyConstraint, Integer, String
from ..db.database import Base
from sqlalchemy.orm import relationship

# class Users(Base):
#     __tablename__ = "users"
#     id = Column(Integer,primary_key=True,index=True)
#     name = Column(String(255),index=True)
#     email = Column(String(255), unique=True, index=True)
#     todos = relationship("Todo",back_populates="owner")
#     is_active = Column(Boolean,default=False)

# class Todo(Base):
#     __tablename__ = "todos"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(255), index=True)
#     description = Column(String(255), index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#     owner = relationship("Users",back_populates="todos")


class Accident(Base):
    __tablename__ = "accident"
    accident_no = Column(String(255), primary_key=True, index=True)
    lga_name = Column(String(255), index=True)
    latitude = Column(String(255))
    longitude = Column(String(255))
    severity = Column(String(255))
    nodes = relationship("Node",back_populates="accident")
    accident_route = relationship("Accident_Routes",back_populates="accident_route")
    
class Node(Base):
    __tablename__ = "node"
    node_id = Column(String(255), primary_key=True, index=True)
    lga_name = Column(String(255), index=True)
    latitude = Column(String(255))
    longitude = Column(String(255))
    accident_no = Column(String(255), ForeignKey("accident.accident_no"))
    accident = relationship("Accident",back_populates="nodes")
    
class Route(Base):
    __tablename__ = "route"
    route_id = Column(Integer, primary_key=True, index=True)
    geo_shape = Column(String(255))
    type = Column(String(255))
    accident_routes = relationship("Accident_Route",back_populates="route")
    
class Accident_Route(Base):
    __tablename__ = "accident_route"
    accident_route_id = Column(Integer, primary_key=True, autoincrement=True)
    accident_no =  Column(String(255), ForeignKey("accident.accident_no"), index=True)
    route_id = Column(Integer,ForeignKey("route.route_id"), index=True)
    accident_route = relationship("Accident",back_populates="accident_route")
    route = relationship("Route",back_populates="accident_routes")
    