from manim import *
import random


class Part1_FeatureExtraction(Scene):
    def construct(self):
        # 1. 开场标题
        title = Text("万物皆矢量", font_size=48).to_edge(UP)
        self.play(Write(title))

        # 2. 出现一些代表“狗”的点
        dogs = VGroup()
        labels = VGroup()
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE]
        dog_names = ["吉娃娃", "金毛", "哈士奇", "泰迪", "牧羊犬"]

        for i in range(5):
            dot = Dot(color=colors[i], radius=0.15)
            # 随机分布在屏幕中央
            dot.move_to(np.array([random.uniform(-3, 3), random.uniform(-2, 2), 0]))
            label = Text(dog_names[i], font_size=20).next_to(dot, UP)
            dogs.add(dot)
            labels.add(label)

        self.play(FadeIn(dogs), Write(labels))
        self.wait(1)

        # 3. 建立一维坐标轴 (体型)
        axes_1d = NumberLine(
            x_range=[0, 10, 1],
            length=10,
            color=BLUE,
            include_numbers=False,
            label_direction=UP,
        ).shift(DOWN * 2)
        axis_label = Text("体型大小", font_size=24).next_to(axes_1d, RIGHT)

        self.play(
            FadeOut(labels),
            Create(axes_1d),
            Write(axis_label),
            dogs.animate.arrange(RIGHT, buff=1.5).shift(UP * 0.5)  # 先排列好
        )

        # 4. 点落到一维坐标上
        # 模拟不同体型：吉娃娃(1) -> 牧羊犬(9)
        positions = [1, 7, 6, 3, 8]
        anims = []
        for i, dot in enumerate(dogs):
            target_x = axes_1d.number_to_point(positions[i])[0]
            anims.append(dot.animate.move_to([target_x, axes_1d.get_y(), 0]))

        self.play(*anims)
        self.wait(1)

        # 5. 发现一维不够，建立二维坐标轴 (增加毛长)
        axes_2d = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        ).shift(DOWN * 0.5)

        x_label = axes_2d.get_x_axis_label("body type")
        y_label = axes_2d.get_y_axis_label("hair length")

        self.play(
            FadeOut(axes_1d), FadeOut(axis_label),
            Create(axes_2d), Write(x_label), Write(y_label)
        )

        # 6. 点移动到二维坐标
        # (体型, 毛长)
        coords = [(1, 2), (7, 8), (6, 5), (3, 6), (8, 4)]
        anims_2d = []
        for i, dot in enumerate(dogs):
            target = axes_2d.c2p(coords[i][0], coords[i][1])
            anims_2d.append(dot.animate.move_to(target))

        self.play(*anims_2d)

        # 7. 总结文本
        conclusion = Text("特征 -> 坐标 -> 向量", font_size=36, color=YELLOW).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)


class Part2_Embeddings(ThreeDScene):
    def construct(self):
        # 1. 3D 坐标系引入
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        text_3d = Text("更多特征 = 更高维度", font_size=30).to_corner(UL)
        self.add_fixed_in_frame_mobjects(text_3d)  # 固定文字不随相机旋转
        self.play(Create(axes), Write(text_3d))

        # 生成一些 3D 点
        dots = VGroup()
        for _ in range(15):
            dot = Dot3D(color=BLUE, radius=0.08)
            dot.move_to(np.array([
                random.uniform(-3, 3),
                random.uniform(-3, 3),
                random.uniform(-3, 3)
            ]))
            dots.add(dot)
        self.play(ShowSubmobjectsOneByOne(dots), run_time=2)

        # 旋转展示高维概念
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2)
        self.stop_ambient_camera_rotation()

        # 2. 切换回 2D 展示 Embedding 过程
        self.play(FadeOut(dots), FadeOut(axes), FadeOut(text_3d))
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)  # 恢复2D视角

        # 案例：图片转向量
        # 用方块代替图片
        img_rect = Square(color=WHITE, fill_opacity=0.5).scale(1).shift(LEFT * 3)
        img_label = Text("图片 / 文本", font_size=24).next_to(img_rect, UP)

        arrow = Arrow(LEFT, RIGHT, color=YELLOW)

        # 向量数组
        vector_vals = DecimalMatrix(
            [[0.2], [0.9], [0.1], [0.5]],
            element_to_mobject_config={"number_config": {"font_size": 24}}
        ).shift(RIGHT * 3)
        vector_label = Text("Embedding (向量)", font_size=24).next_to(vector_vals, UP)

        self.play(
            FadeIn(img_rect), Write(img_label),
            GrowArrow(arrow),
            Write(vector_vals), Write(vector_label)
        )
        self.wait(1)

        # 3. 强调语义相似性 (猫 vs 老鼠 / 警察 vs 小偷)
        self.play(FadeOut(img_rect), FadeOut(img_label), FadeOut(arrow), FadeOut(vector_vals), FadeOut(vector_label))

        # 简单的向量算术可视化
        t1 = Text("语义空间", font_size=36).to_edge(UP)
        self.play(Write(t1))

        # 绘制 King - Man + Woman = Queen 的抽象演示
        vec_start = ORIGIN
        v_king = Arrow(vec_start, [2, 2, 0], buff=0, color=BLUE)
        l_king = Text("King", font_size=20).next_to(v_king.get_end(), UP)

        v_man = Arrow([2, 2, 0], [1, 1, 0], buff=0, color=RED)  # 减去 Man (反向)
        l_man = Text("-Man", font_size=20).next_to(v_man.get_end(), RIGHT)

        v_woman = Arrow([1, 1, 0], [3, 0, 0], buff=0, color=GREEN)
        l_woman = Text("+Woman", font_size=20).next_to(v_woman.get_end(), DOWN)

        v_queen = Arrow(ORIGIN, [3, 0, 0], buff=0, color=PURPLE)
        l_queen = Text("≈ Queen", font_size=20).next_to(v_queen.get_end(), RIGHT)

        self.play(GrowArrow(v_king), Write(l_king))
        self.play(GrowArrow(v_man), Write(l_man))
        self.play(GrowArrow(v_woman), Write(l_woman))
        self.play(GrowArrow(v_queen), Write(l_queen))

        self.wait(2)


class Part5_LSH(Scene):
    def construct(self):
        # 1. 准备随机数据
        dots = VGroup()
        for _ in range(30):
            dots.add(Dot([random.uniform(-5, 5), random.uniform(-3, 3), 0], color=GRAY))
        self.add(dots)

        title = Text("位置敏感哈希 (LSH)", font_size=36).to_edge(UP)
        self.play(Write(title))

        # 2. 第一刀 (Hyperplane 1)
        # 定义线：y = x
        line1 = Line(LEFT * 4 + DOWN * 4, RIGHT * 4 + UP * 4, color=YELLOW)
        label1 = Text("Hash 1", font_size=20, color=YELLOW).next_to(line1, UP)

        self.play(Create(line1), Write(label1))

        # 分类逻辑：线上方为1，下方为0
        code_texts = VGroup()
        for dot in dots:
            x, y, z = dot.get_center()
            code = "1" if y > x else "0"
            t = Text(code, font_size=16, color=YELLOW).next_to(dot, RIGHT, buff=0.05)
            dot.code = code  # 存储哈希值
            dot.code_text = t
            code_texts.add(t)

        self.play(Write(code_texts))
        self.wait(1)

        # 3. 第二刀 (Hyperplane 2)
        # 定义线：y = -x
        line2 = Line(LEFT * 4 + UP * 4, RIGHT * 4 + DOWN * 4, color=BLUE)
        label2 = Text("Hash 2", font_size=20, color=BLUE).next_to(line2, UP)

        self.play(FadeOut(code_texts))  # 先清除旧文字
        self.play(Create(line2), Write(label2))

        # 更新哈希码
        new_code_texts = VGroup()
        buckets = {}  # 用于存储最后的桶

        for dot in dots:
            x, y, z = dot.get_center()
            bit2 = "1" if y > -x else "0"
            dot.code += bit2  # 追加一位，例如 "0" -> "01"

            t = Text(dot.code, font_size=16, color=WHITE).next_to(dot, RIGHT, buff=0.05)
            new_code_texts.add(t)

            # 分桶逻辑
            if dot.code not in buckets:
                buckets[dot.code] = VGroup()
            buckets[dot.code].add(dot)

        self.play(Write(new_code_texts))

        # 4. 碰撞与分桶展示
        self.play(
            FadeOut(dots), FadeOut(line1), FadeOut(line2),
            FadeOut(label1), FadeOut(label2), FadeOut(new_code_texts)
        )

        # 展示桶 (Buckets)
        bucket_viz = VGroup()
        keys = list(buckets.keys())
        for i, key in enumerate(keys):
            # 桶的容器
            rect = Rectangle(width=2, height=3, color=WHITE)
            rect.move_to(LEFT * 4 + RIGHT * 2.5 * i)
            label = Text(f"桶: {key}", font_size=24).next_to(rect, UP)

            # 把点放进去（视觉化）
            group = buckets[key]
            group.arrange_in_grid(cols=3, buff=0.2)
            group.move_to(rect.get_center())
            group.set_color(random_color())  # 每个桶一种颜色

            bucket_viz.add(VGroup(rect, label, group))

        self.play(FadeIn(bucket_viz))

        final_text = Text("哈希值相同 -> 归入同桶 -> 快速候选", font_size=32, color=GREEN).to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)