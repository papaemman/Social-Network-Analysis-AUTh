##################################
#                                #
#  User importance - influence   #
#                                #
##################################

# You want to approximate someone’s influence based upon their popularity and the popularity of their followers.

library(rtweet)
library(tidyverse)
library(scales)

influence_snapshot <- function(user, trans=c("log10", "identity")) {
  
  # Test
  # user <- "hadleywickham"
  # trans=c("log10", "identity")
  
  user <- user[1]
  trans <- match.arg(tolower(trimws(trans[1])), c("log10", "identity"))
  
  # Get user's info from twitter api
  user_info <- lookup_users(user)
  dim(user_info)
  head(user_info)
  user_info$followers_count
  
  # Get user's followers
  user_followers <- get_followers(user_info$user_id, n = 110000)
  dim(user_followers)
  head(user_followers)
  
  # Get details for user's followers (uf)
  uf_details <- lookup_users(user_followers$user_id)
  head(uf_details %>% select(user_id, screen_name, followers_count))
  
  # Compute primary influence (2-step neighbors)
  primary_influence <- sum(c(uf_details$followers_count, user_info$followers_count))
  primary_influence <- scales::comma(primary_influence)
  primary_influence
  
  # Plot
  gg <- uf_details %>%
    filter(followers_count > 0) %>% 
    ggplot(aes(followers_count)) +
    geom_histogram(aes(y=..count..), color="lightslategray", fill="lightslategray", alpha=2/3, size=1) +
    scale_x_continuous(expand=c(0,0), trans="log10", labels=scales::comma) +
    labs(
      x="Number of Followers of Followers (log scale)", 
      y="Number of Followers (Count)",
      title=sprintf("Follower chain distribution of %s (@%s)", user_info$name, user_info$screen_name))
  
  print(gg)
  
  return(invisible(list(user_info=user_info, follower_details=uf_details)))
  
}

# Hadley wicham
hadleywickham <- influence_snapshot("hadleywickham")
hadleywickham

# Hadley wicham
rstatstweet <- influence_snapshot("rstatstweet")
rstatstweet
