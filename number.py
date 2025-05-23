import random

while(True):
    print("\n")
    print("Welcome To The Game!!")
    print("1.Start A New Game!!")
    print("2. Exit!!")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        random_num = random.randint(1,5)
        number = int(input("Give A Number Between 1 to 5 : "))

        if number == random_num:
            print("Congo!! You Win!")
            print("\n")
        else:
            print("You Loss!!")
            print("\n")
    elif choice == 2:
        print("Thank You!!")
        print("\n")
        break
    else:
        print("Invalid Choice!!")
        print("\n")