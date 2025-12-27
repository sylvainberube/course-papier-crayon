from manim import *
from core import *

class Scene010_Intro(SceneDeuxPanneauxGrille):
    def construct(self):
        # Setup commun
        self.setup_layout(show_frames=False)   # mets False quand tu ne veux plus voir les cadres

        # Titre
        title = self.make_title()
        self.play(
            FadeIn(title),
            run_time=3.0
        )

        # Grille
        self.build_grid()
        self.play(
            FadeIn(self.grid),
            run_time=3.0
        )

        # Fin
        self.wait(20.0)
