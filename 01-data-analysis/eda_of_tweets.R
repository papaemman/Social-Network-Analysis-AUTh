####################################################
#                                                  #
#  Exploratory Data analysis for twitter dataset   #
#                                                  #
####################################################

# Load packages
library(dplyr)
library(ggplot2)


# Import dataset
tweets <- read.csv("datasets/with_retweets.csv")

dim(tweets)
