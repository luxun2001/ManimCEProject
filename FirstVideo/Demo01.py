from manim import *
import numpy as np


class DemoScene(Scene):
    def construct(self):
        # Copyright text
        copyright_txt = Text('本视频所有信息属于：luxun23@qq.com', font='SimSun', font_size=18,
                             t2c={'所有信息': RED, 'luxun23@qq.com': RED})
        self.play(copyright_txt.animate.to_corner(DR))

        # First test text
        txt = Text('这是一段测试代码', font='SimSun', font_size=80)
        self.play(Write(txt))
        self.play(txt.animate.to_corner(UL))
        self.wait(2)
        self.play(FadeOut(txt))

        # Create initial table data
        data = [
            ['地区', '面积', '价格'],
            ['上海', '2', '20'],
            ['上海', '5', '60'],
            ['南阳', '10', '6'],
            ['南阳', '12', '7'],
        ]

        # Table parameters
        cell_height = 0.8
        cell_width = 1.5
        rows, cols = len(data), len(data[0])

        # Create a VGroup to hold the table
        table1 = VGroup()

        # Create the table
        for row in range(rows):
            for col in range(cols):
                # Create cell
                cell = Rectangle(height=cell_height, width=cell_width)
                cell.move_to(np.array([col * cell_width - (cols * cell_width / 2) + cell_width / 2,
                                       -row * cell_height + (rows * cell_height / 2) - cell_height / 2, 0]))

                # Add text to cell
                txt = Text(data[row][col], font='SimSun', font_size=24)
                txt.move_to(cell.get_center())

                # Add text to cell and cell to table
                cell.add(txt)
                table1.add(cell)

        # Display the table
        self.play(Create(table1))  # Use Create instead of ShowCreation
        self.wait(2)

        # Highlight table cells with yellow stroke
        for i in range(9):  # Assuming table has 9 cells
            point_center = table1[i].get_center()
            table1[i].set_stroke(color=YELLOW, opacity=0.6)
        self.wait(2)

        self.play(FadeOut(table1))

        # New data for the updated table
        new_data = [
            ['地区', '面积', '价格'],
            ['上海', '5', '60'],
            ['南阳', '11', '7.5'],
            ['上海', '5', '60'],
            ['上海', '8', '70'],
            ['南阳', '10', '6'],
            ['南阳', '12', '7'],
            ['南阳', '15', '8'],
            ['上海', '2', '20'],
            ['南阳', '12', '7'],
        ]

        # Create new table
        new_table = VGroup()
        for row in range(len(new_data)):
            for col in range(len(new_data[0])):
                # Create cell
                cell = Rectangle(height=cell_height, width=cell_width)
                cell.move_to(np.array([col * cell_width - (cols * cell_width / 2) + cell_width / 2,
                                       -row * cell_height + (rows * cell_height / 2) - cell_height / 2, 0]))

                # Add text to cell
                txt = Text(new_data[row][col], font='SimSun', font_size=24)
                txt.move_to(cell.get_center())

                # Add text to cell and cell to table
                cell.add(txt)
                new_table.add(cell)

        # Scale and shift the new table
        new_table.scale(0.8)
        new_table.shift(UP * 2)

        # Display new table
        self.play(Create(new_table))  # Use Create instead of ShowCreation
        self.wait(2)
        self.play(FadeOut(new_table))

        # Continue with further texts and operations
        a_txt = Text('我们继续考虑第一种情况', font='SimSun')
        self.play(Write(a_txt))
        self.play(FadeOut(a_txt))

        # Show the first table again
        self.play(Create(table1))  # Use Create instead of ShowCreation
        self.play(table1.animate.to_corner(UL))
        self.wait(2)
        self.play(FadeOut(table1))

        txt2 = Text('现在我们增加更多类似于将上面的数据并且将他们按照面积和价格画到二维坐标系上面', font='SimSun',
                    font_size=24, t2c={'面积': RED, '价格': BLUE})
        self.play(Write(txt2))
        self.play(txt2.animate.to_corner(UL))
        self.play(FadeOut(txt2))
        self.wait(2)

        txt3 = Text('横坐标:面积，纵坐标:价格', font='SimSun', font_size=24, t2c={'面积': RED, '价格': BLUE})
        self.play(Write(txt3))
        self.play(txt3.animate.to_corner(UR))
        self.wait(2)

        # Create axes for the graph
        axes = Axes(
            x_range=(0, 15),
            y_range=(0, 80, 10),
            axis_config={"include_numbers": True}
        )
        self.play(Create(axes))  # Use Create instead of ShowCreation
        self.wait(2)

        # Create some dots for the graph
        upper_dots = VGroup()
        lower_dots = VGroup()

        upper_dot1 = Dot(axes.coords_to_point(2, 20), color=YELLOW)
        upper_dot2 = Dot(axes.coords_to_point(5, 60), color=YELLOW)
        lower_dot1 = Dot(axes.coords_to_point(10, 6), color=RED)
        lower_dot2 = Dot(axes.coords_to_point(12, 7), color=RED)

        upper_dots.add(upper_dot1, upper_dot2)
        lower_dots.add(lower_dot1, lower_dot2)

        self.play(Create(upper_dots))  # Use Create instead of ShowCreation
        self.play(Create(lower_dots))  # Use Create instead of ShowCreation
        self.wait(2)

        # Graph lines (fixing the color issue)
        line1 = axes.plot(lambda x: 5 * x + 1)
        line2 = axes.plot(lambda x: x)

        # Apply color to the graph lines after creation
        line1.set_color(BLUE)
        line2.set_color(PINK)

        self.play(Create(line1))  # Use Create instead of ShowCreation
        self.play(Create(line2))  # Use Create instead of ShowCreation
        self.wait(2)

        # Generate some random other points
        other_dots = VGroup()
        for i in range(10):
            x = np.random.uniform(low=8, high=12)
            y = np.random.uniform(low=4, high=15)
            other_dot = Dot(axes.coords_to_point(x, y), color=RED)
            other_dots.add(other_dot)

        for j in range(10):
            x = np.random.uniform(low=2, high=8)
            y = np.random.uniform(low=20, high=60)
            other_dot = Dot(axes.coords_to_point(x, y), color=YELLOW)
            other_dots.add(other_dot)

        self.play(Create(other_dots))  # Use Create instead of ShowCreation
        self.play(FadeOut(axes))
        self.play(FadeOut(upper_dots))
        self.play(FadeOut(line1))
        self.play(FadeOut(line2))
        self.play(FadeOut(lower_dots))
        self.play(FadeOut(other_dots))
        self.play(FadeOut(txt3))

        # Continue the rest of the scene similarly...

        self.wait(2)


class Meeting(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        # Copyright text
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=18,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED})
        self.play(copyright_txt.animate.to_corner(DR))

        '''开始介绍码的方法'''
        self._start()
        self._explanationsTokenizer()

    def _start(self):
        # 定义文本
        start_text = Text("基于transformer的变形——", color=BLACK)
        midle_text = Text("解码器", t2c={"解码器": BLUE})
        mim_text = Text("和", color=BLACK)
        midle_text2 = Text("编码器", t2c={"编码器": RED})
        # self.add(start_text)
        start_text.move_to(np.array([-3, 0, 0]))

        # 调整位置
        midle_text.next_to(start_text, RIGHT)  # 第二行在第一行下面
        mim_text.next_to(midle_text, RIGHT)  # 第三行在第二行下面
        midle_text2.next_to(mim_text, RIGHT)  # 第四行在第三行下面

        vg1 = VGroup(midle_text, midle_text2)
        # 播放创建动画
        self.play(Create(start_text))
        self.play(Create(mim_text))
        self.play(Create(vg1))

        # 淡出动画
        self.play(FadeOut(start_text), FadeOut(mim_text))

        self.play(vg1.animate.move_to(np.array([0, 0, 0])))

        self.wait(2)
        self.play(FadeOut(vg1))
        text1 = Text("为什么编解码", color=BLACK, t2f={"码": "STXingkai"}, t2c={"码": RED})

        self.play(Transform(vg1, text1))
        self.wait(2)
        self.play(FadeOut(vg1))
        '''第一个做翻译的人'''
        self._explanntion()
        explain_text = Text("就这样将苯和自然界中这个物质联系起来了", color=BLACK, t2w={"苯": BOLD, "这个物质": BOLD},
                            t2c={"苯": YELLOW, "这个物质": RED})
        self.play(FadeIn(explain_text))
        self.wait(2)
        self.play(FadeOut(explain_text))
        firstyaoqiu = Text("1、因为使用的是计算机，因此需要数字化。", color=BLACK, t2c={"数字化": RED})
        secondyaoqiu = Text("2、数据之间是需要有一定关系的。", color=BLACK, t2c={"关系": BLUE}).next_to(firstyaoqiu, DOWN)
        self.play(Create(firstyaoqiu), Create(secondyaoqiu))
        self.play(FadeOut(firstyaoqiu))
        self.play(secondyaoqiu.animate.move_to(firstyaoqiu.get_center()).scale(1.2))
        self.wait(2)
        self.play(FadeOut(secondyaoqiu))

    def _explanntion(self):
        # 小人的头部
        head = Circle(radius=0.5, color=BLACK).shift(UP * 2.5)

        # 小人的身体
        body = Line(start=head.get_bottom(), end=DOWN * 0.5, color=BLACK)

        # 小人的手臂
        left_arm = Line(start=body.get_center(), end=LEFT * 1 + UP * 0.5, color=BLACK)
        right_arm = Line(start=body.get_center(), end=RIGHT * 1 + UP * 0.5, color=BLACK)

        # 小人的腿
        left_leg = Line(start=body.get_end(), end=LEFT * 0.5 + DOWN * 2, color=BLACK)
        right_leg = Line(start=body.get_end(), end=RIGHT * 0.5 + DOWN * 2, color=BLACK)

        # 小人的手指
        hand = right_arm.get_end()  # 获取右手末端位置
        finger = Line(start=hand, end=hand + RIGHT * 0.5, color=YELLOW, buff=1)

        # 创建小人
        stick_figure = VGroup(head, body, left_arm, right_arm, left_leg, right_leg, finger)

        # 小苹果
        apple = ImageMobject(
            filename_or_array=r'D:\manim\data_pro\Demo_01\learning\media\images\Demo01\ketcher.png').scale(0.5).move_to(
            RIGHT * 3)

        # 添加手指指向的箭头
        arrow = Arrow(start=finger.get_end(), end=apple.get_center(), buff=0.1, color=BLUE)

        questions = Text("这个叫什么？", font_size=12)
        questions.next_to(apple, DOWN)
        # 播放动画
        self.play(Create(stick_figure))  # 画出小人
        self.play(FadeIn(apple))  # 显示小苹果
        self.play(Create(questions))
        self.play(Create(arrow))  # 手指指向小苹果

        # 等待观察
        self.wait(2)
        self.play(FadeOut(stick_figure, apple, questions, arrow))

    def _explanationsTokenizer(self):
        dirxs = Text("Tokenizer方法", color=BLACK, t2c={"Tokenizer": RED})
        dirxs.to_corner(UL)
        chem1 = ImageMobject(filename_or_array=r'D:\manim\data_pro\Demo_01\learning\media\images\Demo01\ketcher.png').scale(0.5)
        chem1.next_to(dirxs, DOWN)
        # chem1.align_to(dirxs, RIGHT)
        chem1_vector = MathTex(r"\left |1,0,0  \right | ", color=BLACK)
        chem1_vector.next_to(chem1, RIGHT)
        chem2 = ImageMobject(filename_or_array=r'D:\manim\data_pro\Demo_01\learning\media\images\Demo01\benanze-oh.png').scale(0.5)
        chem2.next_to(chem1, DOWN)
        chem2_vector = MathTex(r"\left |0,1,0  \right | ", color=BLACK)
        chem2_vector.next_to(chem2, RIGHT)
        chem1_vector.align_to(chem2_vector, direction=RIGHT)

        self.play(Write(dirxs))
        self.play(FadeIn(chem1))
        self.play(Write(chem1_vector))
        self.play(FadeIn(chem2))
        self.play(Write(chem2_vector))
        self.wait(3)


class LineMutex(Scene):
    def construct(self):
        # Copyright text
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', font='SimSun', font_size=10,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED})
        self.play(copyright_txt.animate.to_corner(DR))
        self._table_to_axes()
        self._net_work()

    def _table_to_axes(self):
        # 表格数据
        data = [
            ["甲醇", "7", "0.492"],
            ["乙醇", "7", "0.998"],
            ["甲酸", "2.4", "1.22"],
            ["乙酸", "2.4", "1.049"]
        ]

        # 创建表格
        table = Table(
            data,
            col_labels=[Text("类别"), Text("PH"), Text("Density")],  # 列标签
            include_outer_lines=True  # 包括外边框
        )

        # 显示表格
        self.play(Create(table))
        self.wait(2)

        # 添加解释文本
        text = Text("我们将这个表格中的数据映射到坐标轴上", t2c={"坐标轴": RED})
        self.play(Transform(table, text))
        self.wait(2)
        self.play(FadeOut(table))

        # 创建二维坐标轴
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 2, 0.2],
            x_length=6,
            y_length=5,
            tips=True,  # 显示坐标轴箭头
            axis_config={"include_numbers": True},
        )
        # 添加坐标轴标签
        x_label = axes.get_x_axis_label("PH")
        y_label = axes.get_y_axis_label("Density")
        self.play(Create(axes), Write(x_label), Write(y_label))

        # 映射表格数据到坐标轴
        points = [
            {"label": "甲醇", "x": 7, "y": 0.492},
            {"label": "乙醇", "x": 7, "y": 0.998},
            {"label": "甲酸", "x": 2.4, "y": 1.22},
            {"label": "乙酸", "x": 2.4, "y": 1.049},
        ]

        # 添加数据点和标签
        for point in points:
            dot = Dot(axes.c2p(point["x"], point["y"]), color=BLUE)
            label = Text(point["label"], font_size=24).next_to(dot, UP, buff=0.2)
            self.play(Create(dot), Write(label))

        # 等待一会儿以查看结果
        self.wait(2)
        # 绘制分类线
        # 定义函数线 y = ax + b
        line1 = axes.plot(lambda x: 0.2 * x + 0.2, color=GREEN, x_range=[0, 10])  # 第一个分割线
        line2 = axes.plot(lambda x: 0.2 * x, color=YELLOW, x_range=[0, 10])  # 第二个分割线
        line3 = axes.plot(lambda x: 0.15 * x + 0.5, color=PURPLE, x_range=[0, 10])  # 第三个分割线

        # 绘制函数线段
        self.play(Create(line1), Create(line2), Create(line3))

        self.wait(2)

        self.play(FadeOut(line1, line2))

        # 绘制每个点的垂直线段到直线
        for point in points:
            # 点的坐标
            x0, y0 = point["x"], point["y"]
            # 直线的斜率和截距
            a, b = 0.15, 0.5  # line3 的斜率和截距

            # 计算垂直线交点
            x1 = (x0 + a * (y0 - b)) / (1 + a ** 2)
            y1 = a * x1 + b

            # 绘制从数据点到直线交点的线段
            start = axes.c2p(x0, y0)  # 数据点
            end = axes.c2p(x1, y1)  # 垂直交点
            vertical_line = Line(start, end, color=YELLOW)

            # 绘制与交点的连接线
            connecting_line = Line(start, end, color=RED)  # 红色线段表示点到直线的连接

            # 显示垂直线段的长度
            distance = np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)  # 垂直线段长度
            distance_text = Text(f"{distance:.2f}", font_size=18).next_to(connecting_line, RIGHT)

            self.play(Create(connecting_line), Write(distance_text))
            self.wait(2)
        self.wait(2)
        self.clear()
        self._crossLoss()

    def _crossLoss(self):
        # 创建交叉熵公式
        text = Text("交叉熵：", t2c={"交叉": BLUE, "熵": RED}).to_corner(UL)
        cross_entropy_formula = MathTex(
            r"H(p, q) = - \sum_{x} p(x) \log(q(x))"
        ).next_to(text, RIGHT)
        self.play(Write(text), Write(cross_entropy_formula))
        # 定义 x 轴范围
        x_range = np.linspace(-4, 4, 100)

        # 生成高斯分布函数
        def gaussian(x, mean=0, std=1):
            return (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * std ** 2))

        # 计算高斯分布的 y 值
        gaussian_dist = gaussian(x_range)

        # 创建坐标系
        random_graph = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 0.5, 0.1],
            x_length=5,
            y_length=3,
            tips=False,
        ).to_edge(LEFT)

        gaussian_graph = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 0.5, 0.1],
            x_length=5,
            y_length=3,
            tips=False,
        ).to_edge(RIGHT)

        # 绘制右侧的高斯分布
        gaussian_curve = gaussian_graph.plot(lambda x: gaussian(x), x_range=[-5, 5], color=RED)

        # 复制右侧的高斯分布到左侧
        left_gaussian_curve = random_graph.plot(lambda x: gaussian(x * 0.5), x_range=[-5, 5], color=BLUE)

        # 将图像添加到场景中
        self.play(Create(random_graph), Create(gaussian_graph))
        self.play(Create(gaussian_curve), Create(left_gaussian_curve))
        self.wait(2)

        # 动画：使左侧的图形进行左右拉伸
        left_gaussian_stretched = random_graph.plot(lambda x: gaussian(x * 1.5), x_range=[-5, 5], color=BLUE)
        self.play(Transform(left_gaussian_curve, left_gaussian_stretched))
        self.wait(1)

        # 动画：使左侧的图形进行上下拉伸
        left_gaussian_updown = random_graph.plot(lambda x: gaussian(x) * 1.5, x_range=[-5, 5], color=BLUE)
        self.play(Transform(left_gaussian_curve, left_gaussian_updown))
        self.wait(2)

        self.clear()

    def _net_work(self):
        # 创建输入节点（使用圆形）
        input_1 = Circle(radius=0.2, color=RED).move_to(np.array([-4, 1, 0]))
        input_3 = Circle(radius=0.2, color=RED).move_to(np.array([-4, -1, 0]))

        # 创建输出节点（使用圆形）
        output = Circle(radius=0.2, color=GREEN).move_to(np.array([0, 0, 0]))

        # 添加节点标签
        input_1_label = Tex("x1").next_to(input_1, LEFT)
        input_3_label = Tex("x2").next_to(input_3, LEFT)
        output_label = Tex("z").next_to(output, RIGHT)

        # 创建连接线和权重标签
        line1 = Line(input_1.get_center(), output.get_center(), stroke_width=0.5)
        line3 = Line(input_3.get_center(), output.get_center(), stroke_width=0.5)

        weight_label1 = Tex("w1").move_to(line1.get_center() + UP * 0.3)
        weight_label3 = Tex("w2").move_to(line3.get_center() + UP * 0.3)

        out_line = Line(output.get_center(), np.array([4, 0, 0]), stroke_width=0.5)
        out_line_label1 = Tex("sigmoid(z)").move_to(out_line.get_center() + UP * 0.3)

        # 添加公式
        gongshi1 = MathTex(r'z = w1 \cdot x1 + w2 \cdot x2 + b').move_to(UL)

        # 使用self.play创建动画
        # 将所有需要缩小和移动的对象打包到 VGroup 中
        network_group = VGroup(
            input_1, input_3, output,  # 节点
            input_1_label, input_3_label, output_label,  # 节点标签
            line1, line3, out_line,  # 连线
            weight_label1, weight_label3, out_line_label1  # 权重标签和输出标签
        )

        # 对整个网络缩放，并移动到右上角
        network_group.scale(0.5)  # 缩小为原来的 50%
        network_group.to_corner(UR)  # 移动到右上角

        # 动画展示
        self.play(Create(network_group))

        self.wait(2)
        gongshi2 = MathTex(
            r"z = \begin{bmatrix} w_1 & w_2 \end{bmatrix}",
            r"\cdot",
            r"\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}^\top",
            r"+ b"
        )
        # 将原始公式移动到左上角
        self.play(gongshi1.animate.to_corner(UL))
        gongshi2.next_to(gongshi1, DOWN).scale(0.7)
        self.play(Write(gongshi2))
        self.wait(2)
        new_input_1 = Circle(radius=0.2, color=RED).move_to(np.array([-4, 1, 0]))
        new_input_2 = Circle(radius=0.2, color=RED).move_to(np.array([-4, -1, 0]))

        # 创建两个神经元节点（使用圆形）
        new_neuron_1 = Circle(radius=0.2, color=GREEN).move_to(np.array([0, 1, 0]))
        new_neuron_2 = Circle(radius=0.2, color=BLUE).move_to(np.array([0, -1, 0]))

        # 创建输出节点（使用圆形）
        new_output = Circle(radius=0.2, color=YELLOW).move_to(np.array([4, 0, 0]))

        # 添加节点标签
        new_input_1_label = Tex("x1").next_to(new_input_1, LEFT)
        new_input_2_label = Tex("x2").next_to(new_input_2, LEFT)
        new_neuron_1_label = Tex("h1").next_to(new_neuron_1, RIGHT)
        new_neuron_2_label = Tex("h2").next_to(new_neuron_2, RIGHT)
        new_output_label = Tex("z").next_to(new_output, RIGHT)

        # 创建连接线（权重连接）
        new_line1 = Line(new_input_1.get_center(), new_neuron_1.get_center(), stroke_width=0.5)
        new_line2 = Line(new_input_1.get_center(), new_neuron_2.get_center(), stroke_width=0.5)
        new_line3 = Line(new_input_2.get_center(), new_neuron_1.get_center(), stroke_width=0.5)
        new_line4 = Line(new_input_2.get_center(), new_neuron_2.get_center(), stroke_width=0.5)

        # 权重标签
        new_w1_label = Tex("w1").move_to(new_line1.get_center() + UP * 0.3)
        new_w2_label = Tex("w2").move_to(new_line2.get_center() + UP * 0.3)
        new_w3_label = Tex("w3").move_to(new_line3.get_center() + UP * 0.3)
        new_w4_label = Tex("w4").move_to(new_line4.get_center() + UP * 0.3)

        # 输出连接线和标签
        new_out_line1 = Line(new_neuron_1.get_center(), new_output.get_center(), stroke_width=0.5)
        new_out_line2 = Line(new_neuron_2.get_center(), new_output.get_center(), stroke_width=0.5)
        new_out_line_label = Tex("sigmoid(z)").move_to(new_out_line1.get_center() + UP * 0.3)

        # 创建网络的 VGroup
        new_network_group = VGroup(
            new_input_1, new_input_2, new_neuron_1, new_neuron_2, new_output,  # 节点
            new_input_1_label, new_input_2_label, new_neuron_1_label, new_neuron_2_label, new_output_label,  # 标签
            new_line1, new_line2, new_line3, new_line4,  # 连线
            new_w1_label, new_w2_label, new_w3_label, new_w4_label,  # 权重标签
            new_out_line1, new_out_line2, new_out_line_label  # 输出线和标签
        )

        # 将整个神经网络缩放并移动到右上角
        new_network_group.scale(0.5)
        new_network_group.to_corner(UR)

        # 动画展示
        self.play(Transform(network_group, new_network_group))

        self.wait(2)

        gongshi3 = MathTex(
            r"z = \begin{bmatrix} w_{11} & w_{12} \\ w_{21} & w_{22} \end{bmatrix}",
            r"\cdot",
            r"\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}^\top",
            r"+ \begin{bmatrix} b_1 \\ b_2 \end{bmatrix}"
        )
        gongshi3.next_to(gongshi2, DOWN).scale(0.7)
        self.play(Write(gongshi3))
        self.wait(2)
