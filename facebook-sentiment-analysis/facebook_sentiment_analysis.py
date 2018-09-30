import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.downloader.download('vader_lexicon')

file = "/Users/deepanshusinha/git/Python/BasicPythonGame/facebook-sentiment-analysis/convertcsv.xlsx"

# Read from excel
xl = pd.ExcelFile(file)

# Parsing Excel sheet to data frame
dfs = xl.parse(xl.sheet_names[0])

# Removes the blank rows from the data frame
dfs = list(dfs['Timeline'])
print(dfs)

sid = SentimentIntensityAnalyzer()
str1 = "UTC+05:30"

for data in dfs:
    a = data.find(str1)
    if(a == -1):
        ss = sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k, ss[k])
