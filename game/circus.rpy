default mask =0
label circus:
  $  viet = 1
  show doll1 as char
  show screen small
  menu:
    "Ask something about Remido":
      jump youc
    "Ask something about others":
      jump otherc
        
  label youc:
    Remido "?"
    menu:
      "What was your relationship with victim?":
        jump yc1
      "Why are you wearing this mask?":
        jump yc2
      "Where were you when he was killed?":
        jump yc3
      "Do you like blood?":
        jump yc4
      "Nevermind":
        jump circus
  
  label yc1:
    $  reizes +=1
    Remido "I hated him"
    "I was ready for this answer"
    "But you just asked it yourself"
    "Yeah, but I thought you will just say that you don't have any relationship or something like that..?"
    Remido "No, I hated him"
    show doll2 as char
    Remido "My best friend allways complined about him"
    Remido "I believe not just my friend, but almost everyone else hated him"
    "So, technically it could be you..."
    Remido "Please, do you really think that I would tell you all of this if I killed him?"
    Remido "Who do you think am I?"
    show doll1 as char
    Remido "Some kind of a self hater?"
    Remido "No, it's not me. I just believe you will make the right choice and thats all"
    "..."
    Remido "I really care about my friend and I hope you will find the imposter"
    jump count

  label yc2:
    $  reizes +=1
    if mask == 0:
      show doll2 as char
      Remido "I jsut feel more safe in it"
      "That's it?"
      Remido "Yeah"
      show doll3 as char
      "You are lying"
      $  mask +=1
      jump count
    elif mask == 1:
      show doll3 as char
      Remido "Looks like you don't understand with first time"
      "I know you are lying"
      show doll4 as char
      Remido "And you are placing your nose where you don't have to"
      Remido "You come here, ask disturbing questions and still..."
      show doll5 as char
      Remido "DESIRE TO GET AN ANSWER"
      show doll6 as char
      Remido "WHO ARE YOU?!"
      show doll7 as char
      Remido "DETECTIVE"
      show doll6 as char
      Remido "YOU ARE TOO PROUD BUT YOU DONT UNDERSTAND ONE THING"
      show doll7 as char
      Remido "THEY WILL JUST REPLACE YOU IF YOU DIE"
      show doll5 as char
      Remido "SO, look what questions you are asking"
      show doll4 as char
      Remido "And I'm sorry for my act"
      show doll3 as char
      Remido "But I think you now got a point"
      jump count

  label yc3:
    $  reizes +=1
    Remido "With my friend"
    "What it's name?"
    show doll2 as char
    Remido "Is it another question?"
    "But you didn't even answer me this properly!"
    show doll1 as char
    Remido "It's another question"
    "But-{cps=1} {/cps}{nw}"
    Remido "Other questoin"
    "Ugh..."
    jump count

  label yc4:
    $  reizes +=1
    Remido "Maybe"
    "And.....?"
    Remido "That's all"
    show doll2 as char
    "I used one of my five possible questoins for this and you just say that's all?"
    Remido "It is the next question?"
    jump count

  label otherc:
    Remido "Which one?"
    menu:
      "Tell me about Eye":
        jump ceye
      "Tell me about Judge":
        jump cJudge
      "Tell me about Furry":
        jump cFurry
      "Tell me about Moth":
        jump cMoth
      "Nevermind":
        jump circus

  label ceye:
    $  reizes +=1
    show doll2 as char
    Remido "You mean Eyenile?"
    "Yeah, the one who lives in Drop Forest"
    if killer == "Eyenile":
      show doll1 as char
      Remido "She is shy"
      Remido "Ofcourse if you ask something her she is not who easily reject you"
      "I would want more information about if she could be a murderer"
      Remido "I don't think so"
      show doll2 as char
      Remido "I would say it's little disgusting that you could think of her that way"
      "?"
      Remido "Yes, Victim was rude to her, but she could never do something like that"
      jump count
    else:
      show doll1 as char
      Remido "She has claws and IS bloodsucker"
      "Wow, you really tell me everything about her?"
      "I thought you will be silent"
      show doll2 as char
      Remido "Because I'm sure she is not the murderer"
      "And I will continue to belive it"
      jump count
    

  label cJudge:
    $  reizes +=1
    Remido "I hate them"
    "Just like that?"
    show doll3 as char
    Remido "They are aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaannoying"
    Remido "They think I am violating the law"
    "You have laws here?"
    show doll2 as char
    Remido "No, but they think otherwise"
    Remido " - Remido, you are too loud"
    show doll3 as char
    Remido "- Remido, I am sure you are selling somthing illegal"
    show doll4 as char
    Remido " - Remido, I'm sure you killed someone{cps=1} {/cps}{nw}"
    "huh?"
    show doll2 as char
    Remido "But to be honest they are really careful"
    "Hmmm..."
    jump count

  label cFurry:
    $  reizes +=1
    show doll2 as char
    Remido "You want know more about TV furry guy?"
    "Why you all call him furry...?"
    Remido "..."
    Remido "You want know more about TV furry guy?"
    Remido "Well, he has claws"
    show doll3 as char
    Remido "But I think it's obviously by just looking at him"
    "But he is just TV"
    Remido "Poor detective, got fooled by Furry box"
    "?????"
    show doll2 as char
    Remido "He just shows as something cute"
    Remido "I can't explain, but I feel something dark from him"
    "...."
    Remido "I have doubts that he is stable"
    jump count


  label cMoth:
    $  reizes +=1
    show doll2 as char
    Remido "Mostly hides in flowers"
    Remido "Has horns"
    "And...."
    Remido "That's all"
    "It's a joke, right?"
    show doll1 as char
    Remido "Listen, if you want hear something more about it, then better would be if you ask Eyenile about it"
    Remido "She is more closer to it than I"
    Remido "I am not real fan of bugs"
    jump count


  