"""
Purpose: Use the Math Module to create some Functions with Basketball

Author: Wade Bryson

Function 1 - Calculate the point differential between two teams.
Function 2 - Calculate the total amount of starting lineup combinations for a team
Function 3 - Find the total points scored for a team


"""

#Import the Math module
import math

#Setting up the logger
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

#Function 1 - Find the difference for a teams points scored vs their opponent
#Defining the function
def find_point_difference_given_scores(home_score, visitor_score):
   
    #Creating a variable that calculates the differance between two teams scores.
    point_differential = home_score - visitor_score
    logger.info(f"The point differential for your game is {point_differential}")
    return point_differential

#Running Function 1
#Showing that it works for positive values (Games that you WIN)
find_point_difference_given_scores(85, 42)
#Showing that it works for negative values (Games that you LOSE)
find_point_difference_given_scores(34, 68)
#Showing that it works for games that end in a TIE
find_point_difference_given_scores(45, 45)

#Function 2 - Find the total possible starting lineup combinations for a basketball team
#Defining the function
def total_lineup_combinations(total_players):

    #Creating a variable that calculates the total starting lineup combinations for a basketball team (From the total, choose 5 starters)
    total_combos = math.comb(total_players,5)
    logger.info(f"The total number of combinations for your starting lineup is {total_combos}")
    return total_combos

#Test Running Function 2
total_lineup_combinations(10)
total_lineup_combinations(20)
total_lineup_combinations(5)

#Function 3 - Find the total points scored for a team
#Defining the function
def total_points_scored(threes_made, twos_made, free_throws_made):

    #Creating a variable that calculates the total points scored for a team
    total_points = 3*threes_made + 2*twos_made + free_throws_made
    logger.info(f"The total number of points scored for your team was {total_points}")
    return total_points

#Test Running Function 3
total_points_scored(10, 12, 5)
total_points_scored(25, 39, 25)

#Logging info as required in task 3.1
logger.info("Explore some functions in the math module")
logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")

# Print the logged information
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())