from bs4 import BeautifulSoup
import requests, time


	#select a 'URL patern'
url="http://basketball.realgm.com/player/Marko-Keselj/Summary/102"

#request URL
r = requests.get(url)

if r.status_code != requests.codes.ok:
	print "status code not good"


#read response content
result = r.content 

	#make BeautifulSoup object
soup = BeautifulSoup(result, 'html.parser')

	#find the table


	#i = x-100+1
	#f.write(str(i)+"\t")

	#f.write()

name_l = soup.h2.get_text().strip()

if name_l.find('#') == -1:

	name_pos = name_l
	print name_pos
	print len(name_pos)
	len_name_pos = len(name_l)

	if(name_pos[len_name_pos-2].isalpha()):
		position = name_pos[len_name_pos-3:]
		name = name_pos[0:len_name_pos-4]
	else:
		position = name_pos[len_name_pos-1:]
		name = name_pos[0:len_name_pos-2] #dovde bi trebalo da radi
else:

	index = name_l.index('#')
	end = len(name_l)-index
	name_pos = name_l[0:-(end+2)]
	len_name_pos = len(name_pos)
	if(name_pos[len_name_pos-2].isalpha()):
		position = name_pos[len_name_pos-2:]
		name = name_pos[0:len_name_pos-3]
	elif (name_pos[len_name_pos-3].isalpha()):
		position = name_pos[len_name_pos-3:]
		name = name_pos[0:len_name_pos-4]


print name

print position
print len(name)
	
	
