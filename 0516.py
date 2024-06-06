import streamlit as st

# 假设背景音乐文件位于同级目录下的 images 文件夹中
st.audio("images/1132983854.mp3", format="audio/mp3")

# 假设我们有以下题目、答案和代码的数据
questions = [
    {
        "text": "第一题：有多少学生在完成学位课程的同时参加了认证课程?",
        "answer": """生成四个不同的条形图，分别表示总学生数、参加了认证课程的学生数（回答"Yes"）、大学成绩大于等于60分的学生数，以及大学成绩大于等于60分学生中，同时参加了课程认证。 读取'Student_Behaviour.csv'文件，筛选的条件是：第A列"Have you completed any certification courses, or are you currently enrolled in any?"这个问题的选项必须为yes，第H列"college mark"的分数必须大于等于60""",
        "code": """import pandas as pd
import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是一种常见的中文黑体

# 指定CSV文件的路径
file_path = 'Student_Behaviour.csv'  # 请确保这是文件的正确路径

try:
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 计算总学生数
    total_students = len(df)

    # 筛选出参加了认证课程的学生（Yes）
    certified_students = df[df['Have you completed any certification courses, or are you currently enrolled in any?'] == 'Yes']
    num_certified_students = len(certified_students)

    # 筛选出大学成绩大于等于60分的学生
    above_60_students = df[df['college mark'] >= 60]
    num_above_60_students = len(above_60_students)

    # 在大学成绩大于等于60分的学生中，进一步筛选出同时参加了认证课程的学生
    certified_above_60_students = above_60_students[above_60_students['Have you completed any certification courses, or are you currently enrolled in any?'] == 'Yes']
    num_certified_above_60_students = len(certified_above_60_students)

    # 可视化结果
    labels = ['总学生数', '参加了认证课程的学生数', '大学成绩≥60分的学生数', '大学成绩≥60分且参加了认证课程的学生数']
    values = [total_students, num_certified_students, num_above_60_students, num_certified_above_60_students]

    # 创建条形图
    plt.bar(labels, values)

    # 在每个条上方添加数值标签
    for i in range(len(values)):
        plt.text(i, values[i], str(values[i]), ha='center', va='bottom')

    plt.title('不同条件的学生数量分布')
    plt.xlabel('筛选条件')
    plt.ylabel('学生数量')

    # 显示图表
    plt.tight_layout()  # 调整布局以适应标签
    plt.show()

except FileNotFoundError:
    print(f"文件 {file_path} 未找到，请检查路径是否正确。")

except Exception as e:
    print(f"发生错误：{e}")""",
        "images": ["图片1.png"]
    },
    # 添加剩余的题目...
    {
        "text": "第二题：男生和女生在期望薪资方面有什么差异?",
        "answer": "答案如图所示",
        "code": "这一题没有代码",
        "images": ["图片2.png","图片2-1.png"]
    },

    {
        "text": "第三题：运动是最受欢迎的业余爱好还是看电影更受欢迎?",
        "answer": "答案如图所示",
        "code": """import pandas as pd
import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是一种常见的中文黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 指定CSV文件的路径
file_path = 'Student_Behaviour.csv'  # 请确保这是文件的正确路径

try:
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 获取"hobbies"列，并将其值转换为列表
    hobbies = df['hobbies'].dropna().unique().tolist()

    # 统计每个爱好的频率
    hobbies_count = df['hobbies'].value_counts()

    # 创建条形图
    bars = plt.bar(hobbies_count.index, hobbies_count.values, tick_label=hobbies_count.index)

    # 在每个条上方添加数值标签
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval),  # 偏移量1用于美观
                 ha='center', va='bottom')

    # 设置标题和坐标轴标签
    plt.title('学生爱好分布')
    plt.xlabel('爱好')
    plt.ylabel('学生数量')

    # 显示图表
    plt.tight_layout()  # 调整布局以适应标签
    plt.show()

except FileNotFoundError:
    print(f"文件 {file_path} 未找到，请检查路径是否正确。")

except Exception as e:
    print(f"发生错误：{e}")""",
        "images": ["图片3.png"]
    },


    {
        "text": "第四题：每天学习时间最长的学生群体是哪个?",
        "answer": "在Matplotlib中，要同时显示多个图表，我们可以使用subplot来创建一个图形窗口中的多个子图。以下是修改后的代码，它将在同一个图形窗口中并排显示两个条形图",
        "code": """import pandas as pd
import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是一种常见的中文黑体

# 指定CSV文件的路径
file_path = 'Student_Behaviour.csv'  # 请确保这是文件的正确路径

try:
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 筛选出每天学习时间超过4小时的学生
    long_study_time_students = df[df['daily studing time'] == 'More Than 4 hour']

    # 根据"Gender"列生成条形图
    gender_distribution = long_study_time_students['Gender'].value_counts()
    gender_distribution.plot(kind='bar')
    plt.title('每天学习时间超过4小时的学生性别分布')
    plt.xlabel('性别')
    plt.ylabel('学生数量')
    plt.show()

    # 根据"Department"列生成条形图
    department_distribution = long_study_time_students['Department'].value_counts()
    department_distribution.plot(kind='bar')
    plt.title('每天学习时间超过4小时的学生系部分布')
    plt.xlabel('系部')
    plt.ylabel('学生数量')
    plt.show()

except FileNotFoundError:
    print(f"文件 {file_path} 未找到，请检查路径是否正确。")

except Exception as e:
    print(f"发生错误：{e}")

第四题每天学习时间最长的学生群体是哪个? 方法二

import pandas as pd
import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是一种常见的中文黑体

# 指定CSV文件的路径
file_path = 'Student_Behaviour.csv'  # 请确保这是文件的正确路径

try:
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 筛选出每天学习时间超过4小时的学生
    long_study_time_students = df[df['daily studing time'] == 'More Than 4 hour']

    # 创建一个图形窗口和两个子图
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

    # 根据"Gender"列生成条形图在第一个子图
    gender_distribution = long_study_time_students['Gender'].value_counts()
    axes[0].bar(gender_distribution.index, gender_distribution.values)
    axes[0].set_title('每天学习时间超过4小时的学生性别分布')
    axes[0].set_xlabel('性别')
    axes[0].set_ylabel('学生数量')
    axes[0].set_xticklabels(gender_distribution.index, rotation=45)

    # 在每个条上方添加数值标签
    for i in gender_distribution.index:
        axes[0].text(i, gender_distribution[i], str(gender_distribution[i]), ha='center')

    # 根据"Department"列生成条形图在第二个子图
    department_distribution = long_study_time_students['Department'].value_counts()
    axes[1].bar(department_distribution.index, department_distribution.values)
    axes[1].set_title('每天学习时间超过4小时的学生系部分布')
    axes[1].set_xlabel('系部')
    axes[1].set_ylabel('学生数量')
    axes[1].set_xticklabels(department_distribution.index, rotation=45)

    # 在每个条上方添加数值标签
    for i in department_distribution.index:
        axes[1].text(i, department_distribution[i], str(department_distribution[i]), ha='center')

    # 调整子图间距
    plt.tight_layout()

    # 显示图表
    plt.show()

except FileNotFoundError:
    print(f"文件 {file_path} 未找到，请检查路径是否正确。")

except Exception as e:
    print(f"发生错误：{e}")""",
        "images": ["图片4-1.png","图片4-2.png","图片4-3.png","图片4-4.png"]
    },


    {
        "text": "第五题：上午还是晚上更适合学习?",
        "answer": """Anytime 73.378108, Morning 68.133247, Night 68.382979
这是一个分组汇总的结果，显示了在不同学习时段（Anytime, Morning, Night）下“college mark”列的平均值（或可能是某种其他统计量，但通常是平均值）。这表示在“Anytime”学习的人平均分数是73.38，而“Morning”和“Night”学习的人平均分数稍低。


ANOVA结果
F-value: 3.2032449111528067
这是ANOVA检验的F统计量。F值用于比较组内和组间变异，并确定不同组之间的平均值是否有显著差异。
P-value: 0.042433585249618176
P值用于确定观察到的数据是否可能是由随机误差产生的。在这个例子中，P值小于通常选择的显著性水平（如0.05），因此我们拒绝原假设（即不同学习时段下的平均分数没有显著差异），并得出结论：不同学习时段下的平均分数存在显著差异。
There is a significant difference in college marks between different study times.
这是基于P值小于显著性水平而得出的结论，表示在不同学习时段下，学生的“college mark”存在显著差异。""",
        "code": """import pandas as pd  
from scipy import stats  
  

# 假设你已经有了DataFrame，这里用df代替  
df = pd.read_csv('Student_Behaviour.csv')  # 如果你是从CSV文件读取的话  
  
# 检查数据以确保没有缺失值  
print(df.info())  
  
# 提取学习时段和学习分数  
study_time = df['prefer to study in']  
college_mark = df['college mark']  
  
# 确保学习时段中没有缺失值或需要处理的非标准值  
# 如果需要，可以使用fillna(), dropna(), replace()等方法处理缺失值或非标准值  
  
# 进行ANOVA分析  
# 首先，我们需要将数据按照学习时段分组，并计算每组的平均学习分数  
grouped = df.groupby('prefer to study in')['college mark'].mean()  
  
# 检查分组后的数据  
print(grouped)  
  
# 进行ANOVA检验  
# 由于我们需要比较多个组（至少三个），所以使用stats.f_oneway  
# 注意：f_oneway需要单独的数组作为输入，而不是pandas Series  
f_value, p_value = stats.f_oneway(  
    df[df['prefer to study in'] == 'Morning']['college mark'],  
    df[df['prefer to study in'] == 'Night']['college mark'],  
    df[df['prefer to study in'] == 'Anytime']['college mark'],  
    # 如果还有其他时段，继续添加...  
)  
  
# 输出结果  
print(f"ANOVA results:")  
print(f"F-value: {f_value}")  
print(f"P-value: {p_value}")  
  
# 解释结果  
alpha = 0.05  
if p_value < alpha:  
    print(f"There is a significant difference in college marks between different study times.")  
else:  
    print(f"There is no significant difference in college marks between different study times.")""",
        "images": ["图片5.png","图片5-1.png","图片5-2.png"]
    },

    {
        "text": "第六题：学生们平均每天花在社交媒体和视频游戏上的时间有多长?",
        "answer": "答案如图所示",
        "code": """import pandas as pd
import matplotlib.pyplot as plt

# 指定CSV文件的路径
file_path = 'Student_Behaviour.csv'  # 请确保这是文件的正确路径

# 定义时间映射函数
def map_time_to_minutes(time_str):
    if pd.isnull(time_str):  # 处理空值
        return None
    if time_str == '0 Minute':
        return 0
    elif '30 - 60' in time_str:
        return 45  # 取中间值
    elif '1 - 1.30 hour' in time_str or '1.30 - 2 hour' in time_str:
        return 90  # 取中间值
    elif 'More than 2 hour' in time_str:
        return 150  # 假设为2.5小时，即150分钟
    else:
        return None

# 读取CSV文件
df = pd.read_csv(file_path)

# 应用时间映射函数
df['time_in_minutes'] = df['social medai & video games spending Time'].apply(map_time_to_minutes)

# 筛选出非空的时间数据并计算平均时间
average_time_minutes = df['time_in_minutes'].dropna().mean()

# 统计各个时间选项的人数
time_options = ['0 Minute', '30 - 60 Minute', '1 - 1.30 hour', '1.30 - 2 hour', 'More than 2 hour']
time_counts = df['social medai & video games spending Time'].value_counts(normalize=False).reindex(time_options, fill_value=0)

# 创建条形图
fig, ax = plt.subplots()
time_counts.plot(kind='bar', ax=ax, color='skyblue')

# 在每个柱子上方添加人数标签
for i, count in enumerate(time_counts):
    ax.text(i, count, str(count), ha='center', va='bottom')

# 用红色虚线表示平均数
ax.axhline(y=average_time_minutes, color='red', linestyle='dashed', linewidth=1)
ax.text(len(time_options)/2, average_time_minutes, 'Average Time: ' + str(round(average_time_minutes, 2)), color='red', va='center')

# 设置图表标题和坐标轴标签
ax.set_title('Time Spent on Social Media and Video Games')
ax.set_xlabel('Time Options')
ax.set_ylabel('Number of Students')

# 显示图表
plt.tight_layout()
plt.show()""",
        "images": ["图片6-1.png","图片6-2.png"]
    },

    {
        "text": "第七题：大多数学生是否认为他们的学位与未来职业相关?",
        "answer": """读取"Student_Behaviour.csv",选取里面的第M列"possibility of choosing their career based on their degree : "，包含"25%"和"50%","75%","100%"四个选项，进行统计并生成条形图，每一个条形图最上面有这个柱子的具体数值""",
        "code": """import pandas as pd  
import matplotlib.pyplot as plt  
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是一种常见的中文黑体
  
# 列名  
column_name = "possibility of choosing  their career based on their degree : "  
  
# 读取CSV文件  
df = pd.read_csv('Student_Behaviour.csv')  
  
# 提取列的数据  
responses = df[column_name]  
  
# 统计每个选项的数量  
counts = responses.value_counts(normalize=False)  
  
# 确保我们统计了所有需要的选项  
# 如果某些选项不存在，可以通过pd.Series填充为0  
options_to_check = ['25%', '50%', '75%', '100%']  
counts = counts.reindex(options_to_check, fill_value=0)  
  
# 创建条形图  
fig, ax = plt.subplots()  
  
# 绘制条形图  
bars = ax.bar(counts.index, counts.values, color='blue')  
  
# 在每个条形图的顶部添加具体数值  
for bar in bars:  
    height = bar.get_height()  
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, str(height), ha='center', va='bottom')  
  
# 设置x轴和y轴的标签以及标题  
ax.set_xlabel('Percentage')  
ax.set_ylabel('Count')  
ax.set_title('Percentage of Students Choosing Career Based on Degree')  
  
# 显示图形  
plt.tight_layout()  
plt.show()""",
        "images": ["图片7.png"]
    },

    {
        "text": "第八题：在不同的体重和身高范围内,学习成绩有何差异?",
        "answer": """要同时分析在不同的体重和身高范围内学习成绩的差异，您可以使用SPSS进行多因素方差分析（MANOVA）或两因素方差分析（Two-Way ANOVA），但这里更常见的是使用两因素方差分析，因为它专注于一个因变量（学习成绩）和两个自变量（身高和体重）。

为了使用Python将CSV文件中的连续数值（身高和体重）转换为离散化的组，并生成一个新的CSV文件（test8.csv），你可以使用pandas库。以下是一个示例代码，展示了如何读取CSV文件、离散化身高和体重列，并将结果保存到一个新的CSV文件中。""",
        "code": """
import pandas as pd  
  
# 读取CSV文件  
df = pd.read_csv('Student_Behaviour.csv')  
  
# 假设我们想要将身高分为'矮', '中等', '高'三组  
# 将体重分为'轻', '正常', '重'三组  
  
# 设定身高和体重的分组边界  
height_bins = [0, 150, 175, 200]  # 根据实际情况调整  
weight_bins = [20, 60, 80, 120]  # 根据实际情况调整  
  
# 使用cut函数进行离散化  
df['Height_Group'] = pd.cut(df['Height(CM)'], bins=height_bins, labels=['矮', '中等', '高'])  
df['Weight_Group'] = pd.cut(df['Weight(KG)'], bins=weight_bins, labels=['轻', '正常', '重'])  
  
# 删除原始的身高和体重列（如果需要的话）  
# df.drop(['Height(CM)', 'Weight(KG)'], axis=1, inplace=True)  
  
# 将结果保存到新的CSV文件中  
df.to_csv('test8.csv', index=False)  
  
print("处理完成，新的CSV文件已保存为test8.csv")""",
        "images": ["图片8.png","图片8-1.png","图片8-2.png","图片8-3.png","图片8-4.png","图片8-5.png","图片8-6.png","图片8-7.png","图片8-8.png"]
    },

    {
        "text": "第九题：财务状况较差的学生在学习上是否存在困难?",
        "answer": "答案如图所示",
        "code": """""",
        "images": ["图片9.png","图片9-1.png","图片9-2.png","图片9-3.png","图片9-4.png"]
    },

    {
        "text": "第十题：有多少学生目前有兼职工作?",
        "answer": "答案如图所示",
        "code": """import pandas as pd  
import matplotlib.pyplot as plt  
  
# 读取CSV文件  
df = pd.read_csv('Student_Behaviour.csv')  
  
# 计算“yes”和“no”的数量  
job_counts = df['Are you doing a part-time job right now?'].value_counts()  
  
# 绘制条形图  
plt.bar(job_counts.index, job_counts.values)  
  
# 添加具体数值到每个柱子上  
for index, value in enumerate(job_counts.values):  
    plt.gca().text(index, value + 0.5, value, va='center')  # 0.5是为了稍微调整文本位置  
  
# 设置图表的标题和轴标签  
plt.title('Number of Students with Part-time Jobs')  
plt.xlabel('Part-time Job Status')  
plt.ylabel('Number of Students')  
  
# 显示图表  
plt.show()""",
        "images": ["图片10.png"]
    }
]

#定义了一个名为 questions 的列表，其中包含若干个字典。
#该字典有四个键：text 存储题目内容，answer 存储答案内容，code 存储与题目相关的代码示例
#（使用三引号定义多行字符串），images 存储与题目相关的图片文件列表。

# 如果 session_state 中没有 'current_index'，则初始化它为 0。session_state 用于跨页面刷新保持状态。
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 创建应用
def main():
    # 使用 session_state 中的 current_index
    current_index = st.session_state.current_index

    # 获取当前题目
    question = questions[current_index]

    # 添加页面标题
    st.title("题目解析")
    
    # 显示当前题目
    st.markdown(f"# {question['text']}")

    # 显示答案
    st.markdown(question['answer'])

    # 如果存在代码字段，则以 Markdown 代码块形式显示代码
    if 'code' in question:
        st.code(question['code'], language="python")

    # 显示图片
    for image in question["images"]:
        st.image(f"images/{image}", use_column_width=True)

    # 使用列布局来放置按钮
    # 这行代码使用 st.columns 函数创建了一个水平的列布局。
    # [1, 1] 参数指定了列的相对宽度。在这个例子中，创建了两列宽度相同的布局，每列的宽度是父容器的一半。
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("上一题"):
            new_index = (current_index - 1) % len(questions)
            st.session_state.current_index = new_index
            st.experimental_rerun()
    
    # 使用 with col1: 进入列容器 col1 的上下文。
    # st.button("上一题") 创建了一个按钮，标签为 "上一题"。
    # 如果用户点击了 "上一题" 按钮，则执行以下操作:
    # 计算新的索引 new_index，这是当前索引 current_index 减去 1（使用 % len(questions) 确保索引循环回到列表末尾）。
    # 更新 session_state 中的 current_index 为新的索引。
    # 调用 st.experimental_rerun() 刷新应用程序。这是一个实验性功能，用于在交互事件发生后重新运行应用程序。
    
    with col2:
        if st.button("下一题"):
            new_index = (current_index + 1) % len(questions)
            st.session_state.current_index = new_index
            st.experimental_rerun()

    # 使用 with col2: 进入列容器 col2 的上下文。
    # st.button("下一题") 创建了一个按钮，标签为 "下一题"。
    # 如果用户点击了 "下一题" 按钮，则执行以下操作:
    # 计算新的索引 new_index，这是当前索引 current_index 加上 1（使用 % len(questions) 确保索引循环回到列表开头）。
    # 更新 session_state 中的 current_index 为新的索引。
    # 调用 st.experimental_rerun() 刷新应用程序。


# 运行应用
if __name__ == "__main__":
    main()