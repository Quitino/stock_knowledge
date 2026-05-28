"""ch4_bull_bear.py - 标普500牛熊市历史时间轴"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

cc.setup()

# (start_year, end_year, type, label)
periods = [
    (1990, 2000, "bull", "牛市\n+417%"),
    (2000, 2002, "bear", "熊市\n-49%"),
    (2003, 2007, "bull", "牛市\n+101%"),
    (2007, 2009, "bear", "熊市\n-57%"),
    (2009, 2020, "bull", "牛市\n+400%+"),
    (2020.1, 2020.3, "bear", "熊市\n-34%"),
    (2020.3, 2022, "bull", "牛市"),
    (2022, 2022.8, "bear", "熊市\n-27%"),
]

fig, ax = plt.subplots(figsize=(12, 4))

for start, end, t, label in periods:
    color = cc.RED if t == "bear" else cc.GREEN
    alpha = 0.75
    ax.barh(0, end - start, left=start, height=0.6,
            color=color, alpha=alpha, edgecolor="white", linewidth=0.5)
    mid = (start + end) / 2
    fs = 8 if (end - start) < 1 else 9
    ax.text(mid, 0, label, ha="center", va="center",
            fontsize=fs, color="white", fontweight="bold")

# 图例
bull_p = mpatches.Patch(color=cc.GREEN, alpha=0.75, label="牛市")
bear_p = mpatches.Patch(color=cc.RED, alpha=0.75, label="熊市")
ax.legend(handles=[bull_p, bear_p], fontsize=11, loc="upper left")

ax.set_xlim(1989, 2023)
ax.set_ylim(-0.5, 0.5)
ax.set_xlabel("年份", fontsize=12)
ax.set_title("美股标普500 牛市/熊市历史（1990–2022）", fontsize=13, fontweight="bold")
ax.set_yticks([])
ax.grid(axis="y", alpha=0)

fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch4_bull_bear.png")
print("saved ch4_bull_bear.png")
