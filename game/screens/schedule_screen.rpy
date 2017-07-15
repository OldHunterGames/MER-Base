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
            if self._type == 'optional':
                self._person.schedule.set_optional(self._slot, self._schedule_obj)
            else:
                self._person.schedule.set(self._type, self._schedule_obj)


screen sc_schedule(person):
    $ schedule = person.schedule
    window:
        style 'char_info_window'
        hbox:
            spacing 10
            for i in ('job', 'ration', 'accommodation'):
                vbox:
                    imagebutton:
                        idle getattr(schedule, i).image()
                        action Function(
                                CardMenu(
                                    [SetScheduleItem(person, i, k)
                                    for k in schedule.available(i, core.world)],
                                    current=SetScheduleItem(person, i, getattr(schedule, i))).show)
                    text getattr(schedule, i).name()
        hbox:
            yalign 1.0
            for i in (0, 1, 2):
                python:
                    item = schedule.get_optional(i)
                    if item is None:
                        img = im.Scale(card_back(), 200, 300)
                        txt = 'Optional'
                    else:
                        img = item.image()
                        txt = item.name()
                vbox:
                    imagebutton:
                        idle img
                        action Function(
                                CardMenu(
                                    [SetScheduleItem(person, 'optional', k, i)
                                    for k in schedule.available('optional', core.world)],
                                    current=item, cancel=True).show)
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