
label forest:
    scene backgrounddrop
    $  viet = 2
    show eye1 as char
    show screen small
    menu:
        "Ask something about Eyenile":
            jump youf
        "Ask something about others":
            jump otherf
        
    
    label youf:
        Eyenile "What would you want to know?"
        menu:
            "What was your relationship with victim?":
                jump yf1
            "Why are you hiding your arms?":
                jump yf2
            "Where have you beem when he was killed?":
                jump yf3
            "Do you like blood?":
                jump yf4
            "Nevermind":
                jump forest
                
    label yf1:
        $  reizes +=1
        show eye3 as char
        Eyenile "We... were not friends"
        "why?"
        Eyenile "He was.... really rude"
        Eyenile "Allways thought about himself higher than he is"
        Eyenile "He often visited my forest while I wasn't home and steal my water drops"
        "Why would he do  it?"
        show eye4 as char
        Eyenile "I don't know"
        show eye3 as char
        Eyenile "He had really awful personallity and I don't know anyone who would liked him"
        show eye1 as char
        Eyenile "Maybe exception would be Judge but I have doubts"
        "Why?"
        Eyenile "Is this your next question?"
        jump count
    
    label yf2:
        $  reizes +=1
        if killer == "Eyenile":
            show eye3 as char
            Eyenile "..."
            Eyenile "I would choose not to answer this question"
            show eye2 as char
            "I have to know, I'm detective"
            "It' could be import clue for me-{cps=1} {/cps}{nw}"
            show eye3 as char
            Eyenile "Really? My arms?"
            show eye4 as char
            Eyenile "The only think I don't want to talk about?"
            show eye5 as char
            Eyenile "You are disgusting"
            Eyenile "Actually, you know what?"
            show eye3 as char
            Eyenile "In 155 we know each other, and lived peacefully a long time"
            Eyenile "But suddenly one of us die and they send detective"
            Eyenile "..."
            Eyenile "..."
            "..."
            Eyenile "Detective with really dark soul"
            "..."
            Eyenile "You can ask me other questions, but I won't give an answer for this"
            jump count
        else:
            show eye3 as char
            Eyenile "..."
            Eyenile "I.... don't like my arms"
            "Something is wrong with your arms?"
            Eyenile "I have claws and I don't like them"
            "?"
            show eye4 as char
            Eyenile "It's really painful topic for me"
            show eye5 as char
            Eyenile "Almost nobody wanted to talk with me because of it"
            show eye4 as char
            Eyenile "Just my friend never judged me"
            Eyenile "Because we are alike"
            "who is it?"
            Eyenile "...."
            jump count
     
    label yf3:

        $  reizes +=1
        Eyenile "With my friend"
        "What it's name?"
        Eyenile "Is it another question?"
        show eye4 as char
        "But you didn't even answer me this properly!"
        Eyenile "It's another question"
        "But-{cps=1} {/cps}{nw}"
        Eyenile "Other questoin"
        "Ugh..."
        jump count

    
    label yf4:
        $  reizes +=1
        if killer == "Eyenile":
            Eyenile "I am not against it"
            "But do you like it?"
            show eye3 as char
            Eyenile "Maybe"
            "Not really answer to my question"
            Eyenile "You think it's normal to ask about this kind of thing?"
            "Well, knowing what cretures live here, I could say it's pretty good question"
            Eyenile "You have a point"
            "Well?"
            show eye4 as char
            Eyenile "I think it's time for next question"
            "WHAT?"
            "But you didn't answer about blood"
            Eyenile "Guess"
            "..."
            menu:
                "Yes":
                    jump answerf
                "No":
                    jump answerf 
            label answerf:
                Eyenile "Maybe"  
            jump count


        else:

            Eyenile "Yes"
            "That's it?"
            show eye4 as char
            Eyenile "What you wanted to hear?"
            "I don't know. I thought you will deny"
            show eye1 as char
            Eyenile "Why would I hide it if I know I'm not the killer?"
            "You are so sure that I won't think about you as suspect now?"
            Eyenile "I belive you will make the right choice"
            jump count

    label otherf:
        Eyenile "What would you want to know?"
        menu:
            "Tell me about Doll":
                jump fDoll
            "Tell me about Judge":
                jump fJudge
            "Tell me about Furry":
                jump fFurry
            "Tell me about Moth":
                jump fMoth
            "Nevermind":
                jump forest
    
    label fDoll:
        $  reizes +=1
        Eyenile "You mean Remido?"
        "Yes. The one, who live in circus"
        Eyenile "What do you want to know about him?"
        show eye4 as char
        "Everything you know"
        Eyenile "Hmmmm.... I know lot of things about him"
        Eyenile "He is my best friend"
        "Has claws or horns?"
        if killer == "Remido":
            show eye3 as char
            Eyenile "I don't think I can tell you about it"
            "why?"
            Eyenile "Because he is my friend and I don't want talk too much about my friends"
            "Then tell me if he like blood?"
            Eyenile "..."
            "His personality?"
            Eyenile "..."
            "COME ON"
            "Don't you dare to say that you won't answer any questions about him now???"
            Eyenile "..."
            "..."
            show eye1 as char
            "I hate you"
            jump count

        else:
            show eye4 as char
            Eyenile "Claws"
            "Likes blood?"
            Eyenile "Yes. But he drinks only animal blood"
            "So you are sure that it's not him?"
            Eyenile "Yes"
            "confidently"
            show eye1 as char
            Eyenile "I just know what I am saying"
            jump count

            

    label fJudge:
        $  reizes +=1
        "I want more information about robot, that lives in Confusion Dimension"
        Eyenile "What do you want to know about him?"
        "Everything you know"
        show eye4 as char
        Eyenile "Hmm.... it likes to judge"
        show eye3 as char
        Eyenile "And... he was pretty close to victim"
        "You are talking like you are not sure"
        Eyenile "Because I'm not"
        "Oh..."
        show eye1 as char
        Eyenile "Listen, almost all of us rearly speek to each other"
        Eyenile "Of course there is some exceptions like me and my best friend, but with someone else?"
        show eye4 as char
        Eyenile "No"
        Eyenile "I can say, that judge is one of the most careful thinhs here"
        Eyenile "It knows what it is doing"
        jump count




    label fFurry:
        $  reizes +=1
        Eyenile "You mean about furry that lives in TV Room? "
        "Yes... is it its real name?"
        Eyenile "I don't know, I just call it a furry"
        "..."
        "Wel... what can you say about it?"
        if killer == "Remido" or killer == "Eyenile":
            show eye4 as char
            Eyenile "It has claws"
            "!"
            show eye2 as char
            "Claws? I would't belive it just by looking at it"
            show eye4 as char
            Eyenile "Don't be fooled by its cute apperance"
            Eyenile "It is real monster ir sheep clotches"
            "Can you say a little bit more about it?"
            "I am trying to understand before conclusioins"
            show eye5 as char
            Eyenile "It is a bloodsucking monster"
            Eyenile "Ask Moth from Flower Field"
            "Moth?"

            show eye4 as char
            Eyenile "Yes, he says, that sometimes, more often in night time, you can hear strange noises coming from TV Room"
            "But why would you think he is bloodsucking monster?"
            Eyenile "I can't explain"
            "why?"
            show eye5 as char
            Eyenile "I am scared"
            "?"
            Eyenile "What if you won't charge it?"
            Eyenile "He definetlly will come after me"
            Eyenile "Belive me or not but it has eyes everywhere"
            Eyenile "I don't want to be next victim"
            jump count

        else:
            Eyenile "Hmmmmm"
            Eyenile "I can't say lot of things about it"
            "why?"
            show eye4 as char
            Eyenile "Because I don't really know this person"
            "But don't you all live in one place?"
            Eyenile "Tell me, you know all your neighbors?"
            Eyenile "Well I not"
            show eye1 as char
            Eyenile "Only I can say, that it is real wolf in sheep clotchings"
            "What it supposed to mean?"
            show eye3 as char
            Eyenile "Don't be fooled by it's apperance"
            Eyenile "I don't know it that good like, for example, Judge, but I know it is something strange"
            Eyenile "Something I can't explain"
            show eye4 as char
            Eyenile "Oh, almost forgot, it has claws"
            "Claws?"
            Eyenile "Yeah"
            Eyenile "That's all I can tell you about it"
            jump count

    label fMoth:
        $  reizes +=1
        Eyenile "Moth?"
        "Yes. The one, who lives in Flower Field"
        show eye4 as char
        Eyenile "What do you want to know about him?"
        "Everything you know"
        Eyenile "Hmmmm..."
        Eyenile "Well..he is... pretty normal?"
        "Why so unsure?"
        show eye1 as char
        Eyenile "We are in kind of neutral relationship"
        "What does it means?"
        Eyenile "You ask too many questions"
        "..."
        show eye4 as char
        Eyenile "*Sigh*"
        Eyenile "We rearly talk"
        Eyenile "If we find something interesting then we can exchaing our thoughts"
        Eyenile "He has horns"
        Eyenile "Before I even considered them as cute"
        "I can say something changed"
        Eyenile "He broke one of my drops that grow on tree"
        Eyenile "I know he was sorry, but still I can't really bring myself to think about them as something cute again"
        Eyenile "..."
        show eye1 as char
        "I can say by your face that there is someting else"
        Eyenile "Well, he is pretty careful about different stuff"
        "But you just mentioned that he broke something"
        show eye4 as char
        Eyenile "Yeah, but after that his face was darker than storm cloud"
        Eyenile "He hates when something is not like it's supposed to be"
        "Interesting..."
        jump count
       
    


