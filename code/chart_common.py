"""
公共绘图配置模块
用法：在每个绘图脚本头部 import chart_common as cc，然后调用 cc.setup()
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

FONT_PATH = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

def setup():
    """全局字体与样式设置，每个脚本最开始调用一次"""
    # 直接注册并使用字体文件，绕过字体名称查找
    fm.fontManager.addfont(FONT_PATH)
    prop = fm.FontProperties(fname=FONT_PATH)
    font_name = prop.get_name()

    plt.rcParams["font.family"] = "Noto Sans CJK JP"
    plt.rcParams["axes.unicode_minus"] = False
    plt.rcParams["figure.dpi"] = 150
    plt.rcParams["savefig.dpi"] = 150
    plt.rcParams["figure.facecolor"] = "white"
    plt.rcParams["axes.facecolor"] = "#f8f9fa"
    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.alpha"] = 0.4
    plt.rcParams["grid.linestyle"] = "--"

# 配色方案
RED    = "#e74c3c"
GREEN  = "#27ae60"
BLUE   = "#2980b9"
ORANGE = "#e67e22"
PURPLE = "#8e44ad"
GRAY   = "#7f8c8d"
DARK   = "#2c3e50"
