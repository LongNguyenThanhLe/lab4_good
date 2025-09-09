def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You can choose to take the sword or leave it.")
    print("What do you do?")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You beat the squirel")
    print("You get squirrel meat")
		


def center_path():
    print("You walk straight ahead and find a peaceful clearing with a beautiful pond.")

if __name__ == "__main__":
    intro()
