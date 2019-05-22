"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""

"""
Challenge 2
    Print the secret number and guess number when Player loses using format function 
"""

"""
Challenge 3
    Print too HIGH or too LOW messages for bad guesses using elif. 
"""


"""
Challenge 4
    Let people play again and again until he guesses the right secret number
"""


"""
Challenge 5
Limit the number of guesses to maximum 6 tries 
"""


"""
Challenge 6
    Print the number of tries left 
"""


"""
Challenge 7
    Lets give user the option to play again
"""

"""
Challenge 8
    Catch when someone submits a non integer
"""





import random
i=0
while  i<6:
    s_number=random.randrange(1,11)
    g_number=int(input("enter a number"))
    if type(g_number)!=int:
        print("please enter integer value")
        break
    elif s_number==g_number:
        print("player wins computer lose") 
        break
    else:
        print("player lose and computer wins")
        print("guess number={}".format(g_number))
        print("secret number={}".format(s_number))
        print("try again "+"number of tries left={}".format(5-i))
        chance=int(input("press 0 to exit any any other key to play again"))
        if chance==0:
            break
    i=i+1