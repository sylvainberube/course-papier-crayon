from manim import *
from core import *

class Scene050_Deplacements(SceneDeuxPanneauxGrille):
    def construct(self):
        self.setup_layout(show_frames=False)  # True si tu veux voir les cadres
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

        # Agents
        agents = make_agents_initial_state()
        alexane = agents["Alexane"]
        noam = agents["Noam"]
        self.afficher_agents_noms()

        grille_alexane_debut = grid_point(alexane.visited[0], self.N, self.side, self.right_center)
        dot_alexane_debut = dot_at_cell(
            alexane.visited[0], self.N, self.side, self.right_center, alexane.color
        )
        dot_noam_debut = dot_at_cell(
            noam.visited[0], self.N, self.side, self.right_center, noam.color
        )
        self.add(dot_alexane_debut, dot_noam_debut)

        points_premier_coup = [(1,32),(1,34),(2,32),(2,33),(2,34),(1,33)]
        points_grille_premier_coup = []
        for p in points_premier_coup:
            points_grille_premier_coup.append(grid_point(p, self.N, self.side, self.right_center))

        cercles_premier_coup = []
        fleches_premier_coup = []
        for point_grille in points_grille_premier_coup: 
            cercle = Circle(
                radius=0.05,
                stroke_width=1,
                color=WHITE,
            )
            cercle.move_to(point_grille)
            cercles_premier_coup.append(cercle)

            fleche = Arrow(
                grille_alexane_debut,
                point_grille,
                color=WHITE,
                stroke_width=1,
                max_stroke_width_to_length_ratio=1e6,
                buff=0,
                tip_length=0.05,
                max_tip_length_to_length_ratio=1e6,
            ).set_stroke(opacity=1)
            fleches_premier_coup.append(fleche)

        for i in range(len(cercles_premier_coup)) : 
            self.play(
                FadeIn(cercles_premier_coup[i]),
                FadeIn(fleches_premier_coup[i]),
                run_time=1
            )
        
        self.wait(1)
        self.play(
            FadeOut(*cercles_premier_coup, *fleches_premier_coup),
            run_time=1
        )

        # Fin
        self.wait(10)

