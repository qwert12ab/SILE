import streamlit as st
import pandas as pd
st.markdown('# 学生 雷某 数据档案')
st.markdown('## 😜基础信息')
st.text('''精神状态🤔：累！！！
当前教室：实训204''')
st.markdown('## 🖐拥有的技能')
st.subheader('技能拥有情况')
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="python", value="10%", delta="10%")
c2.metric(label="java", value="70%", delta="-10%")
c3.metric(label="bilibil", value=None, delta="0", delta_color="off")
import streamlit as st  # 导入Streamlit并用st代表它
st.markdown('## python Streamlit学习进度')


# 定义数据,以便创建数据框
st.markdown('## 🖐工作日志')
data = {
    '日期':['2025.10.12','2025.10.13','2025.10.14'],
    '任务':['学习python','学习剪辑','整理书籍'],
    '状态':['✅完成','正在进行中','🗙未完成'],
    '难度':['⭐⭐⭐','⭐⭐','⭐️⭐️⭐️⭐️⭐️']}

index = pd.Series(['1', '2', '3'])
df = pd.DataFrame(data, index=index)
st.write(df)
st.markdown('## 🔑最新代码成果')
st.subheader('Python代码块')
python_code='''
a=12343
b=1123
c=a+b
print(c)
'''
st.code(python_code, line_numbers=True)
st.markdown('***')
st.markdown(':green[>>SYSTEN MESSAGE:]''下一个任务目标已解锁....')
st.markdown(':green[>>TARGET]''课程管理系统')
st.markdown(':green[>>2025.10.20 13:40:12]')


