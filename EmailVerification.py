#Devon Soto
#Code to verify email addresses
#Read README on how to run


import re

# return True if s is a valid email, else return False
def fun(s):

    #check to see if there is a  @ sign in the code.
    pos_at = s.find('@')

    if(pos_at == -1):
        print("{email} is not a valid email, missing @.".format(email=s))
        return False

    #email addresses with at most 3 letters after '.'
    pos_dot = s.find('.',pos_at)
    if(len(s[pos_dot+1:]) > 3 or pos_dot == -1):
        print("Your length of extension, {}, is greater than 3 or {} could not be found".format(len(s[pos_dot+1:]), '.'))
        return False

    #Loop through to see if there is only valid characters in username
    username_length = len(s[:pos_at])
    username = re.sub("[^a-zA-Z0-9\-\_]", '', s[:pos_at])   #replacing every invalid character
    if(len(username) != username_length or username_length == 0):
        print("Username: {} . Username after subsituting invalid characters: {}. Invalid characters in username.".format(s[:pos_at],username))
        return False

    #Loop through to see if there is only valid characters in website
    website_length = len(s[pos_at+1:pos_dot])   #gettinf from @ -> .
    website = re.sub("[^a-zA-Z0-9]", '',s[pos_at+1:pos_dot])
    if(len(s[pos_at+1:pos_dot]) != len(website)):
        print("Beginning website: {}. Website after: {}. Invalid characters in website.".format(s[pos_at+1:pos_dot],website))
        return False
    else:
        return True



#return a sorted list of valid email
n = int(input("Enter the number of emails: "))
valid_elist = []

for i in range(0,n):
    email = input("Enter email address: ")
    if(fun(email) == True):
        valid_elist.append(email)

print(sorted(valid_elist))
