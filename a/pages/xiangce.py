import streamlit as st
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
    
if 'ind'not in st.session_state:
    st.session_state['ind']=0

def BackImg():
    st.session_state['ind']=(st.session_state['ind']-1)%len(images)

def NextImg():
    st.session_state['ind']=(st.session_state['ind']+1)%len(images)
st.image(images[st.session_state['ind']]['ur1'],caption=images[st.session_state['ind']]['parm'])

c1,c2=st.columns(2)

with c1:
    st.button('上一张',on_click=BackImg,use_container_width=True)
with c2:
    st.button('下一张',on_click=NextImg,use_container_width=True)
   






   

