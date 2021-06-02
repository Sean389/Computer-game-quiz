def instructions():
            while True:
                        inst = input("Would you like to read the instructions?\na)yes\nb)no\nEnter here: ").lower()
                        if inst == "yes" or inst == "y" or inst == "yea" or inst == "a":
                                    print("Rules r simple. Answer the multi choice questions by entering (a/b/c/d). For every question you get right you earn a point for every wrong you get nothing.")
                                    break
                        if inst == "no" or inst == "n" or inst == "nah" or inst == "b" :
                                    print("Welcome to Sean's game quiz")
                                    break
                        else:
                                    print("Please enter the options")

