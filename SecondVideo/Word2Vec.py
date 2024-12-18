<<<<<<< HEAD
from manim import *
import numpy as np
import os
import sys

# 获取当前脚本文件所在目录的父目录的父目录路径
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(current_dir, '..', '..')

# 将项目根目录添加到 Python 模块搜索路径中
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

from learning.tool.CreateBall import CreateBall

'''
    English：You are free to use my code, but please do not delete my copyright text.
    中文：您可以随意的使用我的代码，但是请使用的同时不要将我的版权说明文本删除掉。
'''


class Word2Vec(Scene):

    def construct(self):
        self.camera.background_color = "#ece6e2"
        # Copyright text
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=18,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED})
        self.play(copyright_txt.animate.to_corner(DR))
        self._explanations()

    def _explanations(self):
        # 苯
        vg1 = CreateBall(10)
        vg1.scale(0.3)
        vg1.to_corner(UL + np.array([-4, 0, 0]))
        brace_vg1 = Brace(vg1, LEFT, color=BLACK)
        Benzene = Text("Benzene", font="KaiTi", font_size=20, color=BLACK)
        Benzene_vec = MathTex(r'|1, 0, 0|', font_size=28, color=BLACK)
        Benzene.next_to(brace_vg1, LEFT)
        Benzene_vec.next_to(Benzene, DOWN)
        self.play(Create(vg1), Create(brace_vg1))
        self.play(Write(Benzene))
        self.play(Write(Benzene_vec))
        self.wait(2)

        # is
        vg2 = CreateBall(10)
        vg2.scale(0.3)
        vg2.next_to(vg1, DOWN + np.array([0, -2, 0]))
        brace_vg2 = Brace(vg2, LEFT, color=BLACK)
        isBen = Text("is", font="KaiTi", font_size=20, color=BLACK)
        isBen_vec = MathTex(r'|0, 1, 0|', font_size=28, color=BLACK)
        isBen.next_to(brace_vg2, LEFT + np.array([-1, 0, 0]))
        isBen_vec.next_to(isBen, DOWN)
        self.play(Create(vg2), Create(brace_vg2))
        self.play(Write(isBen))
        self.play(Write(isBen_vec))
        self.wait(2)
        #
        # # aromatic
        # vg3 = CreateBall(10)
        # vg3.scale(0.3)
        # vg3.next_to(vg2, DOWN)
        # brace_vg3 = Brace(vg3, LEFT, color=BLACK)
        # aromatic = Text("aromatic", font="KaiTi", font_size=20, color=BLACK)
        # aromatic.next_to(brace_vg3, LEFT)
        # self.play(Create(vg3), Create(brace_vg3))
        # self.play(Write(aromatic))
        # self.wait(2)
        #
        # # and
        # vg4 = CreateBall(10)
        # vg4.scale(0.3)
        # vg4.next_to(vg3, DOWN)
        # brace_vg4 = Brace(vg4, LEFT, color=BLACK)
        # annd = Text("and", font="KaiTi", font_size=20, color=BLACK)
        # annd.next_to(brace_vg4, LEFT)
        # self.play(Create(vg4), Create(brace_vg4))
        # self.play(Write(annd))
        # self.wait(2)

        # and
        vg5 = CreateBall(10)
        vg5.scale(0.3)
        vg5.next_to(vg2, DOWN + np.array([0, -2, 0]))
        brace_vg5 = Brace(vg5, LEFT, color=BLACK)
        flammable = Text("flammable", font="KaiTi", font_size=20, color=BLACK)
        flammable_vec = MathTex(r'|1, 0, 0|', font_size=28, color=BLACK)
        flammable.next_to(brace_vg5, LEFT)
        flammable_vec.next_to(flammable, DOWN)
        self.play(Create(vg5), Create(brace_vg5))
        self.play(Write(flammable))
        self.play(Write(flammable_vec))
        self.wait(2)

        # 这个位置有四个向量
        # 设置基向量：i, j, k
        vec_i = Arrow(start=vg1.get_right(),end=np.array([-2.66111111, 0.86, 0]), color=RED)  # x轴基向量
        vec_i.next_to(vg1, RIGHT)
        vec_j = Arrow(start=vg2.get_right(), end=np.array([-2.66111111, 0.86, 0]), color=GREEN)  # y轴基向量
        vec_j.next_to(vg2, RIGHT)
        vec_k = Arrow(start=vg5.get_right(), end=np.array([-2.66111111, 0.86, 0]), color=BLUE)  # z轴基向量
        vec_k.next_to(vg5, RIGHT)

        vecText = Text("W", font="KaiTi", font_size=25, color=BLACK)
        rect3 = Rectangle(width=2.0, height=2.0, color=BLACK)
        rect3.scale(0.7)
        rect3.next_to(vec_j, RIGHT)
        vecText.move_to(rect3.get_center())
        self.play(Create(rect3))
        self.play(Write(vecText))
        self.wait(2)

        self.play(GrowArrow(vec_i))
        self.play(GrowArrow(vec_j))
        self.play(GrowArrow(vec_k))
        self.wait(2)

        vg6 = CreateBall(20)
        vg6.scale(0.5)
        vg6.next_to(rect3, RIGHT + np.array([7, 0, 0]))
        add = Text("total vec", color=BLACK, font_size=20, font="KaiTi")
        arrow_end = Arrow(start=rect3.get_right(), end=vg6.get_left(), color=BLACK)
        add.next_to(arrow_end, UP)
        self.play(Create(vg6))
        self.wait(2)
        self.play(Create(arrow_end))
        self.play(Write(add))
        self.wait(2)

        vecText2 = Text("inW", font="KaiTi", font_size=25, color=BLACK)
        rect4 = Rectangle(width=2.0, height=2.0, color=BLACK)
        rect4.scale(0.7)
        rect4.next_to(vg6, RIGHT + np.array([1, 0, 0]))
        vecText2.move_to(rect4.get_center())
        arrow_vec = Arrow(start=vg6.get_right(), end=rect4.get_left(), color=BLACK, buff=0)
        self.play(Create(rect4))
        self.play(Write(vecText2))
        self.play(Create(arrow_vec))
        self.wait(2)

        vg7 = CreateBall(20)
        vg7.scale(0.5)
        vg7.stretch(1, dim=1)
        vg7.next_to(rect4, RIGHT + np.array([2, 0, 0]))
        finarrow = Arrow(start=rect4.get_right(), end=vg7.get_left(), buff=0, color=BLACK)
        self.play(Create(vg7))
        self.play(Create(finarrow))
        self.wait(3)
        vg7_br = Brace(vg7, RIGHT, color=BLACK)
        vg7_br_text = MathTex(r'|n, n, n|', font_size=28, color=BLACK)
        vg7_br_text.next_to(vg7_br, RIGHT)
        self.play(Create(vg7_br))
        self.play(Write(vg7_br_text))
        self.wait(3)
        finVg = VGroup(
            vg6,
            vg7
        )
        second_brace = Brace(finVg, direction=DOWN, color=YELLOW)
        second_brace_text = Text("Recovery", font="KaiTi", font_size=18, color=BLACK)
        second_brace_text.next_to(second_brace, DOWN)
        self.play(Create(second_brace))
        self.play(Write(second_brace_text))
        self.wait(3)


class Animation(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=10,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED}).scale(1.3)
        x1 = MathTex("x", color=BLACK)
        x2 = MathTex("y", color=BLACK)
        z = MathTex("z", color=BLACK)
        text1 = Text("Benzene |1,0,0|", font="KaiTi", font_size=20, color=BLACK)
        text2 = Text("is |0,1,0|", font="KaiTi", font_size=20, color=BLACK)
        text3 = Text("flammable |0,0,1|", font="KaiTi", font_size=20, color=BLACK)
        text1.move_to(np.array([-4, -4, 3]))
        text2.move_to(np.array([-2, -2, 3]))
        text3.move_to(np.array([0, 0, 3]))
        self.play(Write(text1))
        self.play(text1.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.play(Write(text2))
        self.play(text2.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.play(Write(text3))
        self.play(text3.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.wait(2)
        # 创建三维坐标系
        axes = ThreeDAxes(
            x_range=np.array([-1.5, 1.5]),
            y_range=np.array([-1.5, 1.5]),
            z_range=np.array([-1.5, 1.5]),
        ).scale(0.5)
        axes.set_color(BLACK)

        self.play(copyright_txt.animate.rotate(angle=190, axis=RIGHT).rotate(angle=PI / 4, axis=OUT))
        self.play(copyright_txt.animate.move_to(np.array([4, 4, -3.3])))
        axes.move_to(np.array([-2, -2, -1]))  # 将坐标系放置在右下角
        self.play(Create(axes))

        # 绘制向量
        vec1 = Arrow(start=axes.c2p(0, 0, 0), end=axes.c2p(1, 0, 0), color=RED, buff=0)
        vec2 = Arrow(start=axes.c2p(0, 0, 0), end=axes.c2p(0, 1, 0), color=YELLOW, buff=0)
        vec3 = Arrow(start=axes.c2p(0, 0, 0), end=axes.c2p(0, 0, 1), color=BLUE, buff=0)

        self.play(Write(vec1))
        self.wait(2)
        self.play(Write(vec2))
        self.wait(2)
        self.play(Write(vec3))
        x1.next_to(axes.get_center() + np.array([3.3, 0, 0]), DOWN).rotate(angle=PI / 2, axis=RIGHT).rotate(
            angle=PI / 4, axis=OUT)
        x2.next_to(axes.get_center() + np.array([0, 3.4, 0]), DOWN).rotate(angle=PI / 2, axis=RIGHT).rotate(
            angle=PI / 4, axis=OUT)
        z.next_to(axes.get_center() + np.array([0, 0, 1.7]), OUT).rotate(angle=PI / 2, axis=RIGHT).rotate(angle=PI / 4,
                                                                                                          axis=OUT)
        self.play(Write(x1), Write(x2), Write(z))
        self.wait(2)


class MatrixRepresentationOfTransformations3D(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=10,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED}).scale(1.3)
        self.play(copyright_txt.animate.rotate(angle=190, axis=RIGHT).rotate(angle=PI / 4, axis=OUT))
        self.play(copyright_txt.animate.move_to(np.array([4, 4, -3.3])))
        text1 = Text("Benzene |1,0,0|", font="KaiTi", font_size=20, color=BLACK)
        text2 = Text("is |0,1,0|", font="KaiTi", font_size=20, color=BLACK)
        text3 = Text("flammable |0,0,1|", font="KaiTi", font_size=20, color=BLACK)
        text1.move_to(np.array([-4, -4, 3]))
        text2.move_to(np.array([-2, -2, 3]))
        text3.move_to(np.array([0, 0, 3]))
        self.play(Write(text1))
        self.play(text1.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.play(Write(text2))
        self.play(text2.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.play(Write(text3))
        self.play(text3.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.wait(2)
        # 创建三维坐标系
        axes = ThreeDAxes()
        axes.scale(0.5)
        axes.set_color(BLACK)

        # 定义基向量 A
        A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 3个基向量
        v1 = A[:, 0]  # 第一列向量
        v2 = A[:, 1]  # 第二列向量
        v3 = A[:, 2]  # 第三列向量

        # 创建基向量的箭头
        vector_v1 = Arrow3D(start=ORIGIN, end=v1, color=RED)
        vector_v2 = Arrow3D(start=ORIGIN, end=v2, color=GREEN)
        vector_v3 = Arrow3D(start=ORIGIN, end=v3, color=BLUE)

        # 显示三维坐标系和基向量
        self.play(Create(axes), Create(vector_v1), Create(vector_v2), Create(vector_v3))
        self.wait(1)

        # 定义随机向量 M
        M = np.random.rand(3, 3) * 2 - 1  # 生成一个随机矩阵，数值在 -1 到 1 之间


        # 计算 A * M
        AM = np.dot(A, M)

        # 创建变换后的向量
        vector_v1_new = Arrow3D(start=ORIGIN, end=AM[:, 0], color=YELLOW)
        vector_v2_new = Arrow3D(start=ORIGIN, end=AM[:, 1], color=PURPLE)
        vector_v3_new = Arrow3D(start=ORIGIN, end=AM[:, 2], color=ORANGE)

        # 展示 A * M 变换后的向量
        self.play(Transform(vector_v1, vector_v1_new), Transform(vector_v2, vector_v2_new), Transform(vector_v3, vector_v3_new))
        self.wait(1)

        # 目标矩阵 B
        B = np.array([[3, -1, 0], [0, 1, -2], [-3, 0, 2]])

        # 创建调整后的 M
        M_adjusted = B @ np.linalg.inv(A)

        # 计算调整后的矩阵乘积 A * M_adjusted
        AM_adjusted = np.dot(A, M_adjusted)

        # 创建调整后的变换向量
        vector_v1_adjusted = Arrow3D(start=ORIGIN, end=AM_adjusted[:, 0], color=YELLOW)
        vector_v2_adjusted = Arrow3D(start=ORIGIN, end=AM_adjusted[:, 1], color=PURPLE)
        vector_v3_adjusted = Arrow3D(start=ORIGIN, end=AM_adjusted[:, 2], color=ORANGE)

        # 展示调整后的变换
        self.play(Transform(vector_v1, vector_v1_adjusted), Transform(vector_v2, vector_v2_adjusted), Transform(vector_v3, vector_v3_adjusted))
        self.wait(2)
        self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(PI/2)
        self.stop_3dillusion_camera_rotation()
=======
from manim import *
import numpy as np
import os
import sys

# 获取当前脚本文件所在目录的父目录的父目录路径
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(current_dir, '..', '..')

# 将项目根目录添加到 Python 模块搜索路径中
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

from learning.tool.CreateBall import CreateBall

'''
    English：You are free to use my code, but please do not delete my copyright text.
    中文：您可以随意的使用我的代码，但是请使用的同时不要将我的版权说明文本删除掉。
'''


class Word2Vec(Scene):

    def construct(self):
        self.camera.background_color = "#ece6e2"
        # Copyright text
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=18,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED})
        self.play(copyright_txt.animate.to_corner(DR))
        self._explanations()

    def _explanations(self):
        # 苯
        vg1 = CreateBall(10)
        vg1.scale(0.3)
        vg1.to_corner(UL + np.array([-4, 0, 0]))
        brace_vg1 = Brace(vg1, LEFT, color=BLACK)
        Benzene = Text("Benzene", font="KaiTi", font_size=20, color=BLACK)
        Benzene_vec = MathTex(r'|1, 0, 0|', font_size=28, color=BLACK)
        Benzene.next_to(brace_vg1, LEFT)
        Benzene_vec.next_to(Benzene, DOWN)
        self.play(Create(vg1), Create(brace_vg1))
        self.play(Write(Benzene))
        self.play(Write(Benzene_vec))
        self.wait(2)

        # is
        vg2 = CreateBall(10)
        vg2.scale(0.3)
        vg2.next_to(vg1, DOWN + np.array([0, -2, 0]))
        brace_vg2 = Brace(vg2, LEFT, color=BLACK)
        isBen = Text("is", font="KaiTi", font_size=20, color=BLACK)
        isBen_vec = MathTex(r'|0, 1, 0|', font_size=28, color=BLACK)
        isBen.next_to(brace_vg2, LEFT + np.array([-1, 0, 0]))
        isBen_vec.next_to(isBen, DOWN)
        self.play(Create(vg2), Create(brace_vg2))
        self.play(Write(isBen))
        self.play(Write(isBen_vec))
        self.wait(2)
        #
        # # aromatic
        # vg3 = CreateBall(10)
        # vg3.scale(0.3)
        # vg3.next_to(vg2, DOWN)
        # brace_vg3 = Brace(vg3, LEFT, color=BLACK)
        # aromatic = Text("aromatic", font="KaiTi", font_size=20, color=BLACK)
        # aromatic.next_to(brace_vg3, LEFT)
        # self.play(Create(vg3), Create(brace_vg3))
        # self.play(Write(aromatic))
        # self.wait(2)
        #
        # # and
        # vg4 = CreateBall(10)
        # vg4.scale(0.3)
        # vg4.next_to(vg3, DOWN)
        # brace_vg4 = Brace(vg4, LEFT, color=BLACK)
        # annd = Text("and", font="KaiTi", font_size=20, color=BLACK)
        # annd.next_to(brace_vg4, LEFT)
        # self.play(Create(vg4), Create(brace_vg4))
        # self.play(Write(annd))
        # self.wait(2)

        # and
        vg5 = CreateBall(10)
        vg5.scale(0.3)
        vg5.next_to(vg2, DOWN + np.array([0, -2, 0]))
        brace_vg5 = Brace(vg5, LEFT, color=BLACK)
        flammable = Text("flammable", font="KaiTi", font_size=20, color=BLACK)
        flammable_vec = MathTex(r'|1, 0, 0|', font_size=28, color=BLACK)
        flammable.next_to(brace_vg5, LEFT)
        flammable_vec.next_to(flammable, DOWN)
        self.play(Create(vg5), Create(brace_vg5))
        self.play(Write(flammable))
        self.play(Write(flammable_vec))
        self.wait(2)

        # 这个位置有四个向量
        # 设置基向量：i, j, k
        vec_i = Arrow(start=vg1.get_right(),end=np.array([-2.66111111, 0.86, 0]), color=RED)  # x轴基向量
        vec_i.next_to(vg1, RIGHT)
        vec_j = Arrow(start=vg2.get_right(), end=np.array([-2.66111111, 0.86, 0]), color=GREEN)  # y轴基向量
        vec_j.next_to(vg2, RIGHT)
        vec_k = Arrow(start=vg5.get_right(), end=np.array([-2.66111111, 0.86, 0]), color=BLUE)  # z轴基向量
        vec_k.next_to(vg5, RIGHT)

        vecText = Text("W", font="KaiTi", font_size=25, color=BLACK)
        rect3 = Rectangle(width=2.0, height=2.0, color=BLACK)
        rect3.scale(0.7)
        rect3.next_to(vec_j, RIGHT)
        vecText.move_to(rect3.get_center())
        self.play(Create(rect3))
        self.play(Write(vecText))
        self.wait(2)

        self.play(GrowArrow(vec_i))
        self.play(GrowArrow(vec_j))
        self.play(GrowArrow(vec_k))
        self.wait(2)

        vg6 = CreateBall(20)
        vg6.scale(0.5)
        vg6.next_to(rect3, RIGHT + np.array([7, 0, 0]))
        add = Text("total vec", color=BLACK, font_size=20, font="KaiTi")
        arrow_end = Arrow(start=rect3.get_right(), end=vg6.get_left(), color=BLACK)
        add.next_to(arrow_end, UP)
        self.play(Create(vg6))
        self.wait(2)
        self.play(Create(arrow_end))
        self.play(Write(add))
        self.wait(2)

        vecText2 = Text("inW", font="KaiTi", font_size=25, color=BLACK)
        rect4 = Rectangle(width=2.0, height=2.0, color=BLACK)
        rect4.scale(0.7)
        rect4.next_to(vg6, RIGHT + np.array([1, 0, 0]))
        vecText2.move_to(rect4.get_center())
        arrow_vec = Arrow(start=vg6.get_right(), end=rect4.get_left(), color=BLACK, buff=0)
        self.play(Create(rect4))
        self.play(Write(vecText2))
        self.play(Create(arrow_vec))
        self.wait(2)

        vg7 = CreateBall(20)
        vg7.scale(0.5)
        vg7.stretch(1, dim=1)
        vg7.next_to(rect4, RIGHT + np.array([2, 0, 0]))
        finarrow = Arrow(start=rect4.get_right(), end=vg7.get_left(), buff=0, color=BLACK)
        self.play(Create(vg7))
        self.play(Create(finarrow))
        self.wait(3)
        vg7_br = Brace(vg7, RIGHT, color=BLACK)
        vg7_br_text = MathTex(r'|n, n, n|', font_size=28, color=BLACK)
        vg7_br_text.next_to(vg7_br, RIGHT)
        self.play(Create(vg7_br))
        self.play(Write(vg7_br_text))
        self.wait(3)
        finVg = VGroup(
            vg6,
            vg7
        )
        second_brace = Brace(finVg, direction=DOWN, color=YELLOW)
        second_brace_text = Text("Recovery", font="KaiTi", font_size=18, color=BLACK)
        second_brace_text.next_to(second_brace, DOWN)
        self.play(Create(second_brace))
        self.play(Write(second_brace_text))
        self.wait(3)


class Animation(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=10,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED}).scale(1.3)
        x1 = MathTex("x", color=BLACK)
        x2 = MathTex("y", color=BLACK)
        z = MathTex("z", color=BLACK)
        text1 = Text("Benzene |1,0,0|", font="KaiTi", font_size=20, color=BLACK)
        text2 = Text("is |0,1,0|", font="KaiTi", font_size=20, color=BLACK)
        text3 = Text("flammable |0,0,1|", font="KaiTi", font_size=20, color=BLACK)
        text1.move_to(np.array([-4, -4, 3]))
        text2.move_to(np.array([-2, -2, 3]))
        text3.move_to(np.array([0, 0, 3]))
        self.play(Write(text1))
        self.play(text1.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.play(Write(text2))
        self.play(text2.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.play(Write(text3))
        self.play(text3.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.wait(2)
        # 创建三维坐标系
        axes = ThreeDAxes(
            x_range=np.array([-1.5, 1.5]),
            y_range=np.array([-1.5, 1.5]),
            z_range=np.array([-1.5, 1.5]),
        ).scale(0.5)
        axes.set_color(BLACK)

        self.play(copyright_txt.animate.rotate(angle=190, axis=RIGHT).rotate(angle=PI / 4, axis=OUT))
        self.play(copyright_txt.animate.move_to(np.array([4, 4, -3.3])))
        axes.move_to(np.array([-2, -2, -1]))  # 将坐标系放置在右下角
        self.play(Create(axes))

        # 绘制向量
        vec1 = Arrow(start=axes.c2p(0, 0, 0), end=axes.c2p(1, 0, 0), color=RED, buff=0)
        vec2 = Arrow(start=axes.c2p(0, 0, 0), end=axes.c2p(0, 1, 0), color=YELLOW, buff=0)
        vec3 = Arrow(start=axes.c2p(0, 0, 0), end=axes.c2p(0, 0, 1), color=BLUE, buff=0)

        self.play(Write(vec1))
        self.wait(2)
        self.play(Write(vec2))
        self.wait(2)
        self.play(Write(vec3))
        x1.next_to(axes.get_center() + np.array([3.3, 0, 0]), DOWN).rotate(angle=PI / 2, axis=RIGHT).rotate(
            angle=PI / 4, axis=OUT)
        x2.next_to(axes.get_center() + np.array([0, 3.4, 0]), DOWN).rotate(angle=PI / 2, axis=RIGHT).rotate(
            angle=PI / 4, axis=OUT)
        z.next_to(axes.get_center() + np.array([0, 0, 1.7]), OUT).rotate(angle=PI / 2, axis=RIGHT).rotate(angle=PI / 4,
                                                                                                          axis=OUT)
        self.play(Write(x1), Write(x2), Write(z))
        self.wait(2)


class MatrixRepresentationOfTransformations3D(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=10,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED}).scale(1.3)
        self.play(copyright_txt.animate.rotate(angle=190, axis=RIGHT).rotate(angle=PI / 4, axis=OUT))
        self.play(copyright_txt.animate.move_to(np.array([4, 4, -3.3])))
        text1 = Text("Benzene |1,0,0|", font="KaiTi", font_size=20, color=BLACK)
        text2 = Text("is |0,1,0|", font="KaiTi", font_size=20, color=BLACK)
        text3 = Text("flammable |0,0,1|", font="KaiTi", font_size=20, color=BLACK)
        text1.move_to(np.array([-4, -4, 3]))
        text2.move_to(np.array([-2, -2, 3]))
        text3.move_to(np.array([0, 0, 3]))
        self.play(Write(text1))
        self.play(text1.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.play(Write(text2))
        self.play(text2.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.play(Write(text3))
        self.play(text3.animate.rotate(angle=190, axis=RIGHT).rotate(angle=45, axis=OUT))
        self.wait(2)
        # 创建三维坐标系
        axes = ThreeDAxes()
        axes.scale(0.5)
        axes.set_color(BLACK)

        # 定义基向量 A
        A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # 3个基向量
        v1 = A[:, 0]  # 第一列向量
        v2 = A[:, 1]  # 第二列向量
        v3 = A[:, 2]  # 第三列向量

        # 创建基向量的箭头
        vector_v1 = Arrow3D(start=ORIGIN, end=v1, color=RED)
        vector_v2 = Arrow3D(start=ORIGIN, end=v2, color=GREEN)
        vector_v3 = Arrow3D(start=ORIGIN, end=v3, color=BLUE)

        # 显示三维坐标系和基向量
        self.play(Create(axes), Create(vector_v1), Create(vector_v2), Create(vector_v3))
        self.wait(1)

        # 定义随机向量 M
        M = np.random.rand(3, 3) * 2 - 1  # 生成一个随机矩阵，数值在 -1 到 1 之间


        # 计算 A * M
        AM = np.dot(A, M)

        # 创建变换后的向量
        vector_v1_new = Arrow3D(start=ORIGIN, end=AM[:, 0], color=YELLOW)
        vector_v2_new = Arrow3D(start=ORIGIN, end=AM[:, 1], color=PURPLE)
        vector_v3_new = Arrow3D(start=ORIGIN, end=AM[:, 2], color=ORANGE)

        # 展示 A * M 变换后的向量
        self.play(Transform(vector_v1, vector_v1_new), Transform(vector_v2, vector_v2_new), Transform(vector_v3, vector_v3_new))
        self.wait(1)

        # 目标矩阵 B
        B = np.array([[3, -1, 0], [0, 1, -2], [-3, 0, 2]])

        # 创建调整后的 M
        M_adjusted = B @ np.linalg.inv(A)

        # 计算调整后的矩阵乘积 A * M_adjusted
        AM_adjusted = np.dot(A, M_adjusted)

        # 创建调整后的变换向量
        vector_v1_adjusted = Arrow3D(start=ORIGIN, end=AM_adjusted[:, 0], color=YELLOW)
        vector_v2_adjusted = Arrow3D(start=ORIGIN, end=AM_adjusted[:, 1], color=PURPLE)
        vector_v3_adjusted = Arrow3D(start=ORIGIN, end=AM_adjusted[:, 2], color=ORANGE)

        # 展示调整后的变换
        self.play(Transform(vector_v1, vector_v1_adjusted), Transform(vector_v2, vector_v2_adjusted), Transform(vector_v3, vector_v3_adjusted))
        self.wait(2)
        self.begin_3dillusion_camera_rotation(rate=2)
        self.wait(PI/2)
        self.stop_3dillusion_camera_rotation()
>>>>>>> 5b8332ed00dad7f454433ed9d16cb1d7a4993abb
