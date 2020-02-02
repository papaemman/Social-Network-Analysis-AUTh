import pandas as pd
import os
import codecs
from io import StringIO
import math

with codecs.open(os.path.abspath("with_retweets.csv"), 'r', encoding='utf-8', errors='ignore') as fdata:
    tweets_string = fdata.read()

tweets = pd.read_csv(StringIO(tweets_string), low_memory=False)

re_tweets = tweets[tweets.is_retweet]


# Creating retweet graph
re_edges = set()

with open(os.path.abspath("./retweet_graph1.csv"), "a", encoding="utf-8") as file:
    file.write("Source,Target,Type")
    file.write("\n")

for _index, row in re_tweets.iterrows():
    edge = "{},{},{}".format(str(int(row.retweet_user_id)), str(int(row.user_id)), "Directed")
    re_edges.add(edge)

for edge in re_edges:
    with open(os.path.abspath("./retweet_graph1.csv"), "a", encoding="utf-8") as file:
        file.write(edge)
        file.write("\n")

# ------------------------------------------------
# Creating mention-retweet graph and mention graph
re_edges = set()
re_edges_mention = set()

for _index, row in tweets.iterrows():

    x = row.mentions_user_id
    user_id = str(int(float(row.user_id)))

    # If this row is a retweet
    if row.is_retweet:

        re_edges.add("{},{},{}".format(str(int(float(row.retweet_user_id))), user_id, "Directed"))

        # If there are more than one mentions
        if "," in str(x):
            mentions = x.split(",")

            # If retweet user is in mentions remove him
            if str(row.retweet_user_id) in mentions:
                mentions.remove(str(row.retweet_user_id))

            for mention in mentions:
                re_edges.add("{},{},{}".format(user_id, str(int(float(mention))), "Directed"))
                re_edges_mention.add("{},{},{}".format(user_id, str(int(float(mention))), "Directed"))

        # If there is exactly one mention and is not retweet user
        elif (not math.isnan(float(str(x)))) and int(float(x)) != int(float(row.retweet_user_id)):
            re_edges.add("{},{},{}".format(user_id, int(float(row.mentions_user_id)), "Directed"))
            re_edges_mention.add("{},{},{}".format(user_id, int(float(row.mentions_user_id)), "Directed"))

    # If this row is an original tweet
    else:
        # Has a list of mentions
        if "," in str(x):
            mentions = x.split(",")

            for mention in mentions:
                re_edges.add("{},{},{}".format(user_id, str(int(float(mention))), "Directed"))
                re_edges_mention.add("{},{},{}".format(user_id, str(int(float(mention))), "Directed"))

        # Has a single mention
        elif not math.isnan(float(str(x))):
            re_edges.add("{},{},{}".format(user_id, int(float(row.mentions_user_id)), "Directed"))
            re_edges_mention.add("{},{},{}".format(user_id, int(float(row.mentions_user_id)), "Directed"))

with open(os.path.abspath("./mention_retweet_graph1.csv"), "a", encoding="utf-8") as file:
    file.write("Source,Target,Type")
    file.write("\n")

    for edge in re_edges:
        file.write(edge)
        file.write("\n")

with open(os.path.abspath("./mention_graph1.csv"), "a", encoding="utf-8") as file:
    file.write("Source,Target,Type")
    file.write("\n")

    for edge in re_edges_mention:
        file.write(edge)
        file.write("\n")
