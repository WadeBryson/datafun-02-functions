"""
Purpose: Class that creates an instantiated object containing a player or team's name and points scored in several games. 
        The Class also calculates the sum, average, and median values for their points scored.

Author: Wade Bryson

"""

from util_datafun_logger import setup_logger

#define the class
class player_points:
    def __init__(self, name, points, data):
        self.name = name
        self.points = points
        self.data = data
    #creating a count function 
    def count(self):
        return len(self.data)
    
    #creating a sum function
    def sum(self):
        return sum(self.data)
    
    #creating an average function
    def average(self):
        return sum(self.data) / len(self.data)
    
    #creating a median function
    def median(self):
        sorted_data = sorted(self.data)
        n = len(self.data)
        if n % 2 == 0:
            return (sorted_data[n//2-1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]
                
    def __str__(self):
        #Returns a string representation of the instantiated object
        
        str = f"NumericSeries with name={self.name}, units={self.points}, and {len(self.data)} data points: {self.data}"
        return str
    
