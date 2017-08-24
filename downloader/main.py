from bs4 import BeautifulSoup
import requests
import os
from keepvid import *


os.system('clear')

finalLink = 'https://www.youtube.com/'
playlistUrl = 'https://www.youtube.com/playlist?list=PLBlnK6fEyqRjMH3mWf6kwqiTbT798eAOm'
playlistUrl = 'https://www.youtube.com/playlist?list=PLR-nyzWqhEMn9DcqAxp5pbsDrLSdDjJ5V'
# https://www.youtube.com/watch?v=xRJCOz3AfYY&list=PL2-dafEMk2A7mu0bSksCGMJEmeddU_H4D&index=1
						
r = requests.get(playlistUrl)
soup = BeautifulSoup(r.content,"html.parser")


links = soup.findAll('tr',{'class':'pl-video yt-uix-tile '})

header = soup.find('')

filename = 'videos/'
for link in links :
	# print link 
	ff = link.find('td',{'class':'pl-video-title'})
	youlink = finalLink + ff.find('a').get('href')
	youtitle = ff.text
	xname = youtitle.strip().replace('\n',' ').strip().split('by')
	xname = xname[0].strip() + ' ' + xname[1].strip()
	print xname, ' ',
	data = get_info(youlink)
	# print youlink
	link = data[0][4]
	audio = data[0][3]
	# print link , audio
	download(link,audio,filename+xname)
	print '-'*50