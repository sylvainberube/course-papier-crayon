# d:
# cd "D:\Enseignement\Course-papier-crayon"

# manim -pqh --resolution 1920,1080 course_manim.py Scene010_Intro
# manim -pqh --resolution 1920,1080 course_manim.py Scene020_Piste
# manim -pqh --resolution 1920,1080 course_manim.py Scene030_MiseEnPlace
# manim -pqh --resolution 1920,1080 course_manim.py Scene040_Deplacements
# manim -pqh --resolution 1920,1080 course_manim.py Scene050_Deplacements
# manim -pqh --resolution 1920,1080 course_manim.py Scene060_Deplacements
# manim -pqh --resolution 1920,1080 course_manim.py Scene070_Sortie
# manim -pqh --resolution 1920,1080 course_manim.py Scene080_Objectif
# manim -pqh --resolution 1920,1080 course_manim.py Scene090_Partie
# -pqh
# -p — preview
# -q — quality
# -h — high
# -qh → high (production)

from manim import config

# Config globale AVANT d'importer les scènes
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

# Import des scènes (classes)
from scene010_intro import Scene010_Intro as _Scene010_Intro
from scene020_piste import Scene020_Piste as _Scene020_Piste
from scene030_mise_en_place import Scene030_MiseEnPlace as _Scene030_MiseEnPlace
from scene040_deplacements import Scene040_Deplacements as _Scene040_Deplacements
from scene050_deplacements import Scene050_Deplacements as _Scene050_Deplacements
from scene060_deplacements import Scene060_Deplacements as _Scene060_Deplacements
from scene070_sortie import Scene070_Sortie as _Scene070_Sortie
from scene080_objectif import Scene080_Objectif as _Scene080_Objectif
from scene090_partie import Scene090_Partie as _Scene090_Partie

class Scene010_Intro(_Scene010_Intro): pass
class Scene020_Piste(_Scene020_Piste): pass
class Scene030_MiseEnPlace(_Scene030_MiseEnPlace): pass
class Scene040_Deplacements(_Scene040_Deplacements): pass
class Scene050_Deplacements(_Scene050_Deplacements): pass
class Scene060_Deplacements(_Scene060_Deplacements): pass
class Scene070_Sortie(_Scene070_Sortie): pass
class Scene080_Objectif(_Scene080_Objectif): pass
class Scene090_Partie(_Scene090_Partie): pass
