from manim import *
from core import *

class Scene080_Objectif(SceneDeuxPanneauxGrille):
    def construct(self):
        self.setup_layout(show_frames=False)
        self.setup_text_columns()

        # Titre
        title = self.make_title().shift(UP * 3)
        self.add(title)

        # Grille
        self.build_grid()
        self.add(self.grid)

        # Piste
        piste = self.make_track()
        self.add(piste)

        # Nouvel agent (mauve Manuel) Crash
        agents = make_agents_initial_state()
        alexane = agents["Alexane"]
        noam = agents["Noam"]

        self.afficher_agents_noms()

        dot_alexane_debut = dot_at_cell(
            alexane.visited[0], self.N, self.side, self.right_center, alexane.color
        )
        dot_noam_debut = dot_at_cell(
            noam.visited[0], self.N, self.side, self.right_center, noam.color
        )
        self.add(dot_alexane_debut, dot_noam_debut)

        self.wait(5)

        arrivee = segment_on_grid(
            (39,1), (31,1),
            N=self.N, side=self.side, center=self.right_center,
            color=RED, stroke_width=24, stroke_opacity=0
        )
        self.play(
            arrivee.animate.set_stroke(opacity=1),
            run_time=2,
            rate_func=there_and_back
        )


        # Fin
        self.wait(5)

