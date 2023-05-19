"""
Purpose: Create a derived class that takes the player_points_class and adds a players age

Author: Wade Bryson

"""
#Import player points class
from player_points_class import player_points

#import logger class
from util_datafun_logger import setup_logger

#defining derived class
class age_derived_player_points(player_points):

    def __init__(self, name, points, data, age):
        super().__init__(name, points, data)

        self.age = age
    
    def __str__(self):
        #Returns a string representation of the instantiated object
        
        str = f"NumericSeries with name={self.name}, age={self.age} years old, units={self.points}, and {len(self.data)} data points: {self.data}"
        return str
