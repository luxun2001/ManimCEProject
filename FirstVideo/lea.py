from manim import *
import numpy as np

def CreateNN(in_size, out_size, hidden_layers, hidden_size):
    layer_sizes = [in_size] + [hidden_size] * hidden_layers + [out_size]

    layers = []
    prev_layer = None
    for i, size in enumerate(layer_sizes):
        layer = VGroup(*[Circle(color=PINK, fill_color=LIGHT_PINK, fill_opacity=1, radius=0.15) for _ in range(size)])
        layer.arrange(DOWN, buff=0.7)
        if prev_layer is not None:
            layer.next_to(prev_layer, RIGHT, buff=1.5)
        layers.append(layer)
        prev_layer = layer

    neurons = VGroup(*layers)

    lines = VGroup()
    for i in range(len(layers) - 1):
        for neuron1 in layers[i]:
            for neuron2 in layers[i + 1]:
                line = Line(neuron1.get_center(), neuron2.get_center(), color=PINK, )
                line.z_index = -1
                lines.add(line)

    network = VGroup(neurons, lines).center()

    return network

# 定义sigmoid函数
def sigmoid(x1, x2, w, b):
    raw_output = np.tanh(w[0] * x1 + w[1] * x2 + b)
    return np.where(raw_output > 0, raw_output, 0.6 * raw_output)
    # return np.maximum(0, raw_output)
    # return 1 / (1 + np.exp(-(raw_output)))
    # return raw_output  # 将值限制在坐标系 z 的范围内


class Brace1(ThreeDScene):
    def construct(self):
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', font='SimSun', font_size=10,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED})
        x1 = MathTex("x_1")
        x2 = MathTex("x_2")
        z = MathTex("z")

        # 创建三维坐标系
        axes = ThreeDAxes(
            x_range=np.array([-4, 4]),
            y_range=np.array([-4, 4]),
            z_range=np.array([-4, 4])
        ).scale(0.5)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.play(copyright_txt.animate.rotate(angle=PI / 2, axis=RIGHT).rotate(angle=PI / 4, axis=OUT))
        self.play(copyright_txt.animate.move_to(np.array([4, 4, -3.3])))
        axes.move_to(np.array([-3, -3, 0]))  # 将坐标系放置在右下角
        self.play(Create(axes))
        x1.next_to(axes.get_center() + np.array([3.3, 0, 0]), DOWN).rotate(angle=PI / 2, axis=RIGHT).rotate(angle=PI / 4, axis=OUT)
        x2.next_to(axes.get_center() + np.array([0, 3.4, 0]), DOWN).rotate(angle=PI / 2, axis=RIGHT).rotate(angle=PI / 4, axis=OUT)
        z.next_to(axes.get_center() + np.array([0, 0, 1.7]), OUT).rotate(angle=PI / 2, axis=RIGHT).rotate(angle=PI / 4, axis=OUT)
        self.play(Write(x1), Write(x2), Write(z))
        self.wait(2)

        # 创建网络对象
        net1 = CreateNN(in_size=2, out_size=1, hidden_size=1, hidden_layers=1).scale(0.7).move_to(np.array([2, 3, 0]))
        net5 = CreateNN(in_size=2, out_size=1, hidden_size=5, hidden_layers=1).scale(0.7).move_to(np.array([2, 3, 0]))
        net5.rotate(angle=PI / 2, axis=RIGHT).rotate(angle=PI / 4, axis=OUT)
        net8 = CreateNN(in_size=2, out_size=1, hidden_size=8, hidden_layers=1).scale(0.7).move_to(np.array([2, 3, 0]))
        net8.rotate(angle=PI / 2, axis=RIGHT).rotate(angle=PI / 4, axis=OUT)
        net10 = CreateNN(in_size=2, out_size=1, hidden_size=10, hidden_layers=1).scale(0.7).move_to(np.array([2, 3, 0]))
        net10.rotate(angle=PI / 2, axis=RIGHT).rotate(angle=PI / 4, axis=OUT)

        # 随机生成权重w和偏置b
        w = np.random.uniform(-9, 4, 2)
        b = np.random.uniform(-2, 8)
        # 创建并显示初始平面
        surface = Surface(
            lambda u, v: axes.c2p(u, v, sigmoid(u, v, w, b)),  # 使用随机生成的w和b
            u_range=[-3, 3],  # x1的范围
            v_range=[-3, 3],  # x2的范围
            resolution=(30, 30)
        )
        surface.set_color_by_gradient(BLUE, GREEN, YELLOW)  # 设置渐变色
        self.play(Create(surface))

        self.wait(2)

        # 显示并旋转第一个神经网络
        self.play(Create(net1))
        self.play(net1.animate.rotate(angle=PI / 2, axis=RIGHT))
        self.play(net1.animate.rotate(angle=PI / 4, axis=OUT))
        self.wait(2)

        # 变换net1到net5并改变平面
        self.play(Transform(net1, net5))
        w = np.random.uniform(-8, 2, 2)
        b = np.random.uniform(-2, 8)
        new_surface = Surface(
            lambda u, v: axes.c2p(u, v, sigmoid(u, v, w, b)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30)
        )
        new_surface.set_color_by_gradient(BLUE, GREEN, YELLOW)
        self.play(Transform(surface, new_surface))  # 变换平面
        self.wait(2)

        # 变换net5到net8并改变平面
        self.play(Transform(net1, net8))
        w = np.random.uniform(-10, 4, 2)
        b = np.random.uniform(-2, 8)
        new_surface = Surface(
            lambda u, v: axes.c2p(u, v, sigmoid(u, v, w, b)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30)
        )
        new_surface.set_color_by_gradient(BLUE, GREEN, YELLOW)
        self.play(Transform(surface, new_surface))  # 变换平面
        self.wait(2)

        # 变换net8到net10并改变平面
        self.play(Transform(net1, net10))
        w = np.random.uniform(-21, 4, 2)
        b = np.random.uniform(-2, 8)
        new_surface = Surface(
            lambda u, v: axes.c2p(u, v, sigmoid(u, v, w, b)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30)
        )
        new_surface.set_color_by_gradient(BLUE, GREEN, YELLOW)
        self.play(Transform(surface, new_surface))  # 变换平面
        self.wait(2)