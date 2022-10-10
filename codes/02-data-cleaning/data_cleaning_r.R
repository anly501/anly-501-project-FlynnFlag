library(tidyverse)
df<-read_csv("C:/Windows/System32/anly-501-project-FlynnFlag/data/00-raw-data/truth.csv")
#see whether there is some missing values and duplicates
print(sum(is.na(df)))
print(df[duplicated(df),])
#add the label column
df$label="truth"
#transform cities to country
df$location[which(df$location == "U.S.A")] = 'USA'
df$location[which(df$location == "Washington, DC")] = 'USA'
df$location[which(df$location == "'New York, NY'")] = 'USA'
#There are urls at the end of every tweet, we need to drop them
df$text=gsub(pattern="(f|ht)tp(s?)://\\S+","",df$text,perl=T)
write_csv(df,"../../data/01-modified-data/labeled_truth_R.csv")