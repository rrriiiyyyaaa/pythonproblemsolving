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