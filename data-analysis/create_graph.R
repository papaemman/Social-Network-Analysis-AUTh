#######################################
#                                     #
#  Create graphs from twitter data    #
#                                     #
#######################################


# Load packages
library(rtweet)
library(tidyverse)

# Import dataset
# twitter_data <- read.csv("data/raw/with_retweets.csv", stringsAsFactors = F)
twitter_data <- read.csv("data/raw/twitter_data.csv", stringsAsFactors = F)
dim(twitter_data)


## Creating a Graph of Retweet Relationships ----


# 1. find the retweets 
# 2. expand out all the mentioned screen names
# 3. create an igraph graph object
# 4. look at some summary statistics for the graph

twitter_data <- twitter_data %>% 
  filter(retweet_count > 0) %>% 
  select(screen_name, mentions_screen_name)

head(twitter_data)


# Keep rows with multiple names to drop them
drop_rows <- c()


for (i in 1:nrow(twitter_data)) {
  
  # If mentions_screen_name has multiple names, then extract all names and add additional rows
  x <- twitter_data$mentions_screen_name[i]
  x <- gsub("^c", "", x)
  x <- gsub("[\r\n]", "", x)
  x <- gsub("[[:punct:]]", "", x)
  # x
  
  names <- str_split(x,pattern = " ")[[1]]
  # names

  if(length(names) !=1){
  
    drop_rows <- c(drop_rows, i)
    for(j in 1:length(names)){
      vec <- c(twitter_data$screen_name[i], names[j])
      twitter_data <- rbind(twitter_data, vec)
    }
  }
}


# Results

nrow(twitter_data)  # 87648
length(drop_rows)   # 10446

tail(twitter_data)

# Sanity check:
twitter_data %>% filter(screen_name == "psforscher")

#   screen_name            mentions_screen_name
# 1  psforscher                    davidimiller
# 2  psforscher imadali, PlayStation, mcmc_stan
# 3  psforscher                         imadali
# 4  psforscher                     PlayStation
# 5  psforscher                        mcmcstan

twitter_data %>% filter(screen_name == "GreeneScientist")


# Drop rows with multiple mentions_screen_name
head(twitter_data[drop_rows,])

twitter_data <- twitter_data[-drop_rows,]

head(twitter_data)
nrow(twitter_data)

# Keep only unique rows
twitter_data <- na.omit(twitter_data)
twitter_data <- unique(twitter_data)
head(twitter_data)
nrow(twitter_data)

# Write graph
write.csv(twitter_data, file = "data/processed/retweet_graph_partial.csv", quote = F, row.names = F)







