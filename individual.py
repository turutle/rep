# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:15:01 2021

@author: turtl
"""

X = int (input ( "Input age of Tanya --> "))
Y = int (input ( "Input age of Mitya --> "))
print( "Middle age: %.2f" % ((X+Y)/2))
print( "Difference of Tanya: %.2f" % abs(X - ((X + Y)/2)))
print( "Difference of Mitya: %.2f" % abs(Y - ((X + Y)/2)))