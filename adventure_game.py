import random
import time

"""
This is a text-based fun game
Programmed by Awopeju Kolawole Moses
"""

person = random.choice(["recluse", "hermit", "loner"])
animal = random.choice(["lion", "tiger", "leopard"])
being = random.choice(["a tribe of sentient beings", "a league of saints", "a gathering of priests"])

def storyline(story):
    print(story)
    time.sleep(3)

def play_again():
    playgame = str(input("Do you want to play again? y/n \n"))
    if playgame == "y" or playgame == "Y":
        game_intro()
    elif playgame == "n" or playgame == "N":
        storyline("Thank you for your time.")
        storyline("Looking forward to seeing you again.")
    else:
        play_again()


def final_lap():
    finaloption = int(input("Please enter 1 or 2:\n"))
    if finaloption == 1:
        storyline("The fate of the Lost World and Earth itself rests in your hands.")
        storyline("Your decisions have far-reaching consequences, affecting not only your character but also the world you inhabit.")
        storyline("As you reflect on your journey, you are left with a sense of purpose and the knowledge that the world's survival depends on those who dare to explore the unknown.")
        storyline("YOU WON!!!🎉")
        storyline("Thank you for playing my game.")
        play_again()
    elif finaloption == 2:
        storyline("You gave away your power due to your selfishness.")
        storyline("You can't help the situation.")
        storyline("The world is doomed.")
        storyline("You are the first to suffer the gruesomeness of the darkness")
        storyline("You lose!!!😔")
        storyline("Try again.")
        play_again()
    else:
        final_lap()

def fourth_choice():
    myoption = int(input("Please enter 1 or 2:\n"))
    if myoption == 1:
        storyline("The climactic showdown takes place in a hidden temple deep within the Lost World.")
        storyline("You confront the cult leader and engage in a battle of wits and strength.")
        storyline("Your choices throughout the game, as well as the allies you've made, determine the outcome.")
        storyline("Will you save the Lost World and restore hope to Earth, or will darkness prevail?")
        storyline("Enter 1 to restore hope to the Earth.")
        storyline("Enter 2 to let darkness prevail because it is not your business to save the Earth.")
        storyline("What would you like to do?")
        final_lap()
    elif myoption == 2:
        storyline("While finding your way back to the portal")
        storyline("You ran out of supplies.")
        storyline("Weak and tired, You couldn't help yourself.")
        storyline("Death came for you.")
        storyline("You lose!!!😔")
        storyline("Try again.")
        play_again()
    else:
        fourth_choice()
        

def third_choice():
    the_option = int(input("Please enter 1 or 2:\n"))
    if the_option == 1:
        storyline("The guardians of the Lost World inform you that to restore Earth, you must collect four Elemental Crystals scattered across the realm.")
        storyline("Each crystal embodies a different aspect of nature: Earth, Fire, Water, and Air.")
        storyline("Your journey takes you through diverse landscapes, battling elemental guardians and overcoming environmental puzzles.")
        storyline("As you collect the Elemental Crystals, you uncover the existence of a dark cult that seeks to exploit the Lost World's power for their sinister purposes.")
        storyline("Your quest becomes a race against time as you confront the cult's leader, who possesses a corrupted crystal.")
        storyline("You must stop them before they plunge the world into eternal darkness.")
        storyline("Enter 1 to dare and face the dark cult.")
        storyline("Enter 2 to go back to the portal.")
        storyline("What would you like to do?")
        fourth_choice()            
    elif the_option == 2:
        storyline("While doing your best to make them fear you and do your bidding.")
        storyline("You woke up a scary {} nearby".format(animal))
        storyline("Knowing their way around, They went to hiding and leave you to your doom.")
        storyline("The scary {} pounced on you and made a beautiful meal out of you.".format(animal))
        storyline("You lose!!!😔")
        storyline("Try again.")
        play_again()
    else:
        third_choice()

def second_choice():
        myopt = int(input("Please enter 1 or 2:\n"))
        if myopt == 1:
            storyline("Using the Gatekeeper's Amulet, you activate the portal and step into the Lost World.")
            storyline("A place teeming with lush forests, strange creatures, and forgotten relics.")
            storyline("Here, you encounter the first of many challenges: a {} who distrust outsiders.".format(being))
            storyline("You must earn their trust and learn about the Lost World's ancient guardians.")
            storyline("Enter 1 to earn their trust.")
            storyline("Enter 2 to threaten them.")
            storyline("What would you like to do?")
            third_choice()
        elif myopt == 2:
            storyline("In the process of trying to find a buyer for the amulet in the wasteland.")
            storyline("You encountered a hungry {}, that didn't hesitate to pounce on you".format(animal))
            storyline("It feasted on your flesh and you lost your life.")
            storyline("You lose!!!😔")
            storyline("Try again.")
            play_again()
        else:
            second_choice()
        
def first_choice():
    option = int(input("Please enter 1 or 2:\n"))
    if option == 1:
        storyline("To open the portal to the Lost World, you must retrieve the Gatekeeper's Amulet, hidden deep within an abandoned research facility.")
        storyline("Along the way, you'll encounter rival scavengers, solve puzzles, and make decisions that will shape your character. Upon acquiring the amulet, you must decipher its cryptic instructions.")
        storyline("Enter 1 to decipher amulet cryptic instructions.")
        storyline("Enter 2 to go find buyer for the amulet")
        storyline("What would you like to do?")
        second_choice()
    elif option == 2:
        storyline("After realizing that you are about to run out of supplies.")
        storyline("You start wandering around trying to find a way make ends meet.")
        storyline("You encountered a ferocious {}, and you were killed because you don't have any weapon to defend yourself".format(animal))
        storyline("You lose!!!😔")
        storyline("Try again.")
        play_again()
    else:
        first_choice()

def game_intro():
    storyline("You wake up in a desolate wasteland, your memories fragmented.")
    storyline("Your first task is to scavenge for supplies, avoid dangerous creatures, and seek shelter.")
    storyline("As you explore, you encounter a mysterious old {} who hints at the existence of the Lost World.".format(person))
    storyline("He gives you a tattered map and advises you to find the fabled \"Gatekeeper's Amulet.\"")
    storyline("\n")
    storyline("Enter 1 to accept the map.")
    storyline("Enter 2 to reject the map")
    storyline("What would you like to do?")
    first_choice()

game_intro()