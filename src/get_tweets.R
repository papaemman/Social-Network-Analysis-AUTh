#######################
#                     #
#  Get tweets script  #
#                     #
#######################

# Load twitter package (the rtweet package is recommended now over twitteR)
library(rtweet)
library(dplyr)


## Define passwords ----

# whatever name you assigned to your created app
appname <- "MSC_SNA"

# api key (example below is not a real key)
key <- "key"

## api secret (example below is not a real key)
secret <- "secret"

access_token <- "access_token"

access_secret <- "access_secret"

# create token named "twitter_token"
twitter_token <- create_token(
  app = appname,
  consumer_key = key,
  consumer_secret = secret,
  access_token = access_token,
  access_secret = access_secret)



## Get tweets ----

# Search for all tweets contain #rstats (actually up to 40.000 tweets)
df <- search_tweets(q = "#rstats", n = 40000, include_rts = T, retryonratelimit = T)

class(df)
str(df$created_at)
print(min(df$created_at))
print(max(df$created_at))


# Append new tweets in the twitter_data.csv file
twitter_data <- read.csv("data/raw/twitter_data.csv", stringsAsFactors = F)

class(twitter_data)
old_max_date <- max(as.POSIXct(twitter_data$created_at))
str(old_max_date)

# Keep only new tweets
df <- df %>% filter(created_at > old_max_date)

twitter_data <- rbind(twitter_data, df)

write.csv(twitter_data, file = "data/raw/twitter_data.csv")

