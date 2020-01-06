# Not this script!

library(rtweet)
library(httpuv)

## autheticate via web browser
token <- create_token(
  app = "MSC_SNA",
  consumer_key = "FDwKA8VHDboYJY88mZinO25qo",
  consumer_secret = "W2gAoeaHEHRF0CG92AqRi3jUb4IoVjLoB92gFSscs4nC41LxW9")

## check to see if the token is loaded
identical(token, get_token())

## authenticate via access token
token <- create_token(
  app = "MSC_SNA",
  consumer_key = "FDwKA8VHDboYJY88mZinO25qo",
  consumer_secret = "W2gAoeaHEHRF0CG92AqRi3jUb4IoVjLoB92gFSscs4nC41LxW9",
  access_token = "3353127743-yNwnTfwjPWnXujnKVpjUIJjw3IvGROShMbmN1RK",
  access_secret = "fq5DdujjlZlZXJ01F3U7Wou7M3S7eqtEw3FEOixqhCC0h")

## check to see if the token is loaded
identical(token, get_token())
