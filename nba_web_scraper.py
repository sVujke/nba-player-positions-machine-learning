from bs4 import BeautifulSoup
import requests, time

start = time.time()

#select a 'URL patern'
url="http://basketball.realgm.com/player/Marko-Keselj/Summary/101"

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

service = s[1].string.strip()[0]


# for x in range(21):
#	 value = table_columns[x].string.strip()
#   file.write(value, "\t")

print "GP: %s" % table_columns[2].string.strip()
print "GS: %s" % table_columns[3].string.strip()
print "MIN: %s" % table_columns[4].string.strip()
print "FGM: %s" % table_columns[5].string.strip()
print "FGA: %s" % table_columns[6].string.strip()
print "FGp: 0%s" % table_columns[7].string.strip()
print "3FGM: %s" % table_columns[8].string.strip()
print "3FGA: %s" % table_columns[9].string.strip()
print "3Pp: 0%s" % table_columns[10].string.strip()
print "FTM: %s" % table_columns[11].string.strip()
print "FTA: %s" % table_columns[12].string.strip()
print "FTp: 0%s" % table_columns[13].string.strip()
print "FIC: %s" % table_columns[14].string.strip()
print "OFF: %s" % table_columns[15].string.strip()
print "DEF: %s" % table_columns[16].string.strip()
print "REB: %s" % table_columns[17].string.strip()
print "AST: %s" % table_columns[18].string.strip()
print "STL: %s" % table_columns[19].string.strip()
print "BLK: %s" % table_columns[20].string.strip()
print "PF: %s" % table_columns[21].string.strip()
print "PTS: %s" % table_columns[23].string.strip()
print "YP: %s" % service

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