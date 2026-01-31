
define Eyenile = Character("Eyenile")
define Remido = Character("Remido")

default reizes =0
default viet =0
label start:
    $ imposters = ["Eyenile","Sam"]
    $ killer = renpy.random.choice(imposters)
    call screen map

    "Hello detective"
    "Your task for today is find the killer"
    "We found several dead bodys in room 15"
    "So for this task we choose you!"
    "You can walk around and ask questions to creatures, that live here"
    "But remember, you can ask only 5 questions"
    "After that they become silent and don't want to talk"
    "We don't care if you ask all of questions to one person or each questin to each creatue"
    "We just need result"
    "Oh, I almost forgot!"
    "If you won't find the real killer, we will just kill you :3"
    "Good luck and have fun! :D"
    
    jump Room



