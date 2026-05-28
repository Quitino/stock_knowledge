"""ch6_macd.py - MACD 指标图"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import numpy as np

cc.setup()

np.random.seed(3)
n = 120
price = 10 + np.cumsum(np.random.randn(n) * 0.18)

def ema(arr, span):
    k = 2 / (span + 1)
    result = [arr[0]]
    for v in arr[1:]:
        result.append(v * k + result[-1] * (1 - k))
    return np.array(result)

ema12 = ema(price, 12)
ema26 = ema(price, 26)
dif   = ema12 - ema26
dea   = ema(dif, 9)
macd  = (dif - dea) * 2

x = np.arange(n)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True,
                                gridspec_kw={"height_ratios": [2, 1.2]})

ax1.plot(x, price, color=cc.DARK, linewidth=1.5, label="价格")
ax1.set_ylabel("价格", fontsize=11)
ax1.set_title("MACD 指标：DIF、DEA 与金叉死叉", fontsize=13, fontweight="bold")
ax1.legend(fontsize=10)

ax2.plot(x, dif, color=cc.BLUE,   linewidth=1.8, label="DIF（快线）")
ax2.plot(x, dea, color=cc.ORANGE, linewidth=1.8, label="DEA（慢线）")
bar_colors = [cc.RED if v >= 0 else cc.GREEN for v in macd]
ax2.bar(x, macd, color=bar_colors, alpha=0.6, width=0.8, label="MACD柱")
ax2.axhline(0, color=cc.DARK, linewidth=0.8)

# 标注金叉死叉
for i in range(1, n):
    if dif[i] > dea[i] and dif[i-1] <= dea[i-1]:
        ax2.annotate("金叉", xy=(i, dif[i]), xytext=(i+2, dif[i]+0.05),
                     fontsize=8, color=cc.GREEN, fontweight="bold",
                     arrowprops=dict(arrowstyle="->", color=cc.GREEN, lw=0.8))
    if dif[i] < dea[i] and dif[i-1] >= dea[i-1]:
        ax2.annotate("死叉", xy=(i, dif[i]), xytext=(i+2, dif[i]-0.06),
                     fontsize=8, color=cc.RED, fontweight="bold",
                     arrowprops=dict(arrowstyle="->", color=cc.RED, lw=0.8))

ax2.set_ylabel("MACD", fontsize=11)
ax2.set_xlabel("交易日", fontsize=11)
ax2.legend(fontsize=9, loc="upper left")

fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch6_macd.png")
print("saved ch6_macd.png")
