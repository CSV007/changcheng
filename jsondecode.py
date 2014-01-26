import urllib2
import simplejson as json
response=urllib2.urlopen('https://graph.facebook.com/htc/feed?access_token=334601356657560|ecff84f4f5701accddb66546a8a83a6e')
html=response.read()

test = json.loads(html)

#file=open('jsondecode.txt','w')
#for i in test:
#    file.write(i+'\n')
#file.close()

print test['data'][0]['id']

for message in test['data']:
	if 'likes' in message:
		print 'this from is post'
		print message.get('id')
		print message.get('likes').get('data') #likes from posts
	
	if message.get('comments'): #if this post has comments
		for comment in message.get('comments')['data']: 
			if 'like_count' in comment:  #get likes from comments
				print 'this is from comment'
				print comment.get('id')
				print comment.get('like_count')
