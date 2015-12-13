#!/usr/bin/env python

import pyperclip
import os
import urllib
from pyperclip import *

copy('')

google = paste()

#print google

while True:

	if google:
		google = urllib.quote(google)
		os.system('firefox http://www.google.com/search?q=%s' % (google))
		copy('')
	
	google = paste()
