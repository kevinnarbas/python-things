grades = ['A','B','C','F','F','A']

def remove_fails(grade):
  return grade != 'F'

# filter(testing_function, list):
# print(list(filter(remove_fails,grades)))

# for loop:
# filtered_grades = []
# for grade in grades:
#   if grade != 'F':
#     filtered_grades.append(grade)
# print(filtered_grades)

# comprehension:

print([grade for grade in grades if grade != 'F'])
