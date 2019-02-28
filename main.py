import sys
import time
import random
from random import randint
from PIL import Image			

import os

#from threading import Thread
import threading, Queue

#importing a bunch of librarys 

score = 0





timeLeft = 0
q = Queue.Queue()			`#starting up the queue for data sharing across threads





#function for randomly generated question on similarity

def similarity():

	ab = randint(1, 50)

	bc = randint(1, 50)		#random generate numbers

	de = randint(1, 50)


	ab = float(ab)

	bc = float(bc)			#data type conversion for syntax

	de = float(de)

	x = (de*bc)/ab			#geometry equation to figure out value of x

	#print float(x)

	x = round(float(x),2)		#rounding x to two decimal points

	#print(x)


	#x = round(x,3)

	#print(x)




	print''			#space between text
	print''

	#print 'line AB of length ' + str(a) + ' and line BC of length ' + str(b) ' of triangle ABC is similar to line DE of length ' + str(d) + ' and line EF of length x of respectively of triangle DEF'
	print 'line AB of length ' + str(ab) + ' and line BC of length ' + str(bc) + ' of triangle ABC is similar to' 
	print 'line DE of length ' + str(de) + ' and line EF of length x of triangle DEF'  #writing question

	print ''

	print 'What does x equal [round two decimal places]?' 

	print ''

	answer = raw_input()   #answer equals user input

	answer = float(answer)  #data type conversion

	print ''

	if answer == x:

		correct()
		#print 'correct'
		#babe()
		#run()

	else:
		print 'wrong loser the answer was ' + str(x)
		lost()
		
#determines which function to run depending on answer



#function for randomly generated question on interior angles of regular polygons
def polyangle():

	print ''
	print ''

	sides = randint(3,20)		#random generate numbers

	sides = float(sides)		#data type conversion	

	angle = (180 * (sides-2))/sides		#geometry equation to figure out measure of interior angle

	angle = round(float(angle),2) 		#round answer to decimal points

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



#function for timer


def timer(timeLeft, q):

	#time.sleep(1)

	
	timeLeft = q.get() #gets value of variable timeLeft from queue
		
	
	#print('yes')

	for i in range(timeLeft):
 



	
		time.sleep(1) #waits a second


	else:
		print ''
		print('you are too slow loser')
		lost()





#randomly runs questions and sets timeLeft


def run(timeLeft, q):



	
	timeLeft = 120
	q.put(timeLeft) #pushes timeLeft into queue
	
	questions = [similarity, polyangle]
	random.choice(questions)()




#sets functions timer() and run() to threads

threadRun = threading.Thread(target=run,args=(timeLeft,q))
threadTimer = threading.Thread(target=timer,args=(timeLeft,q))


#babeeeeeeee

def babe():
	img = Image.open('babe.jpg')

	img.show()


#function for endgame when you get 5 right
	
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

#function for correct answers

def correct():

	global score
	score += 1
	if score == 5:
		endgame()
	run(timeLeft, q)

#runs the threads
def go():

	threadRun.start()
	threadTimer.start()

#begining of code --- instructions
def main():

	print ''
	print ''
	print ''
	raw_input('Welcome to my math game! Press enter to continue...')
	print ''
	raw_input('You will have to answer 5 randomly generated math questions in order to recieve a prize at the end! Press enter to continue...')
	print ''
	raw_input('You will have 120 seconds per question and will need a calculator! Press enter to begin...')
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

#function for when you lose
def lost():

	print ''
	print 'Oops! You lost! Try Again (just hit up arrow and then enter)... Loser'
	print ''
	os._exit(0)

main()

