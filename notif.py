import notify2
import os
from time import *

start_time = time()

notify2.init('')
r = notify2.Notification('', '')
 
while True:
    for i in [ ('TO DO', 'Write JavaScript'),
               ('TO DO', 'Write Python'),
               ('Thought of the Day', 'Support Open Source'),
               ('Learn. . .', 'Use Linux'),
               ('Thought of the Day', 'Stay Cool'), 
               ('Thought of the Day', 'Stop running for cheese'),
	       ('Thought of the Day', 'You are cool')]:
        r.update(i[0], i[1])
        sleep(120)
	x = int(time() - start_time)%120
	if x == 119:
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.5, 500))
        r.show()
