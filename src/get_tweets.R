#######################
#                     #
#  Get tweets script  #
#                     #
#######################

## load twitter package (the rtweet package is recommended now over twitteR)
library(rtweet)


# Q: Can I "hack" the twitter API, in order to get more tweets?
# Ask Maria from Medoid AI.

## Define passwords ----

# whatever name you assigned to your created app
appname <- "MSC_SNA"

# api key (example below is not a real key)
key <- "FDwKA8VHDboYJY88mZinO25qo"

## api secret (example below is not a real key)
secret <- "W2gAoeaHEHRF0CG92AqRi3jUb4IoVjLoB92gFSscs4nC41LxW9"

access_token <- "3353127743-yNwnTfwjPWnXujnKVpjUIJjw3IvGROShMbmN1RK"

access_secret <- "fq5DdujjlZlZXJ01F3U7Wou7M3S7eqtEw3FEOixqhCC0h"

# create token named "twitter_token"
twitter_token <- create_token(
  app = appname,
  consumer_key = key,
  consumer_secret = secret,
  access_token = access_token,
  access_secret = access_secret)



## Get tweets ----

## search for 20 tweets using the #rstats hashtag
tweets <- search_tweets(q = "#rstats", n = 20, retryonratelimit = F)

# view the first 3 rows of the dataframe
head(tweets, n = 3)
View(tweets)

dim(tweets)
colnames(tweets)


tweets$text
tweets$hashtags


# Search for 10000 tweets and write in csv file
df <- search_tweets(q = "#rstats", n = 40000, include_rts = T, retryonratelimit = T)

min(df$created_at)
max(df$created_at)

dim(df)
df <- apply(df, 2, as.character)

write.csv(df, file = "datasets/twitter_data_20203001_rt.csv")

View(df)

## Search for my tweet


df <- as.data.frame(df)
colnames(df)
df$screen_name
library(dplyr)

my_first_tweet <- df %>% filter(screen_name == "Papaemman_pan")
write.csv(my_first_tweet, file = "../datasets/my_first_tweet.csv")
