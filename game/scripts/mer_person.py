# -*- coding: UTF-8 -*-
from random import *
import copy
import collections

import renpy.store as store
import renpy.exports as renpy

from features import Feature, HomeWorld
from anatomy import Anatomy
from psymodel import PsyModel
from schedule import Schedule
from relations import Relations
from genus import available_genuses, Genus
from mer_item import Item

from factions import Faction
from inventory import InventoryWielder
import mer_utilities as utilities
from mer_command import *


class FeaturesGenerator(object):

    def get_body_part_features(self, slot):
        data = store.anatomy_features
        return [key for key, value in data.items() if value['slot'] == slot]

    def get_features_by_slot(self, slot, dict):
        return [key for key, value in dict.items() if value.get('slot') == slot]

    def gen_body_parts(self, person):
        gender = person.gender
        genus = person.genus.name
        if gender == 'male' or gender == 'sexless':
            sizes = {
                'micro_penis': 1,
                'small_penis': 1,
                'normal_penis': 2,
                'large_penis': 3,
                'huge_penis': 3
            }
            part = person.add_body_part('penis')
            if genus == 'lupine' or genus == 'werewolf':
                size = utilities.weighted_random(
                    sizes)
            else:
                size = choice(sizes.keys())

            part.add_feature(genus + '_penis')
            part.add_feature(size)

        else:
            sizes = {
                'micro_vagina': 1,
                'small_vagina': 1,
                'normal_vagina': 1,
                'large_vagina': 1,
                'huge_vagina': 1
            }
            part = person.add_body_part('vagina')
            size = utilities.weighted_random(sizes)
            part.add_feature(size)
            part.add_feature(choice(['wet_vagina', 'dry_vagina']))

            sizes = {'junior':
                     {
                         'micro_boobs': 10,
                         'small_boobs': 10,
                         'normal_boobs': 0,
                         'large_boobs': 0,
                         'huge_boobs': 0
                     },
                     'others':
                     {
                         'micro_boobs': 1,
                         'small_boobs': 1,
                         'normal_boobs': 1,
                         'large_boobs': 1,
                         'huge_boobs': 1
                     }

                     }
            part = person.add_body_part('boobs')
            try:
                size = utilities.weighted_random(sizes[gender])
            except KeyError:
                size = utilities.weighted_random(sizes['others'])
            part.add_feature(size)
        part = person.add_body_part('ass')
        part.add_feature(choice(self.get_body_part_features('ass_size')))
        person.add_body_part('body')
        person.add_body_part('mouth')
        part = person.add_body_part('manipulator')
        part.add_feature('human_hand')
        part = person.add_body_part('foot')
        part.add_feature('human_foot')


class CharacterCustomization(object):

    def __init__(self, person_creator=None):
        if person_creator is None:
            self._creator = PersonCreator()
        else:
            self._creator = person_creator
        self.random = None

    def start(self):
        "Starts player character customization"
        img = renpy.display.im.Image('images/bg/mist.png')
        renpy.show('mist', what=img)
        self.ask_random()
        if self.random != 'custom':
            renpy.hide('mist')
            return self
        self._creator.gender = self._pick_gender()
        self._creator.age = self._pick_ages()
        self._creator.world = self._pick_world()
        if self._creator.age != 'junior':
            self._creator.occupation = self._pick_occupation()
        else:
            self._creator.occupation = None
        self._creator.spirit_feat = self._pick_spirit_feats()
        self._creator.mind_feat = self._pick_mind_feats()
        self._creator.sexual_orientation = self._pick_orientation()
        self._creator.sexual_type = self._pick_sexual_type()
        self._creator.orderliness = self._pick_orderliness()
        self._creator.activity = self._pick_activity()
        self._creator.morality = self._pick_morality()
        renpy.hide('mist')
        return self

    def ask_random(self):
        self.random = renpy.display_menu(
            [
                ('Random male', 'male'),
                ("Random female", 'female'),
                ("Custom", 'custom')
            ]
        )

    def _pick_orientation(self):
        return renpy.display_menu(self._creator.get_orientations())

    def _pick_sexual_type(self):
        return renpy.display_menu(self._creator.get_sex_traits())

    def _pick_gender(self):
        return renpy.display_menu(
            [(store.person_features[i]['name'], i) for i in self._creator.get_genders()])

    def _pick_ages(self):
        return renpy.display_menu(
            [(store.person_features[i]['name'], i) for i in self._creator.get_ages()])

    def _pick_occupation(self):
        return renpy.display_menu(
            [(i.name, i) for i in self._creator.available_occupations()])

    def _pick_world(self):
        return renpy.display_menu(
            [(i.name, i) for i in self._creator.available_worlds()])

    def _pick_orderliness(self):
        return

    def _pick_activity(self):
        return

    def _pick_morality(self):
        return

    def make(self):
        if self.random == 'custom':
            person = self._creator.gen_person()
        else:
            person = self._creator.gen_random_person(
                genus=self.genus, gender=self.random)
        return person


class PersonCreator(object):
    _restrictions = list()

    def __init__(self, **kwargs):
        self.weights = collections.defaultdict(dict)
        self.stats = dict()
        self.add_stats(**kwargs)

    def _weighted_random(self, data):
        data = copy.copy(data)
        for i in self._restrictions:
            try:
                del data[i]
            except KeyError:
                pass
        return utilities.weighted_random(data)

    def add_weights(self, dict_id, dict_):
        # some dicts need special formating
        # see character_generator_data.rpy
        self.weights[dict_id].update(**dict_)

    @staticmethod
    def add_restriction(id):
        PersonCreator._restrictions.append(id)

    @staticmethod
    def remove_restriction(id):
        if id in PersonCreator._restrictions:
            PersonCreator._restrictions.remove(id)

    @staticmethod
    def has_restriction(id):
        return id in PersonCreator._restrictions

    def add_stats(self, **kwargs):
        self.stats.update(**kwargs)

    def available_worlds(self):
        return [HomeWorld(i) for i in store.homeworlds_dict]

    def available_occupations(self, world, person):
        occupations = dict()
        for key, value in store.occupation_features.items():
            if ('any' in value['tags'] or
                    any([i in world.tags for i in value['tags']])):
                occupations[key] = value
        age_tags = ['junior', 'adolescent', 'mature', 'elder']
        for key, value in occupations.items():
            if any([i in value['tags'] for i in age_tags]):
                age = person.feature_by_slot('age')
                age = age and age.id
                if age not in value['tags'] and age is not None:
                    del occupations[key]
        for key, value in occupations.items():
            if 'masculine' in value['tags'] or 'femenie' in value['tags']:
                if person.appearance_type() not in value['tags']:
                    del occupations[key]
        attr_tags = ['menace', 'subtlety', 'hardiness', 'refinement',
                     'competence', 'charisma', 'extravagance', 'purity']
        for key, value in occupations.items():
            for i in attr_tags:
                if i in value['tags']:
                    if getattr(person, i)() < 1:
                        del occupations[key]
                        break

        del occupations['unknown']
        return occupations.keys()

    def _get_weights(self, id):
        weights = copy.copy(getattr(store, id))
        weights.update(self.weights.get(id, dict()))
        return weights

    def get_genuses(self):
        return [Genus(i) for i in store.genuses_dict]

    def random_genus(self):
        return self._weighted_random(
            self._get_weights('genuses_frequency'))

    def random_age(self):
        return self._weighted_random(self._get_weights('ages_frequency'))

    def random_gender(self):
        return self._weighted_random(self._get_weights('sexes_frequency'))

    def random_constitution(self, age):
        if age is None:
            age = 'default'
        return self._weighted_random(
            self._get_weights('constitutions_frequency')[age])

    def random_quirk(self):
        return self._weighted_random(self._get_weights('quirks_frequency'))

    def random_appearance(self, type_):
        return self._weighted_random(
            self._get_weights('appearance_frequency')[type_])

    def random_alignment(self, person):
        alignments = [
            ('chaotic', 'lawful'), ('evil', 'good'), ('ardent', 'timid')]
        no_alignment = 0
        for i in alignments:
            dice = randint(1, 10)
            if dice <= 2:
                person.add_feature(i[0])
            elif dice >= 9:
                person.add_feature(i[1])
            else:
                no_alignment += 1
        if no_alignment == 3:
            person.add_feature('unaligned')

    def random_homeworld(self):
        return choice(self.available_worlds()).id

    def random_occupation(self, world, person):
        try:
            occupation = choice(self.available_occupations(world, person))
        except IndexError:
            occupation = 'unknown'
        return occupation

    def random_needs(self, person):
        needs = [
            ('greedy', 'generous'), ('gourmet', 'moderate_eater'),
            ('sensitive', 'enduring'), ('sybarite', 'ascetic'),
            ('energetic', 'lazy'), ('extrovert', 'introvert'),
            ('curious', 'dull'), ('leader', 'liberal'),
            ('ambitious', 'modest'), ('lewd', 'frigid')]
        for i in needs:
            dice = randint(1, 10)
            if dice <= 2:
                person.add_feature(i[0])
            elif dice >= 9:
                person.add_feature(i[1])

    def random_sexual_type(self, key):
        return utilities.weighted_random(
            self._get_weights('sexual_type_frequency')[key])

    def random_sexual_orientation(self, key):
        return utilities.weighted_random(
            self._get_weights('sexual_orientation_frequency')[key])

    def get_ages(self, genus):
        return genus.ages_names()

    def get_genders(self):
        return ['male', 'female', 'shemale']

    def get_orientations(self, gender):
        dict_ = copy.copy(store.sexual_orientation)
        if gender == 'male':
            del dict_['lesbian']
            del dict_['straight_female']
        elif gender == 'female':
            del dict_['gay']
            del dict_['straight_male']
        return [(i[1]['name'], i[0]) for i in dict_.items()]

    def get_sex_traits(self):
        dict_ = store.sexual_type
        return [(i[1]['name'], i[0]) for i in dict_.items()]

    def gen_random_person(self, **kwargs):
        "Creates fully random person if no agruments specified"
        genus = kwargs.get('genus', self.random_genus())
        genus = Genus(genus)
        if 'ageless' in genus.tags:
            age = None
        else:
            age = kwargs.get('age', self.random_age())
        if 'sexless' in genus.tags:
            gender = None
        else:
            gender = kwargs.get('gender', self.random_gender())
        p = Person(age, gender, genus)
        constitution = kwargs.get('constitution', genus.get_constitution())
        if constitution is None:
            constitution = self.random_constitution(age)
        p.add_feature(constitution)
        if gender is None:
            gender = 'default'
            appearance = 'default'
        else:
            appearance = p.appearance_type()
        p.add_feature(
            kwargs.get('quirk', genus.get_quirk(self.random_quirk())))
        p.add_feature(
            kwargs.get(
                'appearance',
                genus.get_appearance(self.random_appearance(appearance))))
        self.random_alignment(p)
        self.random_needs(p)
        for i in genus.features():
            p.add_feature(i)
        p.homeworld = HomeWorld(kwargs.get(
            'homeworld', self.random_homeworld()))
        p.add_feature(
            kwargs.get('occupation', self.random_occupation(p.homeworld, p)),
            'occupation_features')
        try:
            p.culture = choice(p.feature_by_slot('occupation').cultures)
        except IndexError:
            p.culture = None
        genus.on_apply(p)
        self.gen_name(p, p.culture, p.gender)
        self.gen_avatar(p)
        random_sex_type = self.random_sexual_type(gender)
        random_sex_orientation = self.random_sexual_orientation(appearance)
        p.set_sexual_type(kwargs.get(
            'sexual_type', random_sex_type))
        p.set_sexual_orientation(kwargs.get('sexual_orientation',
                                            random_sex_orientation))
        self.equip_person(p)
        self.get_nickname(p)
        return p

    def equip_person(self, person):
        for key, value in person.feature_by_slot('occupation').equipment.items():
            if value is not None:
                person.equip_on_slot(key, Item(value))

    def gen_person(self):
        "Creates person with predefined parameters"
        person = self.gen_random_person(**self.stats)
        return person

    def gen_name(self, person, culture_id, gender):
        if gender == 'transfemale':
            gender = 'male'
        elif gender in ('shemale', 'transmale'):
            gender = 'female'
        elif gender == 'sexless':
            gender = choice('male', 'female')
        try:
            names = store.firstname[culture_id][gender]
        except KeyError:
            names = store.firstname['default'][gender]
        person.firstname = choice(names)

    def _get_avatars(self, path):
        all_ = renpy.list_files()
        avas = [str_ for str_ in all_ if str_.startswith(path)]
        return avas

    def gen_avatar(self, person):
        start_path = 'images/avatar/'
        start_path += person.genus.get_face_type()
        if person.get_culture() is not None:
            start_path = self._check_avatar(
                start_path, person.get_culture())
        start_path = self._check_avatar(start_path, person.appearance_type())
        start_path = self._check_avatar(start_path, person.age)
        try:
            avatar = choice(self._get_avatars(start_path))
        except IndexError:
            avatar = utilities.default_avatar()
        person.set_avatar(avatar)

    def _check_avatar(self, start_path, attr):
        if attr is not None:
            if renpy.exists(start_path + '/%s' % attr):
                start_path += '/%s' % attr
        return start_path

    def get_nickname(self, person):
        list_ = list()
        for i in person.get_features():
            list_.extend(i.get_nicknames())
        try:
            person.set_nickname(choice(list_))
        except IndexError:
            pass


persons_list = []


class SlaveStorage(object):

    def __init__(self):
        self._max_slaves = 1
        self._slaves = []

    def slaves(self):
        return [i for i in self._slaves]

    def add_slave(self, slave, master):
        if self.has_space():
            self._slaves.append(slave)
            self._slave_relations(slave, master)
            return True
        else:
            self._slaves.pop()
            self._slaves.append(slave)
            return True
        return False

    def remove_slave(self, slave):
        self._slaves.remove(slave)
        slave.set_master(None)

    def set_max_slaves(self, value):
        self._max_slaves = value

    def has_space(self):
        return len(self._slaves) < self._max_slaves

    def _slave_relations(self, slave, master):
        # master.relations(slave).change_type('slave')
        slave.set_master(master)


class DescriptionMaker(object):
    """Class for complex person description generation"""
    # TODO: Refactor this as abstract and allocate realizations by game lang?

    def __init__(self, person):
        self.person = person

    def description(self):
        person = self.person
        pronoun = self.get_pronoun1()
        pronoun2 = self.get_pronoun2()
        possesive = self.get_possesive()
        cap_possesive = possesive.capitalize()
        cap_pronoun = pronoun.capitalize()
        cap_pronoun2 = pronoun2.capitalize()
        sex_type = person.sexual_type['name']
        sex_orientation = person.sexual_orientation['name']
        name = person.name
        nickname = person.nickname
        age = person.feature_by_slot('age')
        if age is None:
            age = ''
        else:
            age = age.description()
        gender = person.feature_by_slot('gender')
        if gender is None:
            gender = ''
        else:
            gender = gender.description()
        genus = person.genus.description()
        homeworld = person.homeworld.description()
        occupation = person.feature_by_slot('occupation').description()
        start_text = "{name} {nickname} is a {age} {genus} {gender}. "
        start_text += homeworld
        start_text += person.feature_by_slot('occupation').description()
        start_text += '. '
        start_text = self.alignment_text(start_text)
        start_text += ' and sexually {pronoun} is {sex_type} {sex_orientation}.'
        # start_text += self.relations_text()
        start_text += '\n'
        start_text = self.features_text(start_text)
        start_text += '\n'
        start_text = self.needs_text(start_text)
        start_text = start_text.format(**locals())
        return start_text

    def features_text(self, text):
        text += self.person.name
        for i in ('constitution', 'shape', 'appearance', 'quirk'):
            feature = self.person.feature_by_slot(i).description()
            if feature is not None:
                text += ' '
                text += self.person.feature_by_slot(i).description()
                if i == 'shape' or i == 'appearance':
                    text += '.'
        return text

    def alignment_text(self, text):
        text += '{cap_possesive} alignment is '
        for i in ("orderliness", "activity", "morality"):
            feature = self.person.feature_by_slot(i)
            if feature is not None:
                text += ' %s' % feature.name()
        if self.person.feature('unaligned') is not None:
            text += ' %s' % self.person.feature('unaligned').name()
        return text

    def needs_text(self, text):
        for i in self.person.needs.values():
            feature = self.person.feature_by_slot(i.name + '_feat')
            if feature is not None:
                text += feature.description()
        return text

    def get_pronoun1(self):
        if self.person.gender == 'male' or self.person.gender == 'sexless':
            return 'he'
        else:
            return 'she'

    def get_pronoun2(self):
        if self.person.gender == 'male' or self.person.gender == 'sexless':
            return 'him'
        else:
            return 'her'

    def get_possesive(self):
        return {'he': 'his', 'she': 'her'}[self.get_pronoun1()]

    def make_weapon_text(self):
        weapons = self.person.weapons()
        if len(weapons) > 1:
            weapon_txt = '{person.name} armed with {person.main_hand.name} and {person.other_hand.name}'.format(
                person=self.person)
        elif len(weapons) == 1:
            weapon_txt = '{person.name} armed with {weapons[0].name}'.format(
                weapons=weapons, person=self.person)
        else:
            weapon_txt = ''
        if self.person.armor is not None:
            weapon_txt += '. {cap_pronoun} wears a {person.armor.name}'
        return weapon_txt

    def relations_text(self, colorize=True, protected=True):
        if not self.person.know_player():
            return ''
        relations = self.person.player_relations()
        stance_type = relations.colored_stance(protected)

        return '{stance_type} ({relations[0]}, {relations[1]}, {relations[2]}) towards you. '.format(
            stance_type=stance_type, relations=relations.description(colorize, protected))


class FoodSystem(object):

    _features = {
        2: 'obese',
        1: {0: 'chubby', 1: 'beefy', -1: 'flabby'},
        0: {0: 'undistinguished', 1: 'muscular', -1: 'skinyfar'},
        -1: {0: 'slim', 1: 'wiry', -1: 'frail'},
        -2: 'emaciated'
    }

    def __init__(self, owner, fatness=0, fitness=0):
        self.owner = owner
        self.satiety = 0
        self._fatness = fatness
        self._fitness = fitness
        self._tonus = 0
        self.amount = 0
        self._set_shape()

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, value):
        self._fitness = value
        self._set_shape()

    @property
    def tonus(self):
        return self._tonus

    @tonus.setter
    def tonus(self, value):
        self._tonus = value

    @property
    def fatness(self):
        return self._fatness

    @fatness.setter
    def fatness(self, value):
        self._fatness = value
        self._set_shape()

    def _set_shape(self):
        data = self._features[self._fatness]
        if not isinstance(data, str):
            data = data[self._fitness]
        self.owner.add_feature(data)

    def rest(self):
        pass

    def set_shape(self, id):
        for key, value in self._features.items():
            if value == id:
                self._fatness = key
                self._fitness = 0
                self._set_shape()
                return
            else:
                try:
                    for k, v in value.items():
                        if v == id:
                            self._fatness = key
                            self._fitness = k
                            self._set_shape()
                            return
                except AttributeError:
                    pass


class Person(InventoryWielder, PsyModel):
    game_ref = None

    @utilities.Observable
    def __init__(self, age=None, gender=None, genus='human', shape=None):
        super(Person, self).__init__()
        self.kink = 'default'
        self.anatomy = Anatomy()

        self.player_controlled = False
        self.init_inventorywielder()
        self.init_psymodel()
        self._event_type = 'person'
        self._firstname = u"Anonimous"
        self._surname = u""
        self._nickname = u""

        # gets Feature() objects and their child's. Add new Feature only with
        # self.add_feature()
        self._features = []
        self.blocked_slots = []
        self.tokens = []  # Special resources to activate various events
        self.relations_tendency = {'convention': 0,
                                   'conquest': 0, 'contribution': 0}
        # obedience, dependecy and respect stats
        self.avatar = utilities.default_avatar()

        self._master = None  # If this person is a slave, the master will be set
        self.supervisor = None
        self.overseer = None
        self.slaves = SlaveStorage()
        self.subordinates = []
        self.ap = 1
        self.schedule = Schedule()
        # init starting features

        self.allowance = 0         # Sparks spend each turn on a lifestyle
        self.sparks = 0
        self.discipline = 0

        self.money = 0
        self._determination = 0
        self._anxiety = 0
        self.rewards = []
        self.sex_standart = 0

        # Other persons known and relations with them, value[1] = [needed
        # points, current points]
        self._relations = []
        self.conditions = []
        if isinstance(genus, Genus):
            self.genus = genus
        else:
            self.genus = Genus(genus)
        self.add_feature(age)
        self.add_feature(gender)
        self.set_avatar()
        self._buffs = []
        self.resources_storage = None
        self.deck = None
        self._calculatable = False
        self.faction = None
        self.food_system = FoodSystem(self)
        if shape is not None:
            self.food_system.set_shape(shape)
        self._known_factions = []
        self.card_storage = None
        self.decks = []
        self.communications_done = []

        self._renpy_character = store.Character(self.firstname)

        self.pocket_money = 0
        self._job = None
        self.job_buffer = None
        self.productivity_raised = False
        self.token = 'power'
        self._spoil_number = 1

        self.quests_to_give = []
        self._phrases = dict()
        self.obligation = False
        # self.rewards = CardsMaker(store.edge_quest_rewards)
        self._interactions = CardsMaker()
        self._active_quest = None
        self._sexual_orientation = None
        self._sexual_type = None

    def change_genus(self, genus):
        self.genus.on_remove(self)
        self.genus = genus
        self.genus.on_apply(self)

    def set_shape(self, id):
        self.food_system.set_shape(id)

    def appearance_type(self):
        return store.gender_correspondence.get(self.gender)

    def orderliness(self):
        return self.feature_by_slot('orderliness')

    def activity(self):
        return self.feature_by_slot('activity')

    def morality(self):
        return self.feature_by_slot('morality')

    @property
    def sexual_orientation(self):
        return self._sexual_orientation

    @property
    def sexual_type(self):
        return self._sexual_type

    def set_sexual_orientation(self, id):
        self._sexual_orientation = store.sexual_orientation[id]

    def set_sexual_type(self, id):
        self._sexual_type = store.sexual_type[id]

    def get_interactions(self):
        self._interactions.set_context(owner=self)
        return self._interactions.run()

    def add_interaction(self, key, value):
        self._interactions.add_entry(key, value)

    def remove_interaction(self, key):
        self._interactions.remove_entry(key)

    # def add_reward(self, reward):
    #     self.rewards.append(reward)

    # def remove_reward(self, reward):
    #     try:
    #         self.rewards.remove(reward)
    #     except ValueError:
    #         pass

    @property
    def master(self):
        return self._master

    def set_active_quest(self, quest):
        self._active_quest = quest

    @property
    def active_quest(self):
        return self._active_quest

    def quest_completed(self, player):
        if self._active_quest is None:
            return False
        else:
            return self._active_quest.completed(player)

    def get_phrase(self, id_, default_value="No phrase"):
        phrase = self._phrases.get(
            id_, store.basic_dialogues.get(
                id_, default_value))
        return phrase

    def set_nickname(self, string):
        self.nickname = string
        self._renpy_character.name = self.name

    def set_phrases(self, dict_):
        self._phrases = dict_

    def has_available_quests(self, player):
        if self._active_quest is not None:
            return False
        return any(self.available_quests())

    def available_quests(self):
        return [i for i in self.quests_to_give if not i.active]

    def clear_quests(self):
        self.quests_to_give = []

    def get_body_part(self, name):
        return self.anatomy.get_part(name)

    def add_body_part(self, name):
        return self.anatomy.add_part(name)

    def has_body_part(self, name):
        if name is None:
            return True
        return self.get_body_part(name) is not None

    def add_quest(self, quest):
        quest.employer = self
        self.quests_to_give.append(quest)

    def remove_quest(self, quest):
        self.quests_to_give.remove(quest)

    def set_pocket_money(self, level):
        self.pocket_money = level

    @property
    def tonus(self):
        return self.food_system.tonus

    @tonus.setter
    def tonus(self, value):
        self.food_system.tonus = value

    def emotional_stability(self):
        return 3 + self.count_modifiers('emotional_stability')

    def armor_heavier_than(self, person):
        return self.count_modifiers('armor_weight') > person.count_modifiers('armor_weight')

    def check_privilege(self, victim):
        privilege = self.menace() - victim.menace()
        if privilege > 2:
            return True

        return False

    def owned_faction(self):
        if self.faction is not None:
            if self.faction.owner == self:
                return self.faction
        return None

    def count_modifiers(self, attribute):
        value = self.inventory.count_modifiers(attribute)
        for i in self.get_features():
            value += i.count_modifiers(attribute)
        value += self._count_conditions(attribute)
        value += self.genus.count_modifiers(attribute)
        return value

    def _count_conditions(self, attribute):
        return sum([i.count_modifiers(attribute) for i in self.conditions])

    def modifiers_separate(self, attribute):
        list_ = super(Person, self).modifiers_separate(attribute)
        list_.extend(self.inventory.get_modifier_separate(attribute))
        return list_

    def ration_status(self):
        return self.food_system.ration_status()

    def get_combat_style(self):
        # TODO: add beast combat style
        skill_level = self.skill('combat').level
        style = 'noncombatant'
        weapons = self.weapons()
        if len(weapons) > 0:
            if skill_level > 2:
                if any([i.type == 'twohand' for i in weapons]):
                    style = 'juggernaut'
                elif self.has_shield():
                    style = 'shieldbearer'
                else:
                    style = 'breter'
            elif skill_level > 1:
                style = 'rookie'
            else:
                style = 'desperado'
        else:
            if skill_level > 1:
                style = 'wrestler'
        return style

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, name):
        self._firstname = name
        self._set_renpy_char_name()

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        self._nickname = value
        self._set_renpy_char_name()

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    def _set_renpy_char_name(self):
        self._renpy_character.name = self.name + ' ' + self.nickname

    def __call__(self, what, interact=True):
        self.game_ref.sayer = self
        self._renpy_character(what, interact=interact)

    def say_phrase(self, phrase_id, default_value='No phrase'):
        phrase = self.get_phrase(phrase_id, default_value)
        self(phrase)

    def predict(self, what):
        self._renpy_character.predict(what)

    def apply_background(self, background):
        self.background = background
        background.apply(self)

    def set_faction(self, faction):
        if self.faction is not None:
            self.faction.remove_member(self)
        self.faction = faction

    def has_faction(self):
        return self.faction is not None

    def remove_faction(self, faction):
        if self.faction is not None:
            self.faction.remove_member(self)
        self.faction = None

    def eat(self, amount, quality):
        self.food_system.set_food(amount, quality)

    def food_info(self):
        return self.food_system.food_info()

    @property
    def calculatable(self):
        return self.player_controlled
        mastered_by_player = False
        master_of_player = False
        supervisor_of_player = False
        try:
            mastered_by_player = self.master.player_controlled
        except AttributeError:
            pass
        master_of_player = any([i for i in self.slaves if i.player_controlled])

        return (self._calculatable or self.player_controlled or
                mastered_by_player or master_of_player)

    @calculatable.setter
    def calculatable(self, value):
        self._calculatable = value

    def set_deck(self, deck):
        self.deck = deck

    def set_resources_storage(self, storage):
        self.resources_storage = storage

    def set_avatar(self, avatar=None):
        if avatar is not None:
            if avatar in renpy.list_files():
                self.avatar = avatar
            else:
                self.avatar = utilities.default_avatar()
            return

    def change_genus(self, genus):
        self.genus.remove(self)
        self.genus = Genus(genus)
        self.genus.apply(self)

    @property
    def known_characters(self):
        list_ = []
        for r in self._relations:
            persons = [p for p in r.persons if p != self]
            list_ += persons
        return list_

    def get_buff_storage(self):
        return self._buffs

    def add_buff(self, id_, time=1):
        Buff(self, id_, time)

    def remove_buff(self, id_):
        for buff in self._buffs:
            if buff.id == id_:
                buff.remove()

    def remove_buff_by_slot(self, slot):
        for buff in self._buffs:
            if buff.slot == slot:
                buff.remove()

    def has_buff(self, id_):
        for buff in self._buffs:
            if buff.id == id_:
                return True
        return False

    def tick_buffs_time(self):
        for buff in [i for i in self._buffs]:
            buff.tick_time()

    def get_buffs(self):
        return [i for i in self._buffs]

    def job_name(self):
        if self._job.name is None:
            return 'idle'
        else:
            return self._job.name

    def job_description(self):
        return self.job.full_description()

    @property
    def determination(self):
        return self._determination

    @determination.setter
    def determination(self, value):
        self._determination = value
        if self._determination < 0:
            self._determination = 0

    @property
    def anxiety(self):
        return self._anxiety

    @anxiety.setter
    def anxiety(self, value):
        self._anxiety = value
        if self._anxiety < 0:
            self_anxiety = 0

    # person gender relies on feature with slot 'gender'
    @property
    def gender(self):
        try:
            gender = self.feature_by_slot('gender').id
            return gender
        except AttributeError:
            return 'sexless'

    # person gender relies on feature with slot 'age'
    @property
    def age(self):
        try:
            gender = self.feature_by_slot('age').id
            return gender
        except AttributeError:
            return 'ageless'

    def get_culture(self):
        return self.culture

    @property
    def name(self):
        s = self.firstname
        return s

    def tick_features(self):
        for feature in self.features:
            feature.tick_time()

    # adds features to person, if mutually exclusive removes old feature
    def add_feature(self, id_, source='person_features'):
        if self.has_feature(id_):
            return
        try:
            feature = Feature(id_, source)
        except KeyError:
            pass
        else:
            if feature.slot is not None:
                self.remove_feature_by_slot(feature.slot)
            self._features.append(feature)

    def feature_by_slot(self, slot):  # finds feature which hold needed slot
        if slot in self.blocked_slots:
            return None
        for f in self._features:
            if f.slot == slot:
                return f
        return None

    def feature(self, id_):  # finds feature with needed name if exist
        for f in self._features:
            if f.id == id_ and f.slot not in self.blocked_slots:
                return f
        return None

    def has_feature(self, id_):
        return self.feature(id_) is not None

    def remove_feature(self, feature):
        if isinstance(feature, str):
            for i in self.features:
                if i.id == feature:
                    self._features.remove(i)
        else:
            try:
                self._features.remove(feature)
            except ValueError:
                return

    def remove_feature_by_slot(self, slot):
        for f in self._features:
            if f.slot == slot:
                self._features.remove(f)
                return

    def get_features(self):
        return [i for i in self._features if i.slot not in self.blocked_slots]

    def block_slot(self, slot):
        self.blocked_slots.append(slot)

    def unlock_slot(self, slot):
        self.blocked_slots.remove(slot)

    def full_name(self):
        return self.firstname + ' "' + self.nickname + '" ' + self.surname

    def description(self):
        txt = self.firstname + ' "' + self.nickname + '" ' + self.surname
        txt += '\n'
        for feature in self.features:
            txt += feature.name
            txt += ','
        return txt

    def overseer_relations(self):
        if self.overseer is not None:
            return self.relations(self.overseer)

    @utilities.Observable
    def rest(self):
        self._favor.tick_time()
        self.favor_income()

        if not self.calculatable:
            return

        # if self.energy < 0:
        #    self.add_buff('exhausted')
        self.food_system.fatness_change()
        self.remove_money(self.decade_bill())

        if self.pocket_money > 0:
            self.satisfy_need('prosperity', self.pocket_money)

        self.ap = 1
        self._stimul = 0
        self.success = 0
        self.purporse = 0
        self.productivity_raised = False
        for key, value in self.tokens_relations.items():
            skill = self.skill(key)
            if skill > 0:
                self.add_chance(skill, value, attributed=key)

    @utilities.Observable
    def tick_time(self):
        if not self.calculatable:
            return
        self.tick_conditions()
        self.tick_buffs_time()
        self.tick_features()
        self.reset_psych()

    @utilities.Observable
    def tick_schedule(self):
        self.bad_markers = []
        self.good_markers = []
        self.decay_corpses()
        if not self.calculatable:
            return
        self.schedule.use(self)

    def know_person(self, person):
        if person in self.known_characters:
            return True
        return False

    def know_player(self):
        if self.player_controlled:
            return False
        for i in self._relations:
            if i.is_player_relations():
                return True
        return False

    def forget_person(self, person):
        to_remove = []
        for i in self._relations:
            if person in i.persons:
                to_remove.append(i)
        for i in to_remove:
            self._relations.remove(i)
            person._relations.remove(i)
        for i in to_remove:
            i.persons = []

    def know_faction(self, faction):
        if faction in self.known_factions():
            return True
        return False

    def known_factions(self, type=None):
        if type is None:
            return self._known_factions
        else:
            return [i for i in self._known_factions if i.type == type]

    def _set_relations(self, person):
        relations = Relations(self, person)
        person._relations.append(relations)
        self._relations.append(relations)
        return relations

    def discover_faction(self, faction):
        if not self.know_faction(faction):
            self._known_factions.append(faction)

    def relations(self, person):
        if person == self:
            raise Exception("relations: target and caller is same person")
        if isinstance(person, Faction):
            self.discover_faction(person)
            if self.know_person(person.owner):
                return self.relations(person.owner)
            else:
                return
        elif isinstance(person, Person):
            if person.faction is not None:
                self.discover_faction(person.faction)
        else:
            raise Exception("relations called with not valid arg: %s" % person)
        if not self.know_person(person):
            relations = self._set_relations(person)
            return relations
        for rel in self._relations:
            if self in rel.persons and person in rel.persons:
                return rel

    def use_token(self):
        if self.token == 'power':
            return
        if self.token != 'antagonism':
            self.player_relations().stability += 1
            self.relations_tendency[self.token] += 1
        self.token = 'power'

    def set_token(self, token, free=False):
        # if we get 2 antagonism in a row, we loose 1 stance point
        # if we get any token, when antagonism is here, we get power instead
        if self.token == 'antagonism':
            if token == 'antagonism':
                self.player_relations().stance -= 1
            else:
                self.token = 'power'
                return
        self.token = token
        renpy.call_in_new_context('lbl_notify', self, token)

    def get_token_image(self):
        return {'power': 'images/tarot/arcana_lust.jpg',
                'conquest': 'images/tarot/arcana_charriot.jpg',
                'convention': 'images/tarot/arcana_justice.jpg',
                'contribution': 'images/tarot/arcana_lovers.jpg',
                'antagonism': 'images/tarot/arcana_moon.jpg'}[self.token]

    def player_relations(self):
        return self.relations(self.game_ref.player)

    def enslave(self, target):
        success = self.slaves.add_slave(target, self)
        if success:
            self.relations(target)

    def remove_slave(self, slave=None):
        slave = self.slaves.slaves()[0]
        self.slaves.remove_slave(slave)
        return slave

    def get_slaves(self):
        return self.slaves.slaves()

    def has_slaves(self):
        return len(self.get_slaves()) > 0

    def set_master(self, master):
        self._master = master

    def set_supervisor(self, supervisor):
        self.supervisor = supervisor

    def desirable_relations(self):
        d = {'lawful': ('formal', 'loyality'), 'chaotic': ('intimate', 'scum-slave'),
             'timid': ('delicate', 'worship'), 'ardent': ('intense', 'disciple'),
             'good': ('supporter', 'dedication'), 'evil': ('contradictor', 'henchman')}
        return [d.get(x) for x in list_]

    def willing_available(self):
        return []

    # favor methods
    def gain_favor(self, value):
        if self.player_controlled:
            return
        if self.game_ref.player not in self.known_characters:
            return
        value = self.favor + value
        if value < 0:
            self.favor = 0
            return
        hard_max = 5
        soft_max = 3 + self.player_stance().value
        favor = min(hard_max, min(soft_max, value))
        self._favor.income(favor)

    @property
    def favor(self):
        return self._favor.value

    def spend_favor(self, value):
        self._favor.spend(-value)

    def add_favor_consumption(self, name, value, slot, time=1, description=""):
        self._favor.add_consumption(self, name, value, slot, time, description)

    def remove_favor_consumption(self, slot):
        self._favor.remove_consumption(self, slot)

    def get_favor_consumption(self):
        return self._favor.consumption_level()

    def calculate_favor(self, value):
        return self._favor.calculate_consumption(value)

    def favor_income(self):
        pass
    # end of favor methods

    def can_tick(self):
        if not self.calculatable:
            return True
        return self._favor.can_tick() and self.has_money(self.decade_bill())

    def decade_bill(self):
        value = self.schedule.get_cost()
        return value

    # methods for conditions, person.conditions list cleared after person.rest
    def add_condition(self, condition):
        if not self.has_condition(condition):
            self.conditions.append(condition)
            condition.on_add(self)

    def remove_condition(self, condition):
        try:
            self.conditions.remove(condition)
            condition.on_remove(self)
        except ValueError:
            pass

    def tick_conditions(self):
        for i in self._conditions:
            i.tick_time()
        self._conditions = filter(
            lambda condition: not condition.ended(),
            self._conditions)

    @utilities.Observable
    def die(self, destroy=False):
        self.remove_relations()
        if destroy:
            self.destroy()
        if self.player_controlled:
            renpy.call('lbl_gameover')
        self.add_feature('dead')

    def destroy(self):
        self.remove_relations()
        self._remove_features()
        self._remove_foodsystem()
        self.remove_genus()
        persons_list.remove(self)

    def remove_genus(self):
        self.genus.remove()

    def _remove_foodsystem(self):
        self.food_system.owner = None

    def _remove_features(self):
        self.features = []

    def remove_relations(self):
        characters = [i for i in self.known_characters]
        for i in characters:
            self.forget_person(i)

    def is_dead(self):
        if self.feature('dead') is not None:
            return True
        return False

    # rating methods
    def allure(self):
        value = self.count_modifiers('allure')
        return max(0, min(value, 5))

    def hardiness(self):
        value = self.count_modifiers('hardiness')
        return max(0, min(value, 5))

    def succulence(self):
        value = 3 + self.count_modifiers('succulence')
        return max(0, min(value, 5))

    def purity(self):
        value = self.count_modifiers('purity')
        return max(0, min(value, 5))

    def menace(self):
        value = self.count_modifiers('menace')
        return max(0, min(value, 5))

    def subtlety(self):
        item = self.get_slot('load').get_item()
        if item is not None:
            if 'accessory' not in item.tags:
                return 0
        value = self.count_modifiers('subtlety')
        return max(0, min(value, 5))

    def refinement(self):
        item = self.get_slot('load').get_item()
        if item is not None:
            if 'accessory' not in item.tags:
                return 0
        value = self.count_modifiers('refinement')
        return max(0, min(value, 5))

    def competence(self):
        value = self.count_modifiers('competence')
        return max(0, min(value, 5))

    def charisma(self):
        value = self.count_modifiers('charisma')
        return max(0, min(value, 5))

    def extravagance(self):
        value = self.count_modifiers('extravagance')
        return max(0, min(value, 5))

    def show_stats(self):
        stats = (
            'allure', 'hardiness', 'succulence', 'purity',
            'menace', 'subtlety', 'refinement', 'competence', 'charisma',
            'extravagance')
        return dict(
            [(store.person_stats.get(i, i), getattr(self, i)()) for i in stats
             if getattr(self, i)() > 0])

    def get_price(self):
        # pricing formula for untrained slaves
        pricing = store.slave_pricing
        modifiers = store.slave_price_modifiers
        basic = max([self.allure(), self.hardiness(), self.succulence()])
        modifier = max([self.purity(), self.exotic()])
        price = pricing[basic]
        price *= modifiers[modifier]
        return int(price)

    def modify_check(self, value):
        for i in self.conditions:
            new_value = i.modify_check(value)
            value = new_value[0]
            if new_value[1]:
                break
        return value
    # end of rating methods

    def focus(self):
        return self.schedule.job.focus

    def job_skill(self):
        return self.schedule.job.skill

    @property
    def job(self):
        return self.schedule.job

    @property
    def accommodation(self):
        return self.schedule.accommodation

    @property
    def ration(self):
        return self.schedule.ration

    @property
    def job_difficulty(self):
        if self.schedule.job.difficulty is not None:
            return self.schedule.job.difficulty
        else:
            return 0

    def increase_productivity(self):
        if self.productivity_raised:
            return
        self.schedule.remove_buffer()
        self.schedule.job.focus += 1
        self.productivity_raised = True

    def reset_productivity(self):
        self.schedule.job.focus = 0

    def job_productivity(self):
        return self.schedule.job.focus

    def world(self):
        # not sure we need core reference here
        return self.game_ref.current_world
