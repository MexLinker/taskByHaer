from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits import axisartist

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题


from pandas.plotting import register_matplotlib_converters
import os  # 导入os模块，用于文件路径操作
register_matplotlib_converters()

# Set the folder path
folder_path = './'  # 替换为你的文件夹路径

# 商品推广.xlsx


def plotF():
    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):  # Check if the file is an Excel file
            file_path = os.path.join(folder_path, file_name)
            data = pd.read_excel(file_path)
            data['日期'] = pd.to_datetime(data['日期'])
            data.sort_values('日期', inplace=True)

            # Start plotting
            plt.figure(figsize=[15, 10])

            # Plot 1: 展示量、点击量和花费随时间的变化

            data['花费'] = 1000 * data['花费']
            data['点击量'] = 100 * data['点击量']

            plt.subplot(3, 1, 1)
            plt.plot(data['日期'], data['展示量'], label='展示量', linestyle='solid', alpha=0.5)
            plt.plot(data['日期'], data['点击量'], label='点击量', linestyle='dashed')
            plt.plot(data['日期'], data['花费'], label='花费', alpha=0.3, linestyle='dotted')
            plt.title(f'{file_name} - 展示量、点击量和花费随时间的变化')
            plt.xlabel('日期')
            plt.ylabel('数量/金额')
            plt.legend()

            # Plot 2: 广告成本销售比(ACOS)和投入产出比(ROAS)随时间的变化
            plt.subplot(3, 1, 2)
            plt.plot(data['日期'], data['广告成本销售比(ACOS)'], label='ACOS')
            plt.plot(data['日期'], data['投入产出比(ROAS)'], label='ROAS')
            plt.title(f'{file_name} - 广告成本销售比(ACOS)和投入产出比(ROAS)随时间的变化')
            plt.xlabel('日期')
            plt.ylabel('比率')
            plt.legend()

            # Plot 3: 7天总订单数和7天总销售额随时间的变化
            plt.subplot(3, 1, 3)
            plt.plot(data['日期'], data['7天总订单数(#)'], label='7天总订单数')
            plt.plot(data['日期'], data['7天总销售额'], label='7天总销售额')
            plt.title(f'{file_name} - 7天总订单数和7天总销售额随时间的变化')
            plt.xlabel('日期')
            plt.ylabel('数量/金额')
            plt.legend()

            plt.tight_layout()
            plt.savefig(os.path.join(folder_path, f'{file_name}_charts.png'))  # Save the figure to the same folder
            plt.close()  # Close the plot to avoid overlapping of figures

plotF()