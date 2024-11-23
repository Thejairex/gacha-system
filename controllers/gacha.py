import random

from sqlalchemy import func

from DB import DB
from Models.character import Character

class Gacha:
    def __init__(self):
        self.db = DB()
        self.probs_base = {
            1: 50,
            2: 30,
            3: 15,
            4: 5,
            5: 1
        }
        self.probs = self.probs_base.copy()
        self.count_rolls = 0
        self.max_probability = 85

    def roll(self):
        self.count_rolls += 1

        if self.count_rolls % 90 == 0:
            rarity = 5
        elif self.count_rolls % 25 == 0:
            rarity = 4
        elif self.count_rolls % 10 == 0:
            rarity = 3
        else:
            rarity = self._random_roll()
        
        self._ajust_prob()
        if rarity in [3,4,5]:
            self._reset_rarity(rarity)
        
        character = self._get_by_star(rarity)
        print(character.name)
        return character
    
    def _random_roll(self):
        rarity = list(self.probs.keys())
        probs = list(self.probs.values())
        return random.choices(rarity, weights=probs, k=1)[0]
    
    def _get_by_star(self, star):
        character = self.db.session.query(Character).filter_by(stars=star).order_by(func.random()).first()
        return character
    
    def _reset_rarity(self, rarity):
        self.probs[rarity] = self.probs_base[rarity]
    
    def _ajust_prob(self):
        """
        Ajust the weight of 5 stars characters based on the number of rolls
        """
        rest_roll = 90 - self.count_rolls
        if rest_roll > 0:
            increment_5 = (rest_roll / 90) / 90 * 10
            self.probs[5] = self.probs[5] + increment_5
            
            increment_4 = (rest_roll / 90) / 90 * 5
            self.probs[4] = self.probs[4] + increment_4
            
            increment_3 = (rest_roll / 90) / 90 * 3
            self.probs[3] = self.probs[3] + increment_3
            
            probs_rest = 100 - (
                self.probs[5] +
                self.probs[4] +
                self.probs[3] 
            )
            self.probs[1] = probs_rest * 0.625 
            self.probs[2] = probs_rest * 0.375 

        # check if the number of sum of probabilities is 100
        print(sum(self.probs.values()))


    def get_rolls(self):
        return f"Total rolls: {self.count_rolls}"

    def get_probabilities(self):
        return f"Probabilities: {self.probs}"

    def banner(self):
        """
        Return all possible characters
        """
        characters = self.db.get_all(Character)
        return f"Total possible characters: {characters}"