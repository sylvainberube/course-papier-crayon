from manim import *
import numpy as np
from dataclasses import dataclass, field
from typing import List, Tuple, Any

# ==================================================
# Modèle de données : Agent
# ==================================================

GridPoint = Tuple[int, int]

@dataclass
class Agent:
    name: str
    color: Any
    visited: List[GridPoint] = field(default_factory=list)

    def place(self, start: GridPoint):
        self.visited = [start]

    def move_to(self, p: GridPoint):
        self.visited.append(p)

    @property
    def pos(self) -> GridPoint:
        if not self.visited:
            raise ValueError(f"L’agent {self.name} n’a pas encore été placé.")
        return self.visited[-1]

coords = [
    (0,0),(0,0),
    (0,39),(0,39),(0,39),(0,39),(0,39),(0,39),(0,39),
    (30,39),(31,39),(30,39),
    (3,39),(2,39),(1,39),(1,39),(1,39),(1,39),(1,39),
    (1,12),(1,10),(1,9),(1,9),(1,8),(1,8),(1,8),(1,9),(1,9),(1,10),(1,12),
    (1,38),(1,39),(1,39),(2,39),(3,39),
    (30,39),(31,39),(31,39),(31,39),(31,39),
]

coords_valides = [
    (j, 40 - i)
    for i in range(len(coords))
    for j in range(coords[i][0] + 1, coords[i][1])
]

def make_agents_initial_state():
    """
    État initial commun (scène 030 et toutes celles après).
    Retourne un dict pour un accès facile.
    """
    alexane = Agent("Alexane", BLUE)
    noam = Agent("Noam", YELLOW)
    manuel = Agent("Manuel", PINK)
    julie = Agent("Julie", PURPLE)

    # Positions de départ (ajuste à ta ligne de départ)
    alexane.place((1, 33))
    alexane.place((1, 33))
    alexane.move_to((2, 33))
    alexane.move_to((4, 33))
    alexane.move_to((7, 33))
    alexane.move_to((11, 33))
    alexane.move_to((16, 33))
    alexane.move_to((22, 32))
    alexane.move_to((27, 32))
    alexane.move_to((31, 32))
    alexane.move_to((34, 31))
    alexane.move_to((36, 30))
    alexane.move_to((37, 29))
    alexane.move_to((37, 28))
    alexane.move_to((36, 27))
    alexane.move_to((34, 26))
    alexane.move_to((31, 25))
    alexane.move_to((27, 24))
    alexane.move_to((22, 23))
    alexane.move_to((18, 22))
    alexane.move_to((15, 22))
    alexane.move_to((12, 22))
    alexane.move_to((10, 21))
    alexane.move_to((8, 19))
    alexane.move_to((7, 16))
    alexane.move_to((7, 12))
    alexane.move_to((8, 9))
    alexane.move_to((10, 7))
    alexane.move_to((13, 6))
    alexane.move_to((17, 6))
    alexane.move_to((22, 6))
    alexane.move_to((27, 6))
    alexane.move_to((31, 5))
    alexane.move_to((34, 3))
    alexane.move_to((36, 1))
    noam.place((1, 37))
    noam.move_to((2, 38))
    noam.move_to((4, 38))
    noam.move_to((7, 38))
    noam.move_to((11, 38))
    noam.move_to((16, 38))
    noam.move_to((21, 38))
    noam.move_to((25, 38))
    noam.move_to((28, 37))
    noam.move_to((30, 35))
    noam.move_to((31, 32))
    noam.move_to((32, 30))
    noam.move_to((32, 29))
    noam.move_to((31, 28))
    noam.move_to((29, 28))
    noam.move_to((26, 28))
    noam.move_to((22, 27))
    noam.move_to((17, 25))
    noam.move_to((13, 23))
    noam.move_to((10, 21))
    noam.move_to((8, 18))
    noam.move_to((7, 15))
    noam.move_to((7, 13))
    noam.move_to((8, 11))
    noam.move_to((10, 10))
    noam.move_to((13, 10))
    noam.move_to((17, 9))
    noam.move_to((22, 8))
    noam.move_to((28, 6))
    noam.move_to((33, 4))
    noam.move_to((37, 1))
    manuel.place((1, 35))
    manuel.move_to((2, 35))
    manuel.move_to((4, 35))
    manuel.move_to((7, 35))
    manuel.move_to((11, 35))
    manuel.move_to((16, 35))
    manuel.move_to((21, 35))
    manuel.move_to((25, 35))
    manuel.move_to((28, 35))
    manuel.move_to((30, 35))
    manuel.move_to((31, 34))
    manuel.move_to((32, 32))
    manuel.move_to((32, 29))
    manuel.move_to((31, 25))
    manuel.move_to((29, 22))
    julie.place((1, 38))
    julie.move_to((2, 37))
    julie.move_to((3, 35))
    julie.move_to((4, 32))

    return {"Alexane": alexane, "Noam": noam, "Manuel": manuel, "Julie": julie}

# Helper pour la création de la grille
def make_square_grid(n: int, side: float, color=BLUE, stroke_width: float = 2) -> VGroup:
    """
    Grille carrée n x n (n cases par côté), avec les bords inclus.
    - n: nombre de cases par côté
    - side: longueur du côté du carré (en unités Manim)
    """
    lines = VGroup()
    step = side / n
    half = side / 2

    # Verticales: x = -half, -half+step, ..., +half
    for k in range(n + 1):
        x = -half + k * step
        lines.add(Line(start=[x, -half, 0], end=[x, half, 0], stroke_width=stroke_width,
            color=color))

    # Horizontales: y = -half, -half+step, ..., +half
    for k in range(n + 1):
        y = -half + k * step
        lines.add(Line(start=[-half, y, 0], end=[half, y, 0], stroke_width=stroke_width,
            color=color))

    return lines

def grid_point(p, N, side, center):
    """(col,row) -> np.array([x,y,0]) en coordonnées Manim."""
    col, row = p
    cell = side / N
    half = side / 2
    x = -half + col * cell
    y = -half + row * cell
    return np.array([x, y, 0.0]) + center

def circles_for_agent(agent, N, side, center, radius=0.05):
    dots = VGroup()
    for cell in agent.visited:
        dots.add(Dot(grid_point(cell, N, side, center), radius=radius, color=agent.color))
    return dots

def dot_at_cell(cell, N, side, center, color, radius=0.05):
    return Dot(grid_point(cell, N, side, center), radius=radius, color=color)

def segment_between_cells(c1, c2, N, side, center, color, stroke_width=6, stroke_opacity=1.0):
    return Line(
        grid_point(c1, N, side, center),
        grid_point(c2, N, side, center),
        color=color,
        stroke_width=stroke_width,
        stroke_opacity=stroke_opacity
    )

def segment_on_grid(p1, p2, N, side, center, color=GRAY_B, stroke_width=2, stroke_opacity=1):
    return Line(
        grid_point(p1, N, side, center),
        grid_point(p2, N, side, center),
        color=color,
        stroke_width=stroke_width,
        stroke_opacity=stroke_opacity
    )

def arc_on_grid(center_cell, radius_cells, start_angle, angle,
                N, side, center, color=GRAY_B, stroke_width=2):
    cell = side / N
    arc = Arc(
        radius=radius_cells * cell,
        start_angle=start_angle,
        angle=angle,
        color=color,
        stroke_width=stroke_width
    )
    arc.move_to(grid_point(center_cell, N, side, center))
    return arc

def make_agent(name: str, color, start_cell, N, side, center, radius=0.07):
    dot = Dot(grid_point(start_cell, N, side, center), radius=radius, color=color)
    trace = VGroup()  # on ajoutera des segments plus tard
    agent = VGroup(trace, dot)  # trace derrière, dot devant
    agent.name = name
    agent.pos = start_cell  # position en (col,row)
    return agent

def add_trace_segment(agent, new_cell, N, side, center, color=None, stroke_width=6):
    old_cell = agent.pos
    seg = Line(
        grid_point(old_cell, N, side, center),
        grid_point(new_cell, N, side, center),
        stroke_width=stroke_width,
        color=(color if color is not None else agent[1].get_color())
    )
    agent[0].add(seg)        # trace = agent[0]
    agent.pos = new_cell
    return seg

def circles_for_agent(agent, N, side, center, radius=0.07):
    """
    Crée un VGroup de cercles correspondant aux points visités par l’agent.
    """
    circles = VGroup()
    for cell in agent.visited:
        c = Dot(
            grid_point(cell, N, side, center),
            radius=radius,
            color=agent.color
        )
        circles.add(c)
    return circles

def coord_valide(p):
    return p in coords_valides

def make_grid_intersection_dots(N: int, side: float, center, radius=0.045, color=WHITE, fill_opacity=0.9):
    """
    Crée un VGroup de points (Dots) sur toutes les intersections de la grille.
    Hypothèse: tes coordonnées de grille sont (0..N-1, 0..N-1).
    """
    dots = VGroup()

    for y in range(N-1, 0, -1):
        for x in range(1,N):
            if coord_valide((x,y)):
                p = grid_point((x, y), N, side, center)
                d = Dot(p, radius=radius, color=color)
                d.set_fill(color, opacity=fill_opacity)
                dots.add(d)
    return dots

class SceneDeuxPanneauxGrille(Scene):
    # Paramètres “globaux” (réutilisés partout)
    N = 40
    margin = 0.01

    def setup_layout(self, show_frames: bool = True, frame_stroke_width: float = 4):
        frame_w = config.frame_width
        frame_h = config.frame_height

        # Largeurs (840 | 1080)
        self.left_w = frame_w * 840 / 1920
        self.right_w = frame_w * 1080 / 1920

        self.left_center = LEFT * (frame_w / 2 - self.left_w / 2)
        self.right_center = RIGHT * (frame_w / 2 - self.right_w / 2)

        # Cadres (debug) — désactivables
        self.zone_gauche = Rectangle(width=self.left_w, height=frame_h, stroke_width=frame_stroke_width).move_to(self.left_center)
        self.zone_droite = Rectangle(width=self.right_w, height=frame_h, stroke_width=frame_stroke_width).move_to(self.right_center)

        if show_frames:
            self.add(self.zone_gauche, self.zone_droite)

        # Taille carrée de la grille dans la zone droite
        self.side = min(self.right_w, frame_h) * (1 - 2 * self.margin)

    def setup_text_columns(self):
        """
        Définit deux centres pour la zone texte :
        - self.text_left_center
        - self.text_right_center
        Positionnés en haut de la zone gauche.
        """
        padding_top = 0.4
        y_top = self.left_center[1] + config.frame_height / 2 - padding_top

        col_offset = self.left_w / 4
        self.text_left_center = self.left_center + LEFT * col_offset
        self.text_right_center = self.left_center + RIGHT * col_offset

        # On place en haut
        self.text_left_center = self.text_left_center + UP * (y_top - self.left_center[1])
        self.text_right_center = self.text_right_center + UP * (y_top - self.left_center[1])

    def make_text_column_boxes(self, height=1.4, stroke_width=2):
        """
        Boîtes de repère pour les 2 colonnes de texte (debug layout).
        """
        col_width = self.left_w / 2

        # Position verticale (en haut de la zone gauche)
        padding_top = 0.4
        y_center = self.left_center[1] + config.frame_height / 2 - padding_top - height / 2

        left_box = Rectangle(
            width=col_width,
            height=height,
            stroke_width=stroke_width,
            stroke_color=BLUE,
        ).move_to(
            [self.left_center[0] - col_width / 2, y_center, 0]
        )

        right_box = Rectangle(
            width=col_width,
            height=height,
            stroke_width=stroke_width,
            stroke_color=BLUE,
        ).move_to(
            [self.left_center[0] + col_width / 2, y_center, 0]
        )

        return VGroup(left_box, right_box)
        
    def make_agent_name(self, agent):
        return Text(
            agent.name,
            font_size=40,
            weight=BOLD,
            color = agent.color
        )

    def afficher_agents_noms(self):
        agents = make_agents_initial_state()
        alexane = agents["Alexane"]
        noam = agents["Noam"]

        alexane_nom = self.make_agent_name(alexane)
        alexane_nom.move_to(self.text_left_center + DOWN * 2.5)
        noam_nom = self.make_agent_name(noam)
        noam_nom.move_to(self.text_right_center + DOWN * 2.5)

        spacing = 0.8
        alexane_dot = Dot(radius=0.3, color=BLUE)
        alexane_dot.move_to(self.text_left_center + DOWN * spacing + DOWN * 2.5)
        noam_dot    = Dot(radius=0.3, color=YELLOW)
        noam_dot.move_to(self.text_right_center + DOWN * spacing + DOWN * 2.5)

        self.add(
            alexane_nom, noam_nom,
            alexane_dot, noam_dot
        )

    def afficher_agents_noms_manuel_julie(self, fadein = True):
        agents = make_agents_initial_state()
        manuel = agents["Manuel"]
        julie = agents["Julie"]

        manuel_nom = self.make_agent_name(manuel)
        manuel_nom.move_to(self.text_left_center + DOWN * 4.5)
        julie_nom = self.make_agent_name(julie)
        julie_nom.move_to(self.text_right_center + DOWN * 4.5)

        spacing = 0.8
        manuel_dot = Dot(radius=0.3, color=manuel.color)
        manuel_dot.move_to(self.text_left_center + DOWN * (spacing + 4.5))
        julie_dot    = Dot(radius=0.3, color=julie.color)
        julie_dot.move_to(self.text_right_center + DOWN * (spacing + 4.5))

        if fadein:
            self.play(
                FadeIn(manuel_nom, manuel_dot,julie_nom, julie_dot),
                run_time=2
            )
        else:
            self.play(
                FadeOut(manuel_nom, manuel_dot,julie_nom, julie_dot),
                run_time=0.5
            )

    def build_grid(self):
        # Construit la grille
        self.grid = make_square_grid(
            self.N,
            self.side,
            color=GRAY_D,
            stroke_width=1
        ).move_to(self.right_center)

    # Titre centré dans la zone gauche, aligné centré
    def make_title(self):
        """Titre standard du projet, prêt à être animé."""
        title = Paragraph(
            "Course",
            "papier–crayon",
            alignment="center",
            line_spacing=0.9,
            weight=BOLD
        ).scale(1.1)

        title.move_to(self.left_center)
        return title

    def make_track(self) -> VGroup:
        return VGroup(
            # Ligne de départ
            segment_on_grid(
                (1,31), (1,39),
                N=self.N, side=self.side, center=self.right_center,
                color=GREEN, stroke_width=24, stroke_opacity=0.5
            ),
            # Courbe 1
            segment_on_grid((1,39), (38,39), N=self.N, side=self.side, center=self.right_center),
            arc_on_grid(
                center_cell=(38.5,38.5), radius_cells=1,
                start_angle=PI/2, angle=-PI/2,
                N=self.N, side=self.side, center=self.right_center
            ),
            segment_on_grid((39,38), (39,22), N=self.N, side=self.side, center=self.right_center),
            arc_on_grid(
                center_cell=(38.5,21.5), radius_cells=1,
                start_angle=0, angle=-PI/2,
                N=self.N, side=self.side, center=self.right_center
            ),
            segment_on_grid((38,21), (13,21), N=self.N, side=self.side, center=self.right_center),
            arc_on_grid(
                center_cell=(10.5,16), radius_cells=5,
                start_angle=PI/2, angle=PI,
                N=self.N, side=self.side, center=self.right_center
            ),
            segment_on_grid((13,11), (36,11), N=self.N, side=self.side, center=self.right_center),
            arc_on_grid(
                center_cell=(37.5,9.5), radius_cells=3,
                start_angle=PI/2, angle=-PI/2,
                N=self.N, side=self.side, center=self.right_center
            ),
            segment_on_grid((39,8), (39,1), N=self.N, side=self.side, center=self.right_center),

            # Ligne d'arrivée
            segment_on_grid(
                (39,1), (31,1),
                N=self.N, side=self.side, center=self.right_center,
                color=RED, stroke_width=24, stroke_opacity=0.5
            ),

            # Courbe 2
            segment_on_grid((31,1), (31,4), N=self.N, side=self.side, center=self.right_center),
            arc_on_grid(
                center_cell=(30.5,4.5), radius_cells=1,
                start_angle=0, angle=PI/2,
                N=self.N, side=self.side, center=self.right_center
            ),
            segment_on_grid((30,5), (6,5), N=self.N, side=self.side, center=self.right_center),
            arc_on_grid(
                center_cell=(3.5,7.5), radius_cells=5,
                start_angle=3*PI/2, angle=-PI/2,
                N=self.N, side=self.side, center=self.right_center
            ),
            segment_on_grid((1,10), (1,24), N=self.N, side=self.side, center=self.right_center),
            arc_on_grid(
                center_cell=(3.5,26.5), radius_cells=5,
                start_angle=PI, angle=-PI/2,
                N=self.N, side=self.side, center=self.right_center
            ),
            segment_on_grid((6,29), (30,29), N=self.N, side=self.side, center=self.right_center),
            arc_on_grid(
                center_cell=(30.5,30.0), radius_cells=1,
                start_angle=-PI/2, angle=PI,
                N=self.N, side=self.side, center=self.right_center
            ),
            segment_on_grid((30,31), (1,31), N=self.N, side=self.side, center=self.right_center),
        )