from manim import *
import numpy as np

'''
    English：You are free to use my code, but please do not delete my copyright text.
    中文：您可以随意的使用我的代码，但是请使用的同时不要将我的版权说明文本删除掉。
'''

'''
    为什么需要使用one-hot编码，是因为如果从tokenizer开始，那么你就无法判断要扩大到多少维度，可是如果从one-hot编码起步，那么最少能保证最大的维度是多少？
    因为one-hot编码的缺点就是空间的信息太过稀疏了。
    编解码，其实就是先将中文的各个汉字编成潜空间的码，然后再把英语单个单词编成码。而后再使用算法将其映射到潜空间中。然后再利用某种融合算法将两个潜空间融合到一起。
    当实行翻译的时候进行比对。
'''
class WordEmbedCode(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        # Copyright text
        copyright_txt = Text('本视频作者联系方式：luxun23@qq.com', color=BLACK, font='SimSun', font_size=18,
                             t2c={'联系方式': RED, 'luxun23@qq.com': RED})
        self.play(copyright_txt.animate.to_corner(DR))
        self._explanations()

    def _explanations(self):
        pass
