screen map:
    add "map.png"
    imagebutton:
        xpos 1343
        ypos 9
        idle "circus1.png"
        hover "circus.png"
        action Jump("circus")
    
    imagebutton:
        xpos 1425
        ypos 660
        idle "forest1.png"
        hover "forest.png"
        action Jump("forest")
    
    imagebutton:
        xpos 770
        ypos 250
        idle "Confus1.png"
        hover "Confus.png"
        action Jump("Confus")

    imagebutton:
        xpos 790
        ypos 720
        idle "flower1.png"
        hover "flower.png"
        action Jump("flower")

    imagebutton:
        xpos 45
        ypos 400
        idle "Xplace1.png"
        hover "Xplace.png"
        action Jump("xplace")

    imagebutton:
        xpos 75
        ypos 750
        idle "TV1.png"
        hover "TV.png"
        action Jump("TV")

screen small:
    imagebutton:
        xpos 1700
        ypos 20
        idle "smallmap.png"
        hover "smallmap1.png"
        action Jump("smallmap")