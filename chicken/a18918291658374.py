n = 0
import random as r
meta = []
while True:
  n += 1
  meta.append(r.randint(1111111111111, 99999999999999))
  f = open("war.chicken." + str(n) + ".wchkn", "a")
  f.write(meta)
  
