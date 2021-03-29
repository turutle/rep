# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:31:20 2021

@author: turtl
"""

h = int ( input ( "Input hours --> "))
m = int ( input ( "Input minutes --> "))
s = int ( input ( "Input seconds --> "))
print ( "Degrees from start of clocks: %.2f" % (720/24*h + 30/60*m + 0.5/60*s))