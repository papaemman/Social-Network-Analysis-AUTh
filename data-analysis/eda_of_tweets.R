####################################################
#                                                  #
#  Exploratory Data analysis for twitter dataset   #
#                                                  #
####################################################

# Load packages
library(dplyr)
library(ggplot2)
library(plotly)
library(tidyr)
library(stringr)

library(wordcloud)
library(wordcloud2)
library(RColorBrewer)


# Import dataset
twitter_data <- read.csv("data/raw/twitter_data.csv", stringsAsFactors = F)


# Explore dataset
dim(twitter_data)
str(twitter_data)
View(head(twitter_data))



# Fix variable types
twitter_data$created_at <- as.POSIXct(twitter_data$created_at)
str(twitter_data$created_at)


# Variables returned by twitter API
sapply(twitter_data, class)


# Min / max date
min(twitter_data$created_at)
max(twitter_data$created_at)


# How many tweets there are for each day?
tweets_per_day <- twitter_data %>% group_by(Day = as.Date(created_at)) %>% summarise(Total_tweets = n())

p <- ggplot(tweets_per_day, aes(Day, Total_tweets)) +
  geom_line() +
  geom_point() +
  
  geom_vline(xintercept  = as.Date("2019-12-28"), colour="red", linetype = "longdash")+
  geom_vline(xintercept = as.Date("2020-01-04"), colour="red", linetype = "longdash")+
  geom_text(aes(as.Date("2019-12-31"), 3300), label = "1st graph")+
  
  geom_vline(xintercept = as.Date("2020-01-12"), colour="red", linetype = "longdash")+
  geom_vline(xintercept = as.Date("2020-01-19"), colour="red", linetype = "longdash")+
  geom_text(aes(as.Date("2020-01-16"), 3300), label = "2nd graph")+
  
  geom_vline(xintercept = as.Date("2020-01-23"), colour="red", linetype = "longdash")+
  geom_vline(xintercept = as.Date("2020-01-30"), colour="red", linetype = "longdash")+
  geom_text(aes(as.Date("2020-01-27"), 3300), label = "3rd graph")+
  
  ggtitle("Total tweets per day")

p

ggplotly(p)



# Identify unique users

unique_users <- twitter_data %>% select(screen_name,user_id, account_created_at) %>% unique() # 13054 
write.csv(unique_users, "output/unique_users.txt", quote = F, row.names = F)


# What are the other hashtags used in conjunction with #rstats?

hastags_df <- twitter_data %>% 
  select(hashtags) %>% 
  mutate(hashtags = tolower(hashtags)) %>% 
  count(hashtags, sort=TRUE)

head(hastags_df)


## Create a word cloud

# 1. Extract hastags
hastags <- hastags_df$hashtags
head(hastags)

hastags <- gsub("^c", "", hastags) 
hastags <- gsub("https\\S*", "", hastags) 
hastags <- gsub("@\\S*", "", hastags) 
hastags <- gsub("amp", "", hastags) 
hastags <- gsub("[\r\n]", "", hastags)
hastags <- gsub("[[:punct:]]", "", hastags)

head(hastags)
hastags <- na.omit(hastags)
hastags <- stringr::str_split(string = hastags, pattern =" ") %>% unlist()

# 2. Create a document-term-matrix
hastags_count_df <- data.frame(table(hastags))
dim(hastags_count_df) # 2635 unique hastags

hastags_count_df <- hastags_count_df %>% arrange(desc(Freq))
write.csv(hastags_count_df, file = "output/hastags_frequencey.csv",row.names = F, quote = F)

# 3. Generate the word cloud
set.seed(1234) 
wordcloud(words = hastags_count_df$hastags, freq = hastags_count_df$Freq,
          min.freq = 5,
          max.words=300,
          random.order=FALSE,
          rot.per=0.35,
          colors=brewer.pal(8, "Dark2"))


wordcloud2(data=hastags_count_df, size=1.3,
           color='random-dark', set.seed(2),
           backgroundColor = "white", shape = "pentagon")



## Extracting a retweets origin
filter(rstats, retweet_count > 0) %>% 
  select(text, mentions_screen_name, retweet_count) %>% 
  mutate(text = substr(text, 1, 30)) %>% 
  unnest()



# Search for my tweet
my_first_tweet <- twitter_data %>% filter(screen_name == "Papaemman_pan")
my_first_tweet