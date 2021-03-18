# import re
 
# def check_num(s):
     
#     # 1) Begins with 0 or 91
#     # 2) Then contains 7 or 8 or 9.
#     # 3) Then contains 9 digits
#     Num = re.compile("(0/91)?[7-9][0-9]{9}")
#     return Num.match(s)
 
# # Driver Code
# s = "347873923408"
# if (isValid(s)): 
#     print ("Valid Number")     
# else :
#     print ("Invalid Number") 
    
    
#importing regular expression(regex) library
import re 
  
# Make a regular expression 
# for validating an Email 
regex = '^(0/91)?[7-9][0-9]{9}$'
      
# Defining a function for 
# for validating an Email 
def check(number):  
  
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex,number)):  
        print("Valid Number")  
          
    else:  
        print("Invalid Number")  
      
  
# Driver Code  
if __name__ == '__main__' :  
    number = input("Enter Mobile Number: ")
    check(number)


 
 