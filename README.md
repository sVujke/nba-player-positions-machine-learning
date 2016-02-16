# NBA Player Positions Classification
This is a Machine Learning project developed as part of the
[Inteligent Systems](http://ai.fon.bg.ac.rs/osnovne/inteligentni-sistemi/) 
course at the [Faculty of Organizational Sciences](http://www.fon.bg.ac.rs/eng/), University of Belgrade

# Problem description
There are several ways to name player positions in basketball, but which is the best?

The traditional way of describing positions was by using the following three:
* Guard (1)
* Forward (2)
* Center (3)

Today it is most common to use 5 positions described as:
* Point Guard (1)
* Shooting Guard (2)
* Small Forward (3)
* Power Forward (4)
* Center (5)

There is also an option with players who can play two positions:
* Point Guard (1)
* Combo Guard (12)
* Shooting Guard (2)
* Guard Forward (23)
* Small Forward (3)
* Point Forward (34)
* Power Forward (4)
* Forward Center(45)
* Center (5)

![alt text](http://snag.gy/GUMzV.jpg)

I will use machine learning to predict player positions based on their individual statistics souch as three 
points made, blocks, games played, height etc.

In order to find out which of the mentioned ways to describe positions is the best I will compare their classification results using
three classification algorithms: 
* Naive Bayes
* Suport Vectore Machine (SVM)
* Logistic Regresssion

#Data Collection 
In oreder to collect enough data I had to use an API or to scrape the data from a website. Since I could not find a good free API 
I decided to scrape http://basketball.realgm.com/ which has a lot of statistics for thousands of professional basketball players. 
This is performed by the [nba_web_scraper.py](https://github.com/sVujke/nba-player-positions/blob/master/nba_web_scraper.py) script.

#Data Exploration 
The collected data is made out of 26 different features. This is a DataFrame representation:

![alt text](http://snag.gy/k5iSf.jpg)

![alt text](http://snag.gy/atRSE.jpg)

Feature names:

Short | Long | Short | Long
--- | --- | --- | ---
GP| Games Played | GS | Games Started
MIN| Minutes Played | FGM | Field Goals Made
FGA| Field Goals Atempted | FG% | Field Goal Percent 
3PM| 3 Points Made | 3PA | 3 Points Atempted
3P%| 3 Points Percent | FTM | Free Throws Made 
FTA| Free Throws Atempted | FT% | Free Throws Percent
OFF| Offensive Rebounds | DEF | Defensive Rebounds
TRB| Total Rebounds | AST | Assists
STL| Steals | BLK | Blocks
PF| Personal Fouls | TOV | Turnovers
PTS| Points | YR | Years playing
POS| Positions | W | Weight
H| Height | NAME | Name

> Features refference http://basketball.realgm.com/info/glossary

The data is split into three sub folders:
*[data3](https://github.com/sVujke/nba-player-positions/tree/master/data3) - For 3 positions classification
*[data5](https://github.com/sVujke/nba-player-positions/tree/master/data5) - For 5 positions classification
*[data](https://github.com/sVujke/nba-player-positions/tree/master/data) - For 9 positions classification

In these folders following files can be found:
* cleaned
* train_data - For training the Classifier
* test_data - For testing the accuracy of the Classifier
* valid_data - For final testing in order to avoid overfit

#Feature Selection 

Feature Selection was done in the same way for all three classifications, thre methods were used:
* Domain knowledge
* Univariate Feature Selection - [Select Percentile](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile) - This helps determine the features with the highest score/relevance for predicting the specified label
* Variance Threshold - Removes all features that don't meet a specified threshold

# Classifying 3 positions 

This is the first option of description mentioned above, with three positions Guard (1), Forward (2), Center (3):

##Fearute selection 

Using domain knowledge I decided to remove the following features:  GP,GS,MIN,FG%,
      3P%,FT%,PTS,YR,POS,3PM,FTM,FGM
Using variance threshold 4 features vere removed

According to Univariate Feature Selection thes features were the most important:

![alt text](http://snag.gy/b9OI4.jpg)

##Classification results:

Feature Selection | Naive Bayes | SVM | Logistic Regression
--- | --- | --- | ---
None | 0.68 | 0.53 | 0.858
Domain Knowledge | 0.79 | 0.893 | 0.877
Univariate | 0.73 | 0.893 | 0.85

# Classifying 5 positions 

This is the first option of description mentioned above, with three positions Point Guard (1), 
Shooting Guard (2), Small Forward (3), Power Forward (4), Center (5)

##Fearute selection 

Using domain knowledge I decided to remove the following features:  GP,GS,MIN,FG%,
      3P%,FT%,PTS,YR,POS,3PM,FTM,FGM
Using variance threshold 4 features vere removed

According to Univariate Feature Selection thes features were the most important:

![alt text](http://snag.gy/Ileu6.jpg)

##Classification results:

Feature Selection | Naive Bayes | SVM | Logistic Regression
--- | --- | --- | ---
None | --- | --- | ---
Domain Knowledge | --- | --- | ---
Univariate | --- | --- | ---
Variance Threshold | --- | --- | ---

# Classifying 9 positions 

This is the first option of description mentioned above, with three positions Point Guard (1), 
Shooting Guard (2), Small Forward (3), Power Forward (4), Center (5), Combo Guard (12), Guard Forward (23), Point Forward (34), Forward Center(45)

##Fearute selection 

Using domain knowledge I decided to remove the following features:  GP,GS,MIN,FG%,
      3P%,FT%,PTS,YR,POS,3PM,FTM,FGM
Using variance threshold 4 features vere removed

According to Univariate Feature Selection thes features were the most important:

![alt text](http://snag.gy/u9t2m.jpg)

##Classification results:

Feature Selection | Naive Bayes | SVM | Logistic Regression
--- | --- | --- | ---
None | --- | --- | ---
Domain Knowledge | --- | --- | ---
Univariate | --- | --- | ---
Variance Threshold | --- | --- | ---
