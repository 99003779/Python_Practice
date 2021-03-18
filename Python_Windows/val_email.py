#importing regular expression(regex) library
import re 
  
# Make a regular expression 
# for validating an Email 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
      
# Defining a function for 
# for validating an Email 
def check(email):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        print("Valid Email")  
          
    else:  
        print("Invalid Email")  
      
  
# Driver Code  
if __name__ == '__main__' :  
    email = input("Enter email: ")
    check(email)

