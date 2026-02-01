label tv:
    $ viet = 4
    show light-sus as char
    show light-default as char
    show screen small
    menu:
        "Ask something about TV":
            jump yout
        "Ask something about others":
            jump othert
    
    label yout:
        show light-sus as char
        TV "What? You'd better not try to steal from my farm, y'hear?"
        menu:
            "What was your relationship with the victim?":
                jump yt1
            "Where were you during the time of the murder?":
                jump yt2
            "So, what are you?":
                jump yt3
            "Can you take off your gloves for me?":
                jump yt4
            "Nevermind":
                jump tv
    
    label othert:
        show light-expectant as char
        TV "Ooh, questions about others?"
        show light-gossip as char
        TV "Why, you've come to the right person for the job! Waddya wanna know?"
        menu:
            "Tell me about Eye":
                jump ot1
            "Tell me about Doll":
                jump ot2
            "Tell me about Judge":
                jump ot3
            "Tell me about Moth":
                jump ot4

    label yt1:
        $ reizes += 1
        show light-furious as char
        TV "UURRGHHH, that guy ALWAYS intruded in my territory!"
        show light-angry as char
        TV "Ah'll say he deserved what he got! Good riddance!"
        "You do know this doesn't paint a good picture for you, right?"
        show light-reluctant as char
        TV "Ugh... I mean..."
        TV "SO BE IT! But I didn't do it, ya hear?!"
        show light-angry as char
        jump count

    label yt2:
        $ reizes += 1
        show light-sus as char
        TV "In my farm... doy!"
        TV "I mean, why would I ever leave?"
        "To guard your territory, perhaps?"
        if killer == "TV":
            TV "Or, or, or MAYBE I just want to hear some out of range gossip!"
            TV "Ever thought of THAT?"
            jump count
        else:
            jump count

    label yt3:
        $ reizes += 1
        show light-proud as char
        TV "I'm a goat farmer... Doy!"
        "Well, you sure don't look entirely the part..."
        show light-angry as char
        TV "Excuse me???"
        "What about those screens? I don't see a farm anywhere..."
        show light-sus as char
        TV "Those are mah plots! Look behind me! Don't you see these luscious fields?"
        TV "Just don't get any ideas! I'm not giving you my produce NOR selling you my plots! GET YOUR OWN!"
        "Okay, sheesh..."
        jump count

    label yt4:
        $ reizes += 1
        show light-furious as char
        TV "NO! ABSOLUTELY NOT!"
        show light-sus as char
        TV "These... Peh, these are mah work gloves!"
        show light-furious as char
        TV "NO! YOU MAY NOT TAKE MY GLOVES AWAY FROM ME! THIEF!"
        "Calm down, I'm not trying to take anything from you..."
        show light-angry as char
        TV "And yet here you stand... IN MY TERRITORY!"
        show light-sus as char
        TV "If ah were you, I'd run for the hills!"
        jump count

    label ot1:
        $ reizes += 1
        TV "That's right, little eyeball..."
        show light-furious as char
        TV "STAY AWAY FROM MY TERRITORY!"
        if killer == "Remido" or killer == "Eyenile":
            TV "But don't spin those lies about me!"
            TV "Why I oughta make a SCARECROW outta her or her little DOLL friend!"
            jump count
        else:
            jump count

    label ot2:
        $ reizes += 1
        show light-furious as char
        TV "WHO DOES THAT GUY THINK HE IS?"
        show light-angry as char
        TV "Don't listen to that doll creature thing whatever..."
        TV "He'll point fingers at anyone when he feels just the slightest bit threatened!"
        show light-reluctant as char
        TV "Even someone as cute and cuddly as me!"
        jump count

    label ot3:
        $ reizes += 1
        show light-reluctant as char
        TV "They're about the only one that respects my warning signals"
        TV "Only one other than that Moth creature, anyways"
        "Anything else?"
        show light-proud as char
        TV "Why, I could make them my farm plot if I wanted to!"
        "So, why don't you?"
        if killer == "TV":
            show light-sus as char
            TV "They... Uh... They'd boil my crops!"
            show light-furious as char
            TV "ALL MY WORK WOULD BE RUINED!"
            jump count
        else:
            show light-reluctant as char
            TV "I shouldn't make 'them' my enemy..."
            TV "Not only would they ruin my crops... THEY'D REPURPOSE THEM INTO BORING MACHINES!"
            TV "I can't let that happen!"
            jump count

    label ot4:
        $ reizes += 1
        show light-default as char
        TV "Eh... who is that?"
        "You don't know?"
        show light-reluctant as char
        TV "Well..."
        TV "Uh..."
        show light-gossip as char
        TV "OKAY, OKAY, I know who that is!"
        TV "They rarely leave their house..."
        TV "Ah've never seen them out and about! They don't approach mah farm, so I don't bother them either!"
        show light-cheer as char
        TV "It's a win-win!"
        "Are you implying you've seen them?"
        if killer == "TV":
            show light-proud as char
            TV "Well, do--"
            show light-shock as char
            TV "I mean, no!"
            show light-angry as char
            TV "No, I haven't!!! "
            "So have you or have you not seen the Moth?"
            show light-furious as char
            TV "Are your ears full of chicken feathers? OF COURSE I HAVEN'T!"
            TV "I mean, how could ah even seen them? I live in a screen!"
            "But you can see me now"
            TV "WELL, MAYBE YOU SHOULD ASK LESS QUESTIONS!!!"
            jump count
        else:
            show light-proud as char
            TV "Well, doy! I've seen that moth..."
            TV "Through their screen!"
            show light-reluctant as char
            TV "Hey, why does this even matter?"
            jump count