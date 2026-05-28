"""ch6_support_resist.py - 支撑位与压力位示意"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import numpy as np

cc.setup()

np.random.seed(99)
n = 100

# 手工构造有支撑/压力的价格序列
p = [10.0]
support, resist = 9.5, 11.2
for i in range(1, n):
    step = np.random.randn() * 0.18
    new  = p[-1] + step
    if new < support + 0.05:
        new = support + abs(np.random.randn() * 0.1)
    if new > resist - 0.05:
        new = resist - abs(np.random.randn() * 0.1)
    p.append(new)
# 让价格在第70步突破压力位
for i in range(68, n):
    p[i] += (i - 68) * 0.04

price = np.array(p)
x = np.arange(n)

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(x, price, color=cc.DARK, linewidth=1.5, label="价格")

# 支撑位（突破前）
ax.axhline(support, xmin=0, xmax=0.68, color=cc.GREEN, linewidth=2,
           linestyle="--", label=f"支撑位 {support}")
# 压力位（突破前变支撑）
ax.axhline(resist, xmin=0, xmax=0.68, color=cc.RED, linewidth=2,
           linestyle="--", label=f"压力位 {resist}")
ax.axhline(resist, xmin=0.68, xmax=1, color=cc.GREEN, linewidth=2,
           linestyle=":", label=f"压力位突破后变支撑")

# 标注区域
ax.fill_between(x[:68], support, support + 0.25,
                alpha=0.12, color=cc.GREEN)
ax.fill_between(x[:68], resist - 0.25, resist,
                alpha=0.12, color=cc.RED)

ax.annotate("多次触及\n支撑位反弹", xy=(15, support + 0.05),
            xytext=(20, 9.0), fontsize=9, color=cc.GREEN,
            arrowprops=dict(arrowstyle="->", color=cc.GREEN))
ax.annotate("突破压力位\n趋势反转信号", xy=(70, resist + 0.1),
            xytext=(72, resist + 0.6), fontsize=9, color=cc.RED,
            arrowprops=dict(arrowstyle="->", color=cc.RED))

ax.set_xlabel("交易日", fontsize=12)
ax.set_ylabel("价格", fontsize=12)
ax.set_title("支撑位与压力位：价格反复博弈的关键价格区域", fontsize=13, fontweight="bold")
ax.legend(fontsize=9, loc="upper left")

fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch6_support_resist.png")
print("saved ch6_support_resist.png")
