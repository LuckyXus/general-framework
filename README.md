# Framework Introduction
In recent years, vegetable prices have fluctuated drastically, which has brought about an undeniable impact on farmers, consumers, as well as the government and other main players in the relevant industry chain. Vegetable price fluctuations are influenced by numerous factors, including supply and demand balance, climate, emergencies, and online public opinion. In the field of vegetable price forecasting, many scholars have combined vegetable prices with a variety of influencing factors to forecast vegetable prices to enhance the interpretability of the forecast. With the development of the Internet and social media, many online platforms have become an important medium for people to vent their emotions and express their opinions, and therefore, online public opinion has become the focus of many scholars' research. In the field of vegetable price prediction, some scholars have also established a connection between vegetable prices and online public opinion, explored the relationship between the two, and quantified online public opinion as an important influencing factor in vegetable price prediction. However, there is a lack of a general framework and a set of benchmarking methods for reference in this field, and the main purpose of this task is to construct a framework for exploring the relationship between vegetable prices and online public opinion, and to conduct research on vegetable price forecasting.
# Instruction
This general framework contains online public opinion related to vegetable prices and weekly prices of six common vegetables (cabbage, potato, enoki mushroom, tomato, cucumber, and bean), and is specifically designed for forecasting vegetable prices and analyzing online public opinion on vegetable prices. Vegetable price online opinion is sourced from the following websites:
- Vegetable Business Network
- China Vegetable Network
- Vegetable Industry Business Platform
- China Agricultural and Rural Information Network
- Xuexi Qiangguo
- CCTV Network

The information published on these websites includes a large number of news reports related to vegetable prices in various regions of China, some of which come from official sources such as governments and enterprises, while the rest is provided by individual farmers, consumers, and experts in related fields, and the vegetable opinions collected cover a wide range of different modes of information, including text, audio, and video.
# Data processing
## Collection of online public opinion data
The public opinion text data were crawled using a crawler program written in Python to crawl public opinion information related to vegetable prices, and the crawled content mainly included the publication time, title, content, and source, while the audio and video data related to vegetable prices were downloaded from CCTV.com and Xuexi Qiangguo through a special downloader, and the publication time, title, and source of the video were recorded, and the time span of the online public opinion data was from 2014 January 3 to July 25, 2024. The collected audio and video data were converted into text using “Tongyi Tingwu”, an AI assistant based on Aliyun big model, and then all the public opinion texts from different sources were subjected to text splitting and cleaning to improve the quality of the textual data and ensure the accuracy of the subsequent analysis and model training.
## Collection of vegetable prices data
Daily price data of six common vegetables, including cucumber, tomato, potato, enoki mushroom, bean curd, and Chinese cabbage, were collected, and the time span was consistent with the vegetable prices public opinion. The acquired time-series data were preprocessed, including missing value filling, outlier removal, and time-series formatting to ensure the accuracy and usability of the data, and the weekly averages of the daily price time-series data of the six vegetables were calculated, and the daily price time-series data of the six vegetables were converted to weekly price time-series data to obtain 551 weeks of data.
# Preparation process
## Public opinion classifition
In order to refine the indexes corresponding to the public opinion texts on vegetable prices, a system of indexes affecting vegetable prices is established, which is mainly divided into four indexes: natural environment, economic policy, supply and demand, and each index has some sub-indicators. An approach based on topic matching and large language model is adopted, firstly, the classification program written in python is used to classify the opinion text, and then the large language model kimi combined with the prompt words of public opinion classification is used to further classify the public opinion texts that does not match, and to classify all the public opinion texts to the maximum extent. kimi is launched by Moonshot AI, which is an AI assistant focusing on text processing. The process was completed by 10 trained professionals, and the matching results were manually revised in order to ensure the accuracy of the matches.
## Judgment of Public Opinion Trends
When making trend judgments of public opinion opinion on prices, the trend of vegetable prices is initially judged using the large language model kimi combined with trend judgment prompt words. Specifically, if the price of vegetables will rise, it is marked as 1; if the price of vegetables is stable or its trend cannot be clearly judged, it is marked as 0; if the price of vegetables falls, it is marked as -1.
## Publi opinion computation
Vegetable price online public opinion sentiment value computation using SnowNLP public opinion analysis tool, with the large language model KIMI combined with prompt words to judge positive and negative vegetable public opinion texts for SonwNLP training, of which there are 1500 positive texts and 1500 negative texts, and using the trained model combined with the Jieba to compute the sentiment value of all public opinion texts.
# Usage
## Method 1: Use of materials provided
Following the preparation process in the framework, the opinion values can be calculated and combined with vegetable prices, and vegetable price prediction can be performed by inputting them into the prediction network.
```
data = pd.read_csv('.csv')
input_features = ['price', 'sentiment scores']
output_features = ['price']
```
## Method 2: Use of other data
If you have a self-constructed public opinion dataset or a public opinion dataset, you can follow the steps below to process vegetable opinions.

*Step1:* Segmentation is performed on the opinion text using the segmentation code provided in the general framework to segment the opinion text into small texts of moderate length.
```
def SentenceSplit(dict):
    all_sentences = []
    for row in eval(dict):
        sentence = row['content']
        sentence = SentenceSplitter.split(sentence)
        sentence = list(sentence)
        for per_sentence in sentence:
            all_sentences.append({"content": per_sentence})
    df = pd.DataFrame(all_sentences)
```

*Step2:* Use the text cleaning code provided in the general framework to perform customized keyword-level text cleaning to get the desired high-quality text.
```
def Non_related(string):
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
            if Non_related(sentence)==True or Price_Judgment(sentence)==False or len(sentence)<=15:
                nontagged.append({ "content": sentence})
            else:
                tagged.append({ "content": sentence})

        except Exception as e:
            print('ValueError:', e)
```
*Step3:* Classification using the public opinion classification codes provided in the open framework, and more comprehensive classification using classification prompt words combined with a large language model.

```
    for index, row in df.iterrows():
        text = str(row[column_name])
        classification = [0, 0, 0, 0]

        if any(keyword in text for keyword in keywords_nature):
            classification[0] = 1

        if any(keyword in text for keyword in keywords_policy):
            classification[1] = 1

        if any(keyword in text for keyword in keywords_supply):
            classification[2] = 1

        if any(keyword in text for keyword in keywords_demand):
            classification[3] = 1
```
*Step4:* Public opinion analysis of vegetable price public opinion is performed using the *sentiment.marshal.3* file provided by this general framework to compute sentiment values.

*Step5:* Price prediction using online public opinion sentiment values and price time series data as inputs and predicted prices as outputs.

## Method 3: Customized corpus training SnowNLP for public opinion computation
*Step1:* Positive and negative texts are determined using kimi in combination with prompt words and *pos.txt* and *neg.txt* texts are constructed for SnowNLP training.

*Step2:* Train SnowNLP using a prepared positive corpus and a negative corpus.
```
from snownlp import sentiment
sentiment.train('neg.txt', 'pos.txt')
sentiment.save("sentiment.marshal")
```
*Step3:* Scoring other online public opinion texts using the trained SnowNLP.

# summary
The proposed general framework has good comprehensiveness and extensibility, and the functions in the framework are not limited to the analysis of vegetable prices online public opinion, but are applicable to all the tasks that need to clean, classification, and trend judgment of online public opinion, as well as public opinion computation. All scholars are welcome to give valuable suggestions on this framework, and we also call on everyone to work together to improve this framework.

# copyright statement
This is a non-commercial project, for pure collection and aggregation of information, if any infringement, please leave a message.
