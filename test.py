import os
directory = raw_input("?")
findit = os.listdir(directory)
findit.sort()
for s in findit:
  print s

