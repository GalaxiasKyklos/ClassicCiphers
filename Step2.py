import sys
from ClassicCiphers import ClassicCiphers

message = open('./ins/Step2.in').read()
algorithm = sys.argv[1]

if algorithm == 'railfence':
  prev = ClassicCiphers.drailfence(message, 1)
  print(1)
  print(prev)
  for i in range(2, len(message) + 1):
      nex = ClassicCiphers.drailfence(message, i)
      if prev != nex:
          print(i)
          print(nex)
          prev = nex
elif algorithm == 'coltrans':
  WORDS = open('./ins/words').read().splitlines()
  for word in sorted(WORDS):
      if word[0].isupper():
          transpos = ClassicCiphers.dcolumnartransposition(message, word.lower())
          print(word)
          print(transpos)
