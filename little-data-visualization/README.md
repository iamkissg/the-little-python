# Python 编程: 从入门到实践 数据可视化项目

- 随机漫步: 每次行走都完全是随机的, 没有明确的方向, 结果由一系列随机决策决定. 自然界中, 随机漫步有实际用途
- nw\_visual\*.py 和 random\_walk\*.py 是随机漫步的例子

## matplotlib ref

- 标准的导入姿势: `import matplotlib.pyplot as plt`
- `plt.plot()` - 绘制折线图, `linewidth` 关键字参数用于设置线宽
- `plt.show()` - 显示绘制的图形
- `plt.title()` - 设置标题, 通过 `fontsize` 关键字参数设置字体大小
- `plt.xlabel()` - 设置 X 轴标签, 通过 `fontsize` 关键字参数设置字体大小
- `plt.ylabel()` - 设置 Y 轴标签, 通过 `fontsize` 关键字参数设置字体大小
- `plt.tick_params()` - 设置刻度标记的大小, `axis` 关键字参数选择轴, `labelsize` 关键字参数设置刻度标记的字号, `which`
- 向绘图函数传递单个数据集时, 以数据集为 Y 轴数据, 索引为 X 轴坐标, 索引从 0 开始. 当传入两个数据集, 前一个作为 X 轴数据, 后一个作为 Y 轴数据
- `plt.scatter()` - 绘制散点图, `s` 关键字参数设置点的尺寸, `edgecolor` 关键字参数设置数据点轮廓颜色, 为 `none` 则删除轮廓, `c` 关键字参数设置数据点颜色, 可以是代表颜色的字符串, 或 RGB 元组 (0~1 取值)
- 在已有一组数据的情况下, 用列表生成式以某个映射关系生成另一组数据
- `plt.axis()` - 设置坐标轴取值范围, 通常用 `[xmin, xmax, ymin, ymax]` 的列表
- 在可视化中, 颜色映射 (colormap) 用于突出数据的规律
- 散点图的颜色映射: 将关键字参数 c 设置成一个值的列表, 再使用参数 cmap 告诉 pyplot 使用哪个颜色映射, 比如: `plt.scatter(x, y, c=y, cmap=plt.cm.Blues, edgecolor="none", s=40)`. 使用颜色映射时, 要注意删除轮廓, 否则轮廓粘连在一起, 就覆盖了颜色映射
- `plt.savefig()` - 保存图表到文件, `bbox_inches` 关键字参数可用于裁剪掉图表多余的空白区
- 隐藏坐标轴: `plt.axes().get_xaxis().set_visible(False)`
- 图表适合屏幕大小时, 更能有效地将数据中的规律呈现出来
- `plt.figure(figsize=(10, 6))` - 设置图表的宽高, 分辨率和背景色. `figsize` 关键字用于指定窗口的尺寸, 单位为英寸, 用 tuple 表示, `dpi` 关键字参数设置分辨率 (每英寸像素点数), 以有效地利用可用的屏幕空间

