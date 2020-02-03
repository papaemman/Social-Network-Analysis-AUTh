#######################
#                    #
#   Analyze graphs   #
#                    #
######################

# Load packages
library(igraph)
library(ggraph)

# Import data
retweet_graph <- read.csv("data/processed/retweet_graph_full.csv",stringsAsFactors = F)

head(retweet_graph)
str(retweet_graph)


# Create igraph object
rt_graph <- graph_from_data_frame(d = retweet_graph, directed = T)

rt_graph


## Analyze graph

# Degrees: 

degrees_df <- data.frame(in_degree = degree(rt_graph,mode = "in"),
                         out_degree = degree(rt_graph,mode = "out"),
                         user_name = V(rt_graph)$name)

rownames(degrees_df) <- NULL

degrees_df <- degrees_df %>%  arrange(desc(in_degree), out_degree)

head(degrees_df, n = 10)


# Most retweeted users
degree(rt_graph,mode = "in") %>% sort(decreasing =T) %>% head()

# Users with most retweets
degree(rt_graph,mode = "out")%>% sort(decreasing =T) %>% head()


# Degree distribution
ggplot(degrees_df, aes(in_degree)) + geom_histogram(binwidth = 10) + ggtitle("In degree distribution")
table(degrees_df$in_degree)

ggplot(degrees_df, aes(out_degree)) + geom_histogram(binwidth = 10) + ggtitle("Out degree distribution")
table(degrees_df$out_degree)


## Visualize graph of retweets ----
summary(degrees_df)

# To help de-clutter the vertex labels, we’ll only add labels for nodes that have a degree of 50 or more
# (I look at the degree distribuiton to guess 
# We’ll also include the degree for those nodes so we can size them properly:
  
V(rt_graph)$name <- unname(ifelse(degree(rt_graph)[V(rt_graph)] > 50, names(V(rt_graph)), "")) 
V(rt_graph)$node_size <- unname(ifelse(degree(rt_graph)[V(rt_graph)] > 50, degree(rt_graph), 0)) 

# Super slow: 
ggraph(rt_graph, layout = 'linear', circular = TRUE) + 
  geom_edge_arc(edge_width=0.125, aes(alpha=..index..)) +
  geom_node_label(aes(label=node_label, size=node_size),
                  label.size=0, fill="#ffffff66", segment.colour="springgreen",
                  color="slateblue", repel=TRUE, family=font_rc, fontface="bold") +
  coord_fixed() +
  scale_size_area(trans="sqrt") +
  labs(title="Retweet Relationships", subtitle="Most retweeted screen names labeled. Darkers edges == more retweets. Node size == larger degree") +
  theme_graph(base_family=font_rc) +
  theme(legend.position="none")



## Community detection





