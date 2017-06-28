start = '''
In the year of 2020, the Russian government bombed the United States with a new bioweapon, causing a world wide Zombie Apocalypse.
You are alone, what do you do...
'''


print(start)


print("You are walking and you find an empty house, do you enter or run?")
user_input = input()
while user_input != "enter" and user_input != "run":
    print("Try again.")
    user_input = input()
if user_input == "enter":
    print("You decide to go inside and find a zombie and kill it. Do you use a gun or an axe?")
    user_input = input()
    while user_input != "gun" and user_input != "axe":
        print("Try again.")
        user_input = input()
    if user_input == "gun":
            print("You attract a hoard who eat you alive.")
    if user_input == "axe":
            print("You killed the zombie and got to stay in the house for the night, you survived.")
elif user_input == "run":
    print("You run into the forest and find a trail. Do you follow or keep going?")
    user_input = input()
    while user_input != "follow" and user_input != "keep going":
        print("Try again.")
        user_input = input()
    if user_input == "follow":
        print("You find a house with a group who let you join in, you live.")
    if user_input == "keep going":
        print("You get lost in the forest and die of starvation.")
