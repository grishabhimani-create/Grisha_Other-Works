# Number mind game

import random
import time

def main_menu():
    while True:
        print("\n" + "="*30)
        print("    ✨ NUMBER MIND GAMES ✨    ")
        print("="*30)
        print("1. Guess the Number (You guess the Computer's number)")
        print("2. Computer Guesses Your Number (Binary Search AI)")
        print("3. Magic Number Trick (Mind Reading)")
        print("4. Number Property Checker (Palindrome & Armstrong)")
        print("5. Exit")
        print("="*30)
        
        choice = input("Select a game (1-5): ").strip()
        
        if choice == '1':
            guess_computer_number()
        elif choice == '2':
            computer_guesses_yours()
        elif choice == '3':
            magic_number_trick()
        elif choice == '4':
            check_number_properties()
        elif choice == '5':
            print("\nThanks for playing! Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# --- GAME 1: USER GUESSES COMPUTER'S NUMBER ---
def guess_computer_number():
    print("\n--- 🎯 Guess the Computer's Number ---")
    print("I am thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("📉 Too low! Try a higher number.")
            elif guess > secret_number:
                print("📈 Too high! Try a lower number.")
            else:
                print(f"🎉 Correct! You found the number in {attempts} attempts!")
                break
        except ValueError:
            print("❌ Please enter a valid integer.")

# --- GAME 2: COMPUTER GUESSES USER'S NUMBER ---
def computer_guesses_yours():
    print("\n--- 🤖 Computer Guesses Your Number ---")
    print("Think of a number between 1 and 100 in your mind.")
    print("I will try to guess it using strict logic. Type:")
    print("  'h' if my guess is too high")
    print("  'l' if my guess is too low")
    print("  'c' if my guess is correct")
    input("Press Enter when you are ready...")
    
    low = 1
    high = 100
    attempts = 0
    
    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"\nIs your number {guess}?")
        feedback = input("Your response (h/l/c): ").strip().lower()
        
        if feedback == 'c':
            print(f"😎 Awesome! I guessed your number in {attempts} attempts!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
            attempts -= 1  # Don't count invalid inputs as an attempt
    else:
        print("🤔 Hmm, something went wrong. Are you sure you gave correct hints?")

# --- GAME 3: MAGIC NUMBER TRICK ---
def magic_number_trick():
    print("\n--- 🔮 Magic Number Trick ---")
    print("Think of any whole positive number. Keep it in your head!")
    time.sleep(2)
    print("\nStep 1: Multiply your number by 2.")
    time.sleep(3)
    print("Step 2: Add 10 to the result.")
    time.sleep(3)
    print("Step 3: Divide the current total by 2.")
    time.sleep(3)
    print("Step 4: Subtract your original secret number from this total.")
    time.sleep(4)
    
    print("\n🔮 Reading your mind...")
    time.sleep(2)
    print("✨ The magic number left in your head is: 5! ✨")

# --- GAME 4: PROPERTY CHECKER ---
def check_number_properties():
    print("\n--- 🔍 Number Property Checker ---")
    try:
        num_str = input("Enter a positive integer to analyze: ").strip()
        num = int(num_str)
        
        if num < 0:
            print("Please enter a positive number.")
            return
            
        # 1. Reverse the number
        reversed_str = num_str[::-1]
        print(f"\n🔄 Reversed Number: {reversed_str}")
        
        # 2. Check Palindrome
        if num_str == reversed_str:
            print("✅ Palindrome: Yes! It reads the same forwards and backwards.")
        else:
            print("❌ Palindrome: No.")
            
        # 3. Check Armstrong Number
        # (An Armstrong number equals the sum of its digits raised to the power of the total number of digits)
        num_digits = len(num_str)
        armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
        
        if armstrong_sum == num:
            print(f"✅ Armstrong Number: Yes! (" + " + ".join(f"{d}^{num_digits}" for d in num_str) + f" = {num})")
        else:
            print("❌ Armstrong Number: No.")
            
    except ValueError:
        print("❌ Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    main_menu()
