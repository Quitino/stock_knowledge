"""ch3_orderbook.py - 买卖盘口示意图"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

cc.setup()

ask_prices = [10.10, 10.09, 10.08]
ask_vols   = [1000,  2000,  500]
bid_prices = [10.05, 10.04, 10.03]
bid_vols   = [1000,  3000,  5000]

fig, ax = plt.subplots(figsize=(8, 5))

# 卖盘（红色，右侧）
bars_ask = ax.barh(ask_prices, ask_vols, height=0.012,
                   color=cc.RED, alpha=0.85, label="卖盘 (Ask)")
# 买盘（绿色，左侧，负值）
bars_bid = ax.barh(bid_prices, [-v for v in bid_vols], height=0.012,
                   color=cc.GREEN, alpha=0.85, label="买盘 (Bid)")

# 标注
for price, vol in zip(ask_prices, ask_vols):
    ax.text(vol + 80, price, f"{price:.2f}  ×{vol}", va="center",
            fontsize=11, color=cc.RED, fontweight="bold")
for price, vol in zip(bid_prices, bid_vols):
    ax.text(-vol - 80, price, f"×{vol}  {price:.2f}", va="center",
            ha="right", fontsize=11, color=cc.GREEN, fontweight="bold")

ax.axvline(0, color=cc.DARK, linewidth=1.5)
ax.axhline(10.065, color=cc.ORANGE, linewidth=1.5, linestyle="--")
ax.text(200, 10.068, "← 买卖价差 (Spread)", fontsize=10, color=cc.ORANGE)

ax.set_xlabel("委托量（股）", fontsize=12)
ax.set_title("买卖盘口结构示意", fontsize=14, fontweight="bold")
ax.set_yticks(ask_prices + bid_prices)
ax.set_yticklabels([f"{p:.2f}" for p in ask_prices + bid_prices], fontsize=10)
ax.set_xlim(-7000, 5000)
ax.xaxis.set_ticklabels([])
ax.legend(fontsize=11, loc="upper right")
ax.grid(axis="y", alpha=0)

fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch3_orderbook.png")
print("saved ch3_orderbook.png")
