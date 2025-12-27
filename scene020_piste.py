from manim import *
from core import *

class Scene020_Piste(SceneDeuxPanneauxGrille):
    def construct(self):
        self.setup_layout(show_frames=False)

        # Titre
        title = self.make_title()
        self.add(title)

        # Grille
        self.build_grid()
        self.add(self.grid)  # grille visible en tout temps

        # Piste
        piste = self.make_track()
        self.play(
            Create(piste),
#            title.animate.shift(UP * 3),
            run_time = 5
        )

        self.wait(1)

        # Lignes de départ et d'arrivée
        depart = segment_on_grid(
            (1,31), (1,39),
            N=self.N, side=self.side, center=self.right_center,
            color=GREEN, stroke_width=24, stroke_opacity=0
        )
        arrivee = segment_on_grid(
            (39,1), (31,1),
            N=self.N, side=self.side, center=self.right_center,
            color=RED, stroke_width=24, stroke_opacity=0
        )
        self.play(
            depart.animate.set_stroke(opacity=1,color=GREEN_B),
            run_time=2,
            rate_func=there_and_back
        )
        self.play(
            arrivee.animate.set_stroke(opacity=1,color=RED_B),
            run_time=2,
            rate_func=there_and_back
        )

        # Fin
        self.wait(10.0)
