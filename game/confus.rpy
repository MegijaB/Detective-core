label confus:
    $ viet = 5
    show judge-default as char
    show screen small
    menu:
        "Ask something about Mutatum":
            jump youco
        "Ask something about others":
            jump otherco

    label youco:
        show judge-dismiss as char
        Mutatum "I will tell you what you need to know"
        menu:
            "What was your relationship with the victim?":
                jump yco1
            "Where were you during the time of the murder?":
                jump yco2
            "What's with the hole in your chest?":
                jump yco3
            "Nevermind":
                jump confus

    label otherco:
        show judge-default as char
        Mutatum "I will tell you what you need to know"
        menu:
            "Tell me about Eye":
                jump oco1
            "Tell me about Doll":
                jump oco2
            "Tell me about Furry":
                jump oco3
            "Tell me about Moth":
                jump oco4
            "Nevermind":
                jump confus

    label yco1:
        $ reizes += 1
        Mutatum "I cared about the victim as much as I do about everyone else"
        "And what does that mean?"
        Mutatum "Do you care about one fly more than the other? What about every moth and eyeball?"
        Mutatum "Of course you do not, you treat them all as equal"
        Mutatum "The same applies to my subjects... Any good judge will tell you that"
        Mutatum "When you care about everyone, 'caring' loses its meaning and everything resets to nil"
        "Is that all?"
        Mutatum "That is all"
        jump count

    label yco2:
        $ reizes += 1
        if killer == "Mutatum":
            show judge-dismiss as char
            Mutatum "Why, 'I' was here, of course"
        else:
            show judge-default as char
            Mutatum "Why, I was here, of course"
        Mutatum "I can't leave this place..."
        show judge-curious as char
        Mutatum "Not until the levels of chaos in this place reach an equilibrium"
        if killer == "Mutatum":
            "Why do I get the feeling there's a catch?"
            Mutatum "For every straightforward thing in this universe, there, too, must be roundabouts"
            Mutatum "Just like my area of expertise"
        jump count
    
    label yco3:
        $ reizes += 1
        show judge-curious as char
        Mutatum "It is a sign of my devotion to reason"
        Mutatum "'I', too, once had a heart..."
        if killer == "Mutatum":
            show judge-dismiss as char
            Mutatum "...but the law is reason, free from passion"
            "But how are you still alive before my eyes?"
            show judge-tilt as char
            Mutatum "Surely you don't want to waste one of your precious chances to ask a question on something as trivial as this?"
            "..."
        else:
            show judge-default as char
            Mutatum "...but 'I' gave it up for the greater good, for the greater balance"
            "What does that mean?"
            show judge-tilt as char
            Mutatum "I told you I'd only tell you what you need to know"
        jump count
    
    label oco1:
        $ reizes += 1
        show judge-default as char
        Mutatum "Even grounded people can sometimes neglect to look at what's in front of them"
        Mutatum "Eyenile is no exception"
        Mutatum "She appears to believe that I am an 'it,' a 'robot'"
        show judge-curious as char
        Mutatum "However, I, too, bleed and require blood for things more than mere fuel"
        show judge-tilt as char
        Mutatum "Could this divergence in her perception be that doll's doing? Or is that one of her careful machinations?"
        "What do you mean?"
        show judge-default as char
        Mutatum "Why don't you go get to know them better and see for yourself?"
        jump count

    label oco2:
        $ reizes += 1
        show judge-default as char
        Mutatum "I am usually not one for jokes, but even people like me must balance out the prim and proper act"
        show judge-curious as char
        Mutatum "It just so happens that Remido is quite easy to tease"
        show judge-default as char
        Mutatum "Well, it is true that he is oh, so unstable on his own"
        "Unstable?"
        Mutatum "Brash, suspicious of others... Not in the childlike way that talking TV is"
        Mutatum "Eyenile balances him out quite well"
        "Anything else you'd like to add, other than 'the balance?'"
        if killer != "Mutatum":
            Mutatum "I suppose... we do share a similarity"
            Mutatum "However, 'my' resources are limited"
            "And what does that mean?"
            Mutatum "Nothing that you need to know"
        else:
            Mutatum "Hmm..."
            show judge-tilt as char
            Mutatum "No"
        jump count
    
    label oco3:
        $ reizes += 1
        show judge-default as char
        Mutatum "I don't know the TV too well" 
        Mutatum "Sometimes when I pass by a random screen close to their domain, that cute character will flicker in the screen"
        "Flicker? Could you elaborate on that?"
        Mutatum "A shadow passes, followed by but a brief flash of light... A little too quick for the average person or creature to make sense of"
        Mutatum "The face that shows during those brief moments hints at frustration"
        show judge-tilt as char
        Mutatum "Perhaps they are merely guarding their territory"
        jump count
    
    label oco4:
        $ reizes += 1
        Mutatum "What a mysterious fellow"
        Mutatum "I've seen their grotesque little hut, all alone in that otherwise beautiful field"
        Mutatum "However, whenever I've tried to communicate with them in any capacity beyond court orders..."
        Mutatum "What followed was a deathly silence"
        "You sure they weren't out for a walk?"
        Mutatum "Certain. My indicators showed signs of life in that house"
        jump count