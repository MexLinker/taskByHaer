import pandas as pd
import plotly.express as px

# import plotly

# 文件路径和sheet名称，根据您的文件进行修改
file_path = './统计.xlsx'
sheets = ['曝光量', '点击量', 'CTR', 'CVR', '花费', 'CPC', 'ACOS', '广告订单', '销售额', '直接成交销售额']

# 遍历每个sheet来创建和显示交互式图表
for sheet in sheets:
    # 读取Excel文件的当前sheet
    df = pd.read_excel(file_path, sheet_name=sheet)

    # 假设Excel文件的第一列是关键词，其余列是日期
    # 转换DataFrame以适应Plotly，melt函数将DataFrame从宽格式变为长格式
    df_melted = df.melt(id_vars=[df.columns[0]], var_name='日期', value_name=sheet)

    # 创建交互式图表
    fig = px.line(df_melted, x='日期', y=sheet, color=df.columns[0], title=f'{sheet}随时间的变化')

    # 显示图表
    fig.show()