#!/usr/bin/python
# Copyright 2013 MTM


# Program to calculate a percentage of a given number, using dict, input parameters
# 
# 

import sys
import re
import os
import shutil
import commands

"""
Program to calculate amounts

General shell:
- store the arguments passed
- print out the arguments
- perform calculations
- print

"""

def calc(order,config):
  """

  """
  
# hash table of percentages
  dict = {}
  dict['T2'] = .53
  dict['T5'] = .63
  dict['T10'] = .65
  dict['T15'] = .60
  dict['T20'] = .62
  dict['T30'] = .64
  dict['T40'] = .65 
  
  print '***Reference Variables***'
  
  config = config.upper()
  if config in dict:
	cr = dict[config]*order
  else:
	cr = 0

  print 'Thing: ' + config.upper()
  print 'Thing %: ' + str(dict[config])
  
  
  print '***Calculations***'
  
  if cr == 0:
	print 'Invalid config. Please re-enter. e.g., T20'
  else:
	print 'CR: $' + str(cr)
  
  
def main():
  # This basic command line argument parsing code is provided.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if len(args) != 2:
    print "usage: [ Pls provide number and the thing e.g., 1400000 T20  ]";
    sys.exit(1)
  else:
	order = args[0]
	config = args[1]

  print '\n\n\n\n\n\n\n\n'
  print '**MTM\'s basic calculator**\n\n'

  calc(float(order),config)
  
if __name__ == "__main__":
  main()
