from manim import *


class VectorSpaceScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # 1. 标题
        title = Text("步骤 2: 向量空间与相似度计算", font_size=30).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)

        # 2. 随机背景点（代表数据库中的其他数据）
        import numpy as np
        dots = VGroup(*[Dot3D(point=[np.random.uniform(-3, 3), np.random.uniform(-3, 3), np.random.uniform(-3, 3)],
                              radius=0.05, color=GRAY) for _ in range(20)])
        self.play(FadeIn(dots))

        # 3. 目标点：反应向量与文献向量
        dot_reaction = Dot3D(point=[-2, 2, 1], color=BLUE, radius=0.15)
        label_reaction = Text("化学反应向量", font_size=20).next_to(dot_reaction, UP)

        dot_paper = Dot3D(point=[2, -2, -1], color=GREEN, radius=0.15)
        label_paper = Text("文献摘要向量", font_size=20).next_to(dot_paper, DOWN)

        self.play(Create(dot_reaction), Create(dot_paper))
        self.add_fixed_in_frame_mobjects(label_reaction, label_paper)  # 标签保持平面

        # 4. 相似度计算：让它们靠拢
        self.wait(1)
        line = Line(dot_reaction.get_center(), dot_paper.get_center(), color=YELLOW)
        dist_text = Text("计算余弦相似度...", font_size=24, color=YELLOW).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(dist_text)

        self.play(Create(line))
        self.play(
            dot_reaction.animate.move_to([0.5, 0.5, 0.5]),
            dot_paper.animate.move_to([0.6, 0.4, 0.6]),
            line.animate.scale(0.1),
            run_time=3
        )

        match_text = Text("匹配成功 (98%)", font_size=30, color=GOLD).to_edge(DOWN)
        self.remove(dist_text)
        self.add_fixed_in_frame_mobjects(match_text)
        self.play(Write(match_text))
        self.wait(2)