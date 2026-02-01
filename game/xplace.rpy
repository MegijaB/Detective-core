label xplace:
    show screen small
    "Wow, I thought I will saw here a room, but..."
    "There is just darkness"
    "In report there was an information about what they could find"
    "hmm"
    if killer == "TV":
        "fixed dark aura, which is usually after unstable"
        "Claw injuries on a corpse"
        "scratches on the walls as if from horns"
        call screen map
    
    elif killer == "Eyenile":
        "blood drained from corpses"
        "Claw injuries on a corpse"
        "No unnecessary actions were taken. Everything was clean. You can tell the murderer was careful."
        call screen map

    elif killer == "Remido":
        "fixed dark aura, which is usually after unstable"
        "blood drained from corpses"
        "Claw injuries on a corpse"
        call screen map

    elif killer == "Moth":
        "fixed dark aura, which is usually after unstable"
        "No unnecessary actions were taken. Everything was clean. You can tell the murderer was careful."
        "scratches on the walls as if from horns"
        call screen map

    elif killer == "Judge":
        "blood drained from corpses"
        "No unnecessary actions were taken. Everything was clean. You can tell the murderer was careful."
        "scratches on the walls as if from horns"
        call screen map