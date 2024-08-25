from pydantic import BaseModel
from enum import Enum


class Timestamp(BaseModel):
    id: int
    timestamp: int


class DogType(str, Enum):

    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"
    Tax = 'Tax'


class Dog(BaseModel):

    name: str
    pk: int
    kind: DogType


