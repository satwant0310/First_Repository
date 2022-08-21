import random
win_number=random.randint(1,11)
# random.randrange(1,11) this is the way to generate random number in python
# added a test comment
ch = 0
while ch >= 0:
    if ch == 0:
        gues_number=int(input("Please Gues any randon number between 1-10: "))
    else:
         gues_number=int(input("Gues again: "))
    ch += 1
    if gues_number >10:
        print("Please enter number between 1-10 ")
    else:
        if gues_number==win_number:
            print(f"you win, you guessed it in {ch} times")
            #print (f"{win_number}")
            break
        else:
            if gues_number < win_number:
                print("too low")
                #print (f"{win_number}")
                continue
            else:
                print("too high")
                #print (f"{win_number}")
                continue
