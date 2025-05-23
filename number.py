import random

while(True):
    print("Welcome To The Game!!")
    print("1.Start A New Game!!")
    print("2. Exit!!")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        random_num = random.randint(1,5)
        number = int(input("Give A Number Between 1 to 5 : "))

        if number == random_num:
            print("Congo!! You Win!")
        else:
            print("You Loss!!")
    elif choice == 2:
        print("Thank You!!")
    else:
        print("Invalid Choice!!")