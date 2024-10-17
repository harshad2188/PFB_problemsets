#!/usr/bin/env python3
'''n = 10
res = 1
while n>0:
 res *= n
 n -= 1
#print(f'Factorial:{res}.')

n = 3
res = 1
while n>0:
 res *= n
 n -= 1
#print(f'Factorial:{res}.')

#Question 6
for num in my_list:
	if num % 2 == 0: 
#		print(num)'''

my_list = [101,2,15,22,95,33,2,27,72,15,52]
sorted(my_list)
print(sorted(my_list))
sorted_list = sorted(my_list)
even = []
odd = []
for num in sorted_list:	
	if num % 2 == 0:
		even.append(num)
	else:
		odd.append(num)

print(sum(even))
print(sum(odd))
#question 9
range(100)
for num in range(100):	
	print(num)


