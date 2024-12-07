from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects import postgresql


BASE = declarative_base()

class Todo(BASE):
    __tablename__ = 'synonyms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    root = Column(String)
    synonyms = Column(postgresql.ARRAY(String))

    def __init__(self, root, synonyms):
        self.root = root
        self.synonyms = synonyms