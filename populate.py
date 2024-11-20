from scripts.add_characters import *

def main():
    # populate the database
    add_characters_starting()
    
    # show all characters
    characters = db.get_all(Character)
    for character in characters:
        print(character)
    
if __name__ == "__main__":
    main()