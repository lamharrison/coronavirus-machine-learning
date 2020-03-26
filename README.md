<div align=left><img width="379" height="114.9" src="https://i.ibb.co/fkQvQfM/logo-prediction.png"/></div>

UK Corona Virus Prediction
===========================
( To be continued ) This project intends to implement the data of confirmed cases of Corona Virus and predict the future trend of the epidemic in the United Kingdom and beyond.

<div align=center><img width="420" height="238" src="https://cdn.cnn.com/cnnnext/dam/assets/200130165125-corona-virus-cdc-image-super-tease.jpg"/></div>

|Author|E-mail|Github
|----|---|---
|Big Tree|lamharrison123@gmail.com|https://github.com/lamharrison
|Jiaming Lu|lujiammy@outlook.com|https://github.com/lujiammy

## Feature
- [x] Implement an MLP model
- [x] Using real time data to predict the epidemic trend within UK
- [x] Using updated data to predict the epidemic trend within Italy
- [ ] predict the epidemic trend of other European countries

## Model
Multilayer Perceptron (MLP) is also known as one of Artificial Neural Network and could utilise Backpropagation to train the model between different nodes. The activation functions of nodes define the output of nodes given an input or set of inputs

![MLP.png](https://miro.medium.com/max/3446/1*-IPQlOd46dlsutIbUq1Zcw.png)

We have considered that the characteristic of the number of people could be represented by the sigmoid function, who have been infected by the Corona Virus in the UK.

We also used activation function like ReLU and linear functions.

![MLP.png](https://miro.medium.com/max/1452/1*XxxiA0jJvPrHEJHD4z893g.png)

## Data source
Jeff (https://isjeff.com/home) provided us with data for Corona Virus within the UK based on the government statistical result. Thanks for his help!    
Global data: https://github.com/isjeffcom/coronavirusDataGlobal    
UK data: https://github.com/isjeffcom/coronvirusFigureUK
