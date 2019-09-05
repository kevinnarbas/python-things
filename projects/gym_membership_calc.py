initial_cost = int(input('Enter the initiation fee: $'))
monthly_cost = int(input('Enter the monthly fee: $'))
length = int(input('Enter how many months you\'d like to calculate for: '))

total_cost = []

for num in range(length + 1):
  if num == 0:
    total_cost.append(initial_cost)
  elif num == 1:
    total_cost.append(monthly_cost + initial_cost)
  else:
    total_cost.append(total_cost[-1] + monthly_cost)


print(f'With an initial cost of ${initial_cost} and a monthly cost of ${monthly_cost} after {length} months your total will be ${total_cost[-1]} with a first month\'s payment of ${total_cost[1]}')
  
