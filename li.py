import streamlit as st
import pandas as pd
import numpy as np
import time
st.markdown("# 🍚南宁美食探索")
st.markdown("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")
st.markdown("## 🌏南宁美食地图")

restaurants_data={
    "餐厅":["好鸡品蒸鸡.烤鸡","开心辣卤鸭","邕味烧烤","螺蛳粉先生","凰姐卷筒粉"],
    "评分":["4.4","4.5","4.2","4.1","4.6"],
    "人均消费(元)":["20","30","15","17","20"],
    'latitude': [22.835601,22.851846,22.851292,22.857659,22.864649],
    'longitude': [108.224323,108.235502,108.239011,108.269416,108.251091]}



st.map(pd.DataFrame(restaurants_data))
st.markdown("## ⭐餐厅评分")
table = pd.DataFrame({
    "餐厅":restaurants_data['餐厅'],
    "评分":restaurants_data['评分']})
st.bar_chart(table)
st.markdown("## 💰不同类型餐厅的价格" )
r_table = pd.DataFrame({
    "餐厅":restaurants_data['餐厅'],
    "评分":restaurants_data['评分'],
    "人均消费(元)":restaurants_data['人均消费(元)'],
    })
st.write(r_table)
st.line_chart(r_table, x='人均消费(元)')
r_table.set_index('人均消费(元)',inplace=True)
st.line_chart(r_table, y='餐厅')
st.markdown("## 12月价格走势图")
data = {
    '月份':['01月','02月','03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'],
    '好鸡品蒸鸡':[200, 150, 180,260,270,180,310,330,360,420,450,433],
    '开心辣卤鸭':[120, 160, 123,230,259,296,310,350,390,410,462,455],
    '邕味烧烤':[250,210,320,360,380,399,409,419,460,455,489,514],
    '螺蛳粉先生':[110, 100, 160,220,260,270,290,299,318,356,399,419],
    '凰姐卷筒粉':[150,160,210,222,275,280,340,355,366,389,410,422]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series(['1','2','3','4','5','6','7','8','9','10','11','12'], name='月份')
# 将新索引应用到数据框上
df.index = index
st.subheader("餐厅")
st.line_chart(df, x='月份')

st.dataframe(df)
st.table(df)

st.markdown("## ⏰用餐高峰时刻")
st.markdown("## 🍽餐厅详情")
st.subheader("开心辣卤鸭")
c1,c2,c3 =st.columns(3)
c1.metric(label="评分",value="4.3/5.0",delta="10%")
c2.metric(label="人均消费",value="20",delta="0",delta_color="off")
c3.metric(label="推荐菜品:",value="❤卤鸭\n❤卤鸭掌\n❤鸡架")
st.markdown("## 当前拥挤程度")




