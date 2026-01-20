from manim import *


class ReconstructionScene(Scene):
    def construct(self):
        title = Text("步骤 3: 自动化重建数据关联", font_size=36).to_edge(UP)
        self.play(Write(title))

        # 1. 左侧：反应列表
        reactions = VGroup(*[Text(f"反应数据 {i}", font_size=24) for i in range(1, 4)]).arrange(DOWN, buff=1)
        reactions.to_edge(LEFT, buff=1.5)

        # 2. 右侧：DOI 文献列表
        dois = VGroup(*[Text(f"DOI: 10.1021/jx00{i}", font_size=20) for i in range(1, 4)]).arrange(DOWN, buff=1)
        dois.to_edge(RIGHT, buff=1.5)

        self.play(FadeIn(reactions), FadeIn(dois))

        # 3. 扫描与连接动画
        for i in range(3):
            # 模拟扫描效果
            scan_line = Line(reactions[i].get_right(), dois[i].get_left(), color=YELLOW_A).set_stroke(width=2)
            self.play(Create(scan_line), run_time=0.5)

            # 确定连接
            final_link = Line(reactions[i].get_right(), dois[i].get_left(), color=GOLD).set_stroke(width=4)
            self.play(ReplacementTransform(scan_line, final_link), reactions[i].animate.set_color(GOLD))
            self.play(Indicate(dois[i], color=GOLD))

        # 4. 总结
        summary = Text("实现化学知识图谱的自动补全", font_size=30, color=BLUE).to_edge(DOWN, buff=1)
        self.play(Write(summary))
        self.wait(3)