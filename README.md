# MyTechLearning

This is a repository for my tech learning. I will store learning codes and relevant files here to record my daily learning progress.

## 目录

- [Learning Progress](#learning-progress)
- [一、Python 常用数据结构方法速查表](#一python-常用数据结构方法速查表)
- [二、Pandas](#二pandas)
- [三、Joining Data with pandas](#三joining-data-with-pandas)
- [四、Introduction to Statistics in Python](#四introduction-to-statistics-in-python)
- [五、Sowing Success 项目（机器学习选作物）](#五sowing-success-项目机器学习选作物)

## Learning Progress

- 7/13
  - Finish Chapter 1 DSfCIipy, learned Big O and algorithm time complexity analysis
  - Finish codedex intermediate py Chapter 1 Data Structures
  - Related codes stored in folder `data structures`
- 7/14
  - Start Chapter 2, completed two array programming exercises (high difficulty)
  - Finish Chapter 2 File I/O
  - Related codes stored in folder `file I/O`
- 7/15 DSCI: Python 常用数据结构方法速查表
- 7/18 Finish DSCI ch2
- 7/25 DSCI Dll & SLL
- 7/26
  - Continue DLL & SLL, learn two pointers technique
  - Finish datacamp *Data Manipulation with pandas* Chapter 1: Transforming DataFrames
- 7/27 No learning record
- 7/28
  - Learn NumPy & Pandas common methods
  - Finish data manipulation cheat sheet for README
- 7/29
  - Finish Data Manipulation with pandas on Datacamp
  - Start learning stack and queue
  - Finish 1 leetcode array question
- 7/30
  - Finish Datacamp *Joining Data with pandas*
- 7/31
  - Finish Datacamp *Introduction to Statistics in Python* ch1
  - Continue learning about stacks and complete 2 LeetCode problems
- 8/1-8/6
  - I completed DataCamp courses covering fundamental Python data‑processing tools, including NumPy, Pandas, Seaborn, Matplotlib and more. I gained a preliminary understanding of implementing regression analysis and hypothesis testing in Python.

  - I have re‑evaluated my current study plan. I find the Data Structures and Algorithms course I am taking overly difficult for now. My revised learning goal for data structures and algorithms is to focus mainly on conceptual understanding: being able to read relevant Python code and grasp core concepts. Therefore, I will temporarily stop the Data Structure for Coding Interviewer course on Eduactive. Instead, I will mainly learn by reading books and doing lightweight coding practice on platforms such as LeetCode.

  - Moving forward, I will study mathematical statistics in parallel and start learning machine‑learning directly.
  

- 8/11
  - Continued studying mathematical statistics: gained a solid understanding of the EM algorithm, and got a preliminary introduction to interval estimation and Bayesian estimation.
  - Re-evaluated how to learn machine learning. The ML course on Eduactive feels too practice-oriented and does not explain the algorithms and mathematical principles behind each model. I found that DataCamp gives clear, simple explanations of ML algorithms, so for the near future I will return to DataCamp to continue learning machine learning.
  - Got a preliminary understanding of several regression models:
    - Linear Regression - fits a linear model by minimizing squared error (OLS)
    - Ridge Regression - Linear Regression with an L2 penalty on coefficients (helps with multicollinearity)
    - LASSO Regression - Linear Regression with an L1 penalty (performs feature selection)
    - Bayesian Regression - estimates a posterior distribution over the weights instead of a single point estimate
    - Logistic Regression - uses the logistic function for binary classification

---

## 一、Python 常用数据结构方法速查表

## 1. list（列表）- 可变序列

| 方法 | 功能说明 | 示例 |
|------|--------|------|
| `append(x)` | 末尾添加单个元素 | `lst.append(5)` |
| `extend(iterable)` | 末尾批量添加多个元素 | `lst.extend([6,7])` |
| `insert(i, x)` | 在索引i位置插入元素 | `lst.insert(2, 99)` |
| `remove(x)` | 删除第一个值为x的元素 | `lst.remove(5)` |
| `pop(i=-1)` | 删除并返回索引i的元素，默认最后一位 | `lst.pop()` / `lst.pop(0)` |
| `clear()` | 清空列表所有元素 | `lst.clear()` |
| `index(x)` | 返回第一个匹配x的索引 | `lst.index(5)` |
| `count(x)` | 统计x在列表中出现次数 | `lst.count(5)` |
| `sort(key=None, reverse=False)` | 原地排序 | `lst.sort()` / `lst.sort(reverse=True)` |
| `reverse()` | 原地反转列表顺序 | `lst.reverse()` |
| `copy()` | 浅拷贝生成新列表 | `new = lst.copy()` |

### 列表常用操作

`len(lst)`、`x in lst`、`lst[i:j]` 切片、`lst + lst2` 列表拼接

## 2. tuple（元组）- 不可变序列

| 方法 | 功能说明 | 示例 |
|------|--------|------|
| `count(x)` | 统计x出现次数 | `t.count(5)` |
| `index(x)` | 返回第一个匹配x的索引 | `t.index(5)` |

### 元组特点

不可修改；支持切片、解包；可作为字典key使用

## 3. dict（字典）- 键值对（Python3.7+ 插入有序）

| 方法 | 功能说明 | 示例 |
|------|--------|------|
| `get(key, default=None)` | 获取键对应值，不存在返回默认值 | `d.get('a', 0)` |
| `setdefault(key, default)` | 获取值，无键则新增键并赋值默认值 | `d.setdefault('b', 5)` |
| `pop(key, default=None)` | 删除指定键并返回对应值 | `d.pop('a')` |
| `popitem()` | 删除并返回最后一组键值对 | `d.popitem()` |
| `update(other)` | 合并更新字典 | `d.update({'c': 3})` |
| `keys()` | 返回字典所有键视图 | `list(d.keys())` |
| `values()` | 返回字典所有值视图 | `list(d.values())` |
| `items()` | 返回 `(key, value)` 键值对视图 | `for k,v in d.items():` |
| `clear()` | 清空字典 | `d.clear()` |
| `copy()` | 浅拷贝字典 | `new_d = d.copy()` |

### 字典基础操作

`key in d` 判断键存在、`d[key]` 取值、`d[key] = value` 新增/修改键值

## 4. set（集合）- 无序、元素唯一

| 方法 | 功能说明 |
|------|--------|
| `add(x)` | 添加单个元素 |
| `remove(x)` | 删除元素，元素不存在时报错 |
| `discard(x)` | 删除元素，不存在不报错 |
| `pop()` | 随机删除并返回一个元素 |
| `clear()` | 清空集合 |
| `union(*others)` / `\|` | 求并集 |
| `intersection(*others)` / `&` | 求交集 |
| `difference(*others)` / `-` | 求差集 |
| `symmetric_difference(other)` / `^` | 求对称差集 |
| `issubset(other)` | 判断是否为子集 |
| `isdisjoint(other)` | 判断两集合是否无交集 |

---

## 二、Pandas

```python
import pandas as pd
import matplotlib.pyplot as plt
```

## 1 Transforming DataFrames 数据变换

### 1.1 查看数据集信息

```python
df.head()                 # 查看前5行
df.tail()                 # 查看最后5行
df.info()                 # 字段类型、缺失值概览
df.describe()             # 数值列统计描述
df.shape                  # 返回 (行数, 列数)
df.columns                # 获取全部列名
```

### 1.2 数据行排序

```python
# 单列升序
df.sort_values("column_name")
# 单列降序
df.sort_values("column_name", ascending=False)
# 多列组合排序
df.sort_values(["col1", "col2"], ascending=[True, False])
```

### 1.3 选取指定列

```python
# 选取单列
df["colname"]
# 选取多列
df[["col1", "col2"]]
```

### 1.4 布尔条件筛选行

```python
# 单一条件筛选
df[df["col"] > 100]
# 多条件组合：& 且 / | 或
df[(df["a"]>5) & (df["b"]=="text")]
# 多枚举值筛选 isin()
df[df["category"].isin(["A","B"])]
```

### 1.5 创建新列

```python
# 通过列运算生成新字段
df["new_col"] = df["col1"] / df["col2"] * 10000
```

## 2 Aggregating DataFrames 聚合统计

### 2.1 基础汇总统计
```python
df["col"].mean()    # 均值
df["col"].median()  # 中位数
df["col"].max()     # 最大值
df["col"].min()     # 最小值
df["col"].sum()     # 求和
df["col"].count()   # 非空计数
# 一次性执行多个统计函数
df["col"].agg(["mean", "median", "max"])
```

### 2.2 去除重复行

```python
# 根据指定多列去重
df = df.drop_duplicates(subset=["col1","col2"])
```

### 2.3 分类变量计数统计

```python
# 统计分类值频次
df["category_col"].value_counts()
# 百分比占比形式
df["category_col"].value_counts(normalize=True)
```

### 2.4 groupby 分组聚合（核心）

```python
# 单字段分组求均值
df.groupby("group_col")["value_col"].mean()
# 多字段分组求和
df.groupby(["g1","g2"])["val"].sum()
# 分组同时执行多种聚合
df.groupby("airline")["nb_bumped"].agg(["sum","mean"])
# 分组结果取消索引，转为普通DataFrame
df.groupby("city")["temp"].mean().reset_index()
```

### 2.5 Pivot tables 透视表

```python
# 基础透视表
df.pivot_table(values="avg_temp_c", index="city", columns="year", aggfunc="mean")
# 透视表缺失值填充
df.pivot_table(values="sales", index="store", columns="type", fill_value=0)
```

## 3 Slicing and Indexing DataFrames 索引与切片

### 3.1 设置/重置索引

```python
# 将指定列设为行索引
df = df.set_index("column_name")
# 将索引还原为普通列
df = df.reset_index()
```

### 3.2 多层索引

```python
# 创建双层索引
df = df.set_index(["country", "city"])
# 索引排序（多层切片前置操作）
df = df.sort_index()
```

### 3.3 .loc[] 按标签切片（行名、列名）

```python
# 取单行索引
df.loc["index_value"]
# 行区间切片
df.loc["Egypt":"India"]
# 多层索引元组区间切片
df.loc[("Egypt","Cairo") : ("India","Delhi")]
# 同时筛选行范围 + 列范围
df.loc[("Egypt","Cairo"):("India","Delhi"), 2005:2010]
```

### 3.4 .iloc[] 按数字位置切片

```python
df.iloc[0]              # 取第0行
df.iloc[1:5, 0:3]       # 行区间1~4，列区间0~2
```

### 3.5 透视表聚合运算

```python
# axis=0：按列（年份）求均值
mean_year = pivot_df.mean(axis=0)
# axis=1：按行（城市）求均值
mean_city = pivot_df.mean(axis=1)
```

## 4 Creating and Visualizing DataFrames 数据集创建、可视化、缺失值处理

### 4.1 Pandas 内置绘图

```python
# 柱状图
series.plot(kind="bar")
# 折线图
series.plot(kind="line")
# 散点图
df.plot(kind="scatter", x="x_col", y="y_col")
# 直方图：alpha透明度，bins柱子数量
df[df.type=="A"]["price"].hist(label="A", alpha=0.5, bins=20)
# Matplotlib 美化设置
plt.title("Title")
plt.legend()
plt.show()
```

### 4.2 缺失值处理

```python
df.isna()                 # 布尔矩阵标记所有缺失位置
df.isna().any()           # 判断每列是否存在缺失值
df.isna().sum()           # 统计每列缺失数量
df.isna().sum().plot(kind="bar") # 缺失值数量柱状可视化
df.dropna()               # 删除包含缺失值的整行
df.fillna(value=0)        # 使用固定值填充缺失
```

### 4.3 手动构造 DataFrame

```python
# 方式1：字典列表（一行一个字典）
data_list = [
    {"date":"2019-11-03", "small_sold":10376832},
    {"date":"2019-11-10", "small_sold":10717154}
]
df = pd.DataFrame(data_list)

# 方式2：列表字典（键为列名，值为列数据）
data_dict = {
    "date":["2019-11-03","2019-11-10"],
    "small_sold":[10376832,10717154]
}
df = pd.DataFrame(data_dict)
```

### 4.4 CSV 文件读写

```python
# 读取CSV文件
df = pd.read_csv("data.csv")
# 导出CSV，index=False 不导出行索引
df.to_csv("output.csv", index=False)
```

---

## 三、Joining Data with pandas（Datacamp 全课程整理）

核心思想：把多个 DataFrame 按“键”关联起来，类似 SQL JOIN。  
主要函数：`pd.merge()`、`pd.concat()`、`pd.merge_ordered()`、`pd.merge_asof()`、`.query()`、`.melt()`。

### 1. Data Merging Basics（基础合并）

#### 1.1 内连接（inner join）——只保留两边都有的键

```python
# 最常用写法（默认 how='inner'）
pd.merge(left_df, right_df, on="key_column")

# 键名不同时
pd.merge(left_df, right_df, left_on="left_key", right_on="right_key")

# 多列作为键
pd.merge(left_df, right_df, on=["col1", "col2"])
```

- **one-to-one**：两边键都唯一 → 结果行数 ≈ 匹配的键数量  
- **one-to-many**：一边键唯一、另一边有重复 → 结果行数 = 多的那边匹配行数  
- **many-to-many**：两边都有重复 → 结果是笛卡尔积（慎用）

#### 1.2 多表连续合并

```python
# 先合并两表，再与第三表合并
merged = pd.merge(df1, df2, on="key")
final = pd.merge(merged, df3, on="key")
```

### 2. Merging Tables With Different Join Types（不同连接类型）

| how 参数 | SQL 等价 | 保留哪些行 | 缺失值处理 |
|----------|----------|------------|------------|
| `'inner'`（默认） | INNER JOIN | 两边都有的键 | 无缺失 |
| `'left'` | LEFT OUTER JOIN | 左表全部 + 右表匹配 | 右表无匹配填 NaN |
| `'right'` | RIGHT OUTER JOIN | 右表全部 + 左表匹配 | 左表无匹配填 NaN |
| `'outer'` | FULL OUTER JOIN | 两边所有键的并集 | 无匹配填 NaN |

```python
# 左连接（最常用，保留主表全部记录）
pd.merge(left_df, right_df, on="key", how="left")

# 右连接
pd.merge(left_df, right_df, on="key", how="right")

# 外连接（完整并集）
pd.merge(left_df, right_df, on="key", how="outer")
```

#### 2.1 自连接（Self Join）

同一张表与自己合并（常用于找层级关系、前后续关系）：

```python
# 例如找电影的续集
pd.merge(movies, movies, left_on="id", right_on="sequel_id", suffixes=("_original", "_sequel"))
```

#### 2.2 基于索引合并

```python
# 两边都用索引作为键
pd.merge(left_df, right_df, left_index=True, right_index=True)

# 左边用列，右边用索引
pd.merge(left_df, right_df, left_on="key", right_index=True)
```

### 3. Advanced Merging and Concatenating（高级合并与拼接）

#### 3.1 Semi-join（半连接）——只保留左表中“在右表有匹配”的行

```python
# 方法：先 inner merge，再只取左表列，或用 isin
semi = left_df[left_df["key"].isin(right_df["key"])]
# 或
merged = pd.merge(left_df, right_df[["key"]], on="key")   # 只取右表的键列
```

#### 3.2 Anti-join（反连接）——只保留左表中“在右表没有匹配”的行

```python
# 经典写法（使用 indicator）
merged = pd.merge(left_df, right_df, on="key", how="left", indicator=True)
anti = merged[merged["_merge"] == "left_only"].drop(columns="_merge")
```

#### 3.3 垂直拼接（concat）

```python
# 按行堆叠（最常用）
pd.concat([df1, df2, df3], ignore_index=True)          # 重置索引
pd.concat([df1, df2], keys=["groupA", "groupB"])       # 添加多层索引标识来源

# 按列拼接（axis=1）
pd.concat([df1, df2], axis=1)
```

#### 3.4 验证合并完整性（validate）

```python
# 强制检查关系类型，不匹配会报错
pd.merge(left, right, on="key", validate="one_to_one")      # 两边键都必须唯一
pd.merge(left, right, on="key", validate="one_to_many")     # 左键唯一
pd.merge(left, right, on="key", validate="many_to_one")     # 右键唯一
pd.merge(left, right, on="key", validate="many_to_many")    # 允许两边都重复
```

### 4. Merging Ordered and Time-Series Data（有序 / 时间序列合并）

#### 4.1 merge_ordered() —— 有序合并（类似 outer + 排序）

适合时间序列、经济数据等已排序数据：

```python
pd.merge_ordered(left, right, on="date", fill_method="ffill")  # 向前填充缺失
pd.merge_ordered(left, right, on=["year", "month"], how="left")
```

#### 4.2 merge_asof() —— 最近匹配合并（非精确匹配）

常用于股票、传感器等“最近时间点”匹配：

```python
# 默认向后匹配（direction='backward'）
pd.merge_asof(left, right, on="timestamp")

# 向前匹配 / 最近匹配
pd.merge_asof(left, right, on="timestamp", direction="forward")
pd.merge_asof(left, right, on="timestamp", direction="nearest")

# 限制最大时间差
pd.merge_asof(left, right, on="timestamp", tolerance=pd.Timedelta("1day"))
```

#### 4.3 .query() —— SQL 风格筛选（字符串表达式）

```python
df.query("col1 > 100 and col2 == 'A'")
df.query("col1 > @threshold")          # 使用外部变量（加 @）
```

#### 4.4 .melt() —— 宽表转长表（unpivot）

```python
# 把多列变成两列（variable + value）
df.melt(id_vars=["id", "name"],           # 保持不变的列
        value_vars=["2020", "2021", "2022"],  # 要融化的列
        var_name="year",                  # 新变量列名
        value_name="sales")               # 新数值列名
```

---

### 快速对比总结

| 场景 | 推荐方法 |
|------|----------|
| 精确键匹配 + 各种 JOIN | `pd.merge(..., how=...)` |
| 只想知道“有没有匹配” | semi-join / anti-join |
| 按行堆叠多表 | `pd.concat(..., axis=0)` |
| 时间序列有序合并 | `pd.merge_ordered()` |
| 最近时间点匹配 | `pd.merge_asof()` |
| 宽表 → 长表 | `.melt()` |
| 类 SQL 条件筛选 | `.query()` |

## 四、Introduction to Statistics in Python

### 描述统计 Descriptive statistics

提炼样本数据特征，**仅总结当前已有数据**
均值、中位数、方差、四分位数、图表（直方图、箱线图）都属于描述统计。

### 推断统计 Inferential statistics

利用样本数据，**推测更大总体（population）** 的性质。
例：抽样调查，用样本均值估计全国均值。

## 1. 数据类型分类

- **Numerical 数值型（定量）**
  - Continuous 连续型：可以取区间内任意数字（碳排放、价格、重量）
  - Discrete 离散型：只能取独立数值（商品数量、订单个数）
- **Categorical 分类型（定性）**
  - Nominal 名义型：无大小顺序（食物种类、国家名称）
  - Ordinal 有序型：存在顺序关系（评级：差/良/优）

## 2. Measures of center 集中趋势

### Mean 均值

$$\bar{x}=\frac{\sum x_i}{n}$$

- 对**极端异常值很敏感**
- 数据近似对称分布时适合使用

### Median 中位数（Q2，50%分位数）

排序后正中间的数值

- **不受异常值影响**
- 数据存在偏态、含有离群点优先选择中位数

### 分布形态规律

1. **右偏分布（正偏）**：均值 > 中位数
2. **左偏分布（负偏）**：均值 < 中位数
3. **对称分布**：均值 ≈ 中位数

## 3. Measures of spread 离散程度

### Variance 方差

衡量数据波动大小，单位是原始数据单位的平方
$$\sigma^2=\frac{\sum(x_i-\bar{x})^2}{n}$$

### Standard deviation 标准差

方差开平方根；**单位和原始数据一致**，更常用。

> Pandas 聚合代码

```python
df['col'].agg(['mean','median','var','std'])
```

## 4. Quantiles 分位数体系

- **Quartiles 四分位数**：`0.25, 0.5, 0.75`（Q1、Q2、Q3）
- **Quintiles 五分位数**：`0.2, 0.4, 0.6, 0.8`
- **Deciles 十分位数**：`0.1,0.2,...,0.9`

### 代码两种写法

```python
# Numpy（课程常考）
import numpy as np
np.quantile(df['co2'], [0.25, 0.5, 0.75])
# 使用linspace自动生成点位
np.quantile(data, np.linspace(0.1,0.9,9))

# Pandas
df['co2'].quantile([0.25,0.5,0.75])
```

## 5. IQR & 异常值检测（Outliers）

1. $IQR = Q3 - Q1$ 四分位距
2. 边界阈值：
$$lower = Q1 - 1.5\times IQR$$
$$upper = Q3 + 1.5\times IQR$$
3. 判断规则：
数值 < lower **或** 数值 > upper → 判定为异常值

### 完整标准代码模板

```python
# 计算四分位数
q1 = np.quantile(data, 0.25)
q3 = np.quantile(data, 0.75)
iqr = q3 - q1

# 上下边界
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# 筛选异常值（Series筛选，注意使用 | 代替or，条件带括号）
outliers = data[(data < lower) | (data > upper)]
```

## 6. 配套可视化工具

- **直方图 `.hist()`**：观察数值分布形态、判断偏态
  - X：变量数值；Y：区间内样本数量
  - `bins` 控制区间数量
- **箱线图 `.boxplot()`**：直观展示四分位数、识别异常值
  - 箱体：Q1 ~ Q3（中间50%数据）
  - 箱体中线：中位数
  - 须以外圆点 = 异常值

---

## 五、Sowing Success 项目（机器学习选作物）

### 项目背景
农民要根据土壤指标选择最适宜种植的作物。本项目用监督式多分类模型，
根据土壤中的氮(N)、磷(P)、钾(K)、pH 四项指标预测最适合作物(crop)，
并找出对预测贡献最大的单一特征。

数据集 `soil_measures.csv`：2200 行 × 5 列，22 种作物每类各 100 条
（完全均衡），无缺失值、无重复行。

### 建模思路
- **目标一**：预测 crop（22 类多分类）。
- **目标二**：找出"最重要的单一特征"。做法不是用一个大模型，
  而是**每个特征单独训练一个模型**，比较谁单独预测得最准——
  最准的那个特征信息量最大。
- **模型**：每个特征用 `LogisticRegression`（包 `StandardScaler` 标准化），
  作为表格数据的标准 baseline。
- **评估**：按 80/20 分层切分（`stratify=y`），用测试集准确率比较特征。

### 关键步骤（完整代码见 `workspace/notebook.ipynb`）
```python
X = crops[["N", "P", "K", "ph"]]     # 4 个输入特征
y = crops["crop"]                    # 目标变量
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 逐特征建模，把每个特征的测试准确率存进字典
feature_performance = {}
for f in ["N", "P", "K", "ph"]:
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=5000, class_weight="balanced")),
    ])
    model.fit(X_train[[f]], y_train)
    feature_performance[f] = accuracy_score(y_test, model.predict(X_test[[f]]))
best_feature = max(feature_performance, key=feature_performance.get)
```

### 结果
单特征测试准确率：N=0.139、P=0.191、**K=0.280**、pH=0.098。
→ **最重要的单一特征是 K（钾）**：若农民只能测一项土壤指标，测钾对选作物最有帮助。

> 注：单特征模型准确率偏低是设计使然，目的只是给特征排重要性顺序；
> 把 4 个特征合并成一个模型，预测准确率会明显提高。
