
define Eyenile = Character("Eyenile")
define Remido = Character("Remido")
define Mutatum = Character("Mutatum")
define TV = Character("TV")
define Moth = Character("Moth")

default reizes =0
default viet = 0
label start:
    $ imposters = ["Eyenile","Remido","Judge","TV","Moth" ]
    $ killer = renpy.random.choice(imposters)

    "Hello, detective"
    "Your task for today is to find the killer"
    "We have found several dead bodies in room 15"
    "So we chose you to crack this case!"
    "You can walk around and ask questions to the creatures that live here"
    "But remember, you can ask only 5 questions"
    "After that, they'll become silent and refuse to talk"
    "We don't care if you use all of your chances to ask questions on just one character or ask everyone one question each"
    "We just need results"
    "Oh, I almost forgot!"
    "If you can't find the real killer, we will just kill you :3"
    "Good luck and have fun! :D"

    call screen map



