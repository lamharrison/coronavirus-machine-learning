<div align=left><img width="379" height="114.9" src="https://i.ibb.co/fkQvQfM/logo-prediction.png"/></div>

UK Corona Virus Prediction
===========================
(To be continued) This project intends to implement the data of confirmed Corona Virus cases and predict the future trend of the epidemic in the United Kingdom and beyond.

<div align=center><img width="420" height="238" src="https://cdn.cnn.com/cnnnext/dam/assets/200130165125-corona-virus-cdc-image-super-tease.jpg"/></div>

|Author|E-mail|Github
|----|---|---
|Big Tree|lamharrison123@gmail.com|https://github.com/lamharrison
|Jiaming Lu|lujiammy@outlook.com|https://github.com/lujiammy

## Feature
- [x] Implementing MLP models and constructing appropriate underlying functions
- [x] Extracting data from trustworthy data sources
- [x] Using real-time data to predict the epidemic trend within the UK
- [x] Predicting the epidemic trend of other similar-sized European countries including Italy, Germany and France
- [x] plotting the result regarding confirmed result and predicting trend into the chart

## Model
This project basically used the Multilayer Perceptron (MLP) model for analysing data. MLP is also known as one of Artificial Neural Networks(ANN) and could utilise Backpropagation to train the model between different nodes. The activation functions of nodes define the output of nodes given an input or set of inputs.

![MLP.png](https://miro.medium.com/max/3446/1*-IPQlOd46dlsutIbUq1Zcw.png)

We have primarily considered activation functions as sigmoid functions that almost perfectly represent the characteristics of the number of people who have been infected by the Corona Virus in the UK. We also used other activation functions like ReLU and linear functions for improving the precision.

![activationfunctions.png](https://miro.medium.com/max/1452/1*XxxiA0jJvPrHEJHD4z893g.png)

## Data source
The trustworthy data sources are always overwhelming essential to ensure the authenticity of reaching the prediction objective. We have collaborated with Jeff (https://isjeff.com/home) who provided us with valuable data for Corona Virus within the UK and other European countries based on the government statistical result. Thanks for his help!

 To find more information about our data sources, the attached link as follows could be friendly visited. 

Global data: https://github.com/isjeffcom/coronavirusDataGlobal    
UK data: https://github.com/isjeffcom/coronvirusFigureUK

![data](https://github.com/lamharrison/coronavirus-machine-learning/blob/master/img/london%20visual.png)
