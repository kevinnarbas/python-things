nums = [1,2,3,4,5,6]

def square(n):
  return n*n


# lambda = anonomous function
print(list(map(lambda n: n * n,nums)))
print(list(map(square,nums)))
