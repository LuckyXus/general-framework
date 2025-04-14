import pandas as pd
from pyltp import SentenceSplitter

def data_import(path,file_name):
    df = pd.read_excel(path+file_name+'.xlsx')
    df.fillna("", inplace=True)
    df_list = []
    for i in df.index.values:
        df_line = df.loc[i, ['', '', '', '']].to_dict()
        df_list.append(df_line)
    with open(path + file_name + '.txt', 'w', encoding='utf-8') as f:
        f.write(str(df_list))

def SentenceSplit(dict):
    #进行分句操作
    all_sentences = []
    for row in eval(dict):
        sentence = row['content']
        sentence = SentenceSplitter.split(sentence)
        sentence = list(sentence)
        for per_sentence in sentence:
            # all_sentences.append({"Article": row['Article'], "Content": per_sentence, "Date": row['Date']})
            all_sentences.append({"content": per_sentence})
    # 将分句结果导入All_Sentences文件中
    df = pd.DataFrame(all_sentences)
    df.to_excel(path + ".xlsx", index=False)

if __name__ == '__main__':
    print("代码开始运行")
    # path = 'E:\\PyCharm\\YJY Project\\SRF\\数据预处理\\Data\\'
    #本文件夹内路径
    path = './'
    #文件名称
    data_import(path, '')
    with open(path + '.txt', 'r', encoding='utf-8') as fp_article:
        article = fp_article.read()
    print("数据导入完成")
    SentenceSplit(article)
    print("分句完成")
    data_import(path, '')
    print("代码运行结束")