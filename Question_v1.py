

#using dictionaries in order to store the questions, choices, and answers
from random import shuffle
quiz = [
["What is the best selling video game of all time?",
 {'answer' :'b', 'choice' : 'a. Roblox \nb. Minecraft \nc. GTA V \nd. Call of Duty \n'}
 ],
["Which of these consoles is the highest selling to date?",
 {'answer' :'a', 'choice' : 'a. PS2 \nb. Nintendo DS \nc. PS4 \nd. Xbox\n'}
 ],
["What game did mario first apear in?",
 {'answer' :'c', 'choice' : 'a. Mario kart \nb. Donkey kong \nc. Super mario bro 35 \nd. Super galaxy mario\n'}
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
total = 10
index = 0
score = 0
optnum = 0
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
            print("yeah you got it right!")
            score +=1
            print("your score is", score)
        else:
                print("you got it wrong")
                print("your score is still",score)
        del quiz[0]

#user_details()
#instructions()
#status()

print("Please enter the alphabet for chosen option")
print("You have succesfully completed Sean's Game Quiz!")
print("Your final score is", score,"out of",total)
print("That means you answered", (round(score/total*100,2)),"% of the questions correctly!")
print("Thanks for playing")
feedback = int(input("How would you rate the quiz from 1-5?: "))


print("Thank you for the feedback!")
exit()


