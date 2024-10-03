import time
import random

def print_halloween_greeting():
    while True:
        # Generate a random colour for the text (orange or yellow)
        text_color = random.choice(["\033[91m", "\033[93m"])
        print(f"{text_color}Happy Halloween\033[0m")

        # Add floating pumpkins ( uploaded random pumpkin picture for this )
        pumpkins = ["🎃", "🎃🎃", "🎃🎃🎃"]
        random_pumpkin = random.choice(pumpkins)
        print(f"   {random_pumpkin}")
 # Pumpkin floats by 
        # Pause for 1 second to let the pumpkins settle
        time.sleep(1)

if __name__ == "__main__":
    # Cast the enhanced spell and watch the pumpkins dance!
    print_halloween_greeting()
