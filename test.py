
from bs4 import BeautifulSoup
import requests, time

start = time.time()
f = open("C:/Users/vujke/Documents/GitHub/Scraper/test.txt" ,"a")
errorFile = open("C:/Users/vujke/Documents/GitHub/Scraper/TestError.txt" ,"w")

dict_pos = {'PG':'1','SG':'2','SF':'3','PF':'4','C':'5','G':'12','GF':'23','F':'34','FC':'45'}

x=500
while x<510:
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


			#i = x-100+1
			#f.write(str(i)+"\t")

			#f.write()

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

		f.write(dict_pos[position]+"\t")
		f.write(name+"\n")
		
	except Exception as e:
        	errorFile.write("Error on line: "+str(x)+"********"+str(e)+"**********"+"\n")
        	pass
    

	x = x+1

f.close()
errorFile.close()

print "done"
time = time.time()-start

if(time > 60):
	print 'It took', time/60, 'minutes.'
else: 
	print 'It took', time, 'seconds.'
	
