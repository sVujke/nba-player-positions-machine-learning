from bs4 import BeautifulSoup
import requests, time

start = time.time()


f = open("C:/Users/vujke/Documents/GitHub/Scraper/NBA_Stats2.txt" ,"w")
errorFile = open("C:/Users/vujke/Documents/GitHub/Scraper/Error.txt" ,"w")

dict_pos = {'PG':'1','SG':'2','SF':'3','PF':'4','C':'5','G':'12','GF':'23','F':'34','FC':'45'}

x = 100

while(x < 200):

	#select a 'URL patern'
	url="http://basketball.realgm.com/player/Marko-Keselj/Summary/"+str(x)

	#request URL
	r = requests.get(url)

	if r.status_code != requests.codes.ok:
		x=x+1
		continue

	try:
		#read response content
		result = r.content 

		#make BeautifulSoup object
		soup = BeautifulSoup(result, 'html.parser')


		#player name and position
		name_l = soup.h2

		if name_l == None:
			x=x+1
			continue

		name_l = name_l.get_text().strip()

		if name_l.find('#') == -1:

			name_pos = name_l
			#print name_pos
			#print len(name_pos)
			len_name_pos = len(name_l)
			print x

			if name_pos[len_name_pos-3].isalpha() and name_pos[len_name_pos-4].isalpha() == False:
				x = x+1
				continue

			if(name_pos[len_name_pos-2].isalpha()):
				position = name_pos[len_name_pos-2:]
				name = name_pos[0:len_name_pos-3]
			else:
				position = name_pos[len_name_pos-1:]
				name = name_pos[0:len_name_pos-2] #dovde bi trebalo da radi
		else:

			index = name_l.index('#')
			end = len(name_l)-index
			name_pos = name_l[0:-(end+2)]
			len_name_pos = len(name_pos)

			if name_pos[len_name_pos-3].isalpha() and name_pos[len_name_pos-4].isalpha() == False:
				x = x+1
				continue

			if(name_pos[len_name_pos-2].isalpha()):
				position = name_pos[len_name_pos-2:]
				name = name_pos[0:len_name_pos-3]
			elif (name_pos[len_name_pos-3].isalpha()):
				position = name_pos[len_name_pos-1:]
				name = name_pos[0:len_name_pos-2]


		#find the table
		table = soup.find("table", {"class" : "tablesaw compact"})

		if table == None:
			x = x+1
			continue

		#find a row
		tr = table.find_all("tr", {"class" : "per_game"})

		#if tr == None:
		#   x = x+1
		#   continue

		table_row = tr[-1]

		#find table columns
		table_columns = table_row.find_all("td")
		print len(table_columns)
		#if table_columns == None:
		#   x = x+1
		#   continue

		div = soup.find("div", {"class":"profile-wrap"})

		s = div.find_all("p")

		#number of years spent in the NBA
		years = s[1].string.strip()[0]

		if years == "0" or years.isalpha():
			x = x+1
			continue

		i = x-100+1
		f.write(str(i)+"\t")

		
		for y in range (2, 23):
			value = table_columns[y].string.strip()
			if value[0] == ".":
				value = "0"+value
			f.write(str(value)+"\t")    

		f.write(str(years)+"\t")

		f.write(dict_pos[position]+"\t")

		f.write(name+"\n")
		#f.write(str"Err"+(year)+"\n")
	
	except Exception as e:
			errorFile.write("Error on x: "+str(x)+"********"+str(e)+"**********"+"\n")
			pass
	
	x = x+1

f.close()
errorFile.close()

time = time.time()-start

if(time > 60):
	print 'It took', time/60, 'minutes.'
else: 
	print 'It took', time, 'seconds.'


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
# POSITION: 1
# NAME: P.J. Tucker