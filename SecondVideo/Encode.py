from manim import *
import numpy as np

'''
    English：You are free to use my code, but please do not delete my copyright text.
    中文：您可以随意的使用我的代码，但是请使用的同时不要将我的版权说明文本删除掉。
'''

class Encode(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        # Copyright text
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=18,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED})
        self.play(copyright_txt.animate.to_corner(DR))
        self._explanation_()
        text1 = Text("1、因为需要使用计算机来表示，所以必须使用数字化的展示。", color=BLACK, t2c={"数字化": BLUE}).scale(
            0.8)
        text2 = Text("2、数字化展示之后的这些化合物之间需要有一定的关系。", color=BLACK, t2c={"关系": RED}).scale(
            0.8).next_to(text1, DOWN)
        text2.align_to(text1, LEFT)
        self.play(Create(text1), Create(text2))
        self.wait(2)
        self.play(FadeOut(text1))
        self.play(text2.animate.scale(1).move_to(np.array([0, 0, 0])))
        self.wait(3)

    def _explanation_(self):
        # 定义键值对
        items = [
            Text(r"分子量: 78.11 g/mol", color=BLACK),
            Text(r"熔点: 5.5 °C", color=BLACK),
            Text(r"沸点: 80.1 °C", color=BLACK),
            Text(r"密度: 0.8765 g/cm³", color=BLACK),
            Text(r"分子式: C6H6", color=BLACK),
            Text(r"结构: ******", color=BLACK),
            Text(r"…………", color=BLACK)
        ]
        ben_img = ImageMobject(filename_or_array=r'D:\manim\data_pro\Demo_01\learning\media\images\Demo01\ketcher.png')
        # 将键值对竖着排列
        items_group = VGroup(*items).scale(0.5).arrange(DOWN, aligned_edge=LEFT).move_to(np.array([-4, 0, 0]))

        # 创建大括号
        left_brace = Brace(items_group, LEFT, color=BLACK)
        right_brace = Brace(items_group, RIGHT, color=BLACK)

        # 为大括号添加文字说明
        a = Arrow(right_brace.get_center(), np.array([1, 0, 0]), color=BLACK)
        # 大括号上面的陈述
        arrow_text = Text("definition", t2c={"definition": RED}, color=BLACK).scale(0.4)
        arrow_text.next_to(a.get_center() + np.array([-1, 0.4, 0]))

        vg2 = VGroup(
            items_group,
            left_brace,
            right_brace,
            a,
            arrow_text
        )
        ben_img.next_to(a.get_end())
        # 添加到场景中
        self.play(Create(vg2))
        self.play(FadeIn(ben_img))
        self.wait(2)
        self.play(vg2.animate.scale(0.5).to_corner(UL))
        self.play(ben_img.animate.scale(0.5).move_to(a.get_end() + np.array([0.5, 0, 0])))
        self.wait(2)

        # 定义键值对
        new_items = [
            Text(r"分子量: 46.07 g/mol", color=BLACK),
            Text(r"熔点: -114.1 °C", color=BLACK),
            Text(r"沸点: 78.37 °C", color=BLACK),
            Text(r"密度: 0.789 g/cm³", color=BLACK),
            Text(r"分子式: C2H5OH", color=BLACK),
            Text(r"结构: ******", color=BLACK),
            Text(r"…………", color=BLACK)
        ]
        img2 = ImageMobject(filename_or_array=r'D:\manim\data_pro\Demo_01\learning\media\images\Demo01\yichun.png')
        # 将键值对竖着排列
        new_items_group = VGroup(*new_items).scale(0.5).arrange(DOWN, aligned_edge=LEFT).move_to(np.array([-4, 0, 0]))

        # 创建大括号
        new_left_brace = Brace(new_items_group, LEFT, color=BLACK)
        new_right_brace = Brace(new_items_group, RIGHT, color=BLACK)

        # 为大括号添加文字说明
        new_a = Arrow(new_right_brace.get_center(), np.array([1, 0, 0]), color=BLACK)
        # 大括号上面的陈述
        new_arrow_text = Text("definition", t2c={"definition": RED}, color=BLACK).scale(0.4)
        new_arrow_text.next_to(new_a.get_center() + np.array([-1, 0.4, 0]))

        vg3 = VGroup(
            new_items_group,
            new_left_brace,
            new_right_brace,
            new_a,
            new_arrow_text
        )
        img2.next_to(new_a.get_end())
        # 添加到场景中
        self.play(Create(vg3))
        self.play(FadeIn(img2))
        self.wait(2)
        self.play(vg3.animate.scale(0.5).next_to(vg2, DOWN))
        self.play(img2.animate.scale(0.5).move_to(new_a.get_end() + np.array([1, 0, 0])))
        self.wait(2)
        self.clear()


class TokenizerEncode(Scene):

    def construct(self):
        self.camera.background_color = "#ece6e2"
        # Copyright text
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=18,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED})
        self.play(copyright_txt.animate.to_corner(DR))
        self._explanations()
        self.wait(2)

    def _explanations(self):
        token_text = Text("No1. Tokenizer 方法", color=BLACK, font='KaiTi', t2c={"Tokenizer": RED})
        onehot_text = Text("No2. One-Hot 方法", color=BLACK, font='KaiTi', t2c={"One-Hot": RED}).next_to(token_text, DOWN)
        onehot_text.align_to(token_text, LEFT)

        self.play(Write(token_text), Write(onehot_text))
        self.wait(2)
        self.play(Unwrite(onehot_text))
        self.play(token_text.animate.to_corner(UL))
        self.wait(2)
        img1 = ImageMobject(filename_or_array=r'D:\manim\data_pro\Demo_01\learning\media\images\Demo01\yichun.png')
        img1.next_to(token_text, DOWN)
        img1.scale(1)
        img1.align_to(token_text, LEFT)
        img1_text = Tex("1", font_size=40, color=BLACK).next_to(img1, RIGHT)

        img2 = ImageMobject(filename_or_array=r'D:\manim\data_pro\Demo_01\learning\media\images\Demo01\bingchun.png')
        img2.next_to(img1, DOWN)
        img2.scale(2)
        img2.align_to(img1, LEFT)
        img2_text = Tex("2", font_size=40, color=BLACK).next_to(img2, RIGHT)
        self.add(img1)
        self.add(img2)

        self.play(Create(img1_text), Create(img2_text))
        self.wait(2)
        token_line = NumberLine(
            x_range=[0, 9 + 1, 1],
            length=6,
            include_numbers=True,
            include_tip=True,
            color=BLACK,
        )
        # 将所有坐标数值设置为黑色
        for number in token_line.numbers:
            number.set_color(BLACK)

        # 播放坐标轴的创建动画
        self.play(Create(token_line))
        self.wait(0.5)
        point_1_position = token_line.n2p(1)
        point_2_position = token_line.n2p(2)

        # 添加一个加粗的点和标签
        highlighted_dot1 = Dot(point_1_position, color=RED, radius=0.12)
        point_label1 = MathTex("1", color=RED, font_size=36).next_to(highlighted_dot1, UP, buff=0.1)

        highlighted_dot2 = Dot(point_2_position, color=RED, radius=0.12)
        point_label2 = MathTex("2", color=RED, font_size=36).next_to(highlighted_dot2, UP, buff=0.1)

        # 播放动画：显示加粗的点和标签
        self.play(GrowFromCenter(highlighted_dot1), Write(point_label1))
        self.wait(2)
        self.play(GrowFromCenter(highlighted_dot2), Write(point_label2))
        self.wait(2)

        temp_vg = VGroup(
            img1_text,
            img2_text
        )
        # 显示关系: |2-1|=2
        abs_equation = MathTex(r"|2-1|=1", color=BLACK, font_size=48)
        ex_brace = Brace(temp_vg, RIGHT, color=BLACK)
        abs_equation.next_to(ex_brace, RIGHT)
        self.play(Create(ex_brace))
        self.play(Write(abs_equation))
        self.wait(1)

        # 显示不等式 r <= 4
        inequality = MathTex(r"r \leq 4", color=BLACK, font_size=48)
        inequality.next_to(token_line, DOWN)
        self.play(Write(inequality))
        self.wait(1)

        # 添加结论: "则为大"
        conclusion = Text("则关系较近", font="KaiTi", color=RED, font_size=48)
        conclusion.next_to(inequality, DOWN, buff=0.5)  # 将文本放在不等式下方

        # 显示结论
        self.play(Write(conclusion))
        self.wait(2)

        img3 = ImageMobject(filename_or_array=r'D:\manim\data_pro\Demo_01\learning\media\images\Demo01\jiajiyimi.png')
        img3.next_to(img2, DOWN)
        img3.scale(2)
        img3.align_to(img2, LEFT)
        img3_text = Tex("1000", font_size=40, color=BLACK).next_to(img3, RIGHT)
        self.play(FadeIn(img3))
        self.play(Write(img3_text))
        self.wait(2)

        self.clear()


class onehotEncoder(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=10,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED}).scale(1.3)
        token_text = Text("No1. Tokenizer 方法", color=BLACK, font='KaiTi', t2c={"Tokenizer": RED})
        onehot_text = Text("No2. One-Hot 方法", color=BLACK, font='KaiTi', t2c={"One-Hot": RED}).next_to(token_text, DOWN)
        onehot_text.align_to(token_text, LEFT)

        self.play(Write(token_text), Write(onehot_text))
        self.wait(2)
        self.play(Unwrite(token_text))
        self.play(onehot_text.animate.scale(2))
        # self.play(token_text.animate.to_corner(UL))
        self.wait(2)
        self.play(Unwrite(onehot_text))
        x1 = MathTex("x", color=BLACK)
        x2 = MathTex("y", color=BLACK)
        z = MathTex("z", color=BLACK)

        img1 = ImageMobject(filename_or_array=r'D:\manim\data_pro\Demo_01\learning\media\images\Demo01\yichun.png').rotate(angle=190, axis=RIGHT).rotate(angle=PI / 5, axis=OUT)
        img1_vec = MathTex(r'|1, 0, 0|', color=BLACK).rotate(angle=190, axis=RIGHT).rotate(angle=PI / 4, axis=OUT)
        img1_vec.scale(0.6)
        img1.scale(0.6)
        img2 = ImageMobject(filename_or_array=r'D:\manim\data_pro\Demo_01\learning\media\images\Demo01\bingchun.png').rotate(angle=190, axis=RIGHT).rotate(angle=PI / 5, axis=OUT)
        img2_vec = MathTex(r'|0, 1, 0|', color=BLACK).rotate(angle=190, axis=RIGHT).rotate(angle=PI / 4, axis=OUT)
        img2_vec.scale(0.6)
        # img2.scale(0.8)
        img3 = ImageMobject(filename_or_array=r'D:\manim\data_pro\Demo_01\learning\media\images\Demo01\jiajiyimi.png').rotate(angle=190, axis=RIGHT).rotate(angle=PI / 5, axis=OUT)
        img3_vec = MathTex(r'|0, 0, 1|', color=BLACK).rotate(angle=190, axis=RIGHT).rotate(angle=PI / 4, axis=OUT)
        img3_vec.scale(0.6)
        # img3.scale(0.8)
        # 创建三维坐标系
        axes = ThreeDAxes(
            x_range=np.array([-4, 4]),
            y_range=np.array([-4, 4]),
            z_range=np.array([-4, 4]),
        ).scale(0.6)
        axes.set_color(BLACK)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.play(copyright_txt.animate.rotate(angle=190, axis=RIGHT).rotate(angle=PI / 4, axis=OUT))
        self.play(copyright_txt.animate.move_to(np.array([4, 4, -3.3])))
        axes.move_to(np.array([-3, -3, -2]))  # 将坐标系放置在右下角
        self.play(Create(axes))
        # 图片和向量设置模块，自己理解一下
        img1.move_to(np.array([-4, -4, 3]))
        img1_vec.move_to(np.array([-3.1, -3.1, 3]))
        img2.move_to(np.array([-4, -4, 2]))
        img2_vec.move_to(np.array([-3.1, -3.1, 2]))
        img3.move_to(np.array([-4, -4, 1]))
        img3_vec.move_to(np.array([-3.1, -3.1, 1]))

        # 绘制向量
        vec1 = Arrow(start=axes.c2p(0, 0, 0), end=axes.c2p(1, 0, 0), color=RED, buff=0)
        vec2 = Arrow(start=axes.c2p(0, 0, 0), end=axes.c2p(0, 1, 0), color=RED, buff=0)
        vec3 = Arrow(start=axes.c2p(0, 0, 0), end=axes.c2p(0, 0, 1), color=RED, buff=0)

        # 播放图片、向量标签和向量的动画
        self.play(FadeIn(img1), Write(img1_vec))
        self.wait(2)
        self.play(Write(vec1))
        self.play(FadeIn(img2), Write(img2_vec))
        self.wait(2)
        self.play(Write(vec2))
        self.play(FadeIn(img3), Write(img3_vec))
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
