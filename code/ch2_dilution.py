"""ch2_dilution.py - 多轮融资股权稀释示意"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

cc.setup()

rounds = ["创立", "天使轮\n(估值1千万)", "A轮\n(估值1亿)", "B轮\n(估值5亿)", "IPO后\n(上市)"]
founder = [100, 90, 81, 72.9, 58.3]
angel   = [0,   10, 9,  8.1,  6.5]
vc_a    = [0,   0,  10, 9,    7.2]
vc_b    = [0,   0,  0,  10,   8.0]
public  = [0,   0,  0,  0,    20.0]

fig, ax = plt.subplots(figsize=(10, 5))
x = range(len(rounds))
bar_w = 0.55

b0 = ax.bar(x, founder, bar_w, label="创始人", color=cc.BLUE)
b1 = ax.bar(x, angel,   bar_w, bottom=founder, label="天使投资人", color=cc.GREEN)
b2 = ax.bar(x, vc_a,    bar_w,
            bottom=[f+a for f,a in zip(founder, angel)], label="A轮VC", color=cc.ORANGE)
b3_bot = [f+a+va for f,a,va in zip(founder, angel, vc_a)]
b3 = ax.bar(x, vc_b, bar_w, bottom=b3_bot, label="B轮VC", color=cc.PURPLE)
b4_bot = [a+b for a,b in zip(b3_bot, vc_b)]
b4 = ax.bar(x, public, bar_w, bottom=b4_bot, label="公众股东(IPO)", color=cc.GRAY)

# 标注创始人持股比例
for i, v in enumerate(founder):
    ax.text(i, v/2, f"{v:.1f}%", ha="center", va="center",
            color="white", fontsize=10, fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels(rounds, fontsize=10)
ax.set_ylabel("持股比例 (%)", fontsize=12)
ax.set_title("多轮融资中的股权稀释过程", fontsize=14, fontweight="bold")
ax.legend(loc="upper right", fontsize=10)
ax.set_ylim(0, 108)
ax.grid(axis="x", alpha=0)

fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch2_dilution.png")
print("saved ch2_dilution.png")
