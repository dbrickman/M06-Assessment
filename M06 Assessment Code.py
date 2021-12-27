#imports
import random

def wheel(): #Wheel function
    global outputs, amount
    outputs = ['BANKRUPT', 'BANKRUPT', 'Lose a turn', 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 500, 900, 300, 400]
    amount = outputs[random.randint(0,len(outputs)-1)]
#---------------------------------------------------------------------------------------
def get_word(): #Get word function
    global word
    word_list = open("words_alpha.txt")
    words = word_list.readlines()
    word=words[random.randint(0,len(words)-1)]
    global already_guessed 
    already_guessed = set()
#---------------------------------------------------------------------------------------
def round(): #player turn function
    global player1_round_score, player2_round_score, player3_round_score, player_going, guess, winning_round_score
    player1_round_score=0
    player2_round_score=0
    player3_round_score=0
    get_word()
    dash = ""
    for i in range(0, len(word)-1): #creates word in dashed form and reveals letters in already_guessed
        if word[i] in already_guessed:
            dash += word[i] + ""
        else:
            dash+="_"
    print('The word contains ' + str(len(word)-1) + " letters.")  #Prints word in dashed form with letters revealed as they are guessed
    list_dash = list(dash)
    print(list_dash)

    player_going = player_playing_1st
    while player_going < 10000:
        round_score = 0
        if player_going % 3 == 0:
            player_going_name = player1
            round_score = player1_round_score
        elif player_going % 3 == 1:
            player_going_name = player2
            round_score = player2_round_score
        elif player_going % 3 == 2:
            player_going_name = player3
            round_score = player3_round_score
        print(player1 + "'s round score is " + str(player1_round_score))
        print(player2 + "'s round score is " + str(player2_round_score))    
        print(player3 + "'s round score is " + str(player3_round_score))
        print(player_going_name + " is up.")
        wheel()
        print("The wheel landed on " + str(amount))
        if amount == "BANKRUPT":
            print("Oof, your round score has been reset to 0. It is now the next player's turn.")
            if player_going % 3 == 0:
                player1_round_score = 0
            elif player_going % 3 == 1:
                player2_round_score = 0
            elif player_going % 3 == 2:
               player3_round_score = 0
            player_going = player_going + 1
        elif amount == "Lose a turn":
            print("Oof, you lost your turn. It is now the next player's turn.")
            player_going = player_going + 1
        else:            
            word_letter = "no"
            while word_letter != "word" and word_letter != "letter":
                word_letter = str(input("Would you like to guess the 'word' or choose a 'letter'? "))
                if word_letter != "word" and word_letter != "letter":
                    print("Please type 'word' or 'letter")
            if word_letter == "word":
                guess = str(input("What word would you like to guess? "))
                if guess in word:
                    print("Congrats, you won the round. Your total for this round has been added to your overall total")
                    if player_going % 3 == 0:
                        player1_round_score = round_score
                        winning_round_score = player1_round_score 
                    elif player_going % 3 == 1:
                        player2_round_score = round_score
                        winning_round_score = player2_round_score           
                    elif player_going % 3 == 2:
                        player3_round_score = round_score
                        winning_round_score = player3_round_score 
                    break                                           
                else:
                    print("That was not the word")                  
                    player_going = player_going + 1
                    continue
            else:
                if round_score >= 250:
                    vowel = str(input("Would you like to buy a vowel for 250? [y/n] "))
                    while vowel != "y" and vowel != "n":
                        print("Please only type in 'y' or 'n'")
                        vowel = str(input("Would you like to buy a vowel for 250? [y/n] "))
                    if vowel == "y":
                        round_score = round_score - 250
                        guess = False
                        while guess != True:
                            guess = str(input("What letter would you like to guess? "))
                            if len(guess) > 1:
                                print("Please only enter 1 letter")
                            elif guess in already_guessed:
                                print("That letter has already been guessed. Please guess a different letter")
                            elif guess != 'a' and guess != 'e' and guess != 'i' and guess != 'o' and guess !='u':
                                print("Please only guess a vowel. You bought a vowel. The vowels are a-e-i-o-u")
                            elif guess not in word:
                                print("There are 0 " + guess + "'s in the word")
                                already_guessed.add(guess)
                                if player_going % 3 == 0:
                                    player1_round_score = round_score
                                elif player_going % 3 == 1:
                                    player2_round_score = round_score          
                                elif player_going % 3 == 2:
                                    player3_round_score = round_score                  
                                player_going = player_going + 1                   
                                guess = True
                            else:
                                already_guessed.add(guess)
                                dash = ""
                                v=0
                                for i in range(0, len(word)-1): #creates word in dashed form and reveals letters in already_guessed
                                    if word[i] in guess:
                                        dash += word[i] + ""
                                        v_new = v+1
                                        v=v_new
                                    else:
                                        dash+="_"
                                print("There are " + str(v_new) + " " + guess + "'s in the word.")
                                round_score = v_new * amount + round_score
                                if player_going % 3 == 0:
                                    player1_round_score = round_score 
                                elif player_going % 3 == 1:
                                    player2_round_score = round_score 
                                elif player_going % 3 == 2:
                                    player3_round_score = round_score 
                                guess = True                           
                    else:
                        guess = False
                        while guess != True:
                            guess = str(input("What letter would you like to guess? "))
                            if len(guess) > 1:
                                print("Please only enter 1 letter")
                            elif guess in already_guessed:
                                print("That letter has already been guessed. Please guess a different letter")
                            elif guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess =='u':
                                print("Please only guess a consonant. You chose not to buy a vowel")
                            elif guess not in word:
                                print("There are 0 " + guess + "'s in the word")
                                already_guessed.add(guess) 
                                if player_going % 3 == 0:
                                    player1_round_score = round_score
                                elif player_going % 3 == 1:
                                    player2_round_score = round_score 
                                elif player_going % 3 == 2:
                                    player3_round_score = round_score 
                                player_going = player_going + 1           
                                guess = True
                            else:
                                already_guessed.add(guess)
                                dash = ""
                                v=0
                                for i in range(0, len(word)-1): #creates word in dashed form and reveals letters in already_guessed
                                    if word[i] in guess:
                                        dash += word[i] + ""
                                        v_new = v+1
                                        v=v_new
                                    else:
                                        dash+="_"
                                print("There are " + str(v_new) + " " + guess + "'s in the word.")
                                round_score = v_new * amount + round_score
                                if player_going % 3 == 0:
                                    player1_round_score = round_score 
                                elif player_going % 3 == 1:
                                    player2_round_score = round_score 
                                elif player_going % 3 == 2:
                                    player3_round_score = round_score 
                                guess = True
                else:
                    guess = False
                    while guess != True:
                        guess = str(input("What letter would you like to guess? "))
                        if len(guess) > 1:
                            print("Please only enter 1 letter")
                        elif guess in already_guessed:
                            print("That letter has already been guessed. Please guess a different letter")
                        elif guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess =='u':
                            print("Please only guess a consonant. You don't have enough money to buy a vowel")
                        elif guess not in word:
                            print("There are 0 " + guess + "'s in the word")
                            already_guessed.add(guess)
                            if player_going % 3 == 0:
                                player1_round_score = round_score
                            elif player_going % 3 == 1:
                                player2_round_score = round_score 
                            elif player_going % 3 == 2:
                                player3_round_score = round_score 
                            player_going = player_going + 1          
                            guess = True
                        else:
                            already_guessed.add(guess)
                            dash = ""
                            v=0
                            for i in range(0, len(word)-1): #creates word in dashed form and reveals letters in already_guessed
                                if word[i] in guess:
                                    dash += word[i] + ""
                                    v_new = v+1
                                    v=v_new
                                else:
                                    dash+="_"
                            print("There are " + str(v_new) + " " + guess + "'s in the word.")
                            round_score = v_new * amount + round_score
                            if player_going % 3 == 0:
                                player1_round_score = round_score 
                            elif player_going % 3 == 1:
                                player2_round_score = round_score 
                            elif player_going % 3 == 2:
                                player3_round_score = round_score + player3_round_score
                            guess = True
        dash = ""
        for i in range(0, len(word)-1): #creates word in dashed form and reveals letters in already_guessed
            if word[i] in already_guessed:
                dash += word[i] + ""
            else:
                dash+="_"
        print('The word contains ' + str(len(word)-1) + " letters.")  #Prints word in dashed form with letters revealed as they are guessed
        list_dash = list(dash)
        print(list_dash)



#---------------------------------------------------------------------------------------
def final_spin(): #Final round function
    print("Congratulations " + final_spin_player + " for making it to the Final Round! Your goal is to guess the word correctly.")
    get_word() #Gets random word that needs to be guessed
    guess = ' '
    rstlne = ['r', 's', 't', 'l', 'n', 'e']
    dash = ""
    for i in range(0,6): #adds r-s-t-n-e to already_guessed
        guess = rstlne[i]
        already_guessed.add(guess)
        i = i+1     
    for i in range(0, len(word)-1): #creates word in dashed form and reveals letters in already_guessed
        if word[i] in already_guessed:
            dash += word[i] + ""
        else:
            dash+="_"
     
    print('The word contains ' + str(len(word)-1) + " letters. R-S-T-L-N-E have already been guessed")  #prints off word with rstlne revealed
    list_dash = list(dash)
    print(list_dash)
    
    print("Please guess 3 consonants and 1 vowel")
    i=0
    while i < 3: #User guesses 3 consonants, mistake messages are added
        guess = str(input("Consonant " + str(i+1) + ": "))
        if guess == 'a' or guess == 'i' or guess == 'o' or guess == 'u':
            print("That is a vowel")
        elif guess in already_guessed:
            print("That letter has already been guessed")
        else:
            already_guessed.add(guess)
            i=i+1
    i=0
    while i < 1: #User guesses 1 vowel, mistake messages are added
        guess = str(input("Vowel: "))
        if guess in already_guessed:
            print("That letter has already been guessed")
        elif guess  == 'a' or guess == 'i' or guess == 'o' or guess == 'u':
            already_guessed.add(guess)
            i=i+1            
        else:
            print("That is not a vowel")

    dash = ""
    for i in range(0, len(word)-1): #Creates word in dashed form with every letter that has already been guessed revealed
        if word[i] in already_guessed:
            dash += word[i] + ""
        else:
            dash+="_"
    list_dash = list(dash)
    print(list_dash) #show rstlne + user gussed 3 consanants 1 vowel added

    guess = str(input("You now have 1 try to guess the word. Good luck: "))
    if guess in word:
        print("Congrats, you won the game. Your prize is $1,000,000!!!!!!")
    else:
        print("I'm sorry, that was not the word. The correct word was " + word + "You would have won $1,000,000 had you guessed the word correctly. Better luck next time")
#---------------------------------------------------------------------------------------
print("WELCOME TO WHEEL OF FORTUNE!")
print("This is a 3 player game")
player1 = str(input("Please enter the 1st player's name: ")) #Players input their names
player2 = str(input("Please enter the 2nd player's name: "))
player3 = str(input("Please enter the 3rd player's name: "))
global player1_bank, player2_bank, player3_bank
player1_bank = 0 #Players bank starts at 0; this is different than round score
player2_bank = 0
player3_bank = 0

print("Welcome " + player1 + ", " + player2 + ", and " + player3 + ". Good luck")
player_playing_1st = random.randint(1, 99) #player is randomly chosen to go 1st in the 1st round

round() #1st round
print(player1 + "'s round score is " + str(player1_round_score))
print(player2 + "'s round score is " + str(player2_round_score))
print(player3 + "'s round score is " + str(player3_round_score))

if player_going % 3 == 0: #whoever won the 1st round, round total gets added to game total (bank)
    player1_bank = winning_round_score
    print("Congrats to " + player1 + " for winning the 1st round")
elif player_going % 3 == 1:
    player2_bank = winning_round_score
    print("Congrats to " + player2 + " for winning the 1st round")
else:
    player3_bank = winning_round_score    
    print("Congrats to " + player3 + " for winning the 1st round")

print(player1 + "'s banks is " + str(player1_bank))
print(player2 + "'s banks is " + str(player2_bank))
print(player3 + "'s banks is " + str(player3_bank))

player_playing_1st = player_playing_1st + 1 #choose next player to start round 2
print("The 2nd round is about to begin")
round() #2nd round
if player_going % 3 == 0: #whoever won the 2nd round, round total gets added to game total (bank)
    player1_bank = winning_round_score + player1_bank
    print("Congrats to " + player1 + " for winning the 2nd round")
elif player_going % 3 == 1:
    player2_bank = winning_round_score + player2_bank
    print("Congrats to " + player2 + " for winning the 2nd round")
elif player_going % 3 == 2:
    player3_bank = winning_round_score + player3_bank    
    print("Congrats to " + player3 + " for winning the 2nd round")

print(player1 + "'s banks is " + str(player1_bank))
print(player2 + "'s banks is " + str(player2_bank))
print(player3 + "'s banks is " + str(player3_bank))

if player1_bank > player2_bank and player1_bank > player3_bank:
    final_spin_player = player1
elif player2_bank > player1_bank and player2_bank > player3_bank:
    final_spin_player = player2
elif player3_bank > player1_bank and player3_bank > player2_bank:
    final_spin_player = player3
elif player1_bank == player2_bank:
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

final_spin()
print("Thank you for playing")