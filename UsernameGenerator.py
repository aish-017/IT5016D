import random # importing a random module to generate random numbers
import string

def generate_username ( length=8 ):
    # Define the characters to choose from 
    characters = string.ascii_letters + string.digits: # Created string called character, it includes both uppercase and lowercase letters and digits 

    # Generate a random username
    username = ''.join(random.choice ( characters ) for _ in range ( length ) ) # Used loop to randomly select characters to form username
    return username # Finally return the generated username

# Example usage:
if __name__ == "__main__": # This block makes sure that the code only runs only when the script is executed directly 
    generated_username = generate_username ( )
    print( f"Generated username: { generated_username }" ) # We print the username, hopefully, we get a good one!
