import streamlit as st
import requests
from bs4 import BeautifulSoup
import jieba
from gensim import corpora
from gensim.models.ldamodel import LdaModel
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# 确保已经安装了nltk的停用词列表
import nltk
nltk.download('stopwords')

# 加载停用词
def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        stopwords = set([line.strip() for line in file])
    return stopwords

# 使用jieba和停用词清洗文本
def clean_text(text, stopwords):
    word_list = jieba.lcut(text)
    filtered_words = [word for word in word_list if word not in stopwords]
    return filtered_words

# 训练LDA模型
def train_lda_model(documents, num_topics=10, num_words=10, passes=10):
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(text) for text in documents]
    lda = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=passes)
    return lda, corpus, dictionary

# 主函数
def main():
    st.title("网页内容主题建模")

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

        # 将清洗后的文本分割为文档集合
        documents = [cleaned_text]

        # 训练 LDA 模型
        lda, corpus, dictionary = train_lda_model(documents)

        # 显示主题
        st.write("## 主题建模结果")
        for idx, topic in lda.print_topics(-1):
            st.write(f"主题 {idx}:")
            st.write(topic)

if __name__ == "__main__":
    main()