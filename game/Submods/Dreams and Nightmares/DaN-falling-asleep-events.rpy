# All code in this file gets called to resolve Monika falling asleep 
# before her dream, and randomly deciding on how she should behave
label DaN_begin_sleep:
    call DaN_dream_quip                
    call DaN_sweet_dreams_chance

    m 6eua ".{w=1}{nw}"
    m 6fua ".{w=1}{nw}"
    m 6tsa ".{w=1}{nw}"
    m 6dsa ".{w=1}.{w=1}.{w=1}{nw}"
    return
# Monika says something random before her dream begins
label DaN_dream_quip:
    python:
        # assemble all possible dream quips
        all_dream_quips = [
            "To sleep, perchance to dream.",
            "I wonder what my dreams will have in store this time.",
            "If I see you there, I'll know it worked."
        ]
        love_quip = "You know that place between sleep and awake?{w=1.5}  That place where you still remember dreaming?{w=1.5}  That's where I'll always love you~"
        enamored_quip = "Off to my dreams...{w=1}  Will you be joining me there?"
        post_nightmare_quips = [
            "Hopefully my dreams will be better this time.",
            "No whammy, no, whammy, no whammy..."
        ]
        subsequent_dream_quip = "Once more, unto the breach..."
        first_dream_quips = [
            "Here's hoping this works...",
            "Cross your fingers, [player]..."
        ]

        #bonus quips based on affection level
        if mas_isMoniLove():
            all_dream_quips.append(love_quip)
        elif mas_isMoniEnamored():
            all_dream_quips.append(enamored_quip)
        
        #bonus quips if Monika had a nightmare before
        if persistent._dan_had_nightmare:               
            all_dream_quips.append(post_nightmare_quips)

        #bonus quips depending on if this is Monika's first dream or not
        if persistent._dan_had_first_dream:
            all_dream_quips.append(subsequent_dream_quip)
        else:
            # on 1000+ affection, Monika will always ask to hold your hand on the first dream
            if mas_isMoniLove():
                all_dream_quips = ["HOLD HAND"]
            else:
                all_dream_quips.append(first_dream_quips)

        dream_quip = renpy.random.choice(all_dream_quips)
        
    if (dream_quip == love_quip):
        m 6ekbfb "[dream_quip]"
    elif (dream_quip == enamored_quip):
        m 6hkb "[dream_quip]"
    elif (dream_quip in post_nightmare_quips):
        m 6rksdrb "[dream_quip]"
    elif (dream_quip == "HOLD HAND"):
        call DaN_hold_monikas_hand
    else:
        m 6eub "[dream_quip]"
    return

# a random chance exists that Monika may ask you to hold her hand before the first dream
label DaN_hold_monikas_hand:
    m 6dubfsdrt "({i}deep exhale{/i})"
    m 2hubfsdrb "I'm still a little nervous, [player]..."
    menu:
        "Is there anything I can do?":
            m 3rublsdrb "Actually, now that you mention it..."
            m 3rublsdrd "If you don't mind..."
            m 5rublsdrb "Could you... {w=2}{nw}"
            extend 5eubssdrb "hold my hand for a second?"
            menu:
                "hold Monika's hand":
                    m 5ekbssdrb "Thank you."
                    m 5dubsc "{w=1}{nw}"
                    m 5hubfa "({i}squeezes back{/i})"
                "\"I... uh...\"  ({i}touch the monitor{/i})":
                    m 5etbssdrd "Uh..."
                    m 5hubfsdrb "I guess that works, ehehehe~"
                    m 5ekbfb "In all seriousness though, thank you for trying your best, [player]."
                    m 5dkbfa "It means a lot to me."
    return    
# determine odds of telling Monika "sweet dreams" before she sleeps
# Odds of this are based on affection level.
# Also, odds after a nightmare rise to that of the next highest relationship level.
label DaN_sweet_dreams_chance:
    python:
        if mas_isMoniLove():
            if persistent._dan_had_nightmare:
                odds_of_sweet_dreams = SWEETDREAMS_LOVE_NM
            else:
                odds_of_sweet_dreams = SWEETDREAMS_LOVE
        elif mas_isMoniEnamored():
            if persistent._dan_had_nightmare:
                odds_of_sweet_dreams = SWEETDREAMS_LOVE 
            else:
                odds_of_sweet_dreams = SWEETDREAMS_ENAMORED
        elif mas_isMoniAff():
            if persistent._dan_had_nightmare:
                odds_of_sweet_dreams = SWEETDREAMS_ENAMORED
            else:
                odds_of_sweet_dreams = SWEETDREAMS_AFF
        else:
            if persistent._dan_had_nightmare:
                odds_of_sweet_dreams = SWEETDREAMS_AFF
            else:
                odds_of_sweet_dreams = SWEETDREAMS_NORMAL
        
        say_sweet_dreams = random.randint(1, odds_of_sweet_dreams) == 1

        #if you say sweet dreams, get a random quip response
        if say_sweet_dreams:
            sweet_dreams_quips = [
                "Just hearig that helps keep the nightmares away.",
                "I feel a better dream coming on already.",
                "Watch over me, " + mas_get_player_nickname() + "."            
            ]

            if mas_isMoniLove():
                sweet_dreams_quips.append("You're like my guardian angel, [player].")
            
            if persistent._mas_first_kiss:
                sweet_dreams_quips.append("KISS")

            sweet_dreams_quip = renpy.random.choice(sweet_dreams_quips)

        #if dev, ignore randomness and force kiss while debugging
        #if persistent._dan_debug_mode:
        #    say_sweet_dreams = True
        #    sweet_dreams_quip = "KISS"

    if say_sweet_dreams:
        menu:
            "Sweet dreams~":
                if sweet_dreams_quip:
                    if sweet_dreams_quip == "KISS":
                        call monika_kissing_motion(initial_exp="6dubfd", mid_exp="6tkbfu", final_exp="6ekbfa")
                    else:
                        m 6fkbfb "[sweet_dreams_quip]"
                else:
                    m 6ekbfa "...{w=3}"
    return
# isolate the selector functionality.  Override if adding more than five dreams.
label DaN_select_dream(random_dream):
    if random_dream == 1:
        call DaN_dream_one 
    elif random_dream == 2: 
        call DaN_dream_two
    elif random_dream == 3:
        call DaN_dream_three  
    elif random_dream == 4:
        call DaN_dream_four  
    elif random_dream == 5:
        call DaN_dream_five
    else:
        m 2duc "{w=0.5}.{w=0.5}.{w=0.5}."
        m 2hub "Ehehehe~"
        m 3gub "Looks like something didn't {i}quite{/i} work out like it was supposed to be..."
        m 1rud "I don't think you should be able to see this."
        m 3rud "You should probably tell this submod's creator, DrakeTheDuelist, that something went wrong."
        m 4eub "I can even link you to the github page for the {a=[SUBMOD_GITHUB_LINK]}{i}{u}Dreams and Nightmares{/u}{/i}{/a} submod."
        m 5gtb "...What {i}am{/i} I talking about?{w=1}  This sure is a lot of work to put into an error screen..."
        m 2hub "Ahahaha~"
    return
