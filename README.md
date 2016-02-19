# NBA Player Positions Classification
This is a Machine Learning project developed as a part of the course in [Inteligent Systems](http://ai.fon.bg.ac.rs/osnovne/inteligentni-sistemi/) at the [Faculty of Organizational Sciences](http://www.fon.bg.ac.rs/eng/), University of Belgrade, Serbia.

# Problem description
There are several ways to name player positions in basketball, but which one is the best?

The traditional way of describing positions is (three positions classification - data set 1):
* Guard (1)
* Forward (2)
* Center (3)

Today the most common approach is to use five positions (five positions classification - data set 2):
* Point Guard (1)
* Shooting Guard (2)
* Small Forward (3)
* Power Forward (4)
* Center (5)

There is also an alternative approach with players who can play at different two positions (nine positions classification - data set 3):
* Point Guard (1)
* Combo Guard (12)
* Shooting Guard (2)
* Guard Forward (23)
* Small Forward (3)
* Point Forward (34)
* Power Forward (4)
* Forward Center(45)
* Center (5)

This is a visual representation of the position naming methods:  

![alt text](http://snag.gy/GUMzV.jpg)

In this project, a machine learning approach is used to predict player position based on his individual statistics, such as: three 
points made, blocks, games played, height etc.

In order to find the best one out of the mentioned ways for describing positions, results of three classification algorithms will be compared: 
* Naive Bayes
* Suport Vectore Machine (SVM) - performs best with [linear kernel](http://scikit-learn.org/stable/modules/svm.html) in this case 
* Logistic Regresssion

#Data Collection 
Since there is no available and free API for collecting the necesarry data for the analysis, a website [RealGM Basketball](http://basketball.realgm.com/) was sraped. The website contains a rich archive with statistics for thousands of professional basketball players.
 
Scraping was performed by the [nba_web_scraper.py](https://github.com/sVujke/nba-player-positions/blob/master/nba_web_scraper.py) script.

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

The data is split into three sub folders:
* [Data Set 1](https://github.com/sVujke/nba-player-positions/tree/master/data3) - For 3 positions classification
* [Data Set 2](https://github.com/sVujke/nba-player-positions/tree/master/data5) - For 5 positions classification
* [Data Set 3](https://github.com/sVujke/nba-player-positions/tree/master/data) - For 9 positions classification

In these folders following files can be found:
* cleaned 
* train_data - For training the Classifier - contains 60% of the data
* test_data - For tuning the classifiers and testing their performance - contains 20% of the data
* valid_data - For final testing in order to avoid overfit - contains 20% of the data

>Feature "NAME" was removed from these data sets because it is not relevant for this classification problem.

#Feature Selection 

The folowing feature selection methods were utilized for each data set:

* None - No feature selection was done (all features were used).
* Domain knowledge - Features are removed using experience, common sense and knowledge about the game. 
* Univariate Feature Selection - [Select Percentile](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile) - This helps determine the features with the highest score/relevance for predicting the specified label.
* Variance Threshold - Removes all features that don't meet a specified threshold.

# Technical Details

This project was implemented using [Python 2.7](https://www.python.org/) and the following third party libraries:

* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) is a Python library for pulling data out of HTML and XML files. It works with your multiple parsers to provide idiomatic ways of navigating, searching, and modifying the parse tree. In this case it was used for scraping player statistics.  
* [Sckit-Learn](http://scikit-learn.org/stable/) is an open source Python library for machine learning built on top of NumPy and Scipy featuring many classification, regression and clustering algorithms. 
* [Pandas](http://pandas.pydata.org/) is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for Python. DataFrames were the most useful datastructure for this particular project because they enabeled easy data manipulation and spreadsheet-like visualisation
* [NumPy](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) is an open source extension for Python, which adds support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays. NumPy enables any algorithm that can be expressed primarily as operations on arrays and matrices to run almost as quickly as the equivalent C code.

The project was developed using [iPtyhon Notebook](http://ipython.org/), an interactive command shell which added flexibility to the workflow and a much better user experience for this purpose than a standard shell, IDE or editor.

# Classification Results

## Classifying 3 positions - Data Set 1 

The code can be found in [Classification_3_positions.ipynb](https://github.com/sVujke/nba-player-positions/blob/master/Classification_3_positions.ipynb)

###Feature selection 

Using the domain knowledge, it has been decided to remove the following features:  GP, GS, MIN, FG%, 3P%, FT%, PTS, YR, POS, 3PM, FTM, FGM.

According to the Univariate Feature Selection these features were the most important:

![alt text](http://snag.gy/HC7za.jpg)

Using variance threshold 3 features were removed:

![alt text](http://snag.gy/pYsFS.jpg)

###Classification results (accuracy scores):

Feature Selection | Naive Bayes | SVM | Logistic Regression
--- | --- | --- | ---
None | 0.735 | 0.893 | 0.849
Domain Knowledge | 0.893 | 0.58 | 0.877
Univariate | 0.786 | 0.901 | 0.857
Variance Threshold | 1.0 | 1.0 | 1.0

Confusion Matrices verticaly ordered in the same as the table above:

![alt text](http://snag.gy/R6Udg.jpg)

## Classifying 5 positions - Data Set 2 
The code can be found in [Classification_5_positions.ipynb](https://github.com/sVujke/nba-player-positions/blob/master/Classification_5_positions.ipynb)

###Feature selection 

Using the domain knowledge, it has been decided to remove the following features: GP, GS, MIN, FG%, 3P%, FT%, PTS, YR, POS, 3PM, FTM, FGM.

According to the Univariate Feature Selection these features were the most important:

![alt text](http://snag.gy/4wjD6.jpg)

Using variance threshold 3 features were removed:

![alt text](http://snag.gy/OhP1Z.jpg)

###Classification results (accuracy scores):

Feature Selection | Naive Bayes | SVM | Logistic Regression
--- | --- | --- | ---
None | 0.661 | 0.711 | 0.570
Domain Knowledge | 0.725 | 0.753 | 0.669
Univariate | 0.683 | 0.725 | 0.598
Variance Threshold | 1.0 |  0.992 |  0.802

Confusion Matrices verticaly ordered in the same as the table above:

![alt text](http://snag.gy/MmDIb.jpg)

## Classifying 9 positions - Data Set 3 
The code can be found in [Classification_9_positions.ipynb](https://github.com/sVujke/nba-player-positions/blob/master/Classification_9_positions.ipynb)

###Feature selection 

Using the domain knowledge, it has been decided to remove the following features: GP, GS, MIN, FG%, 3P%, FT%, PTS, YR, POS, 3PM, FTM, FGM.

According to the Univariate Feature Selection these features were the most important:

![alt text](http://snag.gy/7e1N0.jpg)

Using variance threshold 4 features were removed:

![alt text](http://snag.gy/TyxX6.jpg)

###Classification results (accuracy scores):

Feature Selection | Naive Bayes | SVM | Logistic Regression
--- | --- | --- | ---
None | 0.527 | 0.618 | 0.548
Domain Knowledge | 0.583 | 0.583 | 0.555
Univariate | 0.381 | 0.405 | 0.409
Variance Threshold | 0.576 | 0.618 |0 .559

Confusion Matrices verticaly ordered in the same as the table above:

![alt text](http://snag.gy/uoxtJ.jpg)

#Conclusion 

### 3 positions

In the case of classifying players in three positions, feature selection based on domain knowledge performed a little better than the Univariate feature selection. 

The best algorithm for the job in this case is SVM.

The results are not as good as when classifying in 5 positions because many center players were classified as forwards and vice versa. Also a fewer number of forward players were classified as guards and vice versa. This can be seen from the confusion matrices.  

### 5 positions

The most accurate prediction of player position based on individual statistics can be made when classification is performed in 5 positions (5 classes) which is probably why this is the most common way to name positions. 

Both Naive Bayes and SVM gave good results These algorithms do not tolerate redundant features, therefore removing such features increases their accuracy. On the orher hand, Logistic Regression does tolerate redundant features, they actually increase the algorithm's accuracy, but not for more than 2 - 2.5% in this case.

The best results were achieved when using Univariate Feature selection. 

### 9 positions 

In this case Naive Bayes performed the best. Domain knoweledge was slightly better than Univariate feature selection.

In this case algorithms performed the worst. This can be explained by the fact that many players from the dataset who can play at two positions spend most of the time playing at one position. As a result, there is a lot of players who play at position 45 and were classified to position 5, or from position 34 classified to position 3 etc.

For instance, Pedja Stojakovic can be found in the dataset with a position 34 (scraped from the website) even though he plays position 3. Similarly, when using Naive Bayes, confusion matrix contains 22 players who play at position 12 (able to play both 1 and 2), but are classified to position 2. 

![alt text](http://snag.gy/lDQ0x.jpg)

This is why, for the purpose of this project, a custom metric was developed, titled "custom_accuracy". The metric can be found at [Classification_9_positions.ipynb](https://github.com/sVujke/nba-player-positions/blob/master/Classification_9_positions.ipynb) and it mesures the accuracy of a classifier, but it counts when a position xn is classified as n or x, for x=1,2,3,4 and n=x+1 as a hit. For example: when a player's position is 34 and the player is classified as 3 or 4 or vice versa, this is considered a good classification. 

