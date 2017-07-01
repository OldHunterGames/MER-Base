init python:
    class SetScheduleItem(Command, Card):


        def __init__(self, person, type, scheduleobj):
            self._person = person
            self._type = type
            self._schedule_obj = scheduleobj

        def image(self):
            return self._schedule_obj.image()

        def name(self):
            return self._schedule_obj.name()

        def description(self):
            return self._schedule_obj.description()

        def run(self):
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

        textbutton 'Leave':
            yalign 1.0
            action Hide('sc_schedule')