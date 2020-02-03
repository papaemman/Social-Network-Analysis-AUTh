######################
#                    #
#  More on rtweet    #
#                    #
######################

# Load packages
library(rtweet)



## Resolving User Profile Information ----

# You have a collection of ids and need to resolve basic profile information (such as screen names) for these users.

recent_rtweeters <- lookup_users()


## Crawling Followers to Approximate Primary Influence ----
rtweet::get_followers()


## Analyzing Friendship Relationships such as Friends of Friends ----

# Problem: You want to create a graph that facilitates the analysis of interesting relationships amongst users,
# such as friends of friends.

# Solution:  Systematically harvest all of the friendships for users of interest, 
# and load the data into igraph which offers native graph operations.