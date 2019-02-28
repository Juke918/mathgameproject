import sys
import time
import random
from random import randint
from PIL import Image

import os

#from threading import Thread
import threading, Queue



score = 0





timeLeft = 0
q = Queue.Queue()






def similarity():

	ab = randint(1, 50)

	bc = randint(1, 50)

	de = randint(1, 50)


	ab = float(ab)

	bc = float(bc)

	de = float(de)

	x = (de*bc)/ab

	#print float(x)

	x = round(float(x),2)

	#print(x)


	#x = round(x,3)

	#print(x)




	print''
	print''

	#print 'line AB of length ' + str(a) + ' and line BC of length ' + str(b) ' of triangle ABC is similar to line DE of length ' + str(d) + ' and line EF of length x of respectively of triangle DEF'
	print 'line AB of length ' + str(ab) + ' and line BC of length ' + str(bc) + ' of triangle ABC is similar to' 
	print 'line DE of length ' + str(de) + ' and line EF of length x of triangle DEF'

	print ''

	print 'What does x equal [round two decimal places]?'

	print ''

	answer = raw_input()

	answer = float(answer)

	print ''

	if answer == x:

		correct()
		#print 'correct'
		#babe()
		#run()

	else:
		print 'wrong loser the answer was ' + str(x)
		lost()




def polyangle():

	print ''
	print ''

	sides = randint(3,20)

	sides = float(sides)

	angle = (180 * (sides-2))/sides

	angle = round(float(angle),2)

	#print(angle)

	print 'A regular polygon has ' + str(sides) + ' sides'

	print ''

	print 'What is the measure of an interior angle [round two decimal places]?'

	print ''

	answer = raw_input()

	print ''

	answer = float(answer)

	if answer == angle:

		correct()

		#print 'correct'
		#babe()
		#run()
	else:
		print 'wrong loser the answer was ' + str(angle)
		lost()






def timer(timeLeft, q):

	#time.sleep(1)

	
	timeLeft = q.get()
		
	
	#print('yes')

	for i in range(timeLeft):
 



	
		time.sleep(1)


	else:
		print ''
		print('you are too slow loser')
		lost()








def run(timeLeft, q):



	
	timeLeft = 120
	q.put(timeLeft)
	
	questions = [similarity, polyangle]
	random.choice(questions)()






threadRun = threading.Thread(target=run,args=(timeLeft,q))
threadTimer = threading.Thread(target=timer,args=(timeLeft,q))


def babe():
	img = Image.open('babe.jpg')

	img.show()


def endgame():

	print ''
	print ''
	print 'YOU GOT 5 RIGHT!!!'
	print ''
	raw_input('Are you ready to see your prize? Hit enter to see it...')
	print ''
	print('3')
	time.sleep(1)
	print('2')
	time.sleep(1)
	print('1')
	time.sleep(1)

	babe()
	os._exit(0)

	
def correct():

	global score
	score += 1
	if score == 5:
		endgame()
	run(timeLeft, q)

def go():

	threadRun.start()
	threadTimer.start()


def main():

	print ''
	print ''
	print ''
	raw_input('Welcome to my math game! Press enter to continue...')
	print ''
	raw_input('You will have to answer 5 randomly generated math questions in order to recieve a prize at the end! Press enter to continue...')
	print ''
	raw_input('You will have 20 seconds per question and will need a calculator! Press enter to begin...')
	print ''
	print('3')
	time.sleep(1)
	print('2')
	time.sleep(1)
	print('1')
	time.sleep(1)
	print('GO!!!')
	time.sleep(.25)
	go()


def lost():

	print ''
	print 'Oops! You lost! Try Again (just hit up arrow and then enter)... Loser'
	print ''
	os._exit(0)

main()

