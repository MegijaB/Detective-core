label flower:
    $ viet = 3
    show moth as char
    show screen small
    menu:
        "Ask something about Moth":
            jump youfl
        "Ask something about others":
            jump otherfl

    label youfl:
        menu:
            "What was your relationship with victim?":
                jump fl
            "Where were you when he was killed?":
                jump fl
            "Do you like blood?":
                jump fl
            "Nevermind":
                jump flower
        
    label otherfl:
    Moth "..."
    menu:
        "Tell me about Eye":
            jump fl
        "Tell me about Judge":
            jump fl
        "Tell me about Furry":
            jump fl
        "Tell me about Remido":
            jump fl
        "Nevermind":
            jump flower

    label fl:
        $  reizes +=1
        "So?"
        Moth "Moth"
        "Can you answer on my questoin?"
        Moth "Moth"
        "..."
        Moth "..."
        "You just took my possibility to ask 1 question and still won't answer?"
        Moth "Moth Moth"
        jump count