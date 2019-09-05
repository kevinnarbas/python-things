from random import shuffle

def jumble(word):
  anagram = list(word)
  shuffle(anagram)
  return ''.join(anagram)

words = ['beetroot', 'potatoes', 'carrots']
anagrams = []

# for loop way:
for word in words:
  anagrams.append(jumble(word))
print(anagrams)

# map way: map(function.data)
print(list(map(jumble, words)))

# comprehension way:
print([jumble(word) for word in words])