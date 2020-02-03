# Load unique users data
users <- read.csv("output/unique_users.txt")
head(users)

# Compare retweet_graphs
my_rt_graph <- read.csv("data/processed/retweet_graph_partial.csv")
rt_graph <- read.csv("data/processed/mention_retweet_graph.csv")


nrow(my_rt_graph) # 10078
nrow(rt_graph)    # 20501
 

# Duplicates
sum(duplicated(my_rt_graph))
sum(duplicated(rt_graph))


# Join name
rt_graph <- merge(x = rt_graph, y = users, by.x = c("Source"), by.y = c("user_id"))
rt_graph <- rt_graph %>% rename(source_screen_name = screen_name)
 
rt_graph <- merge(x = rt_graph, y = users, by.x = c("Target"), by.y = c("user_id"))
rt_graph <- rt_graph %>% rename(target_screen_name = screen_name)

head(rt_graph)


# Count unique users
c(my_rt_graph$screen_name, my_rt_graph$mentions_screen_name) %>% unique() %>% length() # 4276
c(rt_graph$source_screen_name, rt_graph$target_screen_name) %>% unique() %>% length()  # 2564





