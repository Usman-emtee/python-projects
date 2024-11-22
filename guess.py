#Generate a random number.
#Allow the user to input guesses.
#Compare the user’s guess to the random number and provide feedback ("too high" or "too low").

import random
while True:
    random_int = random.randint(1, 10)
    user_guess = None 
    attempt = 0
    while random_int != user_guess:
        try:
            attempt += 1
            user_guess = int(input("Enter you guess:"))
            if random_int < user_guess:
                print("too high!")
            elif random_int > user_guess:
                print("too low!")
            else:
                print("Congratulations! you guessed correctly.")
                print("Number of attempt:", attempt)        
    
    
    
    
    
    
    
    
        except ValueError:
            print("try again")

    
    
    cont_play = input("Do you want to continue playing? (yes/no):").strip().lower()
    if cont_play not in 'yes':
        print("thank you for playing")
        break              