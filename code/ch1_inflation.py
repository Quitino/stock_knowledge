"""ch1_inflation.py - 通胀对购买力的侵蚀"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import numpy as np

cc.setup()

years = np.arange(0, 31)
rates = {"1% 低通胀": 0.01, "3% 温和通胀": 0.03, "5% 高通胀": 0.05}
colors = [cc.GREEN, cc.ORANGE, cc.RED]

fig, ax = plt.subplots(figsize=(9, 5))
for (label, r), color in zip(rates.items(), colors):
    values = 10 * (1 - r) ** years
    ax.plot(years, values, label=label, color=color, linewidth=2.2)

ax.axhline(5, color=cc.GRAY, linestyle=":", linewidth=1.2, label="购买力减半线")
ax.set_xlabel("年数", fontsize=12)
ax.set_ylabel("10万元的实际购买力（万元）", fontsize=12)
ax.set_title("通货膨胀对购买力的侵蚀", fontsize=14, fontweight="bold")
ax.legend(fontsize=11)
ax.set_xlim(0, 30)
ax.set_ylim(2, 10.5)
ax.fill_between(years, 10 * (1 - 0.03) ** years, 10,
                alpha=0.08, color=cc.ORANGE, label="_nolegend_")

fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch1_inflation.png")
print("saved ch1_inflation.png")
