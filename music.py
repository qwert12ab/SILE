import streamlit as st
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

