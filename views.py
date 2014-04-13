from django.shortcuts import render
import operator
from random import shuffle

from quiz.models import Question, Aspect, Word
# Create your views here.

def main_page(request):
    question = ordered_question()
    words = random_words()
    context = {
	'question' : question,
	'words' : words
    }
    return render(request, 'quiz.html', context)

#these should really be another module, but eh

#returns a list of question objects in order of "order"
def ordered_question():
    question = []
    for q in Question.objects.all():
	question.append(q)
    question.sort(key = operator.attrgetter('order'))
    return question

#returns a list of lists of words in random order
def random_words():
    rando = []
    for aspect  in Aspect.objects.all():
	temp = []
	for word in Word.objects.all():
	    if word.aspect.aspect == aspect.aspect:
		temp.append(word)
		shuffle(temp)
	rando.append(temp)
    return rando
