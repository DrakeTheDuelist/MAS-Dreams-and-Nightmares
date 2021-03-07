# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="DrakeTheDuelist",
        name="MAS-Dreams-and-Nightmares",
        description="Monika will have a random dream, and you can discuss it with her when she wakes up... or comfort her if she had a nightmare.",
        version="1.0.3",
        settings_pane="settings_screen_for_your_submod"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Dreams and Nightmares",
            user_name="DrakeTheDuelist",
            repository_name="MAS-Dreams-and-Nightmares"
        )