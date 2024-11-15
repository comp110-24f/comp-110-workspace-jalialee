"""simulation of a small river ecosystem of bears and fish"""
__author__ = "730762790"

from exercises.ex07.river import River #importing the function

my_river = River (num_fish = 10,num_bears = 2) #10 fishes and 2 bears

    
my_river.view_river() #viewing the initial state of the river

my_river.one_river_week() #simulation one week

my_river.view_river() #state after one week 



