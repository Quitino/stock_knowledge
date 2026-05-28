"""ch6_ma.py - 均线金叉/死叉示意"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import numpy as np

cc.setup()

np.random.seed(42)
n = 120
price = 10 + np.cumsum(np.random.randn(n) * 0.15)

def ma(arr, w):
    return np.array([np.mean(arr[max(0,i-w+1):i+1]) for i in range(len(arr))])

ma5  = ma(price, 5)
ma20 = ma(price, 20)
ma60 = ma(price, 60)

fig, ax = plt.subplots(figsize=(11, 5))
x = np.arange(n)

ax.plot(x, price, color=cc.DARK, linewidth=1, alpha=0.6, label="价格")
ax.plot(x, ma5,   color=cc.ORANGE, linewidth=1.5, label="MA5（5日均线）")
ax.plot(x, ma20,  color=cc.BLUE,   linewidth=2,   label="MA20（20日均线）")
ax.plot(x, ma60,  color=cc.PURPLE, linewidth=2.2, label="MA60（60日均线）", linestyle="--")

# 找金叉（MA5上穿MA20）
for i in range(1, n):
    if ma5[i] > ma20[i] and ma5[i-1] <= ma20[i-1]:
        ax.annotate("金叉", xy=(i, ma5[i]), xytext=(i-8, ma5[i]+0.4),
                    arrowprops=dict(arrowstyle="->", color=cc.GREEN),
                    fontsize=9, color=cc.GREEN, fontweight="bold")
# 找死叉（MA5下穿MA20）
for i in range(1, n):
    if ma5[i] < ma20[i] and ma5[i-1] >= ma20[i-1]:
        ax.annotate("死叉", xy=(i, ma5[i]), xytext=(i+3, ma5[i]-0.5),
                    arrowprops=dict(arrowstyle="->", color=cc.RED),
                    fontsize=9, color=cc.RED, fontweight="bold")

ax.set_xlabel("交易日", fontsize=12)
ax.set_ylabel("价格", fontsize=12)
ax.set_title("移动均线（MA5 / MA20 / MA60）与金叉死叉", fontsize=13, fontweight="bold")
ax.legend(fontsize=10)

fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch6_ma.png")
print("saved ch6_ma.png")
