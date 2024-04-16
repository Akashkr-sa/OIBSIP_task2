import random
num="1234567890"
Ucase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lcase="abcdefghijklmnopqrstuvwxyz"
symbols="!@$%^&*()_-+-{}{}:\*;\'>,.?//\\"
password=" "
word=" "
len=int(input("Enter Length: "))
print("yes or no")
Uppercase= str(input("Do you want Upper case letter in passward: "))
Lowercase = str(input("Do you want lower case letters in passward: "))
n=str(input("Do you want number in passward: "))
sy=str(input("Do you want symbols in passward: "))

try:
	if Uppercase =="yes":
		word+=Ucase
	if Lowercase =="yes":
		word+=Lcase	
	if n=="yes":
		word+=num
	if sy =="yes":
		word += symbols
	for a in range(len):
		password+=random.choice(word)
	print(password)
except IndexError:
	print("Password can be made of letters, numbers, symbols. You have to set atleast")