from manim import *
from core import *

class Scene030_MiseEnPlace(SceneDeuxPanneauxGrille):
    def construct(self):
        self.setup_layout(show_frames=False)  # True si tu veux voir les cadres
        self.setup_text_columns()

        # Titre
        title = self.make_title()
        self.add(title)

        # Grille
        self.build_grid()
        self.add(self.grid)

        # Piste
        piste = self.make_track()
        self.add(piste)

        self.play(
            title.animate.shift(UP * 3),
            run_time = 1
        )

        # Agents
        agents = make_agents_initial_state()
        alexane = agents["Alexane"]
        noam = agents["Noam"]

        alexane_nom = self.make_agent_name(alexane)
        alexane_nom.move_to(self.text_left_center + DOWN * 2.5)
        noam_nom = self.make_agent_name(noam)
        noam_nom.move_to(self.text_right_center + DOWN * 2.5)

        spacing = 0.8
        velo_icon = ImageMobject("assets/icons/velo.png")
        velo_icon.set_height(0.6)
        velo_icon.move_to(self.text_left_center + DOWN * (2.5+spacing))
        sourire_icon = ImageMobject("assets/icons/sourire.png")
        sourire_icon.set_height(0.6)
        sourire_icon.move_to(self.text_right_center + DOWN * (2.5+spacing))

        alexane_dot = Dot(radius=0.3, color=BLUE)
        alexane_dot.move_to(self.text_left_center + DOWN * (2.5+spacing))
        noam_dot    = Dot(radius=0.3, color=YELLOW)
        noam_dot.move_to(self.text_right_center + DOWN * (2.5+spacing))

        # Affichage
        alexane_circles = circles_for_agent(
            alexane, self.N, self.side, self.right_center
        )
        noam_circles = circles_for_agent(
            noam, self.N, self.side, self.right_center
        )

        self.play(
            FadeIn(alexane_nom, shift=DOWN * 0.2),
            FadeIn(noam_nom, shift=DOWN * 0.2),
            run_time=2
        )
        self.play(
            FadeIn(velo_icon, shift=UP*0.1),
            FadeIn(sourire_icon, shift=UP*0.1),
            run_time=5
        )
        self.play(
            FadeOut(velo_icon),
            FadeOut(sourire_icon),
            FadeIn(alexane_dot),
            FadeIn(noam_dot),
            run_time=3.0
        )
        dot_alexane = point_choisi = dot_at_cell(
            alexane.visited[0], self.N, self.side, self.right_center, alexane.color
        )
        dot_noam = point_choisi = dot_at_cell(
            noam.visited[0], self.N, self.side, self.right_center, noam.color
        )
        self.play(
            FadeIn(dot_alexane, dot_noam),
            run_time = 3.0
        )

        flash_points = make_grid_intersection_dots(
            N=self.N,
            side=self.side,
            center=self.right_center,
            radius=0.05,
            color=WHITE,
            fill_opacity=0.5
        )

        # Flash: fade-in puis fade-out (tout en même temps)
        self.play(LaggedStartMap(FadeIn, flash_points, lag_ratio=0.0005), run_time=3)
        self.play(LaggedStartMap(FadeOut, flash_points, lag_ratio=0.0005), run_time=3)
                
        # Fin
        self.wait(10)

