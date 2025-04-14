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
    all_sentences = []
    for row in eval(dict):
        sentence = row['content']
        sentence = SentenceSplitter.split(sentence)
        sentence = list(sentence)
        for per_sentence in sentence:
            # all_sentences.append({"Article": row['Article'], "Content": per_sentence, "Date": row['Date']})
            all_sentences.append({"content": per_sentence})

    df = pd.DataFrame(all_sentences)
    df.to_excel(path + ".xlsx", index=False)

if __name__ == '__main__':
    print("The code starts running")
    # path = ''

    path = './'

    data_import(path, '')
    with open(path + '.txt', 'r', encoding='utf-8') as fp_article:
        article = fp_article.read()
    SentenceSplit(article)
    data_import(path, '')
    print("Code running over")