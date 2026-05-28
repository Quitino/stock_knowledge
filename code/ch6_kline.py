"""ch6_kline.py - K线基础结构 + 典型形态"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

cc.setup()

fig, axes = plt.subplots(1, 4, figsize=(12, 6))
fig.suptitle("K线形态图解", fontsize=14, fontweight="bold")

def draw_candle(ax, o, h, l, c, title, note=""):
    color = cc.RED if c >= o else cc.GREEN
    # 上下影线
    ax.plot([0.5, 0.5], [l, h], color=cc.DARK, linewidth=1.8, zorder=2)
    # 实体
    body_bot = min(o, c)
    body_h   = abs(c - o) if abs(c - o) > 0 else 0.005 * (h - l)
    rect = mpatches.FancyBboxPatch(
        (0.25, body_bot), 0.5, body_h,
        boxstyle="square,pad=0", linewidth=1,
        edgecolor=color, facecolor=color, alpha=0.9, zorder=3)
    ax.add_patch(rect)
    # 标注
    offset = (h - l) * 0.04
    ax.text(0.85, h, f"最高 {h:.2f}", va="center", fontsize=8, color=cc.DARK)
    ax.text(0.85, l, f"最低 {l:.2f}", va="center", fontsize=8, color=cc.DARK)
    ax.text(0.85, c, f"收盘 {c:.2f}", va="center", fontsize=8,
            color=cc.RED if c >= o else cc.GREEN)
    ax.text(0.85, o, f"开盘 {o:.2f}", va="center", fontsize=8, color=cc.DARK)
    ax.set_xlim(0, 2)
    ax.set_ylim(l - (h-l)*0.3, h + (h-l)*0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=11, fontweight="bold", color=color if color != cc.DARK else cc.DARK)
    if note:
        ax.text(0.5, l - (h-l)*0.2, note, ha="center", fontsize=8.5,
                color=cc.GRAY, style="italic")
    ax.grid(False)

draw_candle(axes[0], 10.00, 10.60, 9.70, 10.45,
            "阳线（涨）", "收盘 > 开盘\n当日上涨")
draw_candle(axes[1], 10.50, 10.65, 9.80, 10.05,
            "阴线（跌）", "收盘 < 开盘\n当日下跌")
draw_candle(axes[2], 10.20, 10.70, 9.50, 10.22,
            "锤子线", "长下影线\n潜在底部信号")
draw_candle(axes[3], 10.30, 10.32, 9.60, 10.31,
            "十字星", "开盘≈收盘\n多空均势")

fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch6_kline.png")
print("saved ch6_kline.png")
