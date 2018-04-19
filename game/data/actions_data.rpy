init python:
    actions_data = {
        'gamble':{
            'name': __("Gamble"),
            'description': __("Gamble"),
            'lbl': 'lbl_actions_gamble'
        },
        'bazar':{
            'name': __("Bazar"),
            'description': __("Go for some trades"),
            'lbl': 'lbl_actions_bazar'
        },
        'slave_market':{
            'name': __("Slave market"),
            'description': __("Here you can buy or sell some slaves"),
            'lbl': 'lbl_actions_slave_market'
        }
    }


label _gamble_fair(person):
    python:
        result = Skillcheck(person, 'subtlety', 3).run()
        if result:
            person.money += 20
        else:
            person.money -= 20
    if result:
        '[person.name] wins 20 sparks'
    else:
        '[person.name] lost 20 sparks'
    return
label lbl_actions_gamble(action):
    python:
        person = action.person
        motivation = UseMotivation(person)
        result = motivation.run()
        if result:
            motivation_type = motivation.used_motivation_type
            if motivation_type == 'enthusiasm':
                mode = 'cheat'
            else:
                mode = 'fair'
        else:
            mode = None
    if mode == 'fair':
        call _gamble_fair(person)
    elif mode == 'cheat':
        menu:
            'fair':
                call _gamble_fair(person)
            'cheat':
                $ person.money += 100
                '[person.name] gets 100 sparks'
    else:
        '[person.name] has no motivation'
    return

init python:
    class BazarBuy(object):
        type = 'buy'
        def __init__(self, item, price):
            self.item = item
            self.price = price
        
    class BazarSell(BazarBuy):
        type = 'sell'

label lbl_actions_bazar(action):
    python:
        person = action.person
        worlds = World.get_worlds()
        choices = [('Gem(%s) - 10 sparks'%i.type, BazarBuy(i, 10)) for i in worlds if person.has_money(10)]
        if len(person.items_with_id('gold_unit')) > 0:
            unit = person.items_with_id('gold_unit')[0]
            choices.append(('Sell gold unit - %s' % unit.price, BazarSell(unit, unit.price)))
        choices.append((__("Leave"), 'leave'))
        choices.append((__("Sparks left: %s" % person.money), None))
        choice = renpy.display_menu(choices)
        if choice == 'leave':
            pass
        elif choice.item in worlds:
            person.money -= choice.price
            print(choice)
            gem = NavigationGem(choice.item(core))
            person.add_item(gem)
        elif choice.type == 'sell':
            person.remove_item(choice.item)
            person.money += choice.price
        else:
            person.money -= choice.price
            person.add_item(choice)
    if choice != 'leave':
        call lbl_actions_bazar(action)
    return

init python:
    class ActionsSlaveMarket(object):

        def __init__(self, core):
            self.slaves = [core.person_creator.gen_random_person(gender='female') for i in range(5)]
            core.skip_turn.add_callback(self.reset_slaves)

        def reset_slaves(self, core, *args, **kwargs):
            self.slaves = [core.person_creator.gen_random_person(gender='female') for i in range(5)]

        def buy_menu(self, person):
            cards = [SlaveMarketBuyCard(person, slave, self) for slave in self.slaves]
            return CardMenu(cards, cancel=True).show()

        def sell_menu(self, person):
            cards = [SlaveMarketSellCard(person, slave, self) for slave in person.get_slaves()]
            return CardMenu(cards, cancel=True).show()

    class SlaveMarketBuyCard(Card, Command):
        def __init__(self, buyer, slave, market):

            self.buyer = buyer
            self.slave = slave
            self.market = market

        def name(self):
            return self.slave.name

        def _cost(self):
            attributes = ['hardiness', 'grace']
            return max([getattr(self.slave, i)() for i in attributes]) * 10

        def description(self):
            return 'Cost: %s' % self._cost()

        def image(self):
            return self.slave.avatar

        def run(self):
            self.buyer.remove_money(self._cost())
            self.buyer.enslave(self.slave)
            self.market.slaves.remove(self.slave)

        def is_active(self):
            return self.buyer.has_money(self._cost())

        def inactive_hint(self):
            return 'Not enough money'

        def has_additional_info(self):
            return True

        def additional_info(self):
            return renpy.call_in_new_context('lbl_cis_glue', person=self.slave)

    class SlaveMarketSellCard(Card, Command):

        def __init__(self, buyer, slave, market):
            self.seller = seller
            self.slave = slave
            self.market = market

        def name(self):
            return self.slave.name

        def _cost(self):
            attributes = ['hardiness', 'grace']
            return max([getattr(self.slave, i)() for i in attributes]) * 6

        def description(self):
            return 'Cost: %s' % self._cost()

        def image(self):
            return self.slave.avatar

        def run(self):
            self.buyer.add_money(self._cost())
            self.buyer.remove_slave(self.slave)
            self.market.slaves.append(self.slave)


    actions_slave_market = None

label lbl_actions_slave_market(action):

    python:
        if actions_slave_market is None:
            actions_slave_market = ActionsSlaveMarket(core)

    menu:
        'Usual slave market'
        'Buy':
            python:
                actions_slave_market.buy_menu(action.person)

        'Sell' if action.person.has_slaves():
            python:
                actions_slave_market.sell_menu(action.person)

        'Leave':
            return
    call lbl_actions_slave_market(action)
    return 