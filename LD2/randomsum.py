import random
list = []
start = 0
end = 1
sum = 0
for x in range(4):
  sk = round(random.uniform(start, end), 2)
  sum += sk
  end = end - sk
  list.append(sk)
list.append(round(1-sum,2))
print(list)