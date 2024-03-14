import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Load your data
file_path = '你的数据文件路径.xlsx'  # 替换为你的Excel文件路径
data = pd.read_excel(file_path)
data['日期'] = pd.to_datetime(data['日期'])
data.sort_values('日期', inplace=True)

# Start plotting
plt.figure(figsize=[15, 10])

# Plot 1: 展示量、点击量和花费随时间的变化
plt.subplot(3, 1, 1)
plt.plot(data['日期'], data['展示量'], label='展示量')
plt.plot(data['日期'], data['点击量'], label='点击量')
plt.plot(data['日期'], data['花费'], label='花费')
plt.title('展示量、点击量和花费随时间的变化')
plt.xlabel('日期')
plt.ylabel('数量/金额')
plt.legend()

# Plot 2: 广告成本销售比(ACOS)和投入产出比(ROAS)随时间的变化
plt.subplot(3, 1, 2)
plt.plot(data['日期'], data['广告成本销售比(ACOS)'], label='ACOS')
plt.plot(data['日期'], data['投入产出比(ROAS)'], label='ROAS')
plt.title('广告成本销售比(ACOS)和投入产出比(ROAS)随时间的变化')
plt.xlabel('日期')
plt.ylabel('比率')
plt.legend()

# Plot 3: 7天总订单数和7天总销售额随时间的变化
plt.subplot(3, 1, 3)
plt.plot(data['日期'], data['7天总订单数(#)'], label='7天总订单数')
plt.plot(data['日期'], data['7天总销售额'], label='7天总销售额')
plt.title('7天总订单数和7天总销售额随时间的变化')
plt.xlabel('日期')
plt.ylabel('数量/金额')
plt.legend()

plt.tight_layout()
plt.show()
