import string
import random
maxlength = int(input("Enter maximum limit of letters you want in your password:"))
res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = maxlength)) 
print("The generated random password: " + str(res))
