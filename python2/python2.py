#!/usr/bin/env python3
		
A = 63
B = 75
if A < 0:
  message = 'negative'
  print(A, message) 
elif A > 0:
  message = 'positive'
  print(A, message)
else: 
  message = '0'
  print(A, message)

if A%2 == 0:
 message = 'number is even'
 print(A, message)
else:
 message = 'number is odd'
 print(A, message)
if B%5==3:
  message = 'not divisible'
  print(B, message)
elif B%5 == 0:
  message = 'divisible by 5'
  print (B, message)
else:
  message = 'done' 	
  print (B, message)

