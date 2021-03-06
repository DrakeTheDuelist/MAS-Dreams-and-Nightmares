# The core event that triggers all other events in the submod.
#
# You must at least have normal affection to attempt this submod.
#
# On first run, Monika will explain the premise of the submod. (Can be skipped later.)
# 
# If Monika has a nightmare, this label will stop you from attempting to
# have Monika dream again for the next 12 hours after the dream concludes.
init 21 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="DaN_try_to_dream",
            category=['Dreams and Nightmares'],
            prompt="Try to dream?",
            conditional="mas_isMoniNormal(higher=True)",
            random=True
        )
    )
            
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="DaN_revisit_dream",
            category=['Dreams and Nightmares'],
            prompt="Revisit a dream?",
            conditional="mas_isMoniNormal(higher=True) and persistent._mas_dreams_had",
            random=True
        )
    )   

    if not persistent._DaN_should_create_events:
        if "DaN_try_to_dream" in persistent.event_database:
            persistent.event_database.pop("DaN_try_to_dream")

        if "DaN_revisit_dream" in persistent.event_database:
            persistent.event_database.pop("DaN_revisit_dream")

# The root action of getting a random dream.
label DaN_try_to_dream:
    if persistent._mas_apprehensive_start:
        # note: This is a valid way to call apprehension because the only POSSIBLE
        # way for Monika to be apprehensive is if she dreamt a minimum of twice
        # (as you can never draw a nightmare the first time), and so you won't be
        # skppping over any necessary explanations.
        call DaN_dream_despite_apprehension()
    else: 
        if persistent._mas_dreams_and_nightmares_explained:
            m 3esc "I recall explaining this to you before."
            m "Would you like me to explain again?"
            menu:
                m "Would you like me to explain again?{fast}"
                "Yes, please.":
                    $ persistent._mas_dreams_and_nightmares_explained = False
                "No thanks.":
                    m 7hub "Good, so you still remember."
                    if mas_isMoniLove():
                        m 5ekbfu "I know you'll hang on my every word, [mas_get_player_nickname()]..."
                    elif mas_isMoniEnamored():
                        m 5eubla "You're such a good listener, [player]."
                    else:
                        m "That should save us both some time."
        if not persistent._mas_dreams_and_nightmares_explained:
            call DaN_explanation
        m 4wub "What do you say?  Could you help me start the code?"
        menu:
            m "Could you help me start the code?{fast}"
            "Not right now.":
                m 1eka "Okay.  I'll wait until you're ready."
                m 3eka "But let's come back to this later.  I'm {i}really{/i} looking forward to this."
            "Let's go!":
                call DaN_perchance_to_dream
    return
# The root action of randomly having a drem Monika has already experienced so far.
label DaN_revisit_dream:
    if persistent._mas_apprehensive_start:
        call DaN_dream_despite_apprehension()
    else: 
        m 1gsb "This dreaming idea would be pretty boring if I only ever got to do it once."
        if persistent._mas_asked_to_stay_dreaming:
            m 5rtd "Plus, I've had some dreams you've woken me up early from.  I'd like to see those through to the end."
        m 7esb "What do you say, [player]?  Would you like to revisit a dream I've had before?"
        menu:
            m "Would you like to revisit a dream I've had before?{fast}"
            "Let's do it!":
                if persistent._mas_dreams_had:
                    call DaN_begin_sleep
                
                    #roll for which dream Monika will have
                    $ random_dream = renpy.random.choice(persistent._mas_dreams_had)

                    call DaN_select_dream(random_dream)
                else:
                    m 4hublb "Silly [player], I need to {i}have{/i} a dream before I can revisit it."
                    m 4rubld "Though I don't think it's your fault that you've found yourself here.  Something must've gone {i}very{/i} wrong."
                    m 3rud "From what I'm seeing in the code, it looks like DrakeTheDuelist was worried that something like this might happen."
                    m "So he left some code for me to run, just in case things went haywire like this."
                    m 3lub "Talk about jamming the code into place when it doesn't want to behave itself.{w=1.5}  Like {i}I{/i} have room to talk..."
                    m 2dud "Hang on a second.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}"
                    $ persistent._mas_all_dreams = [1]
                    $ persistent._mas_dreams_had = []
                    m 2eud "There.  I just ran the tweak."
                    m 2hub "That should get this submod back on the rails."
            "Not right now.":
                m 1eka "Okay.  I'll wait until you're ready."
    return
# regardless of whether dreaming or revisiting an old dream, if Monika is anxious
# due to a past nightmare, she should act the same way.
label DaN_perchance_to_dream:
    if persistent._mas_all_dreams:
        call DaN_begin_sleep
    
        #roll for which dream Monika will have
        $ random_dream = renpy.random.choice(persistent._mas_all_dreams)
        $ persistent._mas_all_dreams.remove(random_dream)
        if (persistent._mas_dreams_had):
            $ persistent._mas_dreams_had.append(random_dream)
        else:
            $ persistent._mas_dreams_had = [random_dream]

        call DaN_select_dream(random_dream)

    # read as soon as Monika's last dream resolves
    if not persistent._mas_all_dreams:
        call DaN_all_dreams_finished
    return