import pandas as pd

# 定义关键词
keywords_nature = {''}
keywords_policy = {''}
keywords_supply = {''}
keywords_demand = {''}


# 读取Excel文件并分类
def classify_sentiment(file_path, column_name, output_file):
    # 使用pandas读取Excel文件
    df = pd.read_excel(file_path, engine='openpyxl')

    # 确保列名存在
    if column_name not in df.columns:
        print(f"Column {column_name} does not exist in the Excel file.")
        return

    # 初始化分类结果列
    df['分类'] = None

    # 遍历每一行，根据关键词进行分类
    for index, row in df.iterrows():
        text = str(row[column_name])
        classification = [0, 0, 0, 0]  # 初始化分类结果

        # 检查自然环境关键词
        if any(keyword in text for keyword in keywords_nature):
            classification[0] = 1

        # 检查经济政策关键词
        if any(keyword in text for keyword in keywords_policy):
            classification[1] = 1

        # 检查供给关键词
        if any(keyword in text for keyword in keywords_supply):
            classification[2] = 1

        # 检查需求关键词
        if any(keyword in text for keyword in keywords_demand):
            classification[3] = 1

        # 将分类结果赋值给当前行
        df.at[index, '分类'] = classification

    # 将分类结果保存到新的Excel文件中
    df.to_excel(output_file, index=False)


# 使用函数
file_path = '.xlsx'  # 替换为你的Excel文件路径
column_name = ''  # 替换为你的列名
output_file = '.xlsx'  # 输出的Excel文件名
classify_sentiment(file_path, column_name, output_file)
print(f"Classification results have been saved to {output_file}")
