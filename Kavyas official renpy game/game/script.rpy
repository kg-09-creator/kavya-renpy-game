# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")
define l = Character("Lorelai" color="#f9d6f2")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black
    "BZZZZZZ....BZZZZZ...BZZZZZ!!"

    menu: 
        "Wake up...":
            jump wake

    label wake: 
        scene bg room with dissolve
        show eileen sleepy 

        e "Wha..? Wh-Where am I...?"

    show eileen turn right
    
    e "Huh...?"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show room view

    e "Where am I? I've never seen this place before..."

    show bedroom door open
    show lorelai morning 
    l "Eileen! You're finally awake!"

    show eileen concerned 
    e "What..? My name's not Eileen, it's-"

    show lorelai lighthearted
    l "Oh Eileen, stop joking around so early in the morning! Come downstairs, Joelle's waiting for you! It's the big day, remember? Aren't you excited?"

    # These display lines of dialogue.

    e "Welcome to my game!"

    e "I've been waiting for someone to talk to. Do you want to go outside, or stay in here with me?"

    menu: 
        "Go outside.":
            jump outside

        "Stay in this room.":
            jump stay

    label outside: 

            scene bg whitehouse with dissolve
            show eileen concerned

            e "It's freezing out here!"
            return

    label stay:

        show eileen happy
        e "Much better. It's warm in here."
        return 
    # This ends the game.

    return
