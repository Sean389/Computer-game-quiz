while True:
   
    inst = input("Would you like to read the instructions on how to play the game?\n Press Y to continue or any other key to exit : ").lower()
   
    if inst == 'yes' or inst == 'a'or inst == 'y' :
        print("The instructions are simple, you will be given random multiple choice questions about Games and you have to choose which answer you think is right. ")
        break
    else:
        exit()
