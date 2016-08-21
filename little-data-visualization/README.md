# Python 编程: 从入门到实践 数据可视化项目

- `数据可视化`指的是通过可视化表示来探索数据, 与`数据挖掘`紧密相关. `数据挖掘`指的是使用代码来探索数据集的规律和关联
- **说白了, 数据可视化就是一种展示的工具**
- Pygal 包, 是一个专注于生成适合在数字设备上显示的图表的第三方包. 通过使用 Pygal, 可在用户与图表交互时突出元素以及调整其大小, 还能轻松调整整个图表的尺寸
- 随机漫步: 每次行走都完全是随机的, 没有明确的方向, 结果由一系列随机决策决定. 自然界中, 随机漫步有实际用途
- nw\_visual\*.py 和 random\_walk\*.py 是随机漫步的例子
- 要处理各种真实世界的数据集, 必须能够访问并可视化各种类型和格式的在线数据
- Web API 是网站的一部分, 用于与使用非常具体的 URL 请求特定信息的程序交互. 请求称为 API 调用
- `https://api.github.com/` - 查看 GitHub 提供的 API
- 要准确地获悉 API 将返回哪些信息, 要么阅读文档, 要么使用代码打印 API 返回的内容
- 大多数 API 都存在速率限制, 即在特定时间内可执行的请求数存在限制. `https://api.github.com/rate_limit` 查看 GitHub 的限制

```json
{
  "resources": {
    "core": {
      "limit": 60,
      "remaining": 60,
      "reset": 1471747825
    },
    "search": {
      "limit": 10,  // 搜索 API 的极限速度为每分钟 10 个请求
      "remaining": 9,
      "reset": 1471744280
    }
  },
  "rate": {
    "limit": 60,
    "remaining": 60,
    "reset": 1471747825
  }
}
```
-

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
- `fig.autofmt_xdate(bottom=0.2, rotation=30, ha="right") - 调整时间轴标签, bottom 关键字参数用于设置标签到图表底部的距离, rotation 关键字参数用于设置旋转角度, 以更好的显示, 角度值
- `plt.fill_between(x, y1, y2=0, where=None, interpolate=False, step=None, hold=None, data=None, **kargs)` - 接收一个 X 值系列, 两个 Y 值系列, 并填充两个 Y 值系列之间的空间

## Pygal ref

- 直方图是一种条形图, 用于指出各种结果出现的频率
- `pygal.Bar()` - 创建条形图实例
- `obj.title = str` - 设置图表标题
- `obj.x_title = str` - 设置 X 轴标题
- `obj.y_title = str` - 设置 Y 轴标题
- `obj.x_labels = str` - 设置 X 轴标签
- `obj.add(title, values, **kwargs)` - add a serie to graph, title 指定的数据集名称, values 可以是 list-like obj 也可以是字典, 若两者都不是, 会尝试将其转换列表. values 为字典时:
 - value - 对于条形图, 指定高度
 - label - 鼠标悬停时, 具体的提示
 - xlink - 超链接
- `obj.render_to_file(filename)` - 将图表渲染成指定文件
- 散点图是 XY 类, value 需要是 list of tuple
- Pygal 中的地图制作工具要求数据为特定的格式: 用国别码表示国家, 用数字表示人口数量
- 处理地理政治数据时, 经常需要用到几个标准的国别码集. Pygal 使用的国别码集存储在模块 i18n (internationalization 的缩写), 字典 COUNTRIES 包含的键和值分别为**两个字母的国别码**和国家名
- Pygal 绘制世界地图, 会根据数字自动给不同国家着深浅不一的颜色 (比如人口越多, 颜色越深)
- `wm_style = RotateStyle("hcc")` -  用十六进制 RGB 颜色设置 Style, 返回一个 Style 对象, (需要导入: `from pygal.style import RotateStyle`), 之后在创建图表对象时, 用 style 关键字参数传入即可
- 使用 `LightColorizedStyle` 加亮, 但其不能自定义颜色. 但可以基于 `LightColorizedStyle`, 设置颜色 Style: `wm_style = RotateStyle("#336699", base_style=LightColorizedStyle)
- 创建图表的时候, 指定 `x_label_rotation` 用于旋转 X 轴标签, `show_legend=bool` 显示/隐藏图例
- 除了 Style 对象, Pygal 还允许创建 Config 对象, 分别用于保存风格和配置, 用于创建指定样式的图表
- `chart.x_labels` - 用列表为 X 轴标签命名
- 在 Pygal 中, 副标签是 X 轴以及 Y 轴上的部分标签, 主标签是 Y 轴上另一部分想要突出的标签
- `Config.truncate_label=int` - 对标签的长度做限制
- `Config.show_y_guides=bool` - 隐藏或显示图表中的水平线 (对于条形图 Bar)
- Pygal 允许为图表中的每个条形添加超链接
