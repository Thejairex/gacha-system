from controllers import Gacha

class Main:
    def __init__(self):
        self.gacha = Gacha()
        self.deck = []
        self.response = None
        
    def run(self):
        while True:
            # clear the screen
            # print("\033[H\033[J")
            if self.response:
                print(str(self.response) + "\n")
                self.response = None
            
            print("1. Roll")
            print("2. Banner")
            print("3. number of rolls")
            print("4. Show my deck")
            print("5. Show Probs")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                character = self.gacha.roll()
                self.deck.append(character)
                self.response = f"You rolled: {character}"
            elif choice == "2":
                self.response = self.gacha.banner()
            elif choice == "3":
                self.response = self.gacha.get_rolls()
            elif choice == "4":
                self.response = self.deck
            elif choice == "5":
                self.response = self.gacha.get_probabilities()
            elif choice == "6":
                break
            
if __name__ == "__main__":
    main = Main()
    main.run()