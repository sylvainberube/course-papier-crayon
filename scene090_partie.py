from manim import *
from core import *

class Scene090_Partie(SceneDeuxPanneauxGrille):
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
        
        # --- Visuels persistants ---
        trace_a = VGroup()
        trace_n = VGroup()

        dot_a = dot_at_cell(alexane.visited[0], self.N, self.side, self.right_center, alexane.color)
        dot_n = dot_at_cell(noam.visited[0], self.N, self.side, self.right_center, noam.color)

        self.add(trace_a, trace_n, dot_a, dot_n)

        # indices : on est déjà au point 0 (départ), donc prochain = 1
        ia, in_ = 1, 1
        turn_alexane = True  # commence par Alexane (change si tu veux)

        step_time = 1  # vitesse d'animation par coup

        past_a = VGroup()
        past_n = VGroup()
        past_a.add(Dot(grid_point(alexane.visited[0], self.N, self.side, self.right_center),
               radius=0.05, color=alexane.color).set_fill(alexane.color, opacity=0.9))
        past_n.add(Dot(grid_point(noam.visited[0], self.N, self.side, self.right_center),
               radius=0.05, color=noam.color).set_fill(noam.color, opacity=0.9))
        self.add(past_a, past_n)

        while ia < len(alexane.visited) or in_ < len(noam.visited):
            if turn_alexane and ia < len(alexane.visited):
                old_cell = alexane.visited[ia - 1]
                new_cell = alexane.visited[ia]

                p_old = grid_point(old_cell, self.N, self.side, self.right_center)
                p_new = grid_point(new_cell, self.N, self.side, self.right_center)

                seg = Arrow(
                    p_old,
                    p_new,
                    color=alexane.color,
                    stroke_width=2,
                    max_stroke_width_to_length_ratio=1e6,
                    buff=0,
                    tip_length=0.15,
                    max_tip_length_to_length_ratio=1e6,
                ).set_stroke(opacity=1)
                
                trace_a.add(seg)

                # point permanent sur la nouvelle case
                new_dot = Dot(
                    grid_point(new_cell, self.N, self.side, self.right_center),
                    radius=0.05,
                    color=alexane.color
                )

                self.play(
                    FadeIn(seg),
                    dot_a.animate.move_to(p_new),
                    run_time=step_time
                )
                self.add(new_dot)

                ia += 1

            elif (not turn_alexane) and in_ < len(noam.visited):
                old_cell = noam.visited[in_ - 1]
                new_cell = noam.visited[in_]

                p_old = grid_point(old_cell, self.N, self.side, self.right_center)
                p_new = grid_point(new_cell, self.N, self.side, self.right_center)

                seg = Arrow(
                    p_old,
                    p_new,
                    color=noam.color,
                    stroke_width=2,
                    max_stroke_width_to_length_ratio=1e6,
                    buff=0,
                    tip_length=0.15,
                    max_tip_length_to_length_ratio=1e6,
                ).set_stroke(opacity=1)
                
                trace_a.add(seg)

                # point permanent sur la nouvelle case
                new_dot = Dot(
                    grid_point(new_cell, self.N, self.side, self.right_center),
                    radius=0.05,
                    color=noam.color
                )

                self.play(
                    FadeIn(seg),
                    dot_n.animate.move_to(p_new),
                    run_time=step_time
                )
                self.add(new_dot)
                
                in_ += 1

            # alterne même si l'autre est “fini”; la boucle gère en sautant les tours impossibles
            turn_alexane = not turn_alexane

        # Fin
        self.wait(10)

