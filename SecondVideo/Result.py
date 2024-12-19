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
from learning.tool import get_point_by_arc

'''
    English：You are free to use my code, but please do not delete my copyright text.
    中文：您可以随意的使用我的代码，但是请使用的同时不要将我的版权说明文本删除掉。
'''


class Result(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        # Copyright text
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=18,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED})
        self.play(copyright_txt.animate.to_corner(DR))
        self.wait(2)
        self._explanations()

    def _explanations(self):
        ball1 = CreateBall(10)
        ball2 = CreateBall(10)
        ball3 = CreateBall(10)
        ball4 = CreateBall(10)
        ball5 = CreateBall(10)

        ball1.to_edge(LEFT)
        ball2.next_to(ball1, RIGHT)
        ball3.next_to(ball2, RIGHT)
        ball4.next_to(ball3, RIGHT)
        ball5.next_to(ball4, RIGHT)
        vg_ball = VGroup(
            ball1,
            ball2,
            ball3,
            ball4,
            ball5,
        ).scale(0.5)
        vg_ball.move_to(np.array([-4, 1, 0]))
        vg_ball_brace = Brace(vg_ball, DOWN, color=BLACK)

        rect = Rectangle(width=4.0, height=0.7)
        rect.set_color(BLACK)
        rect.next_to(vg_ball_brace, DOWN)
        rect_text = Text('Encoder', font="KaiTi", font_size=18, color=BLACK)
        rect_text.move_to(rect.get_center())

        arrow_left = Arrow(start=rect.get_center() + np.array([0, -2, 0]), end=rect.get_center() + np.array([0, -0.8, 0]),
                           color=BLACK, buff=0)
        arrow_left_text = Text("input text", font="KaiTi", font_size=25, color=BLACK)
        arrow_left_text.next_to(arrow_left, DOWN)

        rect2 = Rectangle(width=4.0, height=0.7)
        rect2.set_color(BLACK)
        rect2.move_to(np.array([1, 3, 0]))
        rect2_text = Text('Cross Attention', font="KaiTi", font_size=20, color=BLACK)
        rect2_text.next_to(rect2.get_center() + np.array([-1, 0, 0]))

        arc1 = ArcBetweenPoints(start=ball1.get_top(), end=rect2.get_left(), color=BLACK, angle=-PI / 2)
        arc2 = ArcBetweenPoints(start=ball2.get_top(), end=rect2.get_left(), color=BLACK, angle=-PI / 2)
        arc3 = ArcBetweenPoints(start=ball3.get_top(), end=rect2.get_left(), color=BLACK, angle=-PI / 2)
        arc4 = ArcBetweenPoints(start=ball4.get_top(), end=rect2.get_left(), color=BLACK, angle=-PI / 2)
        arc5 = ArcBetweenPoints(start=ball5.get_top(), end=rect2.get_left(), color=BLACK, angle=-PI / 2)

        output_rect1 = Rectangle(width=0.5, height=0.5, color=BLACK)
        output_rect2 = Rectangle(width=0.5, height=0.5, color=PINK, fill_color=PINK)
        output_rect3 = Rectangle(width=0.5, height=0.5, color=BLACK)
        output_rect4 = Rectangle(width=0.5, height=0.5, color=BLACK)
        output_rect5 = Rectangle(width=0.5, height=0.5, color=PINK, fill_color=PINK)
        output_rect6 = Rectangle(width=0.5, height=0.5, color=PINK, fill_color=PINK)
        output_rect7 = Rectangle(width=0.5, height=0.5, color=PINK, fill_color=PINK)
        output_rect1.next_to(rect, RIGHT + np.array([4, 0, 0]))
        output_rect2.next_to(output_rect1, RIGHT, buff=0.5)
        output_rect3.next_to(output_rect2, RIGHT, buff=0.5)
        output_rect4.next_to(output_rect3, RIGHT, buff=0.5)
        output_rect5.next_to(output_rect4, RIGHT, buff=0.5)
        output_rect6.next_to(output_rect5, RIGHT, buff=0.5)
        output_rect7.next_to(output_rect6, RIGHT, buff=0.5)
        # 七个小矩形之间的虚线相连
        dashed_1 = DashedLine(output_rect1.get_right(), output_rect2.get_left(), color=BLACK)
        dashed_2 = DashedLine(output_rect2.get_right(), output_rect3.get_left(), color=BLACK)
        dashed_3 = DashedLine(output_rect3.get_right(), output_rect4.get_left(), color=BLACK)
        dashed_4 = DashedLine(output_rect4.get_right(), output_rect5.get_left(), color=BLACK)
        dashed_5 = DashedLine(output_rect5.get_right(), output_rect6.get_left(), color=BLACK)
        dashed_6 = DashedLine(output_rect6.get_right(), output_rect7.get_left(), color=BLACK)

        arc1_t2 = DashedLine(start=rect2.get_bottom() + np.array([-1, 0, 0]), end=dashed_1.get_top(), buff=0, color=BLACK)

        dot_arc = DashedLine(end=rect2.get_left() + np.array([-0.2, 0, 0]), start=output_rect1.get_left(), buff=0, color=BLACK)

        start_rect = Arrow(start=output_rect1.get_bottom() + np.array([0, -0.2, 0]), end=output_rect1.get_bottom(), buff=0, color=BLACK)
        start_rect_text = Text('@start@', font="KaiTi",  color=BLACK, font_size=25)
        start_rect_text.next_to(start_rect, DOWN)

        sec_rect = Arrow(end=output_rect1.get_top() + np.array([0, 0.2, 0]), start=output_rect1.get_top(), buff=0, color=BLACK)
        sec_rect_text = Text('lidocanie', font="KaiTi",  color=BLACK, font_size=18)
        sec_rect_text.next_to(sec_rect, UP)

        drug_rect = Arrow(start=output_rect2.get_bottom() + np.array([0, -1, 0]), end=output_rect2.get_bottom(), buff=0, color=BLACK)
        drug_rect_text = Text('@DRUG@', font="KaiTi",  color=BLACK, font_size=15)
        drug_rect_text.next_to(drug_rect, DOWN)

        thr_rect = Arrow(end=output_rect3.get_top() + np.array([0, 0.2, 0]), start=output_rect3.get_top(), buff=0, color=BLACK)
        thr_rect_text = Text('Card', font="KaiTi",  color=BLACK, font_size=18)
        thr_rect_text.next_to(thr_rect, UP)

        four_rect = Arrow(end=output_rect4.get_top() + np.array([0, 0.2, 0]), start=output_rect4.get_top(), buff=0, color=BLACK)
        four_rect_text = Text('asy', font="KaiTi",  color=BLACK, font_size=18)
        four_rect_text.next_to(four_rect, UP)

        diseated_rect = Arrow(start=output_rect5.get_bottom() + np.array([0, -1, 0]), end=output_rect5.get_bottom(), buff=0, color=BLACK)
        diseated_rect_text = Text('@DISEASE@', font="KaiTi",  color=BLACK, font_size=15)
        diseated_rect_text.next_to(diseated_rect, DOWN)

        cid_rect = Arrow(start=output_rect6.get_bottom() + np.array([0, -1, 0]), end=output_rect6.get_bottom(), buff=0, color=BLACK)
        cid_rect_text = Text('@CID@', font="KaiTi",  color=BLACK, font_size=15)
        cid_rect_text.next_to(cid_rect, DOWN)

        end_rect = Arrow(start=output_rect7.get_bottom() + np.array([0, -1, 0]), end=output_rect7.get_bottom(), buff=0, color=BLACK)
        end_rect_text = Text('@END@', font="KaiTi",  color=BLACK, font_size=15)
        end_rect_text.next_to(end_rect, DOWN)
        # DECODER模块
        self.play(Create(vg_ball))
        self.wait(2)
        self.play(Create(vg_ball_brace))
        self.play(Create(rect))
        self.play(Write(rect_text))
        # Attention模块
        self.play(Create(rect2))
        self.play(Write(rect2_text))

        self.play(Create(output_rect1),
                  Create(output_rect2),
                  Create(output_rect3),
                  Create(output_rect4),
                  Create(output_rect5),
                  Create(output_rect6),
                  Create(output_rect7)
                  )
        self.play(Create(dashed_1),
                  Create(dashed_2),
                  Create(dashed_3),
                  Create(dashed_4),
                  Create(dashed_5),
                  Create(dashed_6),
                  )

        # 首先输入一段文本
        self.play(GrowArrow(arrow_left))
        self.play(Write(arrow_left_text))
        self.wait(2)

        # 经过计算传给注意力机制
        self.play(Create(arc1), Create(arc2), Create(arc3), Create(arc4), Create(arc5))
        self.wait(2)
        self.play(Create(arc1_t2))
        self.play(Create(dot_arc))
        self.wait(2)
        self.play(Create(start_rect), Write(start_rect_text))
        self.wait(2)
        self.play(Create(sec_rect), Write(sec_rect_text))
        self.wait(2)
        self.play(Create(drug_rect), Write(drug_rect_text))
        self.wait(2)
        self.play(Create(thr_rect), Write(thr_rect_text))
        self.wait(2)
        self.play(Create(four_rect), Write(four_rect_text))
        self.wait(2)
        self.play(Create(diseated_rect), Write(diseated_rect_text))
        self.wait(2)
        self.play(Create(cid_rect), Write(cid_rect_text))
        self.wait(2)
        self.play(Create(end_rect), Write(end_rect_text))
        self.wait(2)
