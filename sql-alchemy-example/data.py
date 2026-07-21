from sqlalchemy import Integer,String
from sqlalchemy.orm import declarative_base,Mapped,mapped_column

Base = declarative_base()
# similar to table column
class User(Base):
    __tablename__ = "user1"
    id:Mapped[Integer]=mapped_column(Integer,primary_key=True)
    name:Mapped[String]=mapped_column(String)
    email:Mapped[String]=mapped_column(String)
    mobile:Mapped[String]=mapped_column(String)
    password:Mapped[String]=mapped_column(String)
    dob:Mapped[String]=mapped_column(String)

class City(Base):
    __tablename__ ='city'
    id:Mapped[Integer]=mapped_column(Integer,primary_key=True)
    name:Mapped[String]=mapped_column(String)