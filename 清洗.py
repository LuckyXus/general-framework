# -*- coding: utf-8 -*-

import pandas as pd

def data_import(filename,path):
    df = pd.read_excel(path + filename + '.xlsx')
    df.fillna("", inplace=True)
    df_list = []
    for i in df.index.values:
        # loc为按列名索引 iloc 为按位置索引，使用的是 [[行号], [列名]]
        df_line = df.loc[i, []].to_dict()
        # 将每一行转换成字典后添加到列表
        df_list.append(df_line)
    with open(path + filename + '.txt', 'w', encoding='utf-8') as f:
        f.write(str(df_list))

def list_to_xlsx(list,filename,path):
    dataframe = pd.DataFrame(list)
    dataframe.to_excel(path + filename, index=False)


def Non_related(string):
    # 删除没有相关性的文本
    NonRelatedList = ['']
    for word in NonRelatedList:
        if word in string:
            return True
    return False

def Price_Judgment(string):
    if '' in string:
            return True
    return False

def classify(all_text):
    tagged = []
    nontagged = []
    for i in eval(all_text):
        sentence = i['']
        try:
            #判断类型
            if Non_related(sentence)==True or Price_Judgment(sentence)==False or len(sentence)<=15:
                nontagged.append({ "content": sentence})
            else:
                tagged.append({ "content": sentence})

        except Exception as e:
            print('ValueError:', e)
    #保存需要的
    list_to_xlsx(tagged, 'xlsx', './')

    #保存不需要的
    list_to_xlsx(nontagged, 'xlsx', './')

if __name__ == '__main__':
    print("代码开始运行")

    # print("导入数据：start")
    path = './'
    filename = ''
    data_import(filename,path)
    # print("导入数据：over")

    with open(path+filename+'.txt', 'r', encoding='utf-8') as fp:
        all_text = fp.read()

    print("开始打标签")
    classify(all_text)

    print("代码运行结束")