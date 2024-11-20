from sqlalchemy import Column, Integer, String
from DB import Base, DB

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    stars = Column(Integer, nullable=False)
    str_stars = Column(String(255), nullable=False)
    
    def __repr__(self):
        return f"<Character: {self.name} ({self.str_stars})>"