import streamlit as st
from datetime import datetime, timedelta
st.title("📍奶龙")
st.set_page_config(page_title="奶龙简历", page_icon="📍", layout="wide")
c1,c2=st.columns([3,3])
with c1:
    st.subheader('奶龙个人信息表单')
    name=st.text_input('姓名',autocomplete='name')
    work=st.text_input('职位',autocomplete='work')
    phonenumber=st.text_input('电话',autocomplete='phonenumber')
    email=st.text_input('邮箱',autocomplete='email')
    date = st.date_input("出生日期", value=None)
    st.text('性别')
    gender = st.radio(
    '你的性别是:',
    ['男', '女', '奶龙'],
    horizontal=True,
    label_visibility='hidden'
)
    st.text('语言能力')
    language = st.selectbox(
    '你会的语言有？',
    ['中文', '英文', '日语','阿拉伯语','西班牙语'],
    label_visibility='hidden'
)
    st.text('学历')
    degree = st.selectbox(
    '你的学历是',
    ['高中', '专科', '本科','硕士','博士'],
    label_visibility='hidden'
)
    skill = st.multiselect(
    '你拥有的技能',
    ['Python', 'javaScript', 'HTML/CSS', 'SQL', '数据分析','机器学习','深度学习','项目管理','UI/UX设计'],
    
    max_selections=4)
    age=st.slider('工作经验(年)',0,30)
    init_text ='背景故事'
    person1=st.text_area(label='奶龙背景故事', value=init_text,
            height=200, max_chars=200)
    init_text1 ='性格特点'
    person=st.text_area(label='奶龙性格特点', value=init_text,
            height=200, max_chars=200)
    
    w1 = st.time_input("每日最佳联系时间段")
    photo=st.file_uploader("奶龙图片",type=['jpg','png','jpeg'])    
with c2:
    st.subheader('简历实时预览')
    st.markdown('***')
    if photo:
        st.image(photo,caption='我是奶龙',width=200)
    a1,a2=st.columns(2)
    st.markdown('***')
    st.subheader('背景故事')
    st.write(person1)
    st.subheader('性格特点')
    st.write(person)
    
    
    with a1:
        st.write('名字:',name)
        st.write('职位:',work)
        st.write('电话:',phonenumber)
        st.write('邮箱:',email)
        s=''
        for yuyan in skill:
            s=s+ yuyan
        st.write(f'技能:{s}')
    with a2:
        st.write("出生日期:", date)
        st.write(f'性别:{gender}')
        st.write('语言能力',language)
        st.write(f'你的学历是:{degree}')
        st.write('工作经验:',age,'年')
        st.write("你选择时间1是:", w1)
        
    
