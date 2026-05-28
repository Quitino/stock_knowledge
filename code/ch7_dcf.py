"""ch7_dcf.py - DCF 折现概念：未来现金流的现值"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import numpy as np

cc.setup()

years = np.arange(1, 11)
fcf   = 100 * (1.1 ** (years - 1))          # 每年增长10%的现金流

rates = {"折现率 5%": 0.05, "折现率 10%": 0.10, "折现率 15%": 0.15}
colors = [cc.GREEN, cc.BLUE, cc.RED]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 左图：各年现金流现值对比
x = np.arange(len(years))
w = 0.25
for idx, ((label, r), color) in enumerate(zip(rates.items(), colors)):
    pv = fcf / (1 + r) ** years
    ax1.bar(x + idx * w, pv, w, label=label, color=color, alpha=0.8)

ax1.set_xticks(x + w)
ax1.set_xticklabels([f"第{y}年" for y in years], fontsize=9)
ax1.set_ylabel("现值（元）", fontsize=11)
ax1.set_title("未来现金流折现到今天的价值", fontsize=12, fontweight="bold")
ax1.legend(fontsize=9)

# 右图：折现率越高，内在价值越低
r_range = np.linspace(0.02, 0.25, 100)
total_pv = [sum(fcf / (1 + r) ** years) for r in r_range]
ax2.plot(r_range * 100, total_pv, color=cc.BLUE, linewidth=2.5)
ax2.fill_between(r_range * 100, total_pv, alpha=0.1, color=cc.BLUE)
for r_mark, c in [(5, cc.GREEN), (10, cc.ORANGE), (15, cc.RED)]:
    pv_mark = sum(fcf / (1 + r_mark/100) ** years)
    ax2.scatter([r_mark], [pv_mark], s=80, color=c, zorder=5)
    ax2.annotate(f"r={r_mark}%\nPV={pv_mark:.0f}", xy=(r_mark, pv_mark),
                 xytext=(r_mark + 1.5, pv_mark + 50),
                 fontsize=9, color=c, fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=c, lw=0.8))

ax2.set_xlabel("折现率 (%)", fontsize=11)
ax2.set_ylabel("10年现金流总现值（元）", fontsize=11)
ax2.set_title("折现率越高，内在价值越低", fontsize=12, fontweight="bold")

fig.suptitle("DCF 模型：公司内在价值 = 未来现金流的折现之和", fontsize=13, fontweight="bold", y=1.02)
fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch7_dcf.png", bbox_inches="tight")
print("saved ch7_dcf.png")
