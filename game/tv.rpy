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
        TV "UURRGHHH, that guy ALWAYS intruded in my territory!"
        TV "Ah'll say he deserved what he got! Good riddance!"
        TV "UURRGHHH, that guy ALWAYS intruded in my territory!"
        TV "Ah'll say he deserved what he got! Good riddance!"
        "You do know this doesn't paint a good picture for you, right?"
        TV "Ugh... I mean..."
        TV "SO BE IT! But I didn't do it, ya hear?!"
        jump count

    label yt2:
        $ reizes += 1
        TV "In my farm... doy!"
        TV "I mean, why would I ever leave?"
        "To guard your territory, perhaps?"
        if killer == "TV":
            TV "Or, or, or MAYBE I just want to hear some out of range gossip!"
            TV "Ever thought of THAT?"
        jump count

    label yt3:
        $ reizes += 1
        TV "I'm a goat farmer... Doy!"
        "Well, you sure don't look entirely the part..."
        TV "Excuse me???"
        "What about those screens? I don't see a farm anywhere..."
        TV "Those are mah plots! Look behind me! Don't you see these luscious fields?"
        TV "Just don't get any ideas! I'm not giving you my produce NOR selling you my plots! GET YOUR OWN!"
        "Okay, sheesh..."
        jump count

    label yt4:
        $ reizes += 1
        TV "NO! ABSOLUTELY NOT!"
        TV "These... Peh, these are mah work gloves!"
        TV "NO! YOU MAY NOT TAKE MY GLOVES AWAY FROM ME! THIEF!"
        "Calm down, I'm not trying to take anything from you..."
        TV "And yet here you stand... IN MY TERRITORY!"
        TV "If ah were you, I'd run for the hills!"
        jump count

    label ot1:
        $ reizes += 1
        TV "That's right, little eyeball..."
        TV "STAY AWAY FROM MY TERRITORY!"
        if killer == "Remido" or killer == "Eyenile":
            TV "But don't spin those lies about me!"
            TV "Why I oughta make a SCARECROW outta her or her little DOLL friend!"
            jump count
        else:
            jump count

    label ot2:
        $ reizes += 1
        TV "WHO DOES THAT GUY THINK HE IS?"
        TV "Don't listen to that doll creature thing whatever..."
        TV "He'll point fingers at anyone when he feels just the slightest bit threatened!"
        TV "Even someone as cute and cuddly as me!"
        jump count

    label ot3:
        $ reizes += 1
        TV "They're about the only one that can respect my warning signals"
        TV "Only one other than that Moth creature, anyways"
        "Anything else?"
        TV "Why, I could make them my farm plot if I wanted to!"
        "So, why don't you?"
        if killer == "TV":
            TV "They... Uh... They'd boil my crops!"
            TV "ALL MY WORK WOULD BE RUINED!"
            jump count
        else:
            TV "I shouldn't make 'them' my enemy..."
            TV "Not only would they ruin my crops... THEY'D REPURPOSE THEM INTO BORING MACHINES!"
            TV "I can't let that happen!"
            jump count

    label ot4:
        $ reizes += 1
        TV "Eh... who is that?"
        "You don't know?"
        TV "Well..."
        TV "Uh..."
        TV "OKAY, OKAY, I know who that is!"
        TV "They rarely leave their house..."
        TV "Ah've never seen them out and about! They don't approach mah farm, so I don't bother them either!"
        TV "It's a win-win!"
        "Are you implying you've seen them?"
        if killer == "TV":
            TV "Well, do--"
            TV "I mean, no!"
            TV "No, I haven't!!! "
            "So have you or have you not seen the Moth?"
            TV "Are your ears full of chicken feathers? OF COURSE I HAVEN'T!"
            TV "I mean, how could ah even seen them? I live in a screen!"
            "But you can see me now"
            TV "WELL, MAYBE YOU SHOULD ASK LESS QUESTIONS!!!"
            jump count
        else:
            TV "Well, doy! I've seen that moth..."
            TV "Through their screen!"
            TV "Hey, why does this even matter?"
            jump count