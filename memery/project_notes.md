# 股票交易教程 — 项目记忆

## 项目概述

**路径**：`/mnt/data2/trade/`
**目标**：面向零基础程序员的中文股票交易入门教程 markdown，共 11 章 + 附录。
**文档存放**：`docs/`（chapter1.md … chapter11.md + appendix.md + index.md）

---

## 目录结构

```
/mnt/data2/trade/
├── docs/         章节 markdown 文件
├── code/         绘图 Python 脚本（chart_common.py + ch*_*.py）
├── pic/          生成的图片（PNG，150dpi）
├── memery/       本文件所在目录（项目记忆）
└── readme.md
```

---

## 写作约定

- **语言**：中文正文，交流可用英文
- **Q&A 格式**：正文中穿插读者可能提出的问题，用 `> Q: ... > A: ...` 块引用格式，**不要改为正文段落**（用户明确要求保留此格式）
- **无代码**：教程本身不写代码，只讲概念与实操
- **图片引用**：使用相对路径 `./pic/图片名.png`

---

## 各章节内容摘要

| 章节 | 主题 | 插图 |
|---|---|---|
| ch1 | 货币、通胀、资本、金融市场分类 | ch1_inflation.png（通胀侵蚀购买力） |
| ch2 | 股票是什么、股权、IPO、融资之路 | ch2_dilution.png（多轮融资股权稀释） |
| ch3 | 交易所结构、A/美/港股规则、T+1 | ch3_orderbook.png（买卖盘口） |
| ch4 | 指数、大盘、牛熊市、VIX、利率 | ch4_bull_bear.png（牛熊时间轴） |
| ch5 | 三张财务报表、PE/PB/ROE、护城河 | 无图 |
| ch6 | 技术分析：K线、均线、量价、MACD、RSI、布林带、支撑压力位 | 6 张图（kline/ma/volume/macd/rsi_boll/support_resist） |
| ch7 | 估值：DCF、PE、PB、PEG、EV/EBITDA、安全边际 | ch7_dcf.png |
| ch8 | 交易策略：价值/趋势/量化/指数/网格 | 无图 |
| ch9 | 风险管理：仓位、分散、止损、凯利公式、心理偏误 | ch9_diversify.png |
| ch10 | 开户实操：A股/美股/港股、ETF 第一笔交易 | 无图 |
| ch11 | 构建交易体系、选股池、回测、复盘 | 无图 |
| appendix | 书单、数据源、工具、监管参考 | 无图 |

---

## 绘图技术细节

- **字体**：`Noto Sans CJK JP`（系统已安装，通过 `fm.fontManager.addfont()` 注册）
  - 字体文件：`/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc`
  - `get_name()` 返回 `"Noto Sans CJK JP"`，用这个名称设置 `plt.rcParams["font.family"]`
- **公共配置**：`code/chart_common.py`，每个绘图脚本头部 `import chart_common as cc; cc.setup()`
- **输出**：PNG，150dpi，存放 `pic/`

---

## 已有 Q&A 补充列表（docs/ 中的问答块）

- ch2：发行多少股由谁决定 / 期权与股票区别 / 华为虚拟股分红 / 打新条件
- ch3：做市商与竞价 / 沪深港通方向（已更正：北向=境外资金买A股） / 港股打新 / 集合竞价与连续竞价 / 尾盘打价格如何规避 / T+1止损问题
- ch4：3000点含义 / PE/PB解释 / PE越低越好的误解 / ETF是什么 / VIX计算原理 / 行业分类大表

---

## 重要纠错记录

- **ch3 沪深港通方向**：原文写反（已修正）
  - 北向（北上）= 境外/香港资金 → 买 A 股
  - 南向（南下）= 内地资金 → 买港股

---

## 后续可继续的方向

1. ch5 添加财务报表示意图（利润表结构、三表关系）
2. ch6 添加 K 线形态识别的更多案例（吞没形态实际图）
3. ch8 量化交易章节补充实际代码框架示意
4. ch10 开户流程截图说明（若有实际界面素材）
5. 继续在各章节补充读者 Q&A
