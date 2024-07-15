from time import time
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed, 2)

while True:
    ck = input("Ready To test: yes / no: ")
    if ck == 'yes':
        p1 = "In a bustling city filled with the hum of activity, Jane found solace in a small, quaint bookstore nestled between towering skyscrapers. The store, with its worn wooden shelves and cozy reading nooks, was a sanctuary for book lovers."
        p2 = "As the sun dipped below the horizon, casting a golden hue over the tranquil lake, Emily sat on the dock, her feet dangling above the water. The gentle lapping of the waves against the wooden planks provided a soothing rhythm, a stark contrast to the hectic pace of her daily life."
        p3 = "In the heart of the bustling marketplace, vendors called out to passersby, showcasing their vibrant array of goods. Stalls overflowed with colorful fruits, aromatic spices, and handcrafted trinkets. The air was filled with a symphony of sounds – the chatter of shoppers, the clinking of coins, and the occasional laughter of children darting between the stalls."
        test = [p1, p2, p3]
        test1 = r.choice(test)
        print("***** Typing Speed Calculator *****")
        print(test1)
        print("\n")
        time_1 = time()
        testinput = input("Enter: ")
        time_2 = time()

        print("Speed :", speed_time(time_1, time_2, testinput), "w/s")
        print("Error: ", mistake(test1, testinput))    
    elif ck == 'no':
        print("Thank You")
        break
    else:
        print("Invalid Input")
