import numpy as np
from manim import *


def CreateBall(num: int) -> VGroup:
    """
    创建一个VGroup，包含一个矩形和若干圆球，圆球数量根据输入确定
    :param num: int - 圆球的数量
    :return: VGroup
    """
    ball_radius = 0.2
    spacing = 0.6

    balls = VGroup()
    positions = []

    if num <= 5:
        for i in range(num):
            ball = Dot(radius=ball_radius, color=BLUE)
            ball.move_to(UP * i * -spacing)
            balls.add(ball)
            positions.append(ball.get_center())
    else:
        key_positions = [
            0, 1, "ellipsis", num // 2, "ellipsis", num - 2, num - 1
        ]
        index = 0

        for pos in key_positions:
            if pos == "ellipsis":
                ellipsis = MathTex(r"\vdots", color=BLUE).scale(0.8)
                ellipsis.move_to(UP * index * -spacing)
                balls.add(ellipsis)
                positions.append(ellipsis.get_center())
            else:
                ball = Dot(radius=ball_radius, color=BLUE)
                ball.move_to(UP * index * -spacing)
                balls.add(ball)
                positions.append(ball.get_center())
            index += 1

    top_y = positions[0][1] + ball_radius + 0.1
    bottom_y = positions[-1][1] - ball_radius - 0.1
    box_height = top_y - bottom_y
    box_width = 1.5

    rectangle = RoundedRectangle(
        width=box_width, height=box_height, corner_radius=0.2, color=BLUE
    ).move_to(np.array([0, (top_y + bottom_y) / 2, 0]))

    group = VGroup(rectangle, balls)
    return group
