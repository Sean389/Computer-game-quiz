#print("///Welome to the game quiz:///")
print("Welcome to my quiz")

while True:
    name=input("Enter yout name? :")
    if name.isalpha() :
        break
    print("Please enter charecters A-Z only")


while True:
    age = (input("Please enter age? :"))
    if age.isnumeric():
        break
    print("Please enter numbers only")

    
print("Hello", name, "are you",age,"old")
'''This is my next change for asking user details in the previous program tge bbane acceot
numbers and age and yearlevel accepted string.
I will create the proper datatype so that name will accept only strings and age'''

 
    
