# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#c8ffc8")
define l = Character("Lorelai", color="#f9d6f2")
define j = Character("Joelle", color="#abd2ff")
define m = Character("Mrs. Halloway", color="#ffe8bf")
define w = Character("Lawyer", color="#ffffff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black
    "BZZZZZZ....BZZZZZ...BZZZZZ!!"

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
        l "Nonsense, it's such an important day! Don't you remember? You're coming downstairs whether you like it or not."
        e "There's no need for that-"
        show lorelai pulling eileen out of bed 
        l "Come on now-"
        show eileen wrist tattoo
        l "Oh Eileen, did you get a tattoo?"
        e "No... wait what? I've never seen this before in my life-"
        l "Well... I'm sure you have, it couldn't have shown up out of nowhere... it's probably just early-morning sleepiness making you forget. Now come downstairs!"
        
        scene bg downstairs with dissolve
        show eileen uncertain
        show joelle happy
        j "Hi Eileen! You ready for today?"
        e "Hi- Joelle. Sure I am- but remind me again, what's today...?"
        l ""
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
            j "Did you forget? It's the day you finally get your drivers' license!"
            e "Right...my driver's license...!"
            j "No, I'm just kidding - you got that last week, remember? But jokes aside, it is a big day. Today's the day Great Aunt Bellona's will is to be read. We have to host the memorial banquet tonight at her mansion - and we need to leave in an hour to oversee the preparations."
            e "Right... Great Aunt Bellona. And the banquet today - how could I forget?"
            j "Yup. The big day where we see who she left her fortune to."
            e "Right... wait, fortune?"
            j "Yeah... Great Aunt Bellona's mansions, money, and her cars... since she was everyone's favorite aunt, there's a lot of sentiment around her possessions. Anyway, we have to leave now if we want to get to her mansion on time. You coming?"
          
    menu: 
        "Go to the banquet and see what's up with her fortune.":
            jump banquet

        "Stay here and investigate.":
            jump investigate
    
    label investigate: 
        e "Actually, I think I'm gonna stay here today. I'm not feeling that great."
        l "What happened? Are you okay?"
        e "I'm fine, just a bad headache. I didn't sleep well tonight. You guys go ahead and let me know what happens. I might come later if I feel better."
        j "Okay... we'll let everyone know why you weren't able to come. Rest well."
        show lj leaving for banquet
        e "*thinking:* now that they're gone, i'll try to look around and see if i can find any clues as to how i got here and why everyone thinks i'm eileen. i'll start with the office room."
        scene office
        e "Where should I look first?"
    
    menu: 
        "Open the drawers and see if there's anything useful in there.":
            jump drawers 
        "Log onto the computer and see if you can find anything useful on there.":
            jump computer
    
    label drawers:
        e "Old letters, papers, nothing that relates to me...or Eileen. Wait... didn't Joelle mention a drivers' license? Let me see if I can find that..."
        e "Here it is! Eileen Callaghan... she has the same birthday and face as me - which would explain why everyone thinks I'm Eileen! Let me see if I can look into the DMV records to see when the processing for this happened. It might give me a better idea on who Eileen really is."
        j "Eileen? I'm back! We were halfway to the mansion when I realized I forgot my phone! Can you believe it?"
        e "Joelle! Hi-"
        j "What are you doing in here...? I thought you'd be resting because of your headache."
        e "I, uh, wanted to see if I could find some medicine! But I'm all better now so I guess I don't need any!"
        j "Oh, okay, great! Let's head to the banquet together, then, everyone's probably waiting for us!"


    label banquet:
        scene mansion 
        l "Well, we're here."
        e "Yeah..."
        j "Wait Eileen, I don't know if Lorelai told you yet, but everyone's gonna be here today. And by everyone, I mean that includes Uncle Roland, who as we know has always been after Great Aunt Bellona's wealth. Keep your distance from him in case he tries to trick you into giving him your share of inheritance."
        e "Right... Lorelai did...*"
        l "No, I didn't get the chance to tell you yet, but yeah, keep an eye out for him. Alright, I think we should go inside now."
        scene inside of mansion
        e "Woahh, it's huge! And it's so beautiful!"
        l "It really is. But it's been the same since before we were born, it's interesting that you're just noticing it now..."
        e "Uhhh... I guess I just didn't pay as much attention earlier! It really has been the same since then..."
        m "Eileen, Joelle, and Lorelai, welcome."
        l "Mrs. Halloway! It's good to see you."
        m "It's good to see you too, my dears. I'm glad you're here, Roland just arrived a few minutes ago, and he keeps glancing around unsettlingly... Anyway, I need your help. Joelle, please check in with the caterers to make sure they'll be here on time. Lorelai, please check on the guest list with Mr. Primrose. And Eileen, please come with me."
        e "Okay..."
        scene staircase 
        m "So, Eileen, how have you been lately?"
        e "Good, Mrs..."
        show Halloway glance
        m "It's Mrs. Halloway. It's not like you to forget my name, dear, after I raised you all these years. Is everything alright?"
        e "Yes, everything's fine, ma'am..."
        m "Okay, just making sure. To prepare for tonight's banquet, I thought we'd decorate the place with flowers in memory of Lady Bellona. Since you were her favorite niece, I thought you could tell me what her favorite flowers were."
        e "Right, um... she really loved daffodils...?"
        m "Daffodils...that's intriguing. Oh, I see Lorelai over by the flowers."
        l "Hi guys! Mr. Primrose mentioned you wanted to decorate the place with Great Aunt Bellona's favorite flowers, so I asked the florist for four dozen sunflowers."
        m "Sunflowers...Eileen mentioned she was fond of daffodils."
        l "That's odd... she never liked daffodils because they end up killing other plants if they're placed together. She favored sunflowers because of their ability to brighten up a room."
        m "I thought so as well...anyway, Eileen, do you want to come with me to check on the study to make sure everything's ready for the will reading, or greet the guests in the Great Hall?"
    menu: 
        "Go with Mrs. Halloway to check on the will reading ceremony and maybe get a glimpse on whether Eileen is set to inherit anything.":
            jump study 
        "Head to the Great Hall to avoid any further suspicion from Mrs. Halloway.":
            jump greet

    label study:
        e "I'll come with you to the study."
        m "Very well then. Let's go."
        e "Okay."
        m "Has anything exciting happened lately? How's work? And school?"
        e "Nothing much, work's good... school's going great too." 
        m "Good to hear that school's going well... have you seen Hazel in a while?"
        e "Uhhh... no. I haven't seen Hazel in a while..."
        m "You're not really Eileen, are you, dear..."
        e "Wh-what? I am Eileen! Mrs. Calloway, you've known me for so long..."
        m "It's Halloway...and I could tell something was off from the moment you walked in, amazed at the grandness of the mansion as if you'd walked through those double doors for the first time in your life. And Hazel's the name of my sister, you- rather, Eileen, has never met her before. And school couldn't be going well, or, going at all, because you're on summer break from college. So tell me... who are you and why are you here?"
       
    menu: 
        "Tell her who you really are and that you're here for the fortune.":
            jump tell
        "Run before everyone else finds out.":
            jump run
        "Try to convince her that you really are Eileen.":
            jump convince


    label run:
        e "I-"
        show eileen run
        m "Where are you going? Get back here or I'm calling the police!"
        # You were arrested for impersonating Eileen and attempting  to steal the Callaghan fortune. The end.
        show end message(run)
        return

    label convince:
        # i dont like the portion below rn so imma just comment it out until i think of smth better
        # m "I don't know, but you're definitely not Eileen. Tell me who you really are...and maybe we'll make an alliance."
        # e "Uhh...what sort of alliance?"
        # m "Look, according to Callaghan tradition, if the housekeeper of Callaghan Manor is set to inherit something in the will, they will also inherit a share of the fortune that a relative would inherit in the event of their passing."
        # e "And what does that mean...?"
        # m "That if someone from the Callaghan family is set to recieve a portion of Bellona's fortune and passes away before the will is read, I would receive their share of inheritance. I'm suggesting that you help me make this happen in exchange for keeping your secret that you're not really Eileen."
        # e "I- I wouldn't feel right doing something like that." 
        e "I- what do you mean, Mrs. Halloway? I am Eileen! Who else could I be?"
        m "I don't know, dear, but you definitely don't seem like Eileen to me."
        e "I really am Eileen, I- I've just been kind of distracted lately... And I do have a friend named Hazel... we go to college together-"
        m "Alright, dear. I believe you. I was just teasing. Now, we're almost at the study. I want you to make sure the study is organized while I speak to the lawyers to see if everything's ready."
        e "Got it."
        m "Okay, everything seems to be in order. Everyone should be arriving in a few minutes."
        w "We'll be commencing the will reading of Lady Bellona Callaghan now that everyone has arrived."
        w "First off, her mansion and bank assets. Ms. Callaghan leaves those to her beloved niece, Eileen Callaghan..."

    menu: 
        "Tell them who you are. Last chance.":
            jump truth
        "Walk away with a bazillion dollars and an enormous mansion.":
            jump rich
           
    label rich:
        "You're rich. They'll never have to know. The end."

    label truth: 
        e "I'm not Eileen Callaghan."
        j "What?"
        l "Huh?"
        m "Of course you aren't."
        l "What do you mean? Who are you then?"
        e "I'm...Evelyn Kensington. I don't know why everyone thinks I'm Eileen or why I'm here. I just thought I should tell you all before anything happened."
        r "Call the POLICE! SHE TRIED TO STEAL THE CALLAGHAN FORTUNE!"
        e "No- I didn't- I-"
    
    menu: 
        "Run before they call the police.":
            jump run
        "Try to explain yourself.":
            jump explain

    label explain:
        e "I'm telling the truth. I genuinely don't know why everyone thinks I'm Eileen. Whenever I try to explain, people think I'm joking. But I'm not."
        r "Regardless of what happened, we cannot allow you to remain here. Leave or we'll call the police."
        "You leave without the fortune or figuring out how you woke up as Eileen. The end."
        return 

    label tellM:
        e "I'm...Evelyn Kensington. I have no idea how or why everyone thinks I'm Eileen and why I was brought here, but...I agreed to come because I thought...maybe Eileen would inherit part of the fortune from Bellona."
        m "Ah. That explains it. Well, Evelyn, I'm glad you told me the truth, but you cannot receive the fortune Bellona would have wanted Eileen to inherit. I must ask, though, that you continue to act as Eileen and remain at the banquet so that...people like Roland don't seek to usurp all that's left of her possessions."
        e "I understand, ma'am."
        m "Good. I don't know why or where Eileen disappeared, but for now I'd like you to return to the Great Hall and greet guests as she would have done to avoid raising suspicion."
        e "Okay."
        

            # This ends the game.

    # story(1?) - amnesiac [insert her actual name here, not eileen but its undecided tbh] wakes up in a mansion she's never seen surrounded by ppl she's never met on the day the matriarch's will is to be read 

    return
