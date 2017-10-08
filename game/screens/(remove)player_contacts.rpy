init python:
    def withou_faction(player):
        return [i for i in player.known_characters if not i.has_faction()]

    class CardPerson(Card, Command):

        def __init__(self, person, player):
            self.person = person
            self.player = player

        def image(self):
            return self.person.avatar

        def name(self):
            return self.person.name

        def description(self):
            # person = self.person
            # line0 = person.name
            # line1 = '{person.age} {person.gender} {person.genus.name}'.format(person=person)
            # line2 = '{0} {1} {2}'.format(*person.alignment.description())
            # sexual_suite = person.sexual_suite['name']
            # orientation = person.sexual_orientation['name']
            # line3 = '{0} {1}'.format(sexual_suite, orientation)
            # line4 = DescriptionMaker(person).relations_text(protected=False)
            # final_text = line0 + '\n' + line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
            # return final_text
            return 'No description'
        
        def run(self):
            renpy.call_in_new_context('_contacts_glue',
                self.person, True, True, self.player)

    class CardNewContact(Card, Command):
        def __init__(self, player, core):
            self.player = player
            self.core = core

        def image(self):
            return 'images/tarot/arcana_world.jpg'

        def name(self):
            return 'New meeting'

        def description(self):
            return 'No description'

        def run(self):
            person = core.get_phantom()
            if person is None:
                person = self.core.person_creator.gen_random_person()
            self.core.faction.add_member(person)
            self.player.relations(person)


    class CardSkipTurn(Card, Command):

        def __init__(self, core):
            self.core = core

        def image(self):
            return 'images/tarot/arcana_moon.jpg'

        def name(self):
            return 'Skip Turn'

        def description(self):
            return 'No description'

        def run(self):
            self.core.skip_turn()

label lbl_contacts(player):
    $ char_cards = [CardPerson(person, player) for person in player.known_characters()]
    $ char_cards.append(CardNewContact(player, core))
    $ char_cards.append(CardSkipTurn(core))
    $ CardMenu(char_cards).show(True, 150, 150, 10)
    call lbl_contacts(player)
    return

label _contacts_glue(person, _return=True, communicate=True, relations=None):
    call screen sc_cis(person, relations=relations)
    return