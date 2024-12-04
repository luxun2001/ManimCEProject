from manim import *
import numpy as np
import math

def sci_not(x):
    if x == 0:
        return "0"
    significant = x / (10 ** int(math.log10(abs(x))))
    exponent = int(math.log10(abs(x)))
    return "{0:.2f} \\times 10^{{{1}}}".format(significant, exponent)


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