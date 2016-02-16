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
* Combo Guard (2)
* Shooting Guard (2)
* Guard Forward (23)
* Small Forward (3)
* Point Forward (34)
* Power Forward (4)
= Forward Center(45)
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
![alt text](http://snag.gy/GUMzV.jpg)
