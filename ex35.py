from sys import exit

def gold_room():
    print "This room is ful of gold. How much do you take?"

    next_input = raw_input("> ")
    if "0" in next_input or "1" in next_input:
        how_much= int(next_input)
    else:
        dead("Man, learn to type a numbers.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "There bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "atunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go throught it now."
            bear_moved = True
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why,"Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
