from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits import axisartist
import matplotlib.pyplot as plt




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




def plot1Of3():
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):  # Check if the file is an Excel file
            file_path = os.path.join(folder_path, file_name)
            data = pd.read_excel(file_path)
            data['日期'] = pd.to_datetime(data['日期'])
            data.sort_values('日期', inplace=True)

            # Start plotting
            # plt.figure(figsize=[15, 10])

            # Plot 1: 展示量、点击量和花费随时间的变化

            data['花费'] = 1000 * data['花费']
            data['点击量'] = 100 * data['点击量']

            # plt.subplot(3, 1, 1)

            host = host_subplot(111, axes_class=axisartist.Axes)#创建的画图板
            plt.subplots_adjust(right=0.75)#适应画板

            par1 = host.twinx()#建立增加的轴1
            par2 = host.twinx()#再建立一条轴2

            par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))#将轴2固定在右边离框60位置

            par1.axis["right"].toggle(all=True)#轴1放在右边
            par2.axis["right"].toggle(all=True)#轴2放在右边

            p1, = host.plot(data['日期'], data['展示量'], label="展示量", linestyle='solid', alpha=0.5)#默认轴在左边
            p2, = par1.plot(data['日期'], data['点击量'], label="点击量", linestyle='dashed', alpha=0.3)
            p3, = par2.plot(data['日期'], data['花费'], label="花费", linestyle='dotted')

            # plt.plot(data['日期'], data['展示量'], label='展示量', linestyle='solid', alpha=0.5)
            # plt.plot(data['日期'], data['点击量'], label='点击量', linestyle='dashed')
            # plt.plot(data['日期'], data['花费'], label='花费', alpha=0.3, linestyle='dotted')
            plt.title(f'{file_name} - 展示量、点击量和花费随时间的变化')
            plt.xlabel('日期')
            plt.ylabel('数量/金额')
            

            # host.set_xlim(0, 2)#设置x轴坐标
            # host.set_ylim(0, 2)#设置y轴坐标
            # par1.set_ylim(0, 4)
            # par2.set_ylim(1, 65)

            host.set_xlabel("日期")#设置标签
            host.set_ylabel("展示量/1次")
            par1.set_ylabel("点击量/0.01次")
            par2.set_ylabel("花费/0.001$")

            host.legend()

            host.axis["left"].label.set_color(p1.get_color())#设置曲线颜色
            par1.axis["right"].label.set_color(p2.get_color())
            par2.axis["right"].label.set_color(p3.get_color())

            plt.legend()
            # plt.show()

    # host = host_subplot(111, axes_class=axisartist.Axes)#创建的画图板
    # plt.subplots_adjust(right=0.75)#适应画板

    # par1 = host.twinx()#建立增加的轴1
    # par2 = host.twinx()#再建立一条轴2

    # par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))#将轴2固定在右边离框60位置

    # par1.axis["right"].toggle(all=True)#轴1放在右边
    # par2.axis["right"].toggle(all=True)#轴2放在右边

    # p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")#默认轴在左边
    # p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
    # p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")
            plt.savefig(os.path.join(folder_path, f'{file_name}_charts.png'))  # Save the figure to the same folder

plot1Of3()