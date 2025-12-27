from manim import *
from core import *

class Scene070_Sortie(SceneDeuxPanneauxGrille):
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
        manuel = agents["Manuel"]
        julie = agents["Julie"]
        self.afficher_agents_noms()

        dot_alexane_debut = dot_at_cell(
            alexane.visited[0], self.N, self.side, self.right_center, alexane.color
        )
        dot_noam_debut = dot_at_cell(
            noam.visited[0], self.N, self.side, self.right_center, noam.color
        )
        dot_manuel_debut = dot_at_cell(
            manuel.visited[0], self.N, self.side, self.right_center, manuel.color
        )
        dot_julie_debut = dot_at_cell(
            julie.visited[0], self.N, self.side, self.right_center, julie.color
        )
        self.add(dot_alexane_debut, dot_noam_debut)
        self.afficher_agents_noms_manuel_julie()
        self.play(
            FadeIn(dot_manuel_debut,dot_julie_debut),
            run_time=1
        )
        
        dots_manuel = []
        fleches_manuel = []
        for i in range(len(manuel.visited)):
            dots_manuel.append(dot_at_cell(manuel.visited[i], self.N, self.side, self.right_center, manuel.color))

            if i>0:
                fleche = Arrow(
                    grid_point(manuel.visited[i-1], self.N, self.side, self.right_center),
                    grid_point(manuel.visited[i], self.N, self.side, self.right_center),
                    color=manuel.color,
                    stroke_width=2,
                    max_stroke_width_to_length_ratio=1e6,
                    buff=0,
                    tip_length=0.10,
                    max_tip_length_to_length_ratio=1e6,
                ).set_stroke(opacity=1)
                fleches_manuel.append(fleche)

        for i in range(1,len(manuel.visited)):
            # self.add(dots_manuel[i], fleches_manuel[i-1])
            self.play(
                FadeIn(dots_manuel[i]),
                FadeIn(fleches_manuel[i-1]),
                run_time=1
            )

        # Manuel point attendu/possibles
        # 1. Affichage du point attendu et de la flèche menant à ce point
        deplacement = [manuel.visited[-1][j] - manuel.visited[-2][j] for j in range(2)]
        point_attendu = [manuel.visited[-1][j] + deplacement[j] for j in range(2)]
        dot_attendu = dot_at_cell(
            point_attendu, self.N, self.side, self.right_center, WHITE
        )
        fleche_attendu = Arrow(
            grid_point(manuel.visited[-1], self.N, self.side, self.right_center),
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
                grid_point(manuel.visited[-1], self.N, self.side, self.right_center),
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
            run_time=2
        )

        self.wait(2)

        groupe = VGroup(
            *dots_manuel[1:],
            *fleches_manuel
        )
        # self.play(
        #     *[FadeOut(c) for c in cercles_possibles],
        #     *[FadeOut(f) for f in fleches_possibles],
        #     FadeOut(groupe),
        #     run_time=1
        # )

        # Julie
        dots_julie = []
        fleches_julie = []
        for i in range(len(julie.visited)):
            dots_julie.append(dot_at_cell(julie.visited[i], self.N, self.side, self.right_center, julie.color))

            if i>0:
                fleche = Arrow(
                    grid_point(julie.visited[i-1], self.N, self.side, self.right_center),
                    grid_point(julie.visited[i], self.N, self.side, self.right_center),
                    color=julie.color,
                    stroke_width=2,
                    max_stroke_width_to_length_ratio=1e6,
                    buff=0,
                    tip_length=0.10,
                    max_tip_length_to_length_ratio=1e6,
                ).set_stroke(opacity=1)
                fleches_julie.append(fleche)

        for i in range(1,len(julie.visited)):
            # self.add(dots_julie[i], fleches_julie[i-1])
            self.play(
                FadeIn(dots_julie[i]),
                FadeIn(fleches_julie[i-1]),
                run_time=1
            )

        # Julie point attendu/possibles
        # 1. Affichage du point attendu et de la flèche menant à ce point
        deplacement = [julie.visited[-1][j] - julie.visited[-2][j] for j in range(2)]
        point_attendu = [julie.visited[-1][j] + deplacement[j] for j in range(2)]
        dot_attendu = dot_at_cell(
            point_attendu, self.N, self.side, self.right_center, WHITE
        )
        fleche_attendu = Arrow(
            grid_point(julie.visited[-1], self.N, self.side, self.right_center),
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
        points_possibles = [(point_attendu[0] + dx, point_attendu[1] + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
        cercles_possibles = []
        cercles_possibles.clear()
        fleches_possibles = []
        fleches_possibles.clear()
        for point_possible in points_possibles:
            couleur = RED_E
            if not coord_valide(point_possible):
                couleur = RED_E
            cercle = Circle(
                radius=0.05,
                stroke_width=1,
                color=RED_E,
            )
            cercle.move_to(grid_point(point_possible, self.N, self.side, self.right_center))
            cercles_possibles.append(cercle)

            fleche_possible = Arrow(
                grid_point(julie.visited[-1], self.N, self.side, self.right_center),
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
            run_time=2
        )

        groupe = VGroup(
            *dots_julie[1:],
            *fleches_julie
        )
        self.play(
            *[FadeOut(c) for c in cercles_possibles],
            *[FadeOut(f) for f in fleches_possibles],
            FadeOut(groupe),
            run_time=2
        )

        # Fin
        self.wait(10)
