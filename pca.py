# TODO: Évaluer l'utilisation de VGroup au lieu de lists pour hold des mobjects

from manim import *
import numpy as np
import random

class PCA(Scene):
    def construct(self):
        
        dots = self.generate_random_dots(5)
        dots2 = self.generate_random_dots(5)

        dot_test = Dot([1, 1, 1], 0.1, color = RED)
        dot_test2 = Dot([1, 1, 10], 0.1, color = RED)
        numberplane = NumberPlane(x_range=[-10, 10], y_range=[-10, 10])
        
        self.add(numberplane)
        self.add(*dots)

        self.play(*self.create_transformation_list(dots, dots2))
        self.remove(*dots2)
        self.play(*self.apply_to_all(Rotate, [*dots2, numberplane], angle = TAU/8, about_point=ORIGIN))
        # self.play(Rotate(numberplane, -TAU/2, about_point=ORIGIN))

        self.add(dot_test)
        self.play(Rotate(dot_test, TAU, about_point=ORIGIN))
        self.play(Transform(dot_test, dot_test2))
        self.wait(3)

    def generate_random_dot(self, lbound = 0, ubound = 1, generate_z = True):
        return Dot([random.uniform(lbound, ubound), random.uniform(lbound, ubound), generate_z * random.uniform(lbound, ubound)])

    def generate_random_dots(self, n, lbound = 0, ubound = 1, generate_z = True):
        return [self.generate_random_dot(lbound, ubound, generate_z) for i in range(n)]

    def create_transformation_list(self, from_list, to_list):
        return [Transform(from_list[i], to_list[i]) for i in range(len(from_list))]

    def apply_to_all(self, function, list, *args, **kwargs):
        return [function(list[i], *args, **kwargs) for i in range(len(list))]

    def orthogonal_project_point_on_line(self, dot, line):
        """Returns the point on the line segment ab that is closest to p."""
        ap = dot.get_center() - line.get_start()
        ab = line.get_end() - line.get_start()
        return Dot(line.get_start() + np.dot(ap, ab) / np.dot(ab, ab) * ab)

    def orthogonal_project_point_on_line2(self, dot, line):
        """Returns the point on the line segment ab that is closest to p."""
        ap = dot.get_center() - line.get_start()
        ab = line.get_end() - line.get_start()
        return line.get_start() + np.dot(ap, ab) / np.dot(ab, ab) * ab


class PCA_2(PCA):
    def construct(self):
        numberplane = NumberPlane(x_range=[-10, 10], y_range=[-10, 10])

        dots = self.generate_random_dots(5, -4, 4, False)
        dots = [dots[i].set_color(RED) for i in range(len(dots))]
        line_x = Line([0, 0, 0], [10, 0, 0])
        line_y = Line([0, 0, 0], [0, 10, 0])

        line_pca = Line([-10, -10, 0], [10, 10, 0])

        projections_x = self.create_projections(dots, line_x)
        projections_y = self.create_projections(dots, line_y)
        projections_pca = self.create_projections(dots, line_pca)


        self.add(numberplane, *dots)


        self.play(*self.apply_to_all(Create, projections_x))
        self.wait(1)

        self.play(*self.apply_to_all(Uncreate, projections_x))
        self.wait(2)

 
        self.play(*self.apply_to_all(Create, projections_y))
        self.wait(1)

        self.play(*self.apply_to_all(Uncreate, projections_y))
        self.wait(2)


        self.add(line_pca)
        self.wait(1)

        self.play(*self.apply_to_all(Create, projections_pca))
        self.wait(1)

        self.play(*self.apply_to_all(Uncreate, projections_pca))
        self.wait(2)



    def create_projections(self, dots, line):
        proj = [self.orthogonal_project_point_on_line(dots[i], line) for i in range(len(dots))]
        proj_line = [DashedLine(dots[i].get_center(), proj[i].get_center()) for i in range(len(dots))]

        return proj + proj_line


class PCA_3(PCA):
    def construct(self):
        numberplane = Axes()
        dot = Dot([4, 2, 0], 0.1, color = RED)
        line = Line([-5, -5, 0], [5, 5, 0])

        projection_dot = Dot(self.orthogonal_project_point_on_line2(dot, line), color = YELLOW)
        projection_dot.add_updater(lambda d: d.move_to(self.orthogonal_project_point_on_line2(dot, line)))

        projection_line = DashedLine(projection_dot, dot)
        projection_line.add_updater(lambda d: d.become(DashedLine(dot.get_center(), self.orthogonal_project_point_on_line2(dot, line))))

        self.add(dot, line, projection_dot, numberplane, projection_line)
        #self.wait(1)
        #self.play(Transform(dot, Dot([1, 3, 0], 0.1, color = BLUE)))
        #self.wait(1)
        self.play(Rotate(line, TAU/2, about_point=ORIGIN, run_time = 8))
        #self.wait(1)



class PCA_3d(ThreeDScene):
    def construct(self):
        numberplane = ThreeDAxes()
        dot = Dot([4, 2, 5], 0.1, color = RED)
        dot2 = Dot([2, -4, -1], 0.1, color = BLUE_A)
        line = Line([-3, -3, -4], [3, 3, 4], color = RED_B)

        projection_dot = Dot(self.orthogonal_project_point_on_line2(dot, line), color = YELLOW)
        projection_dot.add_updater(lambda d: d.move_to(self.orthogonal_project_point_on_line2(dot, line)))

        projection_line = DashedLine(projection_dot, dot)
        projection_line.add_updater(lambda d: d.become(DashedLine(dot.get_center(), self.orthogonal_project_point_on_line2(dot, line))))

        self.set_camera_orientation(phi=75 * DEGREES, theta=40 * DEGREES)

        self.add(dot, line, projection_dot, numberplane, projection_line, dot2)
        self.wait(1)
        self.play(Transform(dot, Dot([1, 3, 0], 0.1, color = BLUE)))
        self.wait(1)
        self.play(Rotate(line, TAU/2, about_point=ORIGIN, run_time = 8))
        self.wait(1)




    def orthogonal_project_point_on_line2(self, dot, line):
        """Returns the point on the line segment ab that is closest to p."""
        ap = dot.get_center() - line.get_start()
        ab = line.get_end() - line.get_start()
        return line.get_start() + np.dot(ap, ab) / np.dot(ab, ab) * ab