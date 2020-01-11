import re 
# regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
regex  =  '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def check(email):  
    if(re.search(regex,email)):  
        print("Valid Email")  
          
    else:  
        print("Invalid Email")  
email = "john.jagu25@gmai.l.com"
check(email) 


a = '[0-9a-zA-Z]+'
print(re.findall("^\w+b*$","testingbb"))