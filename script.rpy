# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Name")
define s = Character("Octopus Spirit")
define f1 = Character("Friend 1")
define f2 = Character("Mafia Friend")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg meadow

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mc happy

    # These display lines of dialogue.

    mc "(Where am I?)"

    "I looked around and saw I was on a boat in the middle of still water."

    "When I stood up, I saw a figure floating towards me and I froze."

    ??? "Do you know why you're here? Or where this even is?"

    mc "No... but what are you?"

    s "I'm an octopus spirit. More importantly, you're in Limbo; you're stuck in a time between life and death right now."

    mc "Why? Did I do something wrong?"

    s "Yes. Before you died, you were a horrible, cold-hearted person."

    s "However, you died in such a pitiful way that I've decided to give you one more chance at life."

    "I stared wide-eyed at it, hoping that this could only be a dream."

    mc "How will I get back to earth then?"

    s "Well that's not the problem."

    s "I'm only going to give you one month again on earth."

    s "During that time, you must figure out what you did wrong in your past life and how you died."

    s "Not only must you remember these things, but you have to change your ways; if not, you will actually die and never have another chance to live again."

    mc "This is crazy! How am I possibly going to live then?"

    s "That's why it's up to you to figure out your wrongdoings and correct them in this one month that I'm giving you."

    s "Before I send you back to your home on earth, I'll give you a clue."

    s "Do you remember your name?"

    mc "... Name"

    "Right as I remembered my name again, the spirit began to wrap its tentacles around me and I became unconscious."

    # background change



    # This ends the game.

    return
