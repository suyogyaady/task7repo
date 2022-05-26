n= (1, 2, 3, 4, 5, 6, 7, 8, 9) 
odd = 0
even = 0

for x in n:
    if not x % 2:
         even=even +1
    else:
        odd=odd+1	   
  
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)