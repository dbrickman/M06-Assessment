#imports
import random

def wheel(): #Wheel function
    global outputs, amount
    outputs = ['BANKRUPT', 'BANKRUPT', 'Lose a turn', 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 500, 900, 300, 400] #All possible Values wheel can land on
    amount = outputs[random.randint(0,len(outputs)-1)] #Randomize outputs
#---------------------------------------------------------------------------------------
def get_word(): #Get word function
    global word
    word_list = open("words_alpha.txt") #Word document
    words = word_list.readlines()
    word=words[random.randint(0,len(words)-1)] #Get random word
    global already_guessed 
    already_guessed = set() 
#---------------------------------------------------------------------------------------
def round(): #player turn function
    global player1_round_score, player2_round_score, player3_round_score, player_going, guess, winning_round_score
    player1_round_score=0 #initialize round score for each player
    player2_round_score=0
    player3_round_score=0
    get_word() #Gets word for the round
    dash = ""
    for i in range(0, len(word)-1): #creates word in dashed form 
        if word[i] in already_guessed:
            dash += word[i] + ""
        else:
            dash+="_"
    print('The word contains ' + str(len(word)-1) + " letters.")  #Tells players how many letters there are in the word
    list_dash = list(dash)
    print(list_dash) #Prints word in dashed form 

    player_going = player_playing_1st #Gets starting player for the round
    while player_going < 10000: #Keeps game going
        round_score = 0 #Resets round score for each players turn
        if player_going % 3 == 0: #Adds name to the player
            player_going_name = player1
            round_score = player1_round_score #Shows current round score for the current player
        elif player_going % 3 == 1:
            player_going_name = player2
            round_score = player2_round_score
        elif player_going % 3 == 2:
            player_going_name = player3
            round_score = player3_round_score
        print(player1 + "'s round score is " + str(player1_round_score)) #Shows each players round score at the start of each guess
        print(player2 + "'s round score is " + str(player2_round_score))    
        print(player3 + "'s round score is " + str(player3_round_score))
        print(player_going_name + " is up.") #Tells which player is up
        wheel() #Gets random value from our wheel
        print("The wheel landed on " + str(amount)) #Tells player random value of wheel
        if amount == "BANKRUPT": #When wheel lands on BANKRUPT
            print("Oof, your round score has been reset to 0. It is now the next player's turn.")
            if player_going % 3 == 0: #Resets that players round score to 0
                player1_round_score = 0
            elif player_going % 3 == 1:
                player2_round_score = 0
            elif player_going % 3 == 2:
               player3_round_score = 0
            player_going = player_going + 1 #Advances to next player
        elif amount == "Lose a turn": #When wheel lands on Lose a Turn
            print("Oof, you lost your turn. It is now the next player's turn.")
            player_going = player_going + 1 #Advances to next player
        else:            
            word_letter = "no"
            while word_letter != "word" and word_letter != "letter":
                word_letter = str(input("Would you like to guess the 'word' or choose a 'letter'? ")) #Ask user whether they want to guess the word or a letter
                if word_letter != "word" and word_letter != "letter": #Saftey check
                    print("Please type 'word' or 'letter")
            if word_letter == "word": #When player guessess word
                guess = str(input("What word would you like to guess? "))
                if guess in word: #If they guess the word
                    print("Congrats, you won the round. Your total for this round has been added to your overall total")
                    if player_going % 3 == 0: #Adds the player who guessed the word round score to variable to be added to bank
                        player1_round_score = round_score
                        winning_round_score = player1_round_score 
                    elif player_going % 3 == 1:
                        player2_round_score = round_score
                        winning_round_score = player2_round_score           
                    elif player_going % 3 == 2:
                        player3_round_score = round_score
                        winning_round_score = player3_round_score 
                    break #Ends the round                                          
                else: #Player failed at guessing the word
                    print("That was not the word")                  
                    player_going = player_going + 1 #Advances player
                    continue
            else: #Player chooses to guess a letter
                if round_score >= 250: #Player can only guess a vowel if score is > 250
                    if 'a' not in already_guessed or 'e' not in already_guessed or 'i' not in already_guessed or 'o' not in already_guessed or 'u' not in already_guessed: #Safety if all the vowels have been guessed
                        vowel = str(input("Would you like to buy a vowel for 250? [y/n] "))
                        while vowel != "y" and vowel != "n": #Safety, player can only enter y or n
                            print("Please only type in 'y' or 'n'")
                            vowel = str(input("Would you like to buy a vowel for 250? [y/n] "))
                    else: #If all vowels are checked, they can't guess a vowel
                        vowel == 'n'
                    if vowel == 'y': #They choose to guess a vowel
                        round_score = round_score - 250 #It costs 250 to guess a vowel
                        guess = False
                        while guess != True: #Loop for players guess
                            guess = str(input("What letter would you like to guess? ")) 
                            if len(guess) > 1: #Only allows player to enter 1 letter
                                print("Please only enter 1 letter")
                            elif guess in already_guessed: #Safety check if letter has already been guessed
                                print("That letter has already been guessed. Please guess a different letter")
                            elif guess != 'a' and guess != 'e' and guess != 'i' and guess != 'o' and guess !='u': #Safety check making sure player guesses a vowel
                                print("Please only guess a vowel. You bought a vowel. The vowels are a-e-i-o-u")
                            elif guess not in word: #If the vowel is not in the word
                                print("There are 0 " + guess + "'s in the word") #Informs player that there guess is not in the word
                                already_guessed.add(guess) #Add letter to already_guessed table
                                if player_going % 3 == 0: #Adds players round score to their total round score
                                    player1_round_score = round_score
                                elif player_going % 3 == 1:
                                    player2_round_score = round_score          
                                elif player_going % 3 == 2:
                                    player3_round_score = round_score                  
                                player_going = player_going + 1   #Advances to next player               
                                guess = True #Exits loop
                            else: #Vowel is in word
                                already_guessed.add(guess) #Adds letter to already_guessed table
                                dash = ""
                                v=0 #Initializes value for the score they get for guessing the letter
                                for i in range(0, len(word)-1): #Reveals letter placement in word
                                    if word[i] in guess:
                                        dash += word[i] + ""
                                        v_new = v+1 #Calculates how many times that letter was in the word (temp value)
                                        v=v_new #Puts the above value into the variable
                                    else:
                                        dash+="_"
                                print("There are " + str(v_new) + " " + guess + "'s in the word.") #Informs player how many times there guess appears in the word
                                round_score = v_new * amount + round_score #Calculates score for guessing that letter
                                if player_going % 3 == 0: #Adds score to the players round score
                                    player1_round_score = round_score 
                                elif player_going % 3 == 1:
                                    player2_round_score = round_score 
                                elif player_going % 3 == 2:
                                    player3_round_score = round_score 
                                guess = True #Exits loop                        
                    else: #Player has >=250 points but chooses not to guess a vowel
                        guess = False
                        while guess != True:
                            guess = str(input("What letter would you like to guess? ")) #Plaeyr inputs guess
                            if len(guess) > 1: #Saftey to make sure they only enter one letter
                                print("Please only enter 1 letter")
                            elif guess in already_guessed: #Check to see if letter has already been guessed
                                print("That letter has already been guessed. Please guess a different letter")
                            elif guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess =='u': #Reminding them they chose to guess a consonant
                                print("Please only guess a consonant. You chose not to buy a vowel")
                            elif guess not in word: #The consonant they guessed was not in the word
                                print("There are 0 " + guess + "'s in the word")
                                already_guessed.add(guess) #Adds guess to already_guessed
                                if player_going % 3 == 0: #Adds round score to players total round score
                                    player1_round_score = round_score
                                elif player_going % 3 == 1:
                                    player2_round_score = round_score 
                                elif player_going % 3 == 2:
                                    player3_round_score = round_score 
                                player_going = player_going + 1           
                                guess = True #Exits loop
                            else: #Guess is in word
                                already_guessed.add(guess) #Adds guess to already_guessed
                                dash = ""
                                v=0 #Initializes variable for calculating score 
                                for i in range(0, len(word)-1): #Reveals letter placement in word
                                    if word[i] in guess:
                                        dash += word[i] + ""
                                        v_new = v+1 #Calculates how many times letter appeared in the word (temp value)
                                        v=v_new #Assigns temp value to main variable value
                                    else:
                                        dash+="_"
                                print("There are " + str(v_new) + " " + guess + "'s in the word.") #Tells player how many times their guess appeared in the word
                                round_score = v_new * amount + round_score #Calculates score for guessing that letter correctly
                                if player_going % 3 == 0: #Adds score for that guess to overall round score
                                    player1_round_score = round_score 
                                elif player_going % 3 == 1:
                                    player2_round_score = round_score 
                                elif player_going % 3 == 2:
                                    player3_round_score = round_score 
                                guess = True #Exits loop
                else: #Not enough money to even buy a vowel (skips over question)
                    guess = False
                    while guess != True:
                        guess = str(input("What letter would you like to guess? ")) #Gets guess
                        if len(guess) > 1: #Make sure guess is only 1 letter
                            print("Please only enter 1 letter")
                        elif guess in already_guessed: #Make sure guess hasn't been gussed before
                            print("That letter has already been guessed. Please guess a different letter")
                        elif guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess =='u': #Lets player know they don't have enough money to buy a vowel
                            print("Please only guess a consonant. You don't have enough money to buy a vowel")
                        elif guess not in word: #If letter guessed is not in the word
                            print("There are 0 " + guess + "'s in the word") #Informs player
                            already_guessed.add(guess) #Adds that guess to already_guessed
                            if player_going % 3 == 0: #Ads round score to overall round score for that player
                                player1_round_score = round_score
                            elif player_going % 3 == 1:
                                player2_round_score = round_score 
                            elif player_going % 3 == 2:
                                player3_round_score = round_score 
                            player_going = player_going + 1          
                            guess = True #Exits loop
                        else: #Player correctly guessed a letter
                            already_guessed.add(guess) #Adds guess to already_guessed
                            dash = ""
                            v=0 #Initializes score for that letter
                            for i in range(0, len(word)-1): #Reveals letter placement in word
                                if word[i] in guess:
                                    dash += word[i] + ""
                                    v_new = v+1 #Calculates how many times that letter appeared in the word (temp value)
                                    v=v_new #Adds previous calculation to main variable
                                else:
                                    dash+="_"
                            print("There are " + str(v_new) + " " + guess + "'s in the word.") #Informs player how many times that letter appeared in the word
                            round_score = v_new * amount + round_score #Calculates score for correctly guessing that letter
                            if player_going % 3 == 0: #Adds score for that guess to players overall score for that round
                                player1_round_score = round_score 
                            elif player_going % 3 == 1:
                                player2_round_score = round_score 
                            elif player_going % 3 == 2:
                                player3_round_score = round_score + player3_round_score
                            guess = True #Exits loop
        dash = ""
        for i in range(0, len(word)-1): #creates word in dashed form and reveals letters in already_guessed
            if word[i] in already_guessed:
                dash += word[i] + ""
            else:
                dash+="_"
        print('The word contains ' + str(len(word)-1) + " letters.")  #Informs players how many letters are in the word
        list_dash = list(dash)
        print(list_dash) #Prints word in dashed form with letters revealed as they are guessed

#---------------------------------------------------------------------------------------
def final_spin(): #Final round function
    print("Congratulations " + final_spin_player + " for making it to the Final Round! Your goal is to guess the word correctly.")
    get_word() #Gets random word that needs to be guessed
    guess = ' '
    rstlne = ['r', 's', 't', 'l', 'n', 'e']
    dash = ""
    for i in range(0,6): #Adds r-s-t-l-n-e to already_guessed
        guess = rstlne[i]
        already_guessed.add(guess)
        i = i+1     
    for i in range(0, len(word)-1): #Creates word in dashed form and reveals letters in already_guessed (just r-s-t-l-n-e as of now)
        if word[i] in already_guessed:
            dash += word[i] + ""
        else:
            dash+="_"
     
    print('The word contains ' + str(len(word)-1) + " letters. R-S-T-L-N-E have already been guessed")  #Informs player how many letters there are in the word
    list_dash = list(dash)
    print(list_dash) #Prints off word with rstlne revealed
    
    print("Please guess 3 consonants and 1 vowel") #Asks player to guess specific amount of letters
    i=0
    while i < 3: #User guesses 3 consonants
        guess = str(input("Consonant " + str(i+1) + ": "))
        if guess == 'a' or guess == 'i' or guess == 'o' or guess == 'u': #Can't guess a vowel
            print("That is a vowel")
        elif guess in already_guessed: #If that letter has alreayd been guessed
            print("That letter has already been guessed")
        else: #Adds guess to already_guessed
            already_guessed.add(guess)
            i=i+1 #Increases i so that user guesses 3 consonants then can exit this loop
    i=0
    while i < 1: #User guesses 1 vowel
        guess = str(input("Vowel: "))
        if guess in already_guessed: #If vowel has already been guessed
            print("That letter has already been guessed")
        elif guess  == 'a' or guess == 'i' or guess == 'o' or guess == 'u': 
            already_guessed.add(guess) #Adds guess to already_guessed
            i=i+1 #Increases i to exit the loop    
        else: #If user did not input a vowel
            print("That is not a vowel")

    dash = ""
    for i in range(0, len(word)-1): #Creates word in dashed form with every letter that has already been guessed revealed
        if word[i] in already_guessed:
            dash += word[i] + ""
        else:
            dash+="_"

    print('The word contains ' + str(len(word)-1) + " letters.")  #Informs players how many letters are in the word
    list_dash = list(dash)
    print(list_dash) #Shows rstlne + user gussed 3 consanants 1 vowel placement in word

    guess = str(input("You now have 1 try to guess the word. Good luck: ")) #User guesses word
    if guess in word: #If they guessed the word correctly
        print("Congrats, you won the game. Your prize is $1,000,000!!!!!!")
    else: #If they did not guess the word correctly
        print("I'm sorry, that was not the word. The correct word was " + word + "You would have won $1,000,000 had you guessed the word correctly. Better luck next time")
#---------------------------------------------------------------------------------------
print("WELCOME TO WHEEL OF FORTUNE!") #Welcome message pt1
print("This is a 3 player game")
player1 = str(input("Please enter the 1st player's name: ")) #Players input their names
player2 = str(input("Please enter the 2nd player's name: "))
player3 = str(input("Please enter the 3rd player's name: "))
global player1_bank, player2_bank, player3_bank
player1_bank = 0 #Players bank starts at 0; this is different than round score
player2_bank = 0
player3_bank = 0

print("Welcome " + player1 + ", " + player2 + ", and " + player3 + ". Good luck") #Welcom message pt2
player_playing_1st = random.randint(1, 99) #player is randomly chosen to go 1st in the 1st round

round() #1st round

if player_going % 3 == 0: #Whoever won the 1st round, round total gets added to game total (bank)
    player1_bank = winning_round_score
    print("Congrats to " + player1 + " for winning the 1st round")
elif player_going % 3 == 1:
    player2_bank = winning_round_score
    print("Congrats to " + player2 + " for winning the 1st round")
else:
    player3_bank = winning_round_score    
    print("Congrats to " + player3 + " for winning the 1st round")

print(player1 + "'s banks is " + str(player1_bank)) #Shows each players bank after the 1st round
print(player2 + "'s banks is " + str(player2_bank))
print(player3 + "'s banks is " + str(player3_bank))

player_playing_1st = player_playing_1st + 1 #Choose next player to start round 2 (is player who guessed 2nd in round 1)
print("The 2nd round is about to begin")
round() #2nd round
if player_going % 3 == 0: #Whoever won the 2nd round, round total gets added to game total (bank)
    player1_bank = winning_round_score + player1_bank
    print("Congrats to " + player1 + " for winning the 2nd round")
elif player_going % 3 == 1:
    player2_bank = winning_round_score + player2_bank
    print("Congrats to " + player2 + " for winning the 2nd round")
elif player_going % 3 == 2:
    player3_bank = winning_round_score + player3_bank    
    print("Congrats to " + player3 + " for winning the 2nd round")

print(player1 + "'s banks is " + str(player1_bank)) #Shows each players bank after the 2nd round
print(player2 + "'s banks is " + str(player2_bank))
print(player3 + "'s banks is " + str(player3_bank))

if player1_bank > player2_bank and player1_bank > player3_bank: #Selection for final spin
    final_spin_player = player1
elif player2_bank > player1_bank and player2_bank > player3_bank:
    final_spin_player = player2
elif player3_bank > player1_bank and player3_bank > player2_bank:
    final_spin_player = player3
elif player1_bank == player2_bank: #If there are ties
    random = random.randint(1,2)
    if random == 1:
        final_spin_player = player1
    else:
        final_spin_player = player2
elif player1_bank == player3_bank:
    rand = random.randint(1,2)
    if random == 1:
        final_spin_player = player1
    else:
        final_spin_player = player3
elif player2_bank == player3_bank:
    random = random.randint(1,2)
    if random == 1:
        final_spin_player = player2
    else:
        final_spin_player = player3
elif player1_bank == player2_bank == player3_bank:
    random = random.randint(1,3)
    if random == 1:
        final_spin_player = player1
    elif random == 2:
        final_spin_player = player2
    else:
        final_spin_player = player3

final_spin() #Final spin round
print("Thank you for playing") #Closing message