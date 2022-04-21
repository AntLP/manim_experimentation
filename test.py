from manim import *

# https://docs.manim.community/en/stable/examples.html
# manim -p -qh test.py name_of_scene

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        line = Line(square.get_center())
        square.flip(LEFT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(RED, opacity=0.5)

        self.play(Create(square))
        self.play(Create(line))
        self.play(Transform(line, square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)


class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        arrow2 = Arrow(ORIGIN, [2, 3, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        tip_text2 = Text('(2, 3)').next_to(arrow2.get_end(), RIGHT)

        circle = Circle(5)   

        self.add(numberplane, dot, arrow, origin_text, tip_text)
        self.play(Transform(arrow, arrow2), Transform(tip_text, tip_text2))

        self.add(circle)
        self.wait(3)