# Who talks about #rstats on twitter

df1 <- read.csv("datasets/with_retweets.csv")
df2 <- read.csv("datasets/without_retweets.csv")

dim(df1)
dim(df2)

sum(!df1$screen_name %in% df2$screen_name)
sum(!df2$screen_name %in% df1$screen_name)


user_names <- unique(c(unique(df1$screen_name), unique(df2$screen_name)))
  
length(user_names)

which(user_names=="dataandme")

write.csv(user_names, file = "twitter/datasets/rstats_users.csv", row.names = F)

# How many tweets each user have?

str(df1)

write.csv(df1, file = "twitter/datasets/with_retweets.csv")
write.csv(df2, file = "twitter/datasets/without_retweets.csv")

temp <- c("test1","test2")
write.csv(temp, "twitter/datasets/test.txt")


follow_hadley <- get_followers(user = "hadleywickham")
