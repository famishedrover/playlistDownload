from bs4 import BeautifulSoup
import requests
import os
import urllib2
from selenium import webdriver

os.system('clear')


mark = {}
mark['/'] = '%2F'
mark[':'] = '%3A'
mark['?'] = '%3F'
mark['='] = '%3D'

# def download(link,audio,filename):
# 	u = ulib.urlopen(link)
# 	f = open(filename,'wb')
# 	meta = u.info()
# 	print meta.getheaders('Content-Length')
# 	file_size = int(meta.getheaders('Content-Length')[0])

# 	file_dl = 0
# 	blk = 4096

# 	while True :
# 		buff = u.read(blk)
# 		if not buff :
# 			break

# 		file_dl += len(buff)
# 		status = "%10d  [%3.2f%%]" % (file_dl, file_dl * 100. / file_size)
# 		status = status + chr(8)*(len(status)+1)
#         print status
#         f.write(buff)

# 	f.close()

def download(link,audio,filename):
	print ''
	req = urllib2.urlopen(link)
	CHUNK = 1024
	ext = ''
	if audio is True :
		ext = '.mp3'
	else :
		ext = '.mp4'
	i =0 
	with open(filename+ext, 'wb') as fp:
	  while True:
	  	i += 1
	  	chunk = req.read(CHUNK)
	  	if not chunk: break
	  	fp.write(chunk)
	  	print '\b'*int(len(str(i))+1)+str(i),


def download_selenium(link,audio,filename):
	if audio is True :
		ext = '.mp3'
	else :
		ext = '.mp4'
	driver = webdriver.Chrome()
	driver.get(link)
	# driver.quit()



# def download(link ,audio,filename) :
# 	response = requests.get(link, stream=True)
# 	ext = ''
# 	if audio is True :
# 		ext = '.mp3'
# 	else :
# 		ext = '.mp4'

# 	target_path = filename+ext
# 	handle = open(target_path, "wb")
# 	for chunk in response.iter_content(chunk_size=1024):
# 	    if chunk:  # filter out keep-alive new chunks
# 	        handle.write(chunk)


# def download(link,audio,filename):
	# if audio is True :
	# 	ext = 'mp3'
	# else :
	# 	ext = 'mp4'
# 	import urllib2
# 	ffile = urllib2.urlopen(link)
# 	with open(filename+'.'+ext,'wb') as output:
# 		output.write(ffile.read())

# def download(link,audio,filename):
# 	ext = ''
# 	if audio is True :
# 		ext = 'mp3'
# 	else :
# 		ext = 'mp4'
# 	vid = requests.get(link)
# 	with open(filename+ext,'wb') as f :
# 		f.write(vid.content)


def parse_link(link):
	for k,v in mark.iteritems() :
		link = link.replace(k,v)
	return link

def convert_to_keepvid(link) :
	prefix_link = 'http://keepvid.com/?url='
	link = parse_link(link)
	prefix_link += link
	return prefix_link

def get_info(link,out=False):
	link = convert_to_keepvid(link)
	r = requests.get(link)
	soup = BeautifulSoup(r.content,"html.parser")

	data = []

	download = soup.findAll('tr')
	download = download[1:]
	for d in download :
		audio = False
		d_link = d.find('a').get('href')
		if 'https' not in d_link :
			d_link = 'None'
			continue
		ff = d.findAll('td')
		quality= ff[0].text
		ext= ff[1].text
		size= ff[2].text
		if 'ps' in quality :
			audio = True

		if out is True:
			print 'Quality:',quality,'Extension',ext,'Size',size,'Audio',audio
			print d_link
			print '-'*50

		data.append((quality,ext,size,audio,d_link))

	return data

if __name__ == '__main__':

	link = 'https://www.youtube.com/watch?v=QohH89Eu5iM'
	# keepvidlink = 'http://keepvid.com/?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DQohH89Eu5iM'
	keepvidlink = 'http://keepvid.com/?url=https%3A%2F%2Fwww.youtube.com%2F%2Fwatch%3Fv%3DxRJCOz3AfYY&list%3DPL2-dafEMk2A7mu0bSksCGMJEmeddU_H4D&index%3D1'
	data= get_info(link,out=False)
	print data
	link = data[0][4]
	audio = data[0][3]
	# path = 'tester'
	# print filename+'.'+ext
	# download(data[0][4] ,audio, path )

















