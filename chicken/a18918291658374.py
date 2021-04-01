n = 1
while True:
  n += 1
  f = open("war.chicken." + str(n) + ".wchkn", "a")
  x = 0
  c = []
  c.append(x)
  c.append(c)
  x += 1
  x *= x
  print(c)
  f.write(str(c))
