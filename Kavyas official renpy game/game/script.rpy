# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black
    "BZZZZZZ....BZZZZZ...BZZZZZ!!"

    menu: 
        "Wake up...":
            jump wake up

    label wake up:
        scene bg room with dissolve
        show eileen sleepy 

        e "Wha..? Wh-Where am I...?"

    show eileen turn right
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

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
