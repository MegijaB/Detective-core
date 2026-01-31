default mask =0
label circus:
  $  viet = 1
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
      "Where have you beem when he was killed?":
        jump yc3
      "Do you like blood?":
        jump yc4
      "Nevermind":
        jump circus
  
  label yc1:
    $  reizes +=1
    Remido "I hated him"
    "I was ready for rhis answer"
    "But you just asked it by yourself"
    "Yeah, but I thought you will just say that you don't have any relationship or something like that..?"
    Remido "No, I hated him"
    Remido "My best friend allways complined about him"
    Remido "I belive not just my friend, but almost everyone else hated him"
    "So, tehnically it could be you..."
    Remido "Please, you really think that I would tell you all this if I killed him?"
    Remido "Who do you think am I?"
    Remido "Some kind of slefhater?"
    Remido "No, it's not me. I just belive you will make the right choice and thats all"
    "..."
    Remido "I really care about my friend and I hope, you will find the imposter"
    jump count

  label yc2:
    $  reizes +=1
    if mask == 0:
      Remido "I jsut feel more safe in it"
      "That's it?"
      Remido "Yeah"
      "You are lying"
      $  mask +=1
      jump count
    elif mask == 1:
      Remido "Looks like you don't understand with first time"
      "I know you are lying"
      Remido "And you are placing your nose where you don't have to"
      Remido "You come here, ask disturbing questions and still..."
      Remido "DESIRE TO GET AN ANSWER"
      Remido "WHO ARE YOU?!"
      Remido "DETECTIVE"
      Remido "YOU ARE TOO PROUD BUT YOU DONT UNDERSTAND ONE THING"
      Remido "THEY WILL JUST REPLACE YOU IF YOU DIE"
      Remido "SO, look what questions you are asking"
      Remido "And I'm sorry for my act"
      Remido "But I think you now got a point"
      jump count

  label yc3:
    $  reizes +=1
    Remido "With my friend"
    "What it's name?"
    Remido "Is it another question?"
    "But you didn't even answer me this properly!"
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
    "I used one of my five possible questoins for this and you just say that's all?"
    Remido "It is the next question?"
    jump count
    


  