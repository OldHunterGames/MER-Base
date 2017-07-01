# -*- coding: <UTF-8> -*-
import renpy.store as store
import renpy.exports as renpy
from mer_utilities import encolor_text, get_files


class Motivation(object):
    _colors = {
        'desperation': 'red',
        'stress': 'magenta',
        'determination': 'green',
        'enthusiams': 'gold'
    }
    _images_bg = {
        'desperation': 'bronze',
        'stress': 'silver',
        'determination': 'silver',
        'enthusiams': 'gold'
    }

    def __init__(self, id):

        self.id = id

    def data(self):
        return store.motivations_data[self.id]

    @property
    def type(self):
        return self.data().get('type')

    def image(self):
        bg_image = 'images/motivations/' +\
            self._images_bg[self.id] + '.jpg'
        return renpy.display.im.Composite(
            (0, 0), self.get_image(),
            (0, 0), bg_image)

    def get_image(self):
        # testing image getting system
        path = 'images/%s/%s' % (self.data().get('image'), self._id)
        images = get_files(path)
        try:
            img = images[0]
        except IndexError:
            img = None
        return img

    def name(self):
        return encolor_text(self.data().get('name'),
                            self._colors[self.id])

    def run(self):
        renpy.call_in_new_context(self.data.get('run_label'))
