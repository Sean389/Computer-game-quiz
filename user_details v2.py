#instructions v3

while True:
   
    inst = input("Would you like to read the instructions on how to play the game?\n a)Yes\n b)no\nEnter here: ").lower()
   
    if inst == 'yes' or inst == 'a'or inst == 'y' :
        print("The instructions are simple, you will be given random multiple choice questions about Games and you have to choose which answer you think is right. ")
        break
    if inst == 'No' or inst == 'no' or inst == 'B' or inst == 'b' or inst == 'n' or inst == 'N' :
        print("Welcome to Sean game quiz, have fun!")
        break
    else:
        print("<><><><><><><><><><><><><><><><><><><>")
        print("Please enter the options provided only")
        print("<><><><><><><><><><><><><><><><><><><>") 
            
