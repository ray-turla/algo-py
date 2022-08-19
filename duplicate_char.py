import math
from utils.timeit import timeit

"""
This file consists of different implementations of a function that accepts an input of string and returns true if an input has a duplicate character.
"""

@timeit
def dictDup(text):
  strlen = len(text)
  median = int(math.floor(strlen / 2))
  dupDict = {}
  left = [text[s] for s in range(0, median)]
  right = [text[s] for s in range(median, strlen)]
  for i in range(0, len(right)):
    if not left[i] in dupDict:
      dupDict[left[i]] = True
    else:
      return True
    if not right[i] in dupDict:
      dupDict[right[i]] = True
    else:
      return True
  print('f')
  return False

@timeit
def isDuplicate(text):
  strlen = len(text)
  median = int(math.floor(strlen / 2))
  left = [text[s] for s in range(0, median)]
  right = [text[s] for s in range(median, strlen)]
  for i in range(0, len(right)):
    if i < len(left):
      for j in range(len(right)):
        jshift = j + 1
        if jshift < len(left) and not i == jshift:
          if(left[i] == left[jshift]):
            return True
          if(right[i] == right[jshift]):
            return True
        if(left[i] == right[j]):
          return True
  return False

@timeit
def selectD(text):
  strlen = len(text)
  for i in range(0, strlen):
    for j in range(0, strlen):
      jshift = j + 1
      if jshift < strlen and not i == jshift:
        if(text[i] == text[jshift]):
          return True
  return False

selectD("1234567890-qwertyuiop[asdfghjklzxcvbnm,!@#$%^&*()BbPOIUYTRE")
isDuplicate("1234567890-qwertyuiop[asdfghjklzxcvbnm,!@#$%^&*()BbPOIUYTRE")
dictDup("1234567890-qwertyuiop[asdfghjklzxcvbnm,!@#$%^&*()BbPOIUYTRE")