# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")
define l = Character("Lorelai", color="#f9d6f2")
define j = Character("Joelle", color="#abd2ff")


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

    show bg bedroom door open
    show lorelai morning 
    l "Eileen! You're finally awake!"

    show eileen concerned 
    e "What..? My name's not Eileen, it's-"

    show lorelai lighthearted
    l "Oh Eileen, stop joking around so early in the morning! Come downstairs, everyone's waiting for you! It's the big day, remember? Aren't you excited?"

    # These display lines of dialogue.

    show eileen thinking

    e "Should I stay here or play along as Eileen and go downstairs...? I don't know what's going to happen..."

    menu: 
        "Go downstairs.":
            jump downstairs

        "Stay in this room.":
            jump stay

    label stay:

        show eileen uncertain
        e "Ummm, I think I'll stay here, thanks."
        l "Why? Are you feeling okay?"
        e "Yeah, I'm feeling fine. I just don't want to come downstairs right now. You guys carry on, no need to worry about me! Heh heh..."
        show lorelai lighthearted
        l "Nonsense, it's such a big day! Don't you remember? You're coming downstairs whether you like it or not."
        e "There's no need for that-"
        show lorelai pulling eileen out of bed 
        l "Come on now-"
        show eileen wrist tattoo
        l "Oh Eileen, did you get a tattoo?"
        e "No... wait what? I've never seen this before in my life-"
        l "Oh I'm sure you have, it's probably just early-morning sleepiness making you forget. Now come downstairs!"
        
        scene bg downstairs with dissolve
        show eileen uncertain
        show joelle happy
        j "Hi Eileen! What's up? You ready for today?"
        return 

    label downstairs: 

            scene bg downstairs with dissolve
            show eileen uncertain
            show joelle excited

            j "Eileen! There she is!"
            show joelle and eileen hug awkward
            e "Umm... hi- Joelle."
            j "You ready for today? How do you feel?"
            e "Great... if only I knew why this is such a big day for me..."
            j "Did you forget? It's the day you finally got your drivers' license!"
            e "Right...my driver's license...!"
            j "No, I'm just kidding - you got that last week, remember? But jokes aside, it is a big day. Today's the day Great Aunt Bellona's will is to be read. We have to host the memorial banquet tonight at her mansion - and we need to leave in an hour to oversee the preparations."
            e "Right... Great Aunt Bellona. And the banquet today - how could I forget?"
            return


    # This ends the game.

    # story - amnesiac [insert her actual name here] wakes up in a mansion she's never seen surrounded by ppl she's never met on the day the matriarch's will is to be read 

    return
