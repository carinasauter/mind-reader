import sys
import time


def executeSomething(count):
	if count == 0:
		time.sleep(15) # start collecting data after 15 seconds
	sys.stdout.write('\a');
	sys.stdout.flush();
	time.sleep(50) # time for not thinking thought
	sys.stdout.write('\a');
	sys.stdout.flush();
	time.sleep(10) # time for thinking thought 
	return

count = 0
while count < 10:
	executeSomething(count)
	count = count + 1


# 15 seconds 	waiting for device to wake up
# beep			
# 50 seconds	not thinking thought
# beep			
# 10 seconds	thinking thought
# beep
# 50 seconds	not thinking thought
# beep