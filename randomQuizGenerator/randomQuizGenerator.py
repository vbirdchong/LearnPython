#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 


import random

QUIZ_NUM = 5
STATES_NUM = 5
QUIZ_FILE_NUM = 5
QUESTION_NUM = 5

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


def generate_file():
	for quizAndAnswerFileNum in xrange(0, QUIZ_FILE_NUM):
		quizFile = generate_quiz_file(quizAndAnswerFileNum)
		answerKeyFile = generate_answerkey_file(quizAndAnswerFileNum)
		statesForQuestions, correctAnswers, optionAnswers = generate_quiz_and_answer()
		save_quiz_and_answers_to_files(statesForQuestions, correctAnswers, optionAnswers, quizFile, answerKeyFile)
		close_quiz_and_answers_files(quizFile, answerKeyFile)

def generate_quiz_file(quizAndAnswerFileNum):
	quizFile = open('capitalsquiz%s.txt' % (quizAndAnswerFileNum + 1), 'w')
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizAndAnswerFileNum + 1))
	quizFile.write('\n\n')
	return quizFile

def generate_answerkey_file(quizAndAnswerFileNum):
	answerkeyFile = open('capitalsquiz_answers%s.txt' % (quizAndAnswerFileNum), 'w')
	return answerkeyFile

def generate_quiz_and_answer():
	states = list(capitals.keys())
	random.shuffle(states)
	allQuestionStates = states
	allCorrectAnswers = []
	allAnswerOptions = []

	for questionNum in xrange(0,QUESTION_NUM):
		correctAnswer = capitals[states[questionNum]]
		allAnswers = list(capitals.values())

		# we remove the correct answer then we can get 3 wrong answers and add them to answer options.
		allAnswers.remove(correctAnswer)
		wrongAnswers = random.sample(allAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]

		# print('%s-%s' % (states[questionNum], correctAnswer))
		# print(answerOptions)

		random.shuffle(answerOptions)
		allCorrectAnswers.append(correctAnswer)
		allAnswerOptions.append(answerOptions)

	return allQuestionStates, allCorrectAnswers, allAnswerOptions


def save_quiz_and_answers_to_files(statesForQuestions, correctAnswers, optionAnswers, quizFile, answerKeyFile):
	print('-' * 20)
	for questionNum in xrange(0, QUESTION_NUM):
		quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, statesForQuestions[questionNum]))
		for x in xrange(0,4):
			quizFile.write(' %s. %s\n' % ('ABCD'[x], optionAnswers[questionNum][x]))

		# print('%s---%s' % (statesForQuestions[questionNum], optionAnswers[questionNum]))
		# print(correctAnswers[questionNum])
		answerKeyFile.write(' %s. %s\n' % (questionNum + 1, 'ABCD'[optionAnswers[questionNum].index(correctAnswers[questionNum])]))

def close_quiz_and_answers_files(quizFile, answerKeyFile):
	quizFile.close()
	answerKeyFile.close()

def generate_quiz_files():
	for quizNum in range(QUIZ_NUM):
		quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
		answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

		quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
		quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
		quizFile.write('\n\n')

		states = list(capitals.keys())
		random.shuffle(states)
		generate_question(states, quizFile, answerKeyFile)
		quizFile.close()
		answerKeyFile.close()

def generate_question(states, quizFile, answerKeyFile):
	for questionNum in range(STATES_NUM):
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
		save_to_quiz_file(quizFile, answerKeyFile, questionNum, states, answerOptions, correctAnswer)

def save_to_quiz_file(quizFile, answerKeyFile, questionNum, states, answerOptions, correctAnswer):
	quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
	for i in range(4):
		quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
	quizFile.write('\n')
	
	answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))


def main():
	# generate_quiz_files()
	generate_file()

if __name__ == '__main__':
	main()