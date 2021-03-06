init 5 python:
    if persistent._DaN_should_create_events:
        addEvent(
            Event(
                persistent.event_database,
                eventlabel="reset_dreams_and_nightmares",
                category=['Dreams and Nightmares'],
                prompt="Reset",
                random=True
                )
            )
    else:
        if "reset_dreams_and_nightmares" in persistent.event_database:
            persistent.event_database.pop("reset_dreams_and_nightmares")

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
            m 1duc "{w=0.5}.{w=0.5}.{w=0.5}.{w=1}{nw}"
            extend 7eub "And there we go!"
            $ persistent._mas_all_dreams = [1]
            $ persistent._mas_dreams_and_nightmares_explained = False
            $ persistent._mas_had_first_dream = False
            $ persistent._mas_had_nightmare = False
            $ persistent._mas_had_best_dream = False
            $ persistent._mas_apprehensive_start = None
            $ persistent._mas_asked_to_stay_dreaming = False
        "No, that won't be necessary.":
            m 1esb "Okay."
            $ had_dream_text = "{i}have{/i} had a dream once." if persistent._mas_had_first_dream else "{i}haven't{/i} had a dream yet"
            $ had_nightmare_text = "{i}have{/i} had a nightmare once." if persistent._mas_had_nightmare else "{i}haven't{/i} had a nightmare yet"
            m 4esb "For the record, as far as I know, I [had_nightmare_text]."
            m "Also, I [had_dream_text]."
            m 7hkb "It's kinda' weird that my memories can be overridden so easily."
            m 7esb "But I'm sure it's for the sake of the experience that my modder intended."
            m 5ekbsa "As for me, I'll do whatever makes you the happiest, [player]."
    return