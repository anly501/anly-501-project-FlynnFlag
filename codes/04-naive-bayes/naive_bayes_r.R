---
title: "Naive Bayes"
author: "Yifan Bian"
date: "2022-10-10"
output: html_document
---

```{r}
library("tidyverse")
library("e1071")
library("caret")
library("caTools")
data=read_csv("C:/Windows/System32/anly-501-project-FlynnFlag/data/01-modified-data/supervised_data.csv")
data<- data%>%
  select(friends_count,followers_count,retweet_count,favorite_count,label)

# Splitting data into train and test data
split <- sample.split(data$label, SplitRatio = 0.7)
train_cl <- subset(data, split == "TRUE")
test_cl <- subset(data, split == "FALSE")

# Feature Scaling
train_scale <- scale(train_cl[, 1:4])
test_scale <- scale(test_cl[, 1:4])

# Fitting Naive Bayes Model to training dataset
classifier_cl <- naiveBayes(label ~ ., data = train_cl)
classifier_cl

# Predicting on test data'
y_pred <- predict(classifier_cl, newdata = test_cl)
# Confusion Matrix
cm <- confusionMatrix(data = y_pred,reference = as.factor(test_cl$label))
cm
```

```{r}
plt <- as.data.frame(cm$table)
plt$Prediction <- factor(plt$Prediction, levels=rev(levels(plt$Prediction)))
cf=ggplot(plt, aes(Prediction,Reference, fill= Freq)) +
        geom_tile() + geom_text(aes(label=Freq)) +
        scale_fill_gradient(low="white", high="#08306B") +
        labs(x = "Predict Labels",y = "True Labels") +
        ggtitle("Confusion Matrix of Tweet and Account-Naive Bayes")
ggsave("confusion_matirx_Tweet_Account_naive_bayes.png", cf, path = "C:/Windows/System32/anly-501-project-FlynnFlag/501-project-website/images/confusion_matirx_text_naive_bayes.png")

```



