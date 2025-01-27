import random

# Dice options using list() and range()
diceOptions = list(range(1, 7))

# weapons Array
weapons = ["First", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# display avaliable weapons
print("Avaliable Weapons: ", ', '.join(weapons))


def get_comnat_stregth(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 6:
                return value
            else:
                print("Invalid input! Please apresents a number between 1 - 6.")
        except ValueError:
            print("Invalid input! Please apresents a number between 1 - 6.")


combatStreagth = get_comnat_stregth("Enter your combat streagth (1-6)")
mCombatStreagth = get_comnat_stregth("enter a monster's combat streagth (1-6)")

for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    heroTotal = combatStreagth + heroRoll
    monsterTotal = combatStreagth + monsterRoll

    print(f"\nHero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"\nHero selected {heroWeapon}, Monster selected {monsterWeapon}")
    print(f"\nHero total streagth: {heroTotal}, Monster total streagth: {monsterTotal}")

    # defines the winner
    if heroTotal > monsterTotal:
        print("Hero wins")
    elif monsterTotal > heroTotal:
        print("Monster wins")
    else:
        print("it's a tie!")

if j != 11:
    print(f"\n Battle concluded after 20 rounds!")