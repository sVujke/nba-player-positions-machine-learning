from bs4 import BeautifulSoup
import requests, time

start = time.time()


f = open("C:/Users/vujke/Documents/GitHub/basketball-positions-machine-learning/NBA_size.txt" ,"w")
errorFile = open("C:/Users/vujke/Documents/GitHub/basketball-positions-machine-learning/Error_size.txt" ,"w")

dict_pos = {'PG':'1','SG':'2','SF':'3','PF':'4','C':'5','G':'12','GF':'23','F':'34','FC':'45'}

x = 100

while(x < 150):

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

		p = soup.find_all('p')
		#player name and position
		
		#number of years spent in the NBA
		uncleaned_size = ""
		
		for u in range(7):
			uncleaned_size = p[u].text.strip()
			if(uncleaned_size[0] == "H"):
				uncleaned_size = p[u].text.strip()
				break
							
		print x 
		pos = uncleaned_size.index("W")
		
		weight_uncleaned =  uncleaned_size[pos:]
		height_uncleaned = uncleaned_size[:pos-5]

		bracket1 = weight_uncleaned.index("(")

		bracket2 = height_uncleaned.index("(")

		weight = weight_uncleaned[bracket1:].lstrip("(").rstrip(")").strip("kg")
		height = height_uncleaned[bracket2:].lstrip("(").rstrip(")").strip("cm")

		#if x%20 == 0:
		#		print x
		 

		f.write(weight+"\t")
		f.write(height+"\n")
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