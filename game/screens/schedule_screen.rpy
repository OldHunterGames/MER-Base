init python:
    class SetScheduleItem(Command, Card):


        def __init__(self, person, type, scheduleobj, slot=None):
            self._person = person
            self._type = type
            self._schedule_obj = scheduleobj
            self._slot = slot

        def image(self):
            return self._schedule_obj.image()

        def name(self):
            return self._schedule_obj.name()

        def description(self):
            return self._schedule_obj.description()

        def run(self):
            if self._type == 'extra':
                self._person.schedule.set_extra(self._slot, self._schedule_obj)
            else:
                self._person.schedule.set_current(self._type, self._schedule_obj)


screen sc_schedule(person):
    $ schedule = person.schedule
    window:
        style 'char_info_window'
        hbox:
            spacing 10
            for i in ('job', 'ration', 'accommodation'):
                $ current = schedule.get_current(i)
                vbox:
                    imagebutton:
                        idle current.image()
                        action Function(
                                CardMenu(
                                    [SetScheduleItem(person, i, k)
                                    for k in schedule.get_available(i, core.world)],
                                    current=SetScheduleItem(person, i, current)).show)
                    text current.name()
        hbox:
            yalign 1.0
            for i in (0, 1, 2):
                python:
                    item = schedule.get_extra(i)
                    if item is not None:
                        current_item = SetScheduleItem(person, 'extra', item, i)
                    else:
                        current_item = None
                    if item is None:
                        img = im.Scale(card_back(), 200, 300)
                        txt = 'Extra'
                    else:
                        img = item.image()
                        txt = item.name()
                vbox:
                    imagebutton:
                        idle img
                        action Function(
                                CardMenu(
                                    [SetScheduleItem(person, 'extra', k, i)
                                    for k in schedule.get_available('extra', core.world)],
                                    current=current_item, cancel=True).show)
                    text txt
        vbox:
            xalign 1.0
            text 'Decade bill: %s' % person.decade_bill()
            text 'Income %s' % person.civil_income
            text 'Sparks: %s' % person.money
            if not person.can_tick():
                text encolor_text('You have no money to skip turn', 'red')
        textbutton 'Leave':
            yalign 1.0
            xalign 1.0
            action Hide('sc_schedule')