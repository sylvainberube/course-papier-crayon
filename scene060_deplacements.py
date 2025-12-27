from manim import *
from core import *

class Scene060_Deplacements(SceneDeuxPanneauxGrille):
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

        # Agents
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

        for i in range(0, len(alexane.visited)-1):
        # for i in range(0, 6):
            # 1. Affichage du point attendu et de la flèche menant à ce point
            if i == 0:
                deplacement = (0,0)
            else:
                deplacement = [alexane.visited[i][j] - alexane.visited[i-1][j] for j in range(2)]
            point_attendu = [alexane.visited[i][j] + deplacement[j] for j in range(2)]
            dot_attendu = dot_at_cell(
                point_attendu, self.N, self.side, self.right_center, WHITE
            )
            fleche_attendu = Arrow(
                grid_point(alexane.visited[i], self.N, self.side, self.right_center),
                grid_point(point_attendu, self.N, self.side, self.right_center),
                color=WHITE,
                stroke_width=2,
                max_stroke_width_to_length_ratio=1e6,
                buff=0,
                tip_length=0.10,
                max_tip_length_to_length_ratio=1e6,
            ).set_stroke(opacity=1)
            groupe_attendu = VGroup(dot_attendu, fleche_attendu)
            self.play(FadeIn(groupe_attendu), run_time=1)

            # 2. Affichage des 9 voisins à ce point attendu ainsi que les flèches (fade out de 1)
            #    Afficher en rouge les points inaccessibles
            points_possibles = [(point_attendu[0] + dx, point_attendu[1] + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
            cercles_possibles = []
            cercles_possibles.clear()
            fleches_possibles = []
            fleches_possibles.clear()
            for point_possible in points_possibles:
                couleur = WHITE
                if not coord_valide(point_possible):
                    couleur = RED_E
                cercle = Circle(
                    radius=0.05,
                    stroke_width=1,
                    color=couleur,
                )
                cercle.move_to(grid_point(point_possible, self.N, self.side, self.right_center))
                cercles_possibles.append(cercle)

                fleche_possible = Arrow(
                    grid_point(alexane.visited[i], self.N, self.side, self.right_center),
                    grid_point(point_possible, self.N, self.side, self.right_center),
                    color=couleur,
                    stroke_width=1,
                    max_stroke_width_to_length_ratio=1e6,
                    buff=0,
                    tip_length=0.05,
                    max_tip_length_to_length_ratio=1e6,
                ).set_stroke(opacity=1)
                fleches_possibles.append(fleche_possible)

            self.play(
                *[FadeIn(c) for c in cercles_possibles],
                *[FadeIn(f) for f in fleches_possibles],
                FadeOut(groupe_attendu),
                run_time=1
            )

            # 3. Affichage du point choisi
            point_choisi = dot_at_cell(
                alexane.visited[i+1], self.N, self.side, self.right_center, alexane.color
            )
            self.play(
                FadeIn(point_choisi),
                run_time=1
            )

            # 4. Affichage de la nouvelle flèche menant à ce point choisi, fade out du reste
            nouvelle_fleche = Arrow(
                grid_point(alexane.visited[i], self.N, self.side, self.right_center),
                grid_point(alexane.visited[i+1], self.N, self.side, self.right_center),
                color=alexane.color,
                stroke_width=2,
                max_stroke_width_to_length_ratio=1e6,
                buff=0,
                tip_length=0.10,
                max_tip_length_to_length_ratio=1e6,
            ).set_stroke(opacity=1)
            
            self.play(
                FadeIn(nouvelle_fleche),
                *[FadeOut(c) for c in cercles_possibles],
                *[FadeOut(f) for f in fleches_possibles],
                run_time=1
            )

        # Fin
        self.wait(10)

