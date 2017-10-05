
init python:

    stances = {
        (None, None, None): __('Indifferent'),
        (None, None, 'supporter'): __('Amiable'),
        (None, None, 'hater'): __('Offensive'),
        (None, 'personal', None): __('Familiar'),
        (None, 'personal', 'supporter'): __('Friendly'),
        (None, 'personal', 'hater'): __('Hateful'),
        (None, 'formal', None): __('Cold'),
        (None, 'formal', 'supporter'): __('Polite'),
        (None, 'formal', 'hater'): __('Insidious'),
        ('dominant', None, None): __('Arrogant'),
        ('dominant', None, 'supporter'): __('Protective'),
        ('dominant', None, 'hater'): __('Oppressive'),
        ('dominant', 'personal', None): __('Intrusive'),
        ('dominant', 'personal', 'supporter'): __('Paternal'),
        ('dominant', 'personal', 'hater'): __('Baneful'),
        ('dominant', 'formal', None): __('Strict'),
        ('dominant', 'formal', 'supporter'): __('Righteous'),
        ('dominant', 'formal', 'hater'): __('Despotic'),
        ('submissive', None, None): __('Modest'),
        ('submissive', None, 'supporter'): __('Pleasing'),
        ('submissive', None, 'hater'): __('Forced'),
        ('submissive', 'personal', None): __('Dependent'),
        ('submissive', 'personal', 'supporter'): __('Pupil'),
        ('submissive', 'personal', 'hater'): __('Inferior'),
        ('submissive', 'formal', None): __('Subordinate'),
        ('submissive', 'formal', 'supporter'): __('Loyal'),
        ('submissive', 'formal', 'hater'): __('Diminished'),
    }

    relations_sides = {
        'dominant': __('Dominant'),
        'submissive': __('Submissive'),
        'formal': __('Formal'),
        'personal': __('Personal'),
        'supporter': __('Supporter'),
        'hater': __('Hater')
    }

    bonds_data = {'lover': {"name": __('lover'), 'description': __("{actor.full_name} is in love with {target.full_name}."), 'value': 1},
        'friend': {"name": __('friend'), 'description': __("{target.full_name} is {possesive} best friend."), 'value': 1},
        'supporter': {"name": __('supporter'), 'description': __("{target.full_name} betows {pronoun} a full support."), 'value': 1},
        'underling': {"name": __('underling'), 'description': __("{target.full_name} is {possesive} most promient underling."), 'value': 1},
        'humiliated': {"name": __('humiliated'), 'description': __("Hummiliated by {target.full_name}."), 'value': -1},
        'rejected': {"name": __('rejected'), 'description': __("Rejected by {target.full_name}."), 'value': -1},
        'senior': {"name": __('senior'), 'description': __("{actor.full_name} sees {target.full_name} as a senior."), 'value': 0},
        'ally': {'name': __("Ally"), 'description': __("Description"), 'value': 1},   
        'rival': {'name': __("Rival"), 'description': __("Description"), 'value': -1},
        'traitor': {'name': __("Traitor"), 'description': __("Description"), 'value': -1},
        'offender': {'name': __("Offender"), 'description': __("Description"), 'value': -1}            
    }