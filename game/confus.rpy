default
label confus:
    show judge-default as char
    show screen small
    "confus"
    menu:
        "Ask something about Mutatum"
            jump youco
        "Ask something about others"
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
        if killer = "Mutatum":
            show judge-dismiss as char
            Mutatum "Why, 'I' was here, of course"
        else:
            show judge-default as char
            Mutatum "Why, I was here, of course"
        Mutatum "I can't leave this place..."
        show judge-curious as char
        Mutatum "Not until the levels of chaos in this place reach an equilibrium"
        if killer = "Mutatum":
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