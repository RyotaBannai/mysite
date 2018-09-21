from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.urls import reverse
from django.views.generic import ListView
#from django.views.generic import View what the diff list and view
from django.views import View

class Index(ListView):
    template_name = 'meryota/index.html'
    context_object_name = 'latest_question_list'
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #return latest 5 data
    context = {'latest_question_list': latest_question_list, }

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    #output = ', '.join([q.question_text for q in latest_question_list]) #return HttpResponse(output)
    

'''
def acm(request, slug=None):
    context = {'slug':slug}
    return render(request, 'meryota/acm.html', context)
'''

def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'meryota/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'meryota/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'meryota/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('meryota:results', args=(question.id,)))

class Cv(ListView):
    template_name = 'meryota/cv.html'
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super().dispatch(*args, **kwargs)
    myinfo = {
        'Name': 'Ryota Bannai', 
        'Chatchphraes': 'High achiever with an AI reseach and tech-industry experiences, seeking Computer Science education in MS course',
        'Email': 'cy12161@shibaura-it.ac.jp', 
        'Phone':'+13236139942',
        'GPA': '3.38/ 4.00',
        'Website': 'http://www.ryotabannai.us',
        'Motto':[
            '',
            ''],
        'Links':{
            'cwc':'https://www.columbiawestcollege.edu/demo/',
            'git':'https://github.com/RyotaBannai',
        },
        }
    personalsummary = ''
    objective = 'I\'m seeking an education to spericialize in Compuer Vision field. With this skills I\'d like to contribute to an AI industry, specifically Self-Driving system development and space exploration technologies, after gradation.'
    skills_cplanguage = ['C','Python(and Django)','Javascript','Node.js','PHP(and FuelPHP)']
    skills_research = ['Coding NLP and GA','Numpy','Matplotlib','Caffe','Data Cleansing','SQL']
    skills_other =['Git', 'Typing- ave. 85/wpm, max. 118/wpm (as of Sep, 2018) according to Typeracer']
    skills = {
        'skills_cplanguage':skills_cplanguage, 
        'skills_research':skills_research, 
        'skills_other':skills_other
        }
    work = [
        {'corp':'Plate inc.', 
        'address':'Nihonbashi 3-5-15, Chuō, Tokyo, Japan',
        'position':'System Engineer', 
        'details':[
            'Employees\' Salary Caliculation System Development and Maintainance with PHP and FuelPHP',
            'A self-testing system for Products by using Selenium WebDriver - Test-Driven Development',
            'Meeting room reservation system for employees, including Google calender like functions, such as draggable, plan repetition, etc.',
            'Shared the Node.js step by step turorial seminor for System Engineer department'
        ], 
        'date_from':'May 2015-',
        'date_to': 'May 2016'
        },
        {'corp':'GREE inc.',
        'address': 'Roppongi Hills Mori Tower, 6-10-1 Roppongi, Minato, Tokyo, Japan',
        'position':'Customer Service- for GREE provided Games', 
        'details':[
            'Market Research on other competitors\' games concerning target segments, usage policy, etc., to make better strategies for new launch.',
            'Monitoring an abusive, or an abnormal activities, such as huge payment at once and other violations to the game usage.'], 
        'date_from':'Feb 2015-',
        'date_to': 'May 2015'
        }, 
        
        ]
    intern = [
        {'corp':'Columbia West College, Los Angeles',
        'address': '3435 Wilshire Blvd #1700, Los Angeles, CA 90010',
        'position':'Programmer', 
        'details':[
            'Web development for the college advertizement in four different languages and being used in multiple counties'], 
        'date_from':'Jun 2018-',
        'date_to': 'Present'
        }
        ]    
    research = [
        {'name':'An Artificial Chef',
        'subtitle': 'Automatic creation of cuisine recipes with Neural Network and GA(genetic algorithm)',
        'details':[
            'With Supervised Learning by using the online recipe site, Cockpad, a recipe evaluation component rates created recipe with a range 0- 5.',
            'Recipe creation compornent uses existing recipes on Cockpad, and creates new one with GA.' ,
            'In data replacement caused by mutation the component switches an ingridient with another similar one by rule which I prepared beforehand.'], 
        'date':'2016'
        }
        ]
    education = [
        {'name': 'Columbia West College, Los Angeles', 
        'specification':'ESL', 
        'details':[
            'The best student of month out of 300 students in Nob. 2017',
            '163% improvement of TOEFL score since the first test '],
        'date_from':'Jul 2016-','date_to': 'Present'},
        {'name': 'Shibaura Institute of Techonology, Japan',
        'specification':'Engineering and Design, Robotics and Information Course, Bachelor degree', 
        'details':['Study information design, software design, and mechatronics design, and learn about mechatronics, motion control, and similar fields.',],
        'date_from':'Apl 2012-','date_to': 'May 2016',
        },
        ]
    context = {'myinfo':myinfo,'objective':objective, 'skills': skills, 'education': education, 'work': work,'intern':intern, 'research':research}
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    