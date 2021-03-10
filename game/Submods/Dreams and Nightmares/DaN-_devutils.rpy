init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="reset_dreams_and_nightmares",
            category=['Dreams and Nightmares'],
            prompt="Reset",
            random=True
            )
        )
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="dan_devutil_checkevents",
            category=['Dreams and Nightmares'],
            prompt="Check",
            random=True
            )
        )

label dan_devutil_checkevents:
    if "dan_have_new_random_dream" in persistent.event_database: 
        m 1esd "The new dream event exists."
    else:
        m 1esd "The new dream event does not exist."

    if "dan_have_new_random_dream" in persistent._seen_ever:
        m 1esd "The new dream event has been seen."
    else:
        m 1esd "The new dream event has not beeen seen."

    if "dan_revisit_previous_dream" in persistent.event_database:
        m 1esd "The random revisit dream event exists."
    else:
        m 1esd "The random revisit dream event does not exist."

    if "dan_revisit_previous_dream" in persistent._seen_ever:
        m 1esd "The revisit dream event has been seen."
    else:
        m 1esd "The revisit dream event has not beeen seen."
    return

# reset all persistent variables
label reset_dreams_and_nightmares:
    m 3rub "Want to reset my memory of these conversations?"
    menu:
        m "Want to reset my memory of these conversations?{fast}"
        "Yes, please.":
            m 3rub "I get it.  A good amount of work went into this."
            m "You probably want to see everything there is to see."
            m 4esd "Come to think of it, didn't Sayori want you to do that same basic thing in the original game?"
            m 3hsb "And if you want to see more of {i}me{/i}, how could I say no?"
            m 1esd "Hang on a second..."
            init 5 python:
                persistent._dan_all_dreams = [1]
                persistent._dan_dreams_and_nightmares_explained = False
                persistent._dan_dreams_had = False
                persistent._dan_had_first_dream = False
                persistent._dan_had_nightmare = False
                persistent._dan_had_best_dream = False
                persistent._dan_apprehensive_start = None
                persistent._dan_asked_to_stay_dreaming = False
            m 1duc "{w=0.5}.{w=0.5}.{w=0.5}.{w=1}{nw}"
            extend 7eub "And there we go!"
        "No, that won't be necessary.":
            m 1esb "Okay."
            $ had_dream_text = "{i}have{/i} had a dream once." if persistent._dan_had_first_dream else "{i}haven't{/i} had a dream yet"
            $ had_nightmare_text = "{i}have{/i} had a nightmare once." if persistent._dan_had_nightmare else "{i}haven't{/i} had a nightmare yet"
            m 4esb "For the record, as far as I know, I [had_nightmare_text]."
            m "Also, I [had_dream_text]."
            m 7hkb "It's kinda' weird that my memories can be overridden so easily."
            m 7esb "But I'm sure it's for the sake of the experience that my modder intended."
            m 5ekbsa "As for me, I'll do whatever makes you the happiest, [player]."
    return