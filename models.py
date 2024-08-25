from sqlalchemy import Column, String, Integer

from config import Base


class DogDB(Base):
    __tablename__ = "dogs"

    name = Column(String)
    pk = Column(Integer, primary_key=True)
    kind = Column(String)






