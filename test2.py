from bs4 import BeautifulSoup
import requests, time

start = time.time()


f = open("C:/Users/vujke/Documents/GitHub/Scraper/test.txt" ,"w")
errorFile = open("C:/Users/vujke/Documents/GitHub/Scraper/TestError.txt" ,"w")


x = 100

while(x < 105):

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

		#find the table
		table = soup.find("table", {"class" : "tablesaw compact"})

		if table == None:
			x = x+1
			continue

		name_l = soup.h2.get_text().strip()
		index = name_l.index('#')
		end = len(name_l)-index
		name_pos = name_l[0:-(end+2)]
		len_name_pos = len(name_pos)
		position = ""
		name = ""

		if(name_pos[len_name_pos-2].isalpha()):

			position = name_pos[len_name_pos-2:]

			name = name_pos[0:len_name_pos-3]

		elif (name_pos[len_name_pos-3].isalpha()):

			position = name_pos[len_name_pos-3:]

			name = name_pos[0:len_name_pos-4]

		#find a row
		tr = table.find_all("tr", {"class" : "per_game"})

		#if tr == None:
		#	x = x+1
		#	continue

		table_row = tr[-1]

		#find table columns
		table_columns = table_row.find_all("td")

		#if table_columns == None:
		#	x = x+1
		#	continue

		div = soup.find("div", {"class":"profile-wrap"})

		s = div.find_all("p")

		#number of years spent in the NBA
		years = s[1].string.strip()[0]

		if years == "0" or years.isalpha():
			x = x+1
			continue

		i = x-100+1
		f.write(str(i)+"\t")

		
		for y in range (2, 24):
			value = table_columns[y].string.strip()
			f.write(str(value)+"\t")	

		f.write(str(years)+"\t"+position+"\t"+name+"\n")
		#f.write(str"Err"+(year)+"\n")
	
	except Exception as e:
        	errorFile.write("Error on line: "+str(x)+"********"+str(e)+"**********"+"\n")
        	pass
	
	x = x+1

f.close()
errorFile.close()

time = time.time()-start

if(time > 60):
	print 'It took', time/60, 'minutes.'
else: 
	print 'It took', time, 'seconds.'