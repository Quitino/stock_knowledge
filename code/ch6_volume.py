"""ch6_volume.py - 量价配合示意"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import numpy as np

cc.setup()

np.random.seed(7)
n = 80
base_price = 10 + np.cumsum(np.random.randn(n) * 0.12)
# 构造放量上涨和放量下跌区段
base_vol = np.random.randint(500, 1500, n)
base_vol[30:38] = np.random.randint(3000, 5000, 8)   # 放量上涨
base_price[30:38] += np.linspace(0, 1.5, 8)
base_vol[55:62] = np.random.randint(3500, 5500, 7)   # 放量下跌
base_price[55:62] -= np.linspace(0, 1.8, 7)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 6), sharex=True,
                                gridspec_kw={"height_ratios": [3, 1]})

# 价格
ax1.plot(base_price, color=cc.DARK, linewidth=1.5, label="价格")
ax1.axvspan(30, 38, alpha=0.12, color=cc.GREEN, label="放量上涨区段")
ax1.axvspan(55, 62, alpha=0.12, color=cc.RED,   label="放量下跌区段")
ax1.annotate("放量上涨\n趋势可信", xy=(34, base_price[34]),
             xytext=(38, base_price[34]+0.5),
             arrowprops=dict(arrowstyle="->", color=cc.GREEN),
             fontsize=9, color=cc.GREEN, fontweight="bold")
ax1.annotate("放量下跌\n恐慌出逃", xy=(58, base_price[58]),
             xytext=(62, base_price[58]+0.5),
             arrowprops=dict(arrowstyle="->", color=cc.RED),
             fontsize=9, color=cc.RED, fontweight="bold")
ax1.set_ylabel("价格", fontsize=11)
ax1.legend(fontsize=9, loc="upper left")
ax1.set_title("量价配合：成交量是价格信号的置信度", fontsize=13, fontweight="bold")

# 成交量
colors = [cc.RED if base_price[i] >= base_price[i-1] else cc.GREEN for i in range(n)]
colors[0] = cc.RED
ax2.bar(range(n), base_vol, color=colors, alpha=0.75, width=0.8)
ax2.axhline(2000, color=cc.ORANGE, linestyle="--", linewidth=1, label="均量线")
ax2.set_ylabel("成交量", fontsize=11)
ax2.set_xlabel("交易日", fontsize=11)
ax2.legend(fontsize=9)

fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch6_volume.png")
print("saved ch6_volume.png")
