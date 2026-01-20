from manim import *


class EmbeddingScene(Scene):
    def construct(self):
        # 1. 创建标题
        title = Text("步骤 1: 数据嵌入 (Embedding)", font_size=36).to_edge(UP)
        self.play(Write(title))

        # 2. 左侧：原始数据
        reaction_text = MathTex(r"H_2 + O_2 \rightarrow H_2O", color=BLUE).scale(0.8)
        abstract_text = Text("This study explores water synthesis...", font_size=20, color=GREEN)
        left_group = VGroup(reaction_text, abstract_text).arrange(DOWN, buff=1.5).to_edge(LEFT, buff=1)

        # 3. 中间：模型框
        model_box = Rectangle(width=3, height=2, color=WHITE)
        model_label = Text("AI 嵌入模型\n(Transformer)", font_size=24, fill_color='red').move_to(model_box.get_center())
        model_group = VGroup(model_box, model_label).center()

        # 4. 右侧：向量表示
        vec_1 = Matrix([[0.12], [-0.45], [0.88], ["..."]]).scale(0.6).set_color(BLUE)
        vec_2 = Matrix([[0.15], [-0.42], [0.85], ["..."]]).scale(0.6).set_color(GREEN)
        right_group = VGroup(vec_1, vec_2).arrange(DOWN, buff=1.2).to_edge(RIGHT, buff=1)

        # 5. 动画过程
        self.play(FadeIn(left_group))
        self.wait(1)
        self.play(Create(model_box), Write(model_label))

        # 反应式进入模型并变为向量
        self.play(reaction_text.animate.move_to(model_box.get_left()), rate_func=slow_into)
        self.play(ReplacementTransform(reaction_text, vec_1))

        # 摘要进入模型并变为向量
        self.play(abstract_text.animate.move_to(model_box.get_left()), rate_func=slow_into)
        self.play(ReplacementTransform(abstract_text, vec_2))

        self.wait(2)