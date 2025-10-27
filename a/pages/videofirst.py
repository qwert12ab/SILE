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









    
