import streamlit as st
import requests
from bs4 import BeautifulSoup
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
#import nltk
#from nltk.corpus import stopwords

# 确保已经下载了nltk的停用词列表
#nltk.download('stopwords')

# 加载停用词
def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        stopwords = set([line.strip() for line in file])
    return stopwords

# 使用jieba和停用词清洗文本
def clean_text(text, stopwords):
    word_list = jieba.lcut(text)
    filtered_words = [word for word in word_list if word not in stopwords]
    return ' '.join(filtered_words)

# 主函数
def main():
    st.title("网页内容TF-IDF向量化")

    # 用户输入网址
    url = st.text_input("请输入网址:")

    if url:
        # 获取网页内容
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()

        # 加载停用词
        stopwords = load_stopwords('stopwords.txt')  # 确保 stopwords.txt 在同级目录下

        # 清洗文本
        cleaned_text = clean_text(text, stopwords)

        # 使用TF-IDF向量化文本
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform([cleaned_text])
        feature_names = tfidf_vectorizer.get_feature_names_out()

        # 获取文档-词项矩阵的密集表示形式
        dense = tfidf_matrix.toarray()

        # 显示TF-IDF向量化结果
        st.write("## TF-IDF向量化结果")
        st.write("文档-词项矩阵形状:", tfidf_matrix.shape)

        # 打印每个特征的TF-IDF值
        st.write("### 词汇及其TF-IDF值")
        for index, value in enumerate(dense[0]):
            st.write(feature_names[index] + ": " + str(value))

if __name__ == "__main__":
    main()