# Load twitter data
twitter_data <- read.csv("data/raw/twitter_data.csv")
colnames(twitter_data)

# Compare retweet_graphs
my_rt_graph <- read.csv("data/processed/retweet_graph_partial.csv")
rt_graph <- read.csv("data/processed/mention_retweet_graph.csv")


nrow(my_rt_graph) # 10078
nrow(rt_graph)    # 20501
 

# Duplicates
sum(duplicated(my_rt_graph))
sum(duplicated(rt_graph))


# Join name
rt_graph <- merge(x = rt_graph, y = twitter_data %>% select(user_id, screen_name), by.x = c("Source"), by.y = c("user_id"))
rt_graph <- rt_graph %>% rename(source_screen_name = screen_name)
 
rt_graph <- merge(x = rt_graph, y = twitter_data %>% select(user_id, screen_name), by.x = c("Target"), by.y = c("user_id"))
head(rt_graph)
