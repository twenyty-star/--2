import streamlit as st

#标题
st.title("通往夏天的隧道,再见的出口")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")
st.form("This is a key")

#文字
st.write("吓我一跳我释放忍术")
st.write("令神龙造成烟雾")
st.write("沙防掩意手 握握手握握双手")

#图片
st.image("./AI应用/resources/2.webp")





#音频
st.audio("./AI应用/resources/eill - 片っぽ - Acoustic Version.mp3")




#logo
st.logo("./AI应用/resources/4.webp")




#视频
st.video("./AI应用/resources/summer tunnel.mp4")




#表格
student_data = {
    "姓名":["王林","瑞弗金","师绪","石敖"],
    "学号":["1","2","3","4"],
    "语文":["110","120","121","134"]
}

st.table(student_data)





#输入框

name = st.text_input("请输入姓名")
st.write(f"您输入的姓名为{name}")


password = st.text_input("请输入密码",type = "password")
st.write(f"您输入的密码为{password}")








#单选按钮

gender = st.radio("请输入您的性别",["男","女"],)
st.write(f"您的性别为:{gender}")


#按钮
st.button("click me",icon=":material/thumb_up:")



#设置页面的配置项
st.set_page_config(
    page_title="summer tunnel",
    page_icon="🧊",
    #网页布局
    layout="wide",
    #控制侧边栏的状态
    initial_sidebar_state="expanded",
    #菜单信息
    menu_items={
        'Get Help': 'https://www.bilibili.com',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# 这是一个streamlit的入门界面"
    }
)



















