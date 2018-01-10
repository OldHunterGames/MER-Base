init python:
    motivations_data = {
        'desperation': {
            'name': __("Desperation"),
            'type': 'desperation',
        },
        
        'stress': {
            'name': __("Stress"),
            'type': 'stress'
        },
        
        'determination': {
            'name': __("Determination"),
            'type': 'determination'
        },
        
        'enthusiasm': {
            'name': __("Enthusiasm"),
            'type': 'enthusiasm',
        }
    }

    motivations_keys = {
        'taste': __("Taste"),
        'hunger': __("Hunger"),
        'confidence': __("Confidence"),
        'fear': __("Fear"),
        'pleasure': __("Pleasure"),
        'pain': __("Pain"),
        'adrenaline': __("Adrenaline"),
        'deprivation': __("Deprivation"),
        'satisfaction': __("Satisfaction"),
        'desire': __("Desire"),
        'attention': __("Attention"),
        'neglect': __("Neglect"),
        'rapture': __("Rapture"),
        'gloom': __("Gloom"),
        'opulence': __("Opulence"),
        'misery': __("Misery"),
        'humiliation': __("Humiliation"),
        'supremacy': __("Supremacy"),
        'achievement': __("Achievement"),
        'incompetence': __("Incompetence"),
        'valor': __("Valor"),
        'bile': __("Bile"),
        'apathy': __("Apathy"),
        'serenity': __("Serenity"),
        'rigidity': __("Rigidity"),
        'honor': __("Honor"),
        'independence': __("Independence"),
        'infidelity': __("Infidelity"),
        'kindness': __("Kindness"),
        'infirmity': __("Infirmity"),
        'tyranny': __("Tyranny"),
        'power': __("Power"),

    }

label lbl_motivation_desperation_run(motivation, person):
    $ person.angst += 1
    $ person.motivation_level -= 1
    return

label lbl_motivation_enthusiasm_run(motivation, person):
    python:
        if person.motivation_level < 0:
            person.motivation_level = 0
        elif person.angst > 0:
            person.angst = 0
        else:
            person.motivation_level += 1
    return

label lbl_motivation_stress_run(motivation, person):
    $ person.motivation_level -= 1
    return
