# for n in range(5):
#   print(n)


# for n in range(3,10):
#   print(n)


# range(start, end-not inclusive, steps)
# for n in range(0,20,4):
#   print(n)

burgers = ['beef', 'chicken','veg', 'supreme', 'double']

# for n in range(len(burgers)):
#   print(n, burgers[n])

# can also use range(-1,-1,-1) to go backwards
for n in range(len(burgers) - 1, -1, -1):
  print(n,burgers[n])