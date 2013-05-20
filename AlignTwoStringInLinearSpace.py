#!/usr/bin/env python2.7
import sys
import pdb
import argparse
import numpy as np
import copy
import re
"""

The factor limits dynamic programing's application often is not running time (O(nm)) 
but the quardratic space requirement, where n and m are the length of two sequence.
The Hirschberg algorithm reduces the space requirement from O(nm) to O(n) by involves 
divide and conque technique in the dynamic Programming process. Below is an 
implementation of Hirschberg's algorithm. 
http://en.wikipedia.org/wiki/Hirschberg's_algorithm
"""

insertion    = -2
deletion     = -2
substitution = -1
match        =  2
#insertion    = 0
#deletion     = 0
#substitution = 0
#match        = 1

def lastLineAlign(x, y):
  """
  input:  two strings: x and y
  output: an array with a length of |y| that contains the score for the alignment 
          between x and y
  """
  global insertion
  global deletion
  global substitution
  global match 
  row = y
  column = x 
  minLen = len(y)
  prev = [0 for i in range(minLen + 1)]
  current = [0 for i in range(minLen + 1)]


  for i in range(1, minLen + 1):
    prev[i] = prev[i-1] + insertion
  
  current[0] = 0
  for j in range(1, len(column) + 1):
    current[0] += deletion
    for i in range(1, minLen + 1):
      if row[i-1] == column[j-1]:
        try:
          current[i] = max(current[i-1] + insertion, prev[i-1] + match, prev[i] + deletion)
        except:
          pdb.set_trace()
      else:
        current[i] = max(current[i-1] + insertion, prev[i-1] + substitution, prev[i] + deletion)
    prev = copy.deepcopy(current) # for python its very import to use deepcopy here

  return current 

def partitionY(scoreL, scoreR):
  max_index = 0
  max_sum = float('-Inf')
  for i, (l, r) in enumerate(zip(scoreL, scoreR[::-1])):
    # calculate the diagonal maximum index
    if sum([l, r]) > max_sum:
      max_sum = sum([l, r])
      max_index = i
  return max_index 

def dynamicProgramming(x, y):
  global insertion
  global deletion
  global substitution
  global match 
  # M records is the score array
  # Path stores the path information, inside of Path:
  # d denotes: diagnal
  # u denotes: up
  # l denotes: left
  M = np.zeros((len(x) + 1, len(y) + 1))
  Path = np.empty((len(x) + 1, len(y) + 1), dtype=object)

  for i in range(1, len(y) + 1):
    M[0][i] = M[0][i-1] + insertion
    Path[0][i] = "l"
  for j in range(1, len(x) + 1):
    M[j][0] = M[j-1][0] + deletion
    Path[j][0] = "u"
  
  for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
      if x[i-1] == y[j-1]:
        M[i][j] = max(M[i-1][j-1] + match, M[i-1][j] + insertion, M[i][j-1] + deletion)
        if M[i][j] == M[i-1][j-1] + match:
          Path[i][j] =  "d"
        elif M[i][j] == M[i-1][j] + insertion:
          Path[i][j] = "u"
        else:
          Path[i][j] = "l"
      else:
        M[i][j] = max(M[i-1][j-1] + substitution, M[i-1][j] + insertion, M[i][j-1] + deletion)
        if M[i][j] == M[i-1][j-1] + substitution:
          Path[i][j] =  "d"
        elif M[i][j] == M[i-1][j] + insertion:
          Path[i][j] = "u"
        else:
          Path[i][j] = "l"

  row = []
  column= []
  middle = []
  i = len(x)
  j = len(y)
#  print M
#  print Path
  while Path[i][j]:
    if Path[i][j] == "d":
      row.insert(0, y[j-1])
      column.insert(0, x[i-1])
      if x[i-1] == y[j-1]:
        middle.insert(0, '|')
      else:
        middle.insert(0, ':')
      i -= 1
      j -= 1
    elif Path[i][j] == "u":
      row.insert(0, '-')
      column.insert(0, x[i-1])
      middle.insert(0, 'x')
      i -= 1
    elif Path[i][j] == "l":
      column.insert(0, '-')
      row.insert(0, y[j-1])
      middle.insert(0, 'x')
      j -= 1
#  align = "\n".join(map(lambda x: "".join(x), [row, middle, column]))
#  print align
#  print  M[len(x)][len(y)]
#  return align, M[len(x)][len(y)]
#  return row, column, middle
  return row, column, middle


def Hirschberge(x, y):
  row = ""
  column = ""
  middle = ""
#  x is being row-wise iterated (out-most for loop)
#  y is being column-wise iterated (inner-most of the for loop)
  if len(x) == 0 or len(y) == 0:
    if len(x) == 0:
      column = '-' * len(y)
      row = y
      middle =  'x' * len(y)
    else:
      column += x
      row += '-' * len(x)
      middle =  'x' * len(x)
  elif len(x) == 1 or len(y) == 1:
    row, column, middle = dynamicProgramming(x, y)
    # concatenate into string
    row, column, middle = map(lambda x: "".join(x), [row, column, middle]) 
  else:
    xlen = len(x)
    xmid = xlen/2
    ylen = len(y)

    scoreL = lastLineAlign(x[:xmid], y)
    scoreR = lastLineAlign(x[xmid:][::-1], y[::-1])
    ymid = partitionY(scoreL, scoreR)
#    pdb.set_trace()
    row_l, column_u, middle_l = Hirschberge(x[:xmid], y[:ymid])
    row_r, column_d, middle_r = Hirschberge(x[xmid:], y[ymid:])
    row = row_l + row_r
    column = column_u + column_d 
    middle = middle_l + middle_r

  return row, column, middle
        

  
if __name__ == '__main__':
  o = sys.stdout
  e = sys.stderr
  parser= argparse.ArgumentParser(description="")
  parser.add_argument("--file", help="")
  args = parser.parse_args() 
  Xs = ["AGTACGCA", "hello", "T", "T", "T"]
  Ys = ["TATGC", "hllo", "C", "T", ""]
  for i, (x, y) in enumerate(zip(Xs, Ys)):
    row, column, middle = Hirschberge(x, y)
    print '#' * 8, "Alignment %r" % i, '#' * 8
    print row
    print middle
    print column
    print 
