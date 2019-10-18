# What are the even numbers from 1 to num?

num = 123
for i in range(1, num+1):
  if i % 2 == 0:
    print(i, end=' ')
    
start = 2
prime_fact = []

while start <= num:
  if num % start == 0:
    prime_fact += [start]
else:
  start += 1
  
print(prime_fact)
