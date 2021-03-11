import pandas as pd

from summa import keywords
from pytopicrank import TopicRank

from keybert import KeyBERT




transcript = pd.read_csv("C:\\Users\\pasca\\myCloud\\01 Studium\\ZHAW\\Bachelor Wirtschaftsingenieurwesen\\6. Semester\\BA\\summarization\\Dash\\us_election_2020_vice_presidential_debate.csv")


kw_extractor = KeyBERT('distilbert-base-nli-mean-tokens')
for j in range(len(transcript)):
    keywords = kw_extractor.extract_keywords(transcript["text"][j], keyphrase_length=1, stop_words='english')
    print("Keywords of article", str(j+1), "\n", keywords)


    