import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# 加载数据集
df = pd.read_csv('student_data_adjusted_rounded.csv')

# 提取特征和目标变量
X = df[['每周学习时长（小时）', '上课出勤率', '期中考试分数', '作业完成率']]
y = df['期末考试分数']

# 特征标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 训练随机森林回归模型
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 模型评估
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
st.sidebar.markdown(f"**模型平均绝对误差**：{mae:.2f} 分")  # 侧边栏展示模型性能

def predict_grade(study_hours, attendance, midterm, homework):
    # 特征标准化（与训练时保持一致）
    X_test = np.array([[study_hours, attendance, midterm, homework]])
    X_test_scaled = scaler.transform(X_test)
    pred = model.predict(X_test_scaled)[0]
    # 限制分数在0-100之间
    pred_clipped = max(0, min(pred, 100))
    return round(pred_clipped, 1)

def show_grade_prediction():
    st.title("🔮 期末成绩预测")
    st.markdown("请输入学生的学习信息，系统将预测其期末成绩并提供学习建议")

    # 输入表单
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("学号", value="1231231")
            st.selectbox("性别", ["男", "女"])
            st.selectbox("专业", ["信息系统", "人工智能", "计算机", "数据科学", "大数据管理", "软件工程"])
        with col2:
            study_hours = st.slider("每周学习时长(小时)", 0, 50, 10)
            attendance = st.slider("上课出勤率", 0, 100, 100)
            midterm = st.slider("期中考试分数", 0, 100, 40)
            homework = st.slider("作业完成率", 0, 100, 80)
        submit = st.form_submit_button("预测期末成绩", type="primary")

    # 预测结果展示
    if submit:
        pred_grade = predict_grade(study_hours, attendance, midterm, homework)
        st.subheader("🎯 预测结果")
        st.markdown(f"**预测期末成绩：{pred_grade} 分**")
        
        # 更细化的学习建议 + 图片展示
        if pred_grade >= 90:
            st.success("学习建议：你已无敌，建议去竞争更高水平")
            st.image("https://k.sinaimg.cn/n/sinakd20107/580/w690h690/20250210/cf24-9f09b54d0c5e95280c5d9ce2654d4df4.jpg/w700d1q75cms.jpg", 
                     caption="顶尖水平学习建议配图", use_container_width=True)
        elif pred_grade >= 80:
            st.success("学习建议：针对薄弱知识点进行专题突破，有望冲刺更高分！")
            st.image("https://c-ssl.duitang.com/uploads/blog/202202/08/20220208025607_de042.jpg", 
                     caption="高分段学习建议配图", use_container_width=True)
        elif pred_grade >= 70:
            st.info("学习建议：定期进行错题复盘，期末可稳定提分！")
            st.image("https://c-ssl.dtstatic.com/uploads/blog/202408/09/1mSg5wAOsQVY3jz.thumb.1000_0.jpeg", 
                     caption="中分段学习建议配图", use_container_width=True)
        elif pred_grade >= 60:
            st.info("恭喜你刚好过了！")
            st.image("https://c-ssl.duitang.com/uploads/blog/202406/21/pGSpe77OSB8qqB5.jpeg", 
                     caption="及格线附近学习建议配图", use_container_width=True)
        else:
            st.warning("学习建议：没救了！还不去求老师海底捞！！！")
            st.image("https://c-ssl.dtstatic.com/uploads/blog/202406/21/V2S5XNNJim299E3.thumb.400_0.jpeg", 
                     caption="待提升学习建议配图", use_container_width=True)
