num = int(input("Enter a number: "))  
sum = 0  
n = num  
  
while n > 0:  
   rem = n % 10  
   sum += rem ** 3  
   n //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number") 
