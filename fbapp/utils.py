import os
import random
import textwrap

from PIL import Image, ImageFont, ImageDraw

from . import models

def find_content(gender):
    contents = models.Content.query.filter(models.Content.gender == models.Gender[gender]).all()

    return random.choice(contents)


class OpenGraphImage:
    """docstring for OpenGraphImage."""

    def __init__(self, uid, first_name, description):
        self.location = self._location(uid)

        background = self.base()
        # textwrap découpe une chaine de caractères
        # sans couper les mots au milieu.
        sentences = textwrap.wrap(description, width=60)

        # current_h : Hauteur à laquelle commencer à écrire .
        # pad : pixels à ajouter entre chaque ligne, en hauteur.
        current_h, pad = 180, 10

        for sentence in sentences:
          w, h = self.print_on_img(background, sentence, 40, current_h)

          # on incrémente la hauteur pour créer une nouvelle ligne
          # en-dessous.
          current_h += h + pad

        background.save(self._path(uid))
        background.show()

    def _location(self, uid):
        return 'tmp/{}.jpg'.format(uid)

    def _path(self, uid):
        return os.path.join('fbapp','static','tmp', '{}.jpg'.format(uid))

    def base(self):
        return Image.new('RGB', (1200,630), '#18BC9C')

    def print_on_img(self, img, text, size, height):
        font = ImageFont.truetype(os.path.join('fbapp','static', 'fonts', 'Arcon-Regular.otf'), size)

        draw = ImageDraw.Draw(img)

        #return Width and Height of string
        w,h = draw.textsize(text,font)

        # Calcul de la position pour que le texte soit centré
        # et non pas aligné à gauche.
        position = ((img.width - w) / 2, height)

        # Ajout du texte à l'image.
        draw.text(position, text, (255, 255, 255), font=font)

        return (w,h)
