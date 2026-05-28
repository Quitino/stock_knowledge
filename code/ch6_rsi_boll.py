"""ch6_rsi_boll.py - RSI 与布林带"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import numpy as np

cc.setup()

np.random.seed(11)
n = 120
price = 10 + np.cumsum(np.random.randn(n) * 0.15)

# RSI
def rsi(arr, period=14):
    delta = np.diff(arr)
    gain  = np.where(delta > 0, delta, 0)
    loss  = np.where(delta < 0, -delta, 0)
    avg_g = np.array([np.mean(gain[max(0,i-period+1):i+1]) for i in range(len(gain))])
    avg_l = np.array([np.mean(loss[max(0,i-period+1):i+1]) for i in range(len(loss))])
    rs = np.where(avg_l == 0, 100, avg_g / (avg_l + 1e-9))
    return 100 - 100 / (1 + rs)

rsi_val = rsi(price)

# 布林带
w = 20
mid = np.array([np.mean(price[max(0,i-w+1):i+1]) for i in range(n)])
std = np.array([np.std(price[max(0,i-w+1):i+1]) for i in range(n)])
upper = mid + 2 * std
lower = mid - 2 * std

x = np.arange(n)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True,
                                gridspec_kw={"height_ratios": [2, 1.2]})

# 布林带
ax1.plot(x, price, color=cc.DARK, linewidth=1.5, label="价格", zorder=3)
ax1.plot(x, mid,   color=cc.BLUE, linewidth=1.5, linestyle="--", label="中轨 MA20")
ax1.plot(x, upper, color=cc.RED,  linewidth=1.2, label="上轨 (+2σ)")
ax1.plot(x, lower, color=cc.GREEN,linewidth=1.2, label="下轨 (-2σ)")
ax1.fill_between(x, lower, upper, alpha=0.07, color=cc.BLUE)
ax1.set_ylabel("价格", fontsize=11)
ax1.set_title("布林带（Bollinger Bands）与 RSI 指标", fontsize=13, fontweight="bold")
ax1.legend(fontsize=9, loc="upper left")

# RSI
ax2.plot(x[:-1], rsi_val, color=cc.PURPLE, linewidth=1.8, label="RSI(14)")
ax2.axhline(70, color=cc.RED,   linestyle="--", linewidth=1.2, label="超买线 70")
ax2.axhline(30, color=cc.GREEN, linestyle="--", linewidth=1.2, label="超卖线 30")
ax2.fill_between(x[:-1], 70, np.clip(rsi_val, 70, 100),
                 alpha=0.15, color=cc.RED)
ax2.fill_between(x[:-1], np.clip(rsi_val, 0, 30), 30,
                 alpha=0.15, color=cc.GREEN)
ax2.set_ylim(0, 100)
ax2.set_ylabel("RSI", fontsize=11)
ax2.set_xlabel("交易日", fontsize=11)
ax2.legend(fontsize=9, loc="upper left")

fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch6_rsi_boll.png")
print("saved ch6_rsi_boll.png")
