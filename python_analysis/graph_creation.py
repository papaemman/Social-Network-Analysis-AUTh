import pandas as pd
import os
import codecs
from io import StringIO

with codecs.open(os.path.abspath("with_retweets.csv"), 'r', encoding='utf-8', errors='ignore') as fdata:
    tweets_string = fdata.read()

tweets = pd.read_csv(StringIO(tweets_string), low_memory=False)

re_tweets = tweets[tweets.is_retweet]

# re_edges = list()
# re_edges.append(["Source", "Target", "Type"])

with open(os.path.abspath("./retweet_graph.csv"), "a", encoding="utf-8") as file:
    file.write("Source,Target,Type")
    file.write("\n")

for _index, row in re_tweets.iterrows():
    # re_edges.append([str(int(row.retweet_user_id)), str(int(row.user_id)), "Directed"])
    edge = "{},{},{}".format(str(int(row.retweet_user_id)), str(int(row.user_id)), "Directed")
    with open(os.path.abspath("./retweet_graph.csv"), "a", encoding="utf-8") as file:
        file.write(edge)
        file.write("\n")
