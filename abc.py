# main.py
import streamlit as st

# 导入其他文件中的 run 函数
from app_bar2 import run as bar_chart_run
from app_worldcloud import run as wordcloud_run

# 设置页面配置，只能在应用程序的最顶层调用一次
st.set_page_config(page_title="综合文本分析工具", layout="wide")

# 创建下拉列表供用户选择功能
function_options = ["文本分析工具", "生成词云图"]
selected_option = st.sidebar.selectbox("选择功能：", options=function_options)

# 根据用户选择的功能，调用相应的函数
if selected_option == "文本分析工具":
    st.title("文本分析工具")
    bar_chart_run()
elif selected_option == "生成词云图":
    st.title("生成词云图")
    wordcloud_run()

# 注意：不要在子应用程序中调用 st.set_page_config()
