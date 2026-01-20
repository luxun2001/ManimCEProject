from manim import *
import numpy as np


class ChemicalKnowledgeReconstruction(Scene):
    def construct(self):
        # --- 场景 0: 引入问题 (The Data Silo Problem) ---
        title = Text("化学反应数据与文献关系的自动化重建", font_size=40, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP).scale(0.7))

        # 展示两个孤岛
        paper_icon = Rectangle(height=2, width=1.5, color=WHITE).shift(LEFT * 4)
        paper_label = Text("科研文献 (DOI)", font_size=20).next_to(paper_icon, DOWN)
        abstract_text = Text("摘要: '本实验通过...\n合成了聚合物...'", font_size=14).move_to(paper_icon)

        reaction_icon = RoundedRectangle(height=2, width=3, color=BLUE_E).shift(RIGHT * 4)
        reaction_label = Text("化学反应数据库", font_size=20).next_to(reaction_icon, DOWN)
        smiles_text = Text("SMILES: CC(=O)OC1... \nYield: 85%", font_size=14).move_to(reaction_icon)

        self.play(Create(paper_icon), Write(paper_label), FadeIn(abstract_text))
        self.play(Create(reaction_icon), Write(reaction_label), FadeIn(smiles_text))

        question_mark = Text("?", font_size=60, color=RED).move_to(ORIGIN)
        self.play(Write(question_mark))
        self.wait(2)
        self.play(FadeOut(question_mark), FadeOut(abstract_text), FadeOut(smiles_text))

        # --- 场景 1: 化学反应嵌入 (Reaction Embedding) ---
        step1_title = Text("第一阶段: 化学反应向量化 (RXNFP)", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Transform(title, step1_title))

        # 详细展示 SMILES 转化为 向量
        smiles_code = MathTex(r"C_1=CC=C(C=C1)C=O + CH_3NO_2 \rightarrow ...", color=BLUE).scale(0.8)
        smiles_code.move_to(reaction_icon.get_center())

        model_rxn = Rectangle(width=2, height=1.5, color=GREY).move_to(RIGHT * 1)
        model_rxn_label = Text("RXNFP\n模型", font_size=18).move_to(model_rxn)

        reaction_vector = Matrix([[0.1], [0.9], [-0.3], [0.5], ["..."]]).scale(0.5).shift(RIGHT * 4)

        self.play(smiles_code.animate.move_to(LEFT * 2))
        self.play(Create(model_rxn), Write(model_rxn_label))
        self.play(FadeOut(smiles_code))

        arrow1 = Arrow(LEFT * 1, RIGHT * 0)
        self.play(GrowArrow(arrow1))
        self.play(ReplacementTransform(smiles_code.copy(), reaction_vector))
        self.wait(1)

        # --- 场景 2: 文献摘要嵌入 (Text Embedding) ---
        step2_title = Text("第二阶段: 文献摘要语义化 (SciBERT)", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Transform(title, step2_title))

        abstract_content = Text("Abstract: The catalytic condensation\nof benzaldehyde with nitromethane...",
                                font_size=15).move_to(LEFT * 4)
        model_text = Rectangle(width=2, height=1.5, color=GREY).move_to(LEFT * 1)
        model_text_label = Text("SciBERT\n模型", font_size=18).move_to(model_text)

        text_vector = Matrix([[0.12], [0.88], [-0.28], [0.49], ["..."]]).scale(0.5).shift(LEFT * 4 + DOWN * 0.5)
        text_vector.set_color(GREEN)

        self.play(FadeIn(abstract_content))
        self.play(Create(model_text), Write(model_text_label))
        self.play(abstract_content.animate.move_to(model_text.get_left()))
        self.play(ReplacementTransform(abstract_content, text_vector))
        self.wait(2)

        # --- 场景 3: 向量数据库寻址 (Vector Database & Indexing) ---
        self.play(FadeOut(model_rxn), FadeOut(model_rxn_label), FadeOut(model_text), FadeOut(model_text_label),
                  FadeOut(arrow1))
        step3_title = Text("第三阶段: 向量数据库存储与检索", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Transform(title, step3_title))

        # 构建坐标系模拟高维空间
        axes = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3])
        self.play(Create(axes))

        # 将之前的向量转化为空间中的点
        dot_r = Dot3D(point=[1.5, 2, 1], color=BLUE)
        dot_t = Dot3D(point=[1.6, 1.9, 1.1], color=GREEN)
        label_r = Text("反应 A", font_size=15).next_to(dot_r, UP)
        label_t = Text("文献 DOI_X", font_size=15).next_to(dot_t, DOWN)

        self.play(ReplacementTransform(reaction_vector, dot_r), Write(label_r))
        self.play(ReplacementTransform(text_vector, dot_t), Write(label_t))

        # 模拟大量背景数据
        others = VGroup(*[Dot3D(point=[np.random.uniform(-2, 2), np.random.uniform(-2, 2), np.random.uniform(-2, 2)],
                                radius=0.04, color=GRAY, fill_opacity=0.3) for _ in range(50)])
        self.play(FadeIn(others))
        self.wait(1)

        # --- 场景 4: 相似度匹配 (Similarity Calculation) ---
        line = Line(dot_r.get_center(), dot_t.get_center(), color=RED)
        score_label = Variable(0.985, Text("余弦相似度", font_size=20), num_decimal_places=3).to_edge(RIGHT)

        self.play(Create(line), Write(score_label))
        self.play(Indicate(line))
        self.wait(2)

        # --- 场景 5: 结果呈现 (Final Reconstruction) ---
        self.play(FadeOut(axes), FadeOut(others), FadeOut(line), FadeOut(score_label), FadeOut(dot_r), FadeOut(dot_t),
                  FadeOut(label_r), FadeOut(label_t))

        final_title = Text("结果: 自动化重建知识关联", font_size=30, color=GOLD).to_edge(UP)
        self.play(Transform(title, final_title))

        # 展示连接成功的表格样式
        table = Table(
            [["反应 ID: RXN_001", "DOI: 10.1021/abc..."],
             ["反应 ID: RXN_002", "DOI: 10.1038/s41..."],
             ["反应 ID: RXN_003", "DOI: 10.1016/j.j..."]],
            col_labels=[Text("实验数据", font_size=20), Text("对应文献", font_size=20)],
            include_outer_lines=True
        ).scale(0.5)

        self.play(Create(table))

        conclusion = Text("通过向量匹配，我们将孤立的 80% 实验数据重新找回了出处。",
                          font_size=24, color=BLUE_B).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)