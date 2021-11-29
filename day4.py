'''   
  Check the  given no. is a leap year.
'''

def leap(Year):
    

  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  (Year % 100 != 0 and  Year % 4 == 0)):   
        print( Year , "is a leap Year.");  
  
  else:  
        print (Year , "is not a leap Year.") 
        Year = int(input("Enter the number: ")) 
 

leap(Year)  

'''
   Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
'''


print('Print the sum of the current number and the previous number')
pre_num = 0
for i in range(1,11):
    sum = pre_num + i
    print('Current number=', i,"Previous number=", pre_num,'Sum = ', pre_num + i)
    pre_num = i
    
