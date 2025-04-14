# general-framework
instruction
This general framework contains online public opinion related to vegetable prices and weekly prices of six common vegetables (cabbage, potato, enoki mushroom, tomato, cucumbers, and bean), and is specifically designed for vegetable price forecasting and analysis of online public opinion on vegetable prices. Vegetable prices are sourced from the National Agricultural Products Business Information Public Service Platform, and vegetable public opinion is sourced from the following websites:
① Vegetable Business Network
② China Vegetable Network
③ Xuexi Qiangguo
③ China Agricultural Rural Information Network
⑤ CCTV
⑥ Vegetable Network
The information published on these websites includes a large number of news reports related to vegetable prices in various regions of China, some of which come from official sources such as governments and enterprises, while the rest is provided by individual farmers, consumers, and experts in related fields, and the vegetable opinions collected cover a wide range of different modes of information, including text, audio, and video.
Data processing
Vegetable Price online Public Opinion Data
Vegetable public opinion text data were crawled using a crawler program written in Python to crawl public opinion information related to vegetable prices, which mainly included publication time, title, content, and source, while audio and video data related to vegetable prices were downloaded from CCTV.com and Learning Power through a special downloader, and the publication time, title, and source of the video were recorded, and the time span of the online public opinion data was January 3, 2014 to July 25, 2024. The collected audio and video data were converted into text using “Tongyi Listening and Understanding”, an AI assistant based on AliCloud's big model, and then all the public opinion texts from different sources were subjected to clause splitting and cleansing to improve the quality of the textual data and ensure the accuracy of the subsequent analysis and model training.
