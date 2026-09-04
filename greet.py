def MasterGreeter():
    reps = 10 # number of greetings
    name = input("What should I call you? \n")

    for i in range(reps):
        print("Hello master " + name + " " + str(reps-i))


MasterGreeter()