from manim import *
import numpy as np


class ClusteringAlgorithms(Scene):
    def construct(self):

        # Copyright text
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=18,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED})
        self.play(copyright_txt.animate.to_corner(DR))

        # =========== 第一部分：聚类算法概述 ===========
        title = Text("聚类算法", font_size=42, color=BLUE)
        title.to_edge(UP, buff=0.5)

        subtitle = Text("将相似的数据点分组", font_size=28, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.3)

        self.play(Write(title))
        self.wait(0.3)
        self.play(Write(subtitle))
        self.wait(1)

        # 聚类算法类型
        algorithm_types = VGroup(
            Text("• 基于划分: K-means", font_size=26, color=GREEN),
            Text("• 基于层次: 层次聚类", font_size=26, color=YELLOW),
            Text("• 基于密度: DBSCAN", font_size=26, color=RED),
            Text("• 基于模型: 高斯混合模型", font_size=26, color=PURPLE)
        )
        algorithm_types.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        algorithm_types.next_to(subtitle, DOWN, buff=0.8)

        for item in algorithm_types:
            self.play(Write(item))
            self.wait(0.2)
        self.wait(1)

        # 淡出概述部分
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(algorithm_types)
        )
        self.wait(0.5)

        # =========== 第二部分：K-means算法 ===========
        kmeans_title = Text("K-means聚类", font_size=36, color=GREEN)
        kmeans_title.to_edge(UP, buff=0.5)

        kmeans_steps = VGroup(
            Text("1. 随机选择K个中心点", font_size=24),
            Text("2. 将每个点分配到最近的中心点", font_size=24),
            Text("3. 重新计算每个簇的中心点", font_size=24),
            Text("4. 重复2-3直到收敛", font_size=24)
        )
        kmeans_steps.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        kmeans_steps.next_to(kmeans_title, DOWN, buff=0.8).to_edge(LEFT, buff=1)

        self.play(Write(kmeans_title))
        self.wait(0.5)

        for step in kmeans_steps:
            self.play(Write(step))
            self.wait(0.2)

        # 创建数据集
        np.random.seed(42)
        data_points = []
        colors = [BLUE, GREEN, RED]

        # 生成三个簇的数据
        centers = [[-2, 1, 0], [2, -1, 0], [0, 2, 0]]
        scales = [0.5, 0.6, 0.7]

        for i in range(3):
            for _ in range(15):
                point = np.random.normal(centers[i], scales[i], 3)
                dot = Dot(point=point, radius=0.06, color=GRAY)
                data_points.append(dot)

        points_group = VGroup(*data_points)
        points_group.move_to(ORIGIN).shift(RIGHT * 1.5)

        self.play(FadeIn(points_group, scale=0.8))
        self.wait(1)

        # 初始中心点
        k = 3
        initial_centers = []
        for i in range(k):
            center_dot = Dot(
                point=np.random.uniform([-1, -1, 0], [1, 1, 0]),
                radius=0.12,
                color=colors[i]
            )
            center_dot.move_to(points_group.get_center() + np.random.uniform(-2, 2, 3))
            initial_centers.append(center_dot)

        centers_group = VGroup(*initial_centers)

        # 显示初始中心点
        self.play(LaggedStart(*[GrowFromCenter(center) for center in initial_centers]))
        self.wait(1)

        # 分配点到最近的簇
        for iteration in range(3):  # 迭代3次
            # 清空前一次的连接线
            if hasattr(self, 'cluster_lines'):
                self.play(FadeOut(self.cluster_lines))

            # 分配点到最近的簇
            cluster_lines = VGroup()
            clusters = [[] for _ in range(k)]

            for point in data_points:
                distances = []
                for center in initial_centers:
                    dist = np.linalg.norm(point.get_center() - center.get_center())
                    distances.append(dist)

                closest_cluster = np.argmin(distances)
                clusters[closest_cluster].append(point)

                # 创建连接线（仅第一次迭代显示）
                if iteration == 0:
                    line = Line(
                        point.get_center(),
                        initial_centers[closest_cluster].get_center(),
                        stroke_width=1,
                        color=colors[closest_cluster],

                    )
                    cluster_lines.add(line)

            if iteration == 0:
                self.cluster_lines = cluster_lines
                self.play(Create(cluster_lines), run_time=2)

            # 重新计算中心点
            new_centers = []
            for i in range(k):
                if clusters[i]:
                    cluster_points = [point.get_center() for point in clusters[i]]
                    new_center = np.mean(cluster_points, axis=0)

                    # 移动中心点到新位置
                    arrow = Arrow(
                        initial_centers[i].get_center(),
                        new_center,
                        color=colors[i],
                        stroke_width=2,
                        buff=0
                    )

                    self.play(
                        GrowArrow(arrow),
                        initial_centers[i].animate.move_to(new_center)
                    )
                    self.play(FadeOut(arrow))

                    # 为点着色
                    for point in clusters[i]:
                        self.play(point.animate.set_color(colors[i]), run_time=0.01)

            self.wait(0.5)

        self.wait(1)

        # 淡出K-means部分
        self.play(
            FadeOut(kmeans_title),
            FadeOut(kmeans_steps),
            FadeOut(points_group),
            FadeOut(centers_group)
        )
        if hasattr(self, 'cluster_lines'):
            self.play(FadeOut(self.cluster_lines))
        self.wait(0.5)

        # =========== 第三部分：层次聚类 ===========
        hierarchical_title = Text("层次聚类", font_size=36, color=YELLOW)
        hierarchical_title.to_edge(UP, buff=0.5)

        hierarchical_steps = VGroup(
            Text("• 自底向上：每次合并最相似的两个簇", font_size=24),
            Text("• 自顶向下：每次分裂最大的簇", font_size=24),
            Text("• 生成树状图（Dendrogram）", font_size=24)
        )
        hierarchical_steps.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        hierarchical_steps.next_to(hierarchical_title, DOWN, buff=0.8).to_edge(LEFT, buff=1)

        self.play(Write(hierarchical_title))
        self.wait(0.5)

        for step in hierarchical_steps:
            self.play(Write(step))
            self.wait(0.2)

        # 创建更简单的数据集用于层次聚类可视化
        simple_points = []
        for i in range(6):
            point = Dot(point=[i - 2.5, np.random.uniform(-1, 1), 0], radius=0.08)
            point.set_color(WHITE)
            simple_points.append(point)

        points_vgroup = VGroup(*simple_points)
        points_vgroup.shift(RIGHT * 2)

        self.play(FadeIn(points_vgroup))
        self.wait(0.5)

        # 创建树状图
        dendrogram_x = 0  # 树状图的x位置
        leaf_y = -2  # 叶子的y位置

        # 初始点作为叶子
        leaves = []
        for i, point in enumerate(simple_points):
            leaf = Dot(point=[dendrogram_x, leaf_y + i, 0], radius=0.05, color=WHITE)
            leaves.append(leaf)

            # 连接到原始点
            line = Line(
                leaf.get_center(),
                point.get_center(),
                stroke_width=1,
                color=WHITE
            )
            self.play(Create(line), FadeIn(leaf), run_time=0.3)

        # 逐步合并簇 - 修复部分
        current_level = leaves.copy()
        level_height = leaf_y

        # 定义合并序列 - 修复：使用正确的索引
        merge_sequence = []
        while len(current_level) > 1:
            # 每次合并最接近的两个点（简化：合并第一个和第二个）
            if len(current_level) >= 2:
                merge_sequence.append((0, 1))
                # 创建新节点
                level_height += 1
                node_pos = np.mean([
                    current_level[0].get_center(),
                    current_level[1].get_center()
                ], axis=0)
                node_pos[1] = level_height

                # 创建新节点
                node = Dot(point=node_pos, radius=0.06, color=YELLOW)

                # 创建连接线
                line1 = Line(current_level[0].get_center(), node_pos, color=YELLOW)
                line2 = Line(current_level[1].get_center(), node_pos, color=YELLOW)

                # 动画
                self.play(
                    Create(line1),
                    Create(line2),
                    GrowFromCenter(node)
                )

                # 更新当前层
                new_level = []
                for idx in range(2, len(current_level)):
                    new_level.append(current_level[idx])
                new_level.append(node)
                current_level = new_level

                # 为原始点着色
                color = YELLOW if len(current_level) > 2 else GOLD
                self.play(
                    simple_points[0].animate.set_color(color),
                    simple_points[1].animate.set_color(color)
                )

                self.wait(0.3)

        self.wait(1)

        # 淡出层次聚类部分
        self.play(
            FadeOut(hierarchical_title),
            FadeOut(hierarchical_steps),
            FadeOut(points_vgroup),
            FadeOut(VGroup(*leaves))
        )
        # 淡出所有线条
        for mob in self.mobjects:
            if isinstance(mob, Line):
                self.play(FadeOut(mob))
        self.clear()
        self.wait(0.5)


        # Copyright text
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=18,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED})
        self.play(copyright_txt.animate.to_corner(DR))

        # =========== 第四部分：DBSCAN聚类 ===========
        dbscan_title = Text("DBSCAN (基于密度的聚类)", font_size=36, color=RED)
        dbscan_title.to_edge(UP, buff=0.5)

        dbscan_explanation = VGroup(
            Text("• 边界点：在核心点的邻域内", font_size=22),
            Text("• 噪声点：既不是核心点也不是边界点", font_size=22)
        )
        dbscan_explanation.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        dbscan_explanation.next_to(dbscan_title, DOWN, buff=0.8).to_edge(LEFT, buff=1)

        self.play(Write(dbscan_title))
        self.wait(0.5)

        for item in dbscan_explanation:
            self.play(Write(item))
            self.wait(0.2)

        # 创建DBSCAN数据集
        dbscan_points = []

        # 创建三个密集区域
        cluster_centers = [[-2, 0, 0], [0, 1, 0], [2, -1, 0]]

        for center in cluster_centers:
            for _ in range(12):
                point = np.random.normal(center, 0.4, 3)
                dot = Dot(point=point, radius=0.06, color=WHITE)
                dbscan_points.append(dot)

        # 添加一些噪声点
        for _ in range(8):
            point = np.random.uniform([-3, -2, 0], [3, 2, 0])
            dot = Dot(point=point, radius=0.06, color=WHITE)
            dbscan_points.append(dot)

        dbscan_group = VGroup(*dbscan_points)
        dbscan_group.shift(RIGHT * 2)

        self.play(FadeIn(dbscan_group))
        self.wait(0.5)

        # 演示邻域概念
        eps_radius = 0.8
        min_pts = 4

        # 选择一个核心点
        core_point_idx = 5  # 从第一个簇中选一个点
        core_point = dbscan_points[core_point_idx]

        # 绘制邻域圆
        neighborhood_circle = Circle(
            radius=eps_radius,
            color=YELLOW,
            stroke_width=2
        )
        neighborhood_circle.move_to(core_point.get_center())

        self.play(
            core_point.animate.set_color(RED),
            Create(neighborhood_circle)
        )

        # 计算邻域内的点
        points_in_neighborhood = []
        for i, point in enumerate(dbscan_points):
            if i != core_point_idx:
                dist = np.linalg.norm(point.get_center() - core_point.get_center())
                if dist <= eps_radius:
                    points_in_neighborhood.append(point)

        # 高亮邻域内的点
        highlight_anims = []
        for point in points_in_neighborhood[:min_pts - 1]:
            highlight_anims.append(point.animate.set_color(GREEN))

        # 检查是否为核心点
        if len(points_in_neighborhood) >= min_pts - 1:
            core_text = Text("核心点", font_size=24, color=GREEN)
            core_text.next_to(core_point, UP, buff=0.1)
            self.play(Write(core_text))
            self.play(*highlight_anims)
        else:
            core_text = Text("非核心点", font_size=24, color=RED)
            core_text.next_to(core_point, UP, buff=0.1)
            self.play(Write(core_text))

        self.wait(1)

        # 演示密度可达的概念
        # 选择另一个核心点
        second_core_idx = 20  # 从第二个簇中选一个点
        second_core = dbscan_points[second_core_idx]

        second_circle = Circle(
            radius=eps_radius,
            color=BLUE,
            stroke_width=2
        )
        second_circle.move_to(second_core.get_center())

        # 连接两个核心点
        connection_line = DashedLine(
            core_point.get_center(),
            second_core.get_center(),
            color=WHITE,
            stroke_width=2
        )

        self.play(
            FadeOut(core_text),
            second_core.animate.set_color(BLUE),
            Create(second_circle),
            Create(connection_line)
        )

        self.wait(1)

        # 演示DBSCAN聚类结果
        self.play(
            FadeOut(neighborhood_circle),
            FadeOut(second_circle),
            FadeOut(connection_line)
        )

        # 为簇着色
        cluster_colors = [PURPLE, ORANGE, PINK]
        cluster_indices = [
            list(range(12)),  # 第一个簇
            list(range(12, 24)),  # 第二个簇
            list(range(24, 36)),  # 第三个簇
            list(range(36, 44))  # 噪声点（保持白色）
        ]

        for i, indices in enumerate(cluster_indices):
            color = cluster_colors[i] if i < 3 else WHITE
            for idx in indices:
                if idx < len(dbscan_points):
                    self.play(dbscan_points[idx].animate.set_color(color), run_time=0.01)

        # 添加噪声点标签
        noise_text = Text("噪声点", font_size=20, color=GRAY)
        noise_text.next_to(dbscan_group, DOWN, buff=0.3)
        self.play(Write(noise_text))

        self.wait(1)

        # =========== 第五部分：算法比较和总结 ===========
        self.play(
            FadeOut(dbscan_title),
            FadeOut(dbscan_explanation),
            FadeOut(dbscan_group),
            FadeOut(noise_text)
        )

        # 创建算法比较表
        comparison_title = Text("聚类算法比较", font_size=38, color=GOLD)
        comparison_title.to_edge(UP, buff=0.5)

        # 表头
        table_header = VGroup(
            Text("算法", font_size=28, color=YELLOW),
            Text("优点", font_size=28, color=GREEN),
            Text("缺点", font_size=28, color=RED)
        ).arrange(RIGHT, buff=1.5)
        table_header.next_to(comparison_title, DOWN, buff=0.8)

        # 表格内容
        table_rows = [
            ("K-means", "简单高效，适用于凸形簇", "需要指定K，对异常值敏感"),
            ("层次聚类", "无需指定K，可形成层次结构", "计算复杂度高，难以处理大数据"),
            ("DBSCAN", "可发现任意形状簇，抗噪声", "对参数敏感，密度不均时效果差")
        ]

        table_content = VGroup()
        for i, (algo, pro, con) in enumerate(table_rows):
            row = VGroup(
                Text(algo, font_size=24, color=WHITE),
                Text(pro, font_size=22, color=GREEN),
                Text(con, font_size=22, color=RED)
            ).arrange(RIGHT, buff=1.5)
            row.next_to(table_header, DOWN, buff=0.5 + i * 0.7)
            table_content.add(row)

        self.play(Write(comparison_title))
        self.wait(0.3)
        self.play(Write(table_header))
        self.wait(0.3)

        for row in table_content:
            self.play(Write(row))
            self.wait(0.2)

        self.wait(2)

        # 最终总结
        final_title = Text("聚类算法总结", font_size=36, color=BLUE)
        final_title.to_edge(UP, buff=0.5)

        summary_points = VGroup(
            Text("• 聚类是无监督学习的重要方法", font_size=26),
            Text("• 不同算法适用于不同场景", font_size=26),
            Text("• 选择合适的算法和参数至关重要", font_size=26),
            Text("• 广泛应用于市场细分、社交网络分析、图像分割等", font_size=26)
        )
        summary_points.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary_points.next_to(final_title, DOWN, buff=0.8)

        self.play(
            FadeOut(comparison_title),
            FadeOut(table_header),
            FadeOut(table_content),
            Write(final_title)
        )

        for point in summary_points:
            self.play(Write(point))
            self.wait(0.2)

        self.wait(3)

        # 淡出所有
        self.play(FadeOut(final_title), FadeOut(summary_points))
        self.wait(0.5)

# 运行方式：
# manim -pql clustering.py ClusteringAlgorithms
# manim -pqh clustering.py ClusteringAlgorithms