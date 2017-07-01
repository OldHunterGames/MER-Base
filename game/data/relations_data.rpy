
init python:

    stances = {
        (None, None, None): __('indifferent'),
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

    bonds_data = {'lover': {"name": __('lover'), 'description': __("description"), 'value': 1},
        'friend': {"name": __('friend'), 'description': __("description"), 'value': 1},
        'supporter': {"name": __('supporter'), 'description': __("description"), 'value': 1},
        'underling': {"name": __('underling'), 'description': __("description"), 'value': 1},
        'humiliated': {"name": __('humiliated'), 'description': __("description"), 'value': -1},
        'rejected': {"name": __('rejected'), 'description': __("description"), 'value': -1},
        'senior': {"name": __('senior'), 'description': __("description"), 'value': 0},               
    }