from bs4 import BeautifulSoup
import requests, time

start = time.time()


f = open("C:/Users/vujke/Documents/GitHub/Scraper/NBA_Stats.txt" ,"w")
errorFile = open("C:/Users/vujke/Documents/GitHub/Scraper/Error.txt" ,"w")


x = 100

while(x < 500):

	#select a 'URL patern'
	url="http://basketball.realgm.com/player/Marko-Keselj/Summary/"+str(x)

	#request URL
	r = requests.get(url)

	#read response content
	result = r.content 

	#make BeautifulSoup object
	soup = BeautifulSoup(result, 'html.parser')

	#find the table
	table = soup.find("table", {"class" : "tablesaw compact"})

	#find a row
	tr = table.find_all("tr", {"class" : "per_game"})

	table_row = tr[-1]

	#find table columns
	table_columns = table_row.find_all("td")

	div = soup.find("div", {"class":"profile-wrap"})

	s = div.find_all("p")

	#number of years spent in the NBA
	years = s[1].string.strip()[0]

	i = x-100+1
	f.write(str(i)+"\t")

	try:
		for y in range (2, 24):
			value = table_columns[y].string.strip()
			f.write(str(value)+"\t")	

		f.write(str(years)+"\n")
		#f.write(str(year)+"\n")
	
	except Exception as e:
            errorFile.write(str(x)+"********"+str(e)+"**********"+str(table_columns)+"\n")
            pass
	
	x = x+1

f.close()
errorFile.close()

print 'It took', time.time()-start, 'seconds.'


#************* Data labels explained**************

# GM, GP, GS - Games played, games started 

# PTS - Points scorred

# FGM, FGA, FG% - Field goals MADE, ATEMPTED, PERCENTAGE

# 3FGM, 3FGA, 3FG% - Three point field goals MADE, ATEMPTED, PERCENTAGE

# FTM, FTA, FT% - Free throws MADE, ATEMPTED, PERCENTAGE

# OFF, DEF, Reb - Offensive Rebounds, Defensive Rebounds, All Rebounds

# FIC (Floor Impact Counter): A formula to encompass all aspects of the box score into a single statistic. The intent of the statistic is similar to other efficiency stats, but assists, shot creation and offensive rebounding are given greater importance. Created by Chris Reina in 2007. 
# Formula: http://basketball.realgm.com/info/glossary


# Pitanja:
# 1. da li mi treba broj pogodjenih ako imam procenat i broj pokusaja? 
# 2. da li je efikasnije da ubacim for ili da imam ovako 20 linija? 

# GP: 91
# GS: 7
# MIN: 9.5
# FGM: 1.13
# FGA: 2.56
# FGp: 0.44
# 3FGM: 0.2
# 3FGA: 0.6
# 3Pp: 0.30
# FTM: 0.69
# FTA: 1.01
# FTp: 0.68
# FIC: 1.75
# OFF: 0.56
# DEF: 1.08
# REB: 1.64
# AST: 0.48
# STL: 0.29
# BLK: 0.04
# PF: 1.58
# PTS: 3.16
# YP: 2