from random import shuffle

def user_details():
    global name
    while True:
        name = input("Please Enter Your Name: ").capitalize()
        if name.isalpha():
            break
        else:
            print("Please Enter Only Letters")
        
        
       

def instructions():
    inst = input("Please enter y to read the insturctions and any other key to skip : ")
    if inst == 'yes' or inst == 'a'or inst == 'y' :
        print("\nThe instructions are simple, its a multi choice quiz answer a,b,c,d and enjoy!.")
    else:
        pass
        

           
def status():
            status = input("Would you like to play the quiz?\nEnter y to continue or n to exit the quiz : ").lower()
            if status == "y" or status == "yes":
                        print("We shall begin shortly")
            else:
                        
                        exit()

def rounds():
            global r, total
            while True:
                        try:
                                    r = int(input("Please enter the number of questions you would like to answer between 1-10: "))
                                    if 0<r<=10:
                                                break
                                    else:
                                                print("Please enter numbers 1-10 only")
                        except:
                                    print('Please enter numbers only')

            total = r

#using dictionaries in order to store the questions, choices, and answers
quiz = [
["What is the best selling video game of all time?",
 {'answer' :'b', 'choice' : 'a. Roblox \nb. Minecraft \nc. GTA V \nd. Call of Duty \n'}
 ],
["Which of these consoles is the highest selling to date?",
 {'answer' :'a', 'choice' : 'a. PS2 \nb. Nintendo DS \nc. PS4 \nd. Xbox\n'}
 ],
["What game did mario first apear in?",
 {'answer' :'b', 'choice' : 'a. Mario kart \nb. Donkey kong \nc. Super mario bro 35 \nd. Super galaxy mario\n'}
 ],
["How many cards in a full deck of regular playing cards including the jokers?",
 {'answer' :'a', 'choice' : 'a. 54 \nb. 52 \nc. 50 \nd. 48\n'}
 ],
["Who is known as the unkillable demon king?",
 {'answer' :'c', 'choice' : 'a. Bjergsen \nb. Huni \nc. Faker \nd. Madlife\n'}
 ],
["What does frag mean?",
 {'answer' :'b', 'choice' : 'a. Flash bang \nb. Top of the leader board \nc. Frag grenades \nd. Smoke grenades\n'}
 ],
["What colour is the ghost inky?",
 {'answer' :'d', 'choice' : 'a. red \nb. orange \nc. pink \nd. cyan\n'}
 ],
["Who is known as the potato king?",
 {'answer' :'c', 'choice' : 'a. Dream \nb. Skeppy \nc. technoblade \nd. skeppy\n'}
 ],
["Who won worlds 3 times in a row?",
 {'answer' :'a', 'choice' : 'a. Skt \nb. TSM \nc. C9 \nd. fanatic\n'}
 ],
["Blizzard Entertainment is most well known for what video game franchise?",
 {'answer' :'d', 'choice' : 'a.Hearthstone \nb.Fortnite \nc.Overwatch \nd.World of Warcraft\n'}
 ],


]

shuffle(quiz)

index = 0
score = 0
optnum = 0

user_details()
instructions()
status()
rounds()

while r>0:
            data = quiz[0]
            q = data[0]
            data = data[1]
            answer = data['answer']
            choice = data['choice']

            print(q)
            print(choice)
            while True:
                        user_answer = input ("Please enter one of the options (a/b/c/d): ").lower().replace(' ','')
                        if user_answer == 'a' or user_answer == 'b' or user_answer == 'c' or user_answer == 'd':
                                    if user_answer == answer:
                                                print("\n<><><><><><><><><><><><><><>")    
                                                print("Congrats you got it correct")
                                                print("<><><><><><><><><><><><><><>\n") 
                                                score +=1
                                                print("your score is", score)
                                    else:
                                                print("\n><><><><><><><><><><><><><><><><><><><") 
                                                print("You got it wrong better, luck next time! The answer is:", answer)
                                                print("><><><><><><><><><><><><><><><><><><><\n") 
                                                print("your score is still",score)

                                    del quiz[0]
                                    r-=1
                                    break
                        else:
                                    print("Please enter the alphabet for chosen option")
print("You have succesfully completed Sean's Game Quiz!")
print(name,"Your final score is", score,"out of",total)
print("That means you answered", (round(score/total*100,2)),"% of the questions correctly!")
print("Thanks for playing")


def feedback():
  while True:
    try:
      f = int(input("How would you rate the quiz from 1-10?: "))
      if 0<f<=10:
        break
      else:
        print("\nPlease enter numbers 1-10 only\n")
        
    except:
      print('\nPlease enter numbers only\n')
feedback()
    
print("Thank you for the feedback!")
exit()
