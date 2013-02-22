#!/usr/bin/python
# Copyright 2013 MTM


# Program to calculate revenue
# 
# 

import sys
import re
import os
import shutil
import commands

"""
Program to calculate revenue amounts

General shell:
- store the rev arguments passed
- print out the arguments
- perform revenue calculations
- print

"""

def calc_rev(orderrev,config):
  """

  """
  mratio = .1375
  
# hash table of license revenue percentage for rev splits
  dict = {}
  dict['T2'] = .53
  dict['T5'] = .63
  dict['T10'] = .65
  dict['T15'] = .60
  dict['T20'] = .62
  dict['T30'] = .64
  dict['T40'] = .65 
  
  print '***Reference Variables***'
  print 'MRatio: ' + str(mratio*100) + '%'
  
  rev = orderrev*(1-mratio)
  config = config.upper()
  if config in dict:
	crev = dict[config]*orderrev
  else:
	crev = 0

  print 'Model: ' + config.upper()
  print 'Model Cut: ' + str(dict[config])
  
  
  print '***Calculations***'
  print 'Revenue: $' + str(rev)
  
  if crev == 0:
	print 'Invalid config. Please re-enter. e.g., T20'
  else:
	print 'Comp Revenue: $' + str(crev)
  
  
def main():
  # This basic command line argument parsing code is provided.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if len(args) != 2:
    print "usage: [ Pls provide order revenue as number and the thing e.g., 1400000 T20  ]";
    sys.exit(1)
  else:
	orderrev = args[0]
	config = args[1]

  print '\n\n\n\n\n\n\n\n'
  print '**MTM\'s basic calculator**\n\n'

  calc_rev(float(orderrev),config)
  
if __name__ == "__main__":
  main()
