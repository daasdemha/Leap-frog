#source python programing class from 1 to 10 on qmul plus
#https://qmplus.qmul.ac.uk/course/view.php?id=5525
print("Game")
print("Leap Frog")
print("There Are A Total Of Seven Amphibians")
print("Three Frogs, Three Toads And A Blank Space In Between")
Amphibians=["F","F","F","_","T","T","T"]  
print(Amphibians)
print("The Goal Of This Game Is To Move The Toads To The Left And The Frogs The Right Side")
print(input("Press Enter TO Continue"))
print("")
print("Rules")
print("1.You Can Only Move Once Per Turn")
print("2.Frogs Can Only Move Right")
print("3.Toads Can Only Move Left")
print("4.Toads And Frogs Can Only Move To The Blank Space")
print("5.Frogs And Toads can Hop Over Each Other Given That The Blank Space Is After The Frog/Toad You Are Hoping Over")
print("6.Toads And Frogs Cannot Jump Over Two OR More Amphibians")
print("7.Toads And Frogs Cannot Move More Then One Space")
print("8.When moving From A Space To A Space Please Dont Use Other Alphebets Other Then The Given Alphabets  AS They Will Not Be Counted AS Variables")
print(input("Press Enter To Begin Game"))
print("")


#source:from task 2
def menu():
  choice = input("""
  A: Tutorial
  B: Play Game 
  Q: Exit
  Please enter your choice: """)
 
  if choice == "A" or choice =="a":
   #the tutorial just tells you how and how not to play the game its the first thing i made so the code is quite easy
   print("Turtorial")
   Demo=["F","F","F","_","T","T","T"]   
   print(Demo)
  
   print(input("Turn 1 \n Press Enter"))
   print("From: 7")
   print("To: 1")
   print("Invalid Move You Can Only Jump One Space")
   Demo0_1=["F","F","F","_","T","T","T"] 
   print(Demo0_1) 
 
 
 
   print(input("Turn 1 \n Press Enter"))
   print("From: 5")
   print("To: 4")
   Demo2=["F","F","F","T","_","T","T"] 
   print(Demo2)

   print(input("Turn 2 \n Press Enter"))
   print("From: 3")
   print("To: 5")
   Demo3=["F","F","_","T","F","T","T"] 
   print(Demo3)

   print(input("Turn 3 \n Press Enter"))
   print("From: 6")
   print("To: 5")
   print(Demo3) 
   print("Invalid Move Please Move To A Blank Space")
   print("")

   print(input("Turn 3 \n Press Enter"))
   print("From: 2")
   print("To: 3")
   Demo4=["F","_","F","T","F","T","T"] 
   print(Demo4)

   print(input("Turn 4 \n Press Enter"))
   print("From: 4")
   print("To: 2")
   Demo5=["F","T","F","_","F","T","T"] 
   print(Demo5)

   print(input("Turn 5 \n Press Enter"))
   print("From: 6")
   print("To: 4")
   Demo6=["F","T","F","T","F","_","T"] 
   print(Demo6)

   print(input("Turn 6 \n Press Enter"))
   print("From: 6")
   print("To: 4")
   Demo7=["F","T","F","T","F","T","_"] 
   print(Demo7)

   print(input("Turn 7 \n Press Enter"))
   print("From: 7")
   print("To: 6")
   Demo8=["F","T","F","T","F","T","_"] 
   print(Demo8)

   print(input("Turn 8 \n Press Enter"))
   print("From: 5")
   print("To: 7")
   Demo9=["F","T","F","T","_","T","F"] 
   print(Demo9)

   print(input("Turn 9 \n Press Enter"))
   print("From: 3")
   print("To: 5")
   Demo9=["F","T","_","T","F","T","F"] 
   print(Demo9)

   print(input("Turn 10 \n Press Enter"))
   print("From: 1")
   print("To: 3")
   Demo10=["_","T","F","T","F","T","F"] 
   print(Demo10)

   print(input("Turn 11 \n Press Enter"))
   print("From: 2")
   print("To: 1")
   Demo11=["T","_","F","T","F","T","F"] 
   print(Demo11)

   print(input("Turn 12 \n Press Enter"))
   print("From: 4")
   print("To: 2")
   Demo12=["T","T","F","_","F","T","F"] 
   print(Demo12)

   print(input("Turn 13 \n Press Enter"))
   print("From: 6")
   print("To: 4")
   Demo13=["T","T","F","T","F","_","F"] 
   print(Demo13)

   print(input("Turn 14 \n Press Enter"))
   print("From:5 ")
   print("To: 6")
   Demo14=["T","T","F","T","_","F","F"] 
   print(Demo14)

   print(input("Turn 15 \n Press Enter"))
   print("From: 3")
   print("To: 5")
   Demo15=["T","T","_","T","F","F","F"] 
   print(Demo15)

   print(input("Turn 15 \n Press Enter"))
   print("From: 4")
   print("To: 3")
   Demo16=["T","T","T","_","F","F","F"] 
   print(Demo16)
   print("")
   menu()
  
  elif choice == "B" or choice =="b":
    #this is the actual game i tired to make it understandable as possiable so hence the rules
    #a short demo is included if player does not still understand the game
    amphibians = ["F", "F", "F", " ", "T", "T", "T"]

    def Jump(amphibians, A, B):

        A -= 1

        B -= 1

        Alter = amphibians[A]

        amphibians[A] = amphibians[B]

        amphibians[B] = Alter

        print(amphibians)

    def is_valid(amphibians, A, B):

        A -= 1

        B -= 1

        if A < 0 or A >= len(amphibians):

            return False

        if B < 0 or B >= len(amphibians):

            return False

        Word = amphibians[A]

        if Word == "F":

            if amphibians[B] == "T":

                return False

            if amphibians[A+1] == " ":

                return True

            if amphibians[A+1] == "T" and amphibians[A+2] == " ":

                return True

        if Word == "T":

            if amphibians[B] == "F":

                return False

            if amphibians[A-1] == " ":

                return True

            if amphibians[A-1] == "F" and amphibians[A-2] == " ":

                return True

        return False

    def demonstrate():

        amphibians = ["F", "F", "F", " ", "T", "T", "T"]
        print(amphibians)

        Jump(amphibians, 3, 4)

        Jump(amphibians, 5, 3)

        Jump(amphibians, 6, 5)

        Jump(amphibians, 4, 6)

        Jump(amphibians, 2, 4)

        Jump(amphibians, 1, 2)

        Jump(amphibians, 3, 1)

        Jump(amphibians, 5, 3)

        Jump(amphibians, 7, 5)

        Jump(amphibians, 6, 7)

        Jump(amphibians, 4, 6)

        Jump(amphibians, 2, 4)

        Jump(amphibians, 3, 2)

        Jump(amphibians, 5, 3)

        Jump(amphibians, 4, 5)

    print("Type D For A Short Demo,Type R Restart Or Type Q To Retun To The Main Menu")
    print(amphibians)
    while True:
        Value1 = input("from: ")
        if Value1 == "d" or Value1 == "D":
            demonstrate()
            print("reset")
            amphibians = ["F", "F", "F", " ", "T", "T", "T"]
            print(amphibians)
            continue
        if Value1 == "r" or Value1 == "R":
            print("reset")
            amphibians = ["F", "F", "F", " ", "T", "T", "T"]
            print(amphibians)
        if Value1 == "q" or Value1 == "Q":
            menu()
        Value2 = input("to: ")
        if Value2 == "d" or Value2 == "D":
            demonstrate()
            amphibians = ["F", "F", "F", " ", "T", "T", "T"]
            print(amphibians)
            continue
        if Value2 == "r" or Value2 == "R":
            print("reset")
            amphibians = ["F", "F", "F", "", "T", "T", "T"]
            print(amphibians)
        if Value2 == "q" or Value2 == "Q":
            menu()
        A = int(Value1)
        B = int(Value2)
        if is_valid(amphibians, A, B):

            Jump(amphibians, A, B)
        else:

            print("Invalid Move \n Jump One Space Only \n Jump Only To A Blank Space \n You Can Not Jump Over Two Amphibians \n Frogs Can Only Move Right \n Toads Can Only Move Left \n You Can Only Move To A Empty Space \n You Cannot Move The Blank Space Move A Amphibian Instead \n Try Again")


  elif choice=="Q" or choice=="q":
     print("")
     print("End Game")
     print("Goodbye")
     exit()
  else:
      print("You Must Only Select Either A Or B.")
      print("Please Try Again")
      menu()
menu()
