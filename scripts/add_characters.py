from DB import DB
from Models.character import Character

db = DB()
db.create_tables()
def add_characters_starting():
    characters = [
        Character(name="Diego", stars=5, str_stars="★★★★★"),
        Character(name="Pato", stars=4, str_stars="★★★★"),
        Character(name="Mateo", stars=4, str_stars="★★★★"),
        Character(name="Acam", stars=4, str_stars="★★★★"),
        Character(name="Jair", stars=4, str_stars="★★★★"),
        Character(name="Merka", stars=3, str_stars="★★★"),
        Character(name="Nico", stars=3, str_stars="★★★"),
        Character(name="Chip", stars=1, str_stars="★"),
        Character(name="Hydra", stars=1, str_stars="★"),
        Character(name="Lechen", stars=2, str_stars="★★"),
        Character(name="ZeroTwo", stars=2, str_stars="★★"),
    ]
    db.add(characters)
    
def add_character(name, stars):
    str_stars = "★" * stars
    db.add(Character(name=name, stars=stars, str_stars=str_stars))
    