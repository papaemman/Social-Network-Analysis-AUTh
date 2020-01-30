import pandas as pd
import os
import codecs
from io import StringIO
import math

with codecs.open(os.path.abspath("with_retweets.csv"), 'r', encoding='utf-8', errors='ignore') as fdata:
    tweets_string = fdata.read()

tweets = pd.read_csv(StringIO(tweets_string), low_memory=False)

re_tweets = tweets[tweets.is_retweet]
#
# # re_edges = list()
# # re_edges.append(["Source", "Target", "Type"])
#
# with open(os.path.abspath("./retweet_graph.csv"), "a", encoding="utf-8") as file:
#     file.write("Source,Target,Type")
#     file.write("\n")
#
# for _index, row in re_tweets.iterrows():
#     # re_edges.append([str(int(row.retweet_user_id)), str(int(row.user_id)), "Directed"])
#     edge = "{},{},{}".format(str(int(row.retweet_user_id)), str(int(row.user_id)), "Directed")
#     with open(os.path.abspath("./retweet_graph.csv"), "a", encoding="utf-8") as file:
#         file.write(edge)
#         file.write("\n")

# print("," in tweets.iloc[1].mentions_user_id)
# lista = tweets.iloc[0].mentions_user_id.split(",")
# print(lista)

with open(os.path.abspath("./mention_retweet_graph.csv"), "a", encoding="utf-8") as file:
    file.write("Source,Target,Type")
    file.write("\n")

    for _index, row in tweets.iterrows():

        x = row.mentions_user_id

        # If this row is a retweet
        if row.is_retweet:
            user_id = str(int(float(row.user_id)))

            file.write("{},{},{}".format(str(int(float(row.retweet_user_id))), user_id, "Directed"))
            file.write("\n")

            # If there are more than one mentions
            if "," in str(x):
                mentions = x.split(",")

                # If retweet user is in mentions remove him
                if str(row.retweet_user_id) in mentions:
                    mentions.remove(str(row.retweet_user_id))

                for mention in mentions:
                    file.write("{},{},{}".format(user_id, str(int(float(mention))), "Directed"))
                    file.write("\n")

            # If there is exactly one mention and is not retweet user
            elif (not math.isnan(float(str(x)))) and int(float(x)) != int(float(row.retweet_user_id)):
                file.write("{},{},{}".format(user_id, int(float(row.mentions_user_id)), "Directed"))
                file.write("\n")

        # If this row is an original tweet
        else:
            # Has a list of tweets
            if "," in str(x):
                mentions = x.split(",")

                for mention in mentions:
                    file.write("{},{},{}".format(user_id, str(int(float(mention))), "Directed"))
                    file.write("\n")

            # Has a single mention
            elif not math.isnan(float(str(x))):
                file.write("{},{},{}".format(user_id, int(float(row.mentions_user_id)), "Directed"))
                file.write("\n")
