# NBA Player Positions Classification
This is a Machine Learning project developed as a part of the course in [Inteligent Systems](http://ai.fon.bg.ac.rs/osnovne/inteligentni-sistemi/) at the [Faculty of Organizational Sciences](http://www.fon.bg.ac.rs/eng/), University of Belgrade, Serbia.

# Problem description
There are several ways to name player positions in basketball, but which one is the best? In the domain of basketball, usually one of three position classification schemes are used:

1) Three Positions Classification - The traditional way of describing positions is:
* Guard (1)
* Forward (2)
* Center (3)

2) Five Positions Classification - Today the most common approach is to use five positions:
* Point Guard (1)
* Shooting Guard (2)
* Small Forward (3)
* Power Forward (4)
* Center (5)

3) Nine Positions Classification - There is also an alternative approach with players who can play at different two positions:
* Point Guard (1)
* Combo Guard (12)
* Shooting Guard (2)
* Guard Forward (23)
* Small Forward (3)
* Point Forward (34)
* Power Forward (4)
* Forward Center(45)
* Center (5)

Following is a visual representation of the position naming methods:  

![alt text](http://snag.gy/GUMzV.jpg)

In this project, a machine learning approach is used to predict player's position based on his individual statistics, such as: three 
points made, blocks, games played, height etc. And a goal of the project is to define the best position classification scheme for basketball players.

In order to accomplish this, results of three classification algorithms are compared: 
* Naive Bayes
* Suport Vectore Machine (SVM) - used with a [linear kernel](http://scikit-learn.org/stable/modules/svm.html) 
* Logistic Regresssion

#Data Collection 
Since there is no available and free API for collecting the necessary data for the analysis, a website [RealGM Basketball](http://basketball.realgm.com/) was sraped. The website contains a rich archive with statistics for thousands of professional basketball players.

#Data Exploration 
The collected data is made out of 26 different features. Following is the DataFrame representation:

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

The data is split into three datasets:
* [Dataset 1](https://github.com/sVujke/nba-player-positions/tree/master/data3) - For 3 positions classification
* [Dataset 2](https://github.com/sVujke/nba-player-positions/tree/master/data5) - For 5 positions classification
* [Dataset 3](https://github.com/sVujke/nba-player-positions/tree/master/data) - For 9 positions classification

In these folders following files can be found:
* cleaned 
* train_data - For training the Classifier - contains 60% of the data
* test_data - For tuning the classifiers and testing their performance - contains 20% of the data
* valid_data - For final testing in order to avoid overfit - contains 20% of the data

#Feature Selection 

For each dataset, feature "NAME" was removed because it is not relevant for this classification problem. Four different feature selection methods were used on each dataset, so actually, each out of three datasets have four variations.

Feature selection methods:

1. None - No feature selection was done (all features were used).
2. Domain knowledge - Features are removed using experience, common sense and knowledge about the game. 
3. Univariate Feature Selection - [Select Percentile](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile) - This helps determine features with the highest score/relevance for predicting the specified label.
4. Variance Threshold - Removes all features that don't meet a specified threshold.

# Technical Details

This project was implemented using [Python 2.7](https://www.python.org/) and the following third party libraries:

* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) is a Python library for pulling data out of HTML and XML files. It works with your multiple parsers to provide idiomatic ways of navigating, searching, and modifying the parse tree. In this case it was used for scraping player statistics.  
* [Sckit-Learn](http://scikit-learn.org/stable/) is an open source Python library for machine learning built on top of NumPy and Scipy featuring many classification, regression and clustering algorithms. 
* [Pandas](http://pandas.pydata.org/) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for Python. DataFrames were the most useful datastructure for this particular project because they enabeled easy data manipulation and spreadsheet-like visualisation
* [NumPy](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) is an open source extension for Python, which adds support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays. NumPy enables any algorithm that can be expressed primarily as operations on arrays and matrices to run almost as quickly as the equivalent C code.

The project was developed using [iPtyhon Notebook](http://ipython.org/), an interactive command shell which added flexibility to the workflow and a much better user experience for this purpose than a standard shell, IDE or editor.

Data scraping was performed by the [nba_web_scraper.py](https://github.com/sVujke/nba-player-positions/blob/master/nba_web_scraper.py) script.

The code performing classification on each three datasets can respectively be found at:
- [Classification_3_positions.ipynb](https://github.com/sVujke/nba-player-positions/blob/master/Classification_3_positions.ipynb)
- [Classification_5_positions.ipynb](https://github.com/sVujke/nba-player-positions/blob/master/Classification_5_positions.ipynb)
- [Classification_9_positions.ipynb](https://github.com/sVujke/nba-player-positions/blob/master/Classification_9_positions.ipynb)

# Classification Results

## Dataset 1 - Three Positions Classification 

###Feature selection

1) None - all features were used

2) Domain knowledge - the following features were removed: GP, GS, MIN, FG%, 3P%, FT%, PTS, YR, POS, 3PM, FTM, FGM.

3) Univariate Feature Selection - following features were found to be the most important:

* OFF
* AST
* BLK
* W
* H

4) Variance Threshold - 3 features were removed:

* FG%
* 3P%
* FT%

###Classification results (accuracy scores):

Feature Selection | Naive Bayes | SVM | Logistic Regression
--- | --- | --- | ---
None | 0.81 (+/- 0.08) | 0.90 (+/- 0.04) | 0.89 (+/- 0.06)
Domain Knowledge | 0.87 (+/- 0.07) | 0.91 (+/- 0.05) | 0.90 (+/- 0.06)
Univariate | 0.89 (+/- 0.04) | 0.91 (+/- 0.04) | 0.89 (+/- 0.06)
Variance Threshold | 0.82 (+/- 0.07) | 0.90 (+/- 0.04) | 0.90 (+/- 0.05)

###Confusion Matrices ordered verticaly in the same way as the table above:

![alt text](http://snag.gy/R6Udg.jpg)

## Dataset 2 - Five Positions Classification

###Feature selection

1) None - all features were used

2) Domain knowledge - the following features were removed: GP, GS, MIN, FG%, 3P%, FT%, PTS, YR, POS, 3PM, FTM, FGM.

3) Univariate Feature Selection - following features were found to be the most important:

* OFF
* AST
* BLK
* W
* H

4) Variance Threshold - 3 features were removed:

* FG%
* 3P%
* FT%

###Classification results (accuracy scores):

Feature Selection | Naive Bayes | SVM | Logistic Regression
--- | --- | --- | ---
None | 0.70 (+/- 0.15) | 0.82 (+/- 0.12) | 0.69 (+/- 0.15)
Domain Knowledge | 0.74 (+/- 0.09) | 0.82 (+/- 0.09) | 0.72 (+/- 0.11)
Univariate | 0.77 (+/- 0.11) | 0.81 (+/- 0.09) | 0.72 (+/- 0.08)
Variance Threshold | 0.71 (+/- 0.11) |  0.82 (+/- 0.10)|  0.70 (+/- 0.12)

###Confusion Matrices ordered verticaly in the same way as the table above:

![alt text](http://snag.gy/MmDIb.jpg)

## Dataset 3 - Nine positions Classification

###Feature selection

1) None - all features were used

2) Domain knowledge - the following features were removed: GP, GS, MIN, FG%, 3P%, FT%, PTS, YR, POS, 3PM, FTM, FGM.

3) Univariate Feature Selection - following features were found to be the most important:

![alt text](http://snag.gy/7e1N0.jpg)

4) Variance Threshold - 4 features were removed:

 * FG% 
 * 3P% 
 * FT% 
 * STL

###Classification results (accuracy scores):

Feature Selection | Naive Bayes | SVM | Logistic Regression
--- | --- | --- | ---
None | 0.527 | 0.618 | 0.548
Domain Knowledge | 0.583 | 0.583 | 0.555
Univariate | 0.381 | 0.405 | 0.409
Variance Threshold | 0.576 | 0.618 |0 .559

###Confusion Matrices ordered verticaly in the same way as the table above:

![alt text](http://snag.gy/uoxtJ.jpg)

#Conclusion 

### Dataset 1 - Three Positions Classification 

The most accurate prediction of player position based on individual statistics can be made when classification is performed in three positions (3 classes)

In the case feature selection using the Variance Threshold method gave the best results for all three classifiers and it enabled Naive Bayes, SVM and Linear Regression to perform equaly good. 
Univariate feature selection and Domain Knowledge methods also enabeled the classifiers to perform well. The worst performance was recorded for SVM when domain knowledge was used to remove features.  


### Dataset 2 - Five Positions Classification

Classification results are decent, but not as good as when classifying in three positions. 

Again, the best method for feature selection was Variance Threshold and the best performing classifier was Naive Bayes in that particular case. SVM was the most accurate classifier in other variations of feature selection. Logistic Regression performed the worst.

All three classifiers performed the worst when there were no features removed. 

### Dataset 3 - Nine positions Classification

In this case SVM performed the best. Variance Threshold was the best feature selection method, followed by the domain knowledge feature selection method.

Algorithms performed the worst on this dataset. This can be explained by the fact that many players from the dataset who can play at two positions spend most of the time playing at one position. As a result, there is a lot of players who play at position 45 and were classified to position 5, or from position 34 classified to position 3 etc.

For instance, Pedja Stojakovic can be found in the dataset with a position 34 (scraped from the website) even though he plays position 3. Similarly, when using Naive Bayes, confusion matrix contains 21 players who play at position 12 (able to play both 1 and 2), but are classified to position 2. 

![alt text](http://snag.gy/R71nK.jpg)

This is why, for the purpose of this project, a custom metric was developed, titled "custom_accuracy". The metric can be found at [Classification_9_positions.ipynb](https://github.com/sVujke/nba-player-positions/blob/master/Classification_9_positions.ipynb) and it mesures the accuracy of a classifier, but it counts when a position xn is classified as n or x, for x=1,2,3,4 and n=x+1 as a hit. For example: when a player's position is 34 and the player is classified as 3 or 4 or vice versa, this is considered a good classification. 
