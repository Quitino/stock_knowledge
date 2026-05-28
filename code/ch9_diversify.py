"""ch9_diversify.py - 分散投资：相关性与组合风险"""
import sys; sys.path.insert(0, "/mnt/data2/trade/code")
import chart_common as cc
import matplotlib.pyplot as plt
import numpy as np

cc.setup()

np.random.seed(5)
n = 252  # 一年交易日

# 构造三类资产回报
ret_stock  = np.random.randn(n) * 0.015 + 0.0003   # 股票
ret_bond   = np.random.randn(n) * 0.003 + 0.0001   # 债券（与股票低相关）
ret_gold   = np.random.randn(n) * 0.008             # 黄金（近零相关）
# 60/40 组合
ret_port60 = 0.6 * ret_stock + 0.4 * ret_bond

# 累计净值
def cumulative(ret):
    return np.cumprod(1 + ret)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 左图：累计收益对比
x = np.arange(n)
ax1.plot(x, cumulative(ret_stock),  color=cc.RED,   lw=2,   label="纯股票")
ax1.plot(x, cumulative(ret_bond),   color=cc.BLUE,  lw=1.5, label="纯债券", linestyle="--")
ax1.plot(x, cumulative(ret_port60), color=cc.GREEN, lw=2,   label="60% 股票 + 40% 债券")
ax1.set_title("分散投资降低波动：股债组合 vs 纯股票", fontsize=12, fontweight="bold")
ax1.set_xlabel("交易日", fontsize=11)
ax1.set_ylabel("累计净值（初始=1）", fontsize=11)
ax1.legend(fontsize=10)

# 右图：资产数量与组合波动率的关系（理论曲线）
n_assets = np.arange(1, 31)
sigma_single = 0.25
corr = 0.3
port_vol = sigma_single * np.sqrt((1 + corr * (n_assets - 1)) / n_assets)

ax2.plot(n_assets, port_vol * 100, color=cc.BLUE, lw=2.5, marker="o", markersize=4)
ax2.axhline(sigma_single * np.sqrt(corr) * 100, color=cc.GRAY, linestyle="--",
            label=f"系统性风险下限\n(相关系数={corr})")
ax2.fill_between(n_assets,
                 sigma_single * np.sqrt(corr) * 100,
                 port_vol * 100,
                 alpha=0.12, color=cc.BLUE, label="可分散的非系统性风险")
ax2.set_title("持股数量越多，非系统性风险越低", fontsize=12, fontweight="bold")
ax2.set_xlabel("持有不同股票数量", fontsize=11)
ax2.set_ylabel("组合年化波动率 (%)", fontsize=11)
ax2.legend(fontsize=9)

fig.tight_layout()
fig.savefig("/mnt/data2/trade/pic/ch9_diversify.png")
print("saved ch9_diversify.png")
