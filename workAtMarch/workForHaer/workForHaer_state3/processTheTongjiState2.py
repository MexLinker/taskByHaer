import pandas as pd
import plotly.express as px

file_path = './统计.xlsx'  # 更换为您的文件路径
sheets = ['曝光量', '点击量', 'CTR', 'CVR', '花费', 'CPC', 'ACOS', '广告订单', '销售额', '直接成交销售额']

for sheet in sheets:
    df = pd.read_excel(file_path, sheet_name=sheet)
    df_melted = df.melt(id_vars=[df.columns[0]], var_name='日期', value_name=sheet)
    fig = px.line(df_melted, x='日期', y=sheet, color=df.columns[0], title=f'{sheet}随时间的变化')
    fig.update_traces(mode='lines+markers')  # 添加标记以提高清晰度
    fig.update_layout(hovermode='x')  # 改进悬停模式以便同时查看所有关键词
    # 使图表中的线条在未被选中时透明度降低
    fig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color, width=0.5), opacity=0.1))
    # 设置日期轴的显示格式
    fig.update_xaxes(tickformat='%Y-%m-%d')
    fig.show()