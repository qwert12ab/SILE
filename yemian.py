import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
st.title("😡作业大礼包")
tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["雷某学生档案", "南宁美食探索", "简易音乐播放器","熊出没视频网站","动物相册","奶龙个人简介"])
with tab1:
    
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
with tab2:
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
with tab3:   
    st.markdown('# 🎹简易音乐播放器🥰')
    st.markdown('### :red[使用streamlit制作的简单音乐播放器,支持切歌和基本播放控制]😃')
    st.set_page_config(page_title="音乐会",page_icon='🎶',layout='wide')
    images=[
        {'ur1':'https://music.163.com/song/media/outer/url?id=191248.mp3',
         'parm':'张杰明天过后',
         'author':'张杰',
         'work' :'2008年，发行专辑《明天过后》同年，获得韩国MAMA亚洲最佳歌手奖。 2012年，在人民大会堂开启个人首轮巡演',
         'photo':'https://p1.music.126.net/ixIs5kkukgNYMmeDsc35_g==/29686813955450.jpg'},
        {'ur1':'https://music.163.com/song/media/outer/url?id=1406649619.mp3',
         'parm':'颜人中',
         'author':'颜人中',
         'work':'颜人中，男，1994年6月17日出生于台湾省，中国台湾创作型流行乐男歌手,同年，发行个人首张EP《失眠症候群》',
         'photo':'https://p1.music.126.net/8DkTnzi7jdjWGYl4qbwLCg==/109951164517295956.jpg'},
        {'ur1': 'https://music.163.com/song/media/outer/url?id=1369601580.mp3',
         'parm':'颜人中',
         'author':'颜人中',
         'work':'颜人中，男，1994年6月17日出生于台湾省，中国台湾创作型流行乐男歌手,2019年6月5日，与说唱歌手VAVA合作演唱的歌曲《祝你爱我到天荒地老》正式上线',
         'photo':'https://p1.music.126.net/HUndbFyGT5_Eiei0pbiK-w==/109951164124732670.jpg'},
        ]

    
    if 'ind'not in st.session_state:
        st.session_state['ind']=0

    def BackImg():
        st.session_state['ind']=(st.session_state['ind']-1)%len(images)

    def NextImg():
        st.session_state['ind']=(st.session_state['ind']+1)%len(images)

    a1,a2=st.columns([1,2])
    with a1:
        st.image(images[st.session_state['ind']]['photo'],caption=images[st.session_state['ind']]['parm'])
    with a2:
        st.title(images[st.session_state['ind']]['author'])
        st.subheader(images[st.session_state['ind']]['work'])
        st.audio(images[st.session_state['ind']]['ur1'])


    c1,c2=st.columns(2)

    with c1:
        st.button('上一首',on_click=BackImg,use_container_width=True)
    with c2:
        st.button('下一首',on_click=NextImg,use_container_width=True)

    st.markdown('***')
with tab4:

    import streamlit as st
    st.set_page_config(page_title='😝视频网站',page_icon='😃')
#视频地址
    video_url=[{
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/38/12/1374211238/1374211238-1-192.mp4?e=ig8euxZM2rNcNbR1hbdVhwdlhWRghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&og=hw&oi=771356656&uipk=5&platform=html5&gen=playurlv3&nbs=1&trid=c9c7ff17ba5b4c4b867912e7c7b3f4fh&mid=0&deadline=1761302246&os=cosovbv&upsig=160ae404bce0892f2ec67c13f06a618e&uparams=e,og,oi,uipk,platform,gen,nbs,trid,mid,deadline,os&bvc=vod&nettype=0&bw=903323&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
    'title':'熊出没鬼畜视频',
    'work' :'熊出没做早操',
    'profile':'素材出自《熊出没之环球大冒险》第32集 真假松鼠 ',
    'episode':'1'
    },{
     'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/16/01/26791510116/26791510116-1-192.mp4?e=ig8euxZM2rNcNbRa7zdVhwdlhWuahwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&mid=0&oi=771356656&uipk=5&deadline=1761302442&gen=playurlv3&os=cosovbv&og=ali&platform=html5&trid=20c5ce2f9f86482d8882c8d9a86376dh&upsig=d44795a5f97b4513eda30ec62f7d12ca&uparams=e,nbs,mid,oi,uipk,deadline,gen,os,og,platform,trid&bvc=vod&nettype=0&bw=1420893&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
     'title':'熊出没鬼畜视频',
     'work' :'光头强单人合集',
     'profile':'BGM：APT 作者：幻生寻寻子',
     'episode':'2'
     },{
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/22/44/1393504422/1393504422-1-192.mp4?e=ig8euxZM2rNcNbNjhwdVhwdlhbTVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1761302540&nbs=1&trid=2f12db9f4ef34c7a9c54c9fb780a689h&mid=0&oi=771356656&platform=html5&uipk=5&gen=playurlv3&os=cosovbv&og=cos&upsig=8d2deb0fd6a1525b90723f1a941cac85&uparams=e,deadline,nbs,trid,mid,oi,platform,uipk,gen,os,og&bvc=vod&nettype=0&bw=2091234&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
    'title':'熊出没鬼畜视频',
    'work' :'熊出没春节神曲',
    'profile':'BGM：春节序曲，步步高，喜洋洋,作者:S_venti',
    'episode':'3'
    }]
           
    if 'ind' not in st.session_state:
        st.session_state['ind']=0
    st.title(video_url[st.session_state['ind']]['title']+'-第'+video_url[st.session_state['ind']]['episode']+'集')
    
    st.video(video_url[st.session_state['ind']]['url'])
    st.subheader(video_url[st.session_state['ind']]['work'])
    st.subheader(video_url[st.session_state['ind']]['profile'])

    c1,c2,c3=st.columns(3)
    def play(arg):
    #点击哪个按钮就播放几集
        st.text(arg)
        st.session_state['ind']=int(arg)
    for i in range(len(video_url)):
        
        st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))
with tab5:
    st.set_page_config(page_title="动物园",page_icon='🦁')
    images=[
    {'ur1':'https://img95.699pic.com/photo/30725/4843.jpg_wh300.jpg',
     'parm':'狗'},
    {'ur1':'https://wallpapercat.com/w/full/6/5/4/24272-1920x1440-desktop-hd-dog-wallpaper.jpg',
     'parm':'狗'},
    {'ur1': 'https://www.collinsdictionary.com/images/full/dog_230497594.jpg?version=4.0.119',
     'parm':'狗'},
    {'ur1':'https://eskipaper.com/images/birds-7.jpg',
     'parm':'一只好看的鸟'},
    {'ur1':'https://dinoanimals.com/wp-content/uploads/2023/03/Secretarybird.jpg',
     'parm':'一只酷酷的鸟'}]
    
    if 'ide'not in st.session_state:
        st.session_state['ide']=0

    def BackImg():
        st.session_state['ide']=(st.session_state['ide']-1)%len(images)

    def NextImg():
        st.session_state['ide']=(st.session_state['ide']+1)%len(images)
    st.image(images[st.session_state['ide']]['ur1'],caption=images[st.session_state['ide']]['parm'])

    c1,c2=st.columns(2)

    with c1:
        st.button('上一张',on_click=BackImg,use_container_width=True)
    with c2:
        st.button('下一张',on_click=NextImg,use_container_width=True)
with tab6:
    st.title("📍奶龙")
    st.set_page_config(page_title="作业大礼包", page_icon="⌨️", layout="wide")
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

    
   

         
     









    





    
