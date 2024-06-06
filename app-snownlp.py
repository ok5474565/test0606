import requests
import streamlit as st
from snownlp import SnowNLP
from bs4 import BeautifulSoup
import re
from pathlib import Path

# 去除HTML标签
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# 提取网页正文文本
def extract_body_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text

# 情感分析函数
def sentiment_analysis(text):
    s = SnowNLP(text)
    return s.sentiments

# 主函数
def run():
    st.set_page_config(page_title="网页情感分析")
    
    st.write("# 网页情感分析")
    
    url = st.text_input('Enter URL:')
    
    if url:
        r = requests.get(url)
        r.encoding = 'utf-8'
        html_text = r.text
        text = extract_body_text(html_text)
        
        text = remove_html_tags(text)

        # 情感分析
        sentiment_score = sentiment_analysis(text)
        st.write(f"情感分析得分: {sentiment_score:.2f}")

if __name__ == "__main__":
    run()