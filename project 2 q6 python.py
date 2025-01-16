
#6 In this activity, you will create the code that a candy store will use in their state-of-the-art candy vending machine.

        # Instructions
        # Create a loop that prints all of the candies in the store to the terminal, with their index stored in brackets beside them.

        # For example: "[0] Snickers"
       
        # Each time this second loop runs, take in a user's input, preferably a number, and then add the candy with the matching index to the variable candy_cart.

        # For example: If the user enters "0" as their input, "Snickers" should be added into the candy_cart list.

        # Use another loop to print all of the candies selected to the terminal.


# Avaliable list of candies in the store

candies = ["Snickers", "Hersheys","Butterfinger", "Skittles","Reeses","Twix","Milky Way","KitKat"]


# To select candies

def select_candies(candies, allowance=None):
    candy_cart = []
    count = 0

    while allowance is None or count < allowance:
        
            choice = input("Enter the index of the candy you want (or 'stop' to finish): ").strip().lower()
            if choice == "stop":
                break
            choice = int(choice)
            if 0 <= choice < len(candies):
                candy_cart.append(candies[choice])
                print(f"Added {candies[choice]} to your cart.")
                count += 1
            else:
                print("Invalid choice. Please enter a correct candy index.")
        
    return candy_cart


# Create a second loop that runs for a set number of times determined by the variable allowance.

 # For example: If allowance is equal to five, the loop should run five times.


print("You can select up to 5 candies!")
candy_cart = select_candies(candies, allowance=5)

# To Print selected candies

print("Candies you selected:")
for candy in candy_cart:
    print(candy)

# Bonus
 # Create a version of the code that allows a user to select as much candy as they want until they say they do not want any more.

print("BONUS: Select as many candies as you want!")
candy_cart_bonus = select_candies(candies)

# To Print candies selected in the bonus 

print("Candies you selected are in the bonus :")
for candy in candy_cart_bonus:
    print(candy)
