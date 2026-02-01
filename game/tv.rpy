label tv:
    show light-sus as char
    show light-default as char
    show screen small
    "tv"
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
                jump tv
            "Nevermind":
                jump tv