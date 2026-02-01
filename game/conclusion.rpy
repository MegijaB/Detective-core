label conclusion:
    menu:
        "TV":
            jump ChooseTV
        "Eyenile":
            jump ChooseEyenile
        "Remido":
            jump ChooseRemido
        "Moth":
            jump ChooseMoth
        "Judge":
            jump ChooseJudge

    label ChooseTV:
        if killer == "TV":
            jump Correct
        else:
            jump incorrect

    label ChooseEyenile:
        if killer == "Eyenile":
            jump Correct
        else:
            jump incorrect

    label ChooseRemido:
        if killer == "Remido":
            jump Correct
        else:
            jump incorrect

    label ChooseMoth:
        if killer == "Moth":
            jump Correct
        else:
            jump incorrect

    label ChooseJudge:
        if killer == "Judge":
            jump Correct
        else:
            jump incorrect
            
    label Correct:
        "Wow, you found murderer!"
        "We are so proud of you!"
        "But"
        "You now know too much, we can't let you live"
        return

    label incorrect:
        "Well, you got it wrong"
        "You know what does it mean?"
        "Right"
        "You made a mistake and now you have to pay for it"
        return