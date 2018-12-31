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

class Sop(ListView):
    uname_short_to_official = {
        'ucr': 'UCR',
        'ucsc': 'UCSC',
        'ucd': 'UCD',
        'uci': 'UCI',
        'ucsd': 'UCSD',
        'usc_ds': 'USC',
        'usc_se': 'USC',
        'pennstate': 'Penn State University',
        'ucolorado': 'University of Colorado',
        'uu': 'University of Utah',
        'umass': 'UMass Amherst',
    }
    def get(self, request, *args, **kwargs):
        urldata = ("meryota", "sop", "%s.html")
        self.template_name = '/'.join(urldata)
        self.context = {
            'self':self, 'request':request, 'args':args, 'kwargs':kwargs,
            'uname':kwargs['uname'],
            'uname_official': self.uname_short_to_official.get(kwargs['uname']),
        }
        return render(request, self.template_name % (kwargs['uname']), self.context)

class Ps(ListView):
    template_name = 'meryota/ps.html'
    info = {
        'myinfo': {
            'Name': 'Ryota Bannai', 
            'Chatchphraes': 'A high achiever with an AI reseach and tech-industry experiences, seeking Computer Science education in MS course',
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
                'medium':'https://towardsdatascience.com/unpacking-pca-b5ea8bec6aa5'
            },
        },
        'state':{
            'history_1': "I had experienced 311 earthquake in 2011, which struck Fukushima where I had lived for 18 years. Though my place was not near to the coast of the city of Iwaki, where suffered the most, there were a lot of concerns for residents, especially for students. They had to study in the gymnasium with partitions, in the laboratories, or any place available to utilize until temporary facilities were built. By the destructive mainshock, the campus was obliterated. Fukushima and the areas nearby Fukushima were running out of resource such as a gas, foods, beverages for a half year. I got used to the routine that my family woke up at 4 am or so and waited in line to ensure that we could get those resources before they got out of stock. I, as a student, had to kept myself under control and focused on what I needed to do for my later life especially because I faced the annual national exam for university just after 10 months. It turned out well academically, and fortunately now I get a chance to study further in United States. I believe that I can acquire top-notch skills and knowledge at a selective university, and that will give me the capacity to meaningfully help my community. I hope that my contribution will become one of the variables of resistant community toward natural disasters that I had experienced at high school.",
            'history_2': "In 2012, I got accepted by Shibaura Institute of Technology, Engineering and Design. At the university I learnt the areas of architecture, product design, manufacturing, and computer science in the first two years, and then I chose CS for my major. In junior year, in the hope of seeing how graduates with CS degree interact with the society daily, I decided to have a job at tech-company.  Thankfully, in spite of the fact that they had never hired a part-time employee before, GREE, inc., which awarded the epithet \"one of three biggest startup since 2000\", offered me a customer service job. I chiefly dealt with different kinds of customers' troubles in the usage of GREE online games. With this data I helped developers to make better strategies and policies as well. Although I did not belong to technical teams to develop games, I met various people who are highly skilled in his/her profession, are globally experienced, or are foreigners. After all, I thought I needed to explore technical skills to see how CS students make an effort for company, more broadly for my community. I gained a next job at another tech-company as a system engineer, and I skilled in web development. I took several responsibilities in the company, but more importantly I worked with a lot of foreign programmers from French, Spain, Mexico, China, which was unconventionally diverse in Japan. These two environments reshaped my stereotypical ideas on how different each cultures are, but at the same time how similar we perceive and feel, and reminded me of the value of English.",
            'sumup':"I strongly believe that I can obtain unique perspectives by thriving outside Japan. The global experience would allow me to make valuable contributions to society with the personal capacity to facilitate communications between different nations and different people. That would help them to strength their relationship, enriching holistic development.",
        }
    }
    context = {'info': info}
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

class Cv(ListView):
    template_name = 'meryota/cv.html'
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super().dispatch(*args, **kwargs)
    myinfo = {
        'Name': 'Ryota Bannai', 
        'Chatchphraes': 'High achiever with an AI reseach and tech-industry experiences, seeking further understanding in Computer Science MS course',
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
            'medium':'https://towardsdatascience.com/unpacking-pca-b5ea8bec6aa5'
        },
        }
    personalsummary = ''
    objective = 'I\'m seeking an education in the hope of specializing in Computer Vision and AI. After finishing my graduate course, I\'m looking to work at 3D Mapping service, especially for autonomous vehicles, and eventually would like to be a system developer in the space industry.'
    skills_cplanguage = ['C','Python(and Django)','Javascript','Node.js','PHP(and FuelPHP)']
    skills_research = ['Coding knowledge of NLP and GA','Caffe','Scikit-learn','Data Cleansing(Scipy, Pandas, Regex)','Matplotlib/Seaborn','Web Scraping','SQL']
    skills_other =['Git', 'Typing: average 90/wpm, max 132/wpm (as of Dec 2018) according to Typeracer']
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
            'Salary calculation system development and maintenance with PHP and FuelPHP',
            'A self-testing system for products with Selenium WebDriver - Test-Driven Development',
            'Meeting room reservation system for this company, including Google calendar like functions, such as draggable, plan repeating on certain days, etc.',
            'Shared the Node.js step by step tutorial for System Engineer department'
        ], 
        'date_from':'May 2015-',
        'date_to': 'May 2016'
        },
        {'corp':'GREE inc.',
        'address': 'Roppongi Hills Mori Tower, 6-10-1 Roppongi, Minato, Tokyo, Japan',
        'position':'Customer Service at GREE SNS Platform', 
        'details':[
            'Market Research on other competitors\' games in terms of target segments, usage policy, etc., to make better strategies for later service launch.',
            'Monitoring anormal activities, such as a huge payment within a short period and an abusive activities, such as violations to the game usage.'], 
        'date_from':'Feb 2015-',
        'date_to': 'May 2015'
        }, 
        
        ]
    intern = [
        {'corp':'Columbia West College, Los Angeles',
        'address': '3435 Wilshire Blvd #1700, Los Angeles, CA 90010',
        'position':'Programmer', 
        'details':[
            'Web development for the college\'s promotion page in four different languages, being used for six counties'], 
        'date_from':'Jun 2018-',
        'date_to': 'Present'
        }
        ]    
    research = [
        {'name':'An Artificial Chef',
        'subtitle': 'Automatic creation of cuisine recipes with Neural Network and GA(genetic algorithm)',
        'details':[
            'Under Supervised Learning with the online recipe site, Cockpad, a recipe evaluation component rates recipes, which the system generates, with the range 0- 5.',
            'Recipe creation component creates new recipes with GA, based on existing recipes on Cockpad.' ,
            'By mutation, the component switches an ingredient with another similar one by rule which I prepared beforehand, and by crossover, it can breed new recipes.'], 
        'date':'2016'
        }
        ]
    education = [
        {'name': 'Columbia West College, Los Angeles', 
        'specification':'ESL', 
        'details':[
            'The best student of the month/ 300 students in Nobember 2017',
            '163% improvement of TOEFL score since the first test '],
        'date_from':'Jul 2016-','date_to': 'Present'},
        {'name': 'Shibaura Institute of Techonology, Japan',
        'specification':'Engineering and Design, Robotics and Information Design Course, Bachelor degree', 
        'details':['Study information design, software design, and mechatronics design, and learn about mechatronics, motion control, and similar fields.',],
        'date_from':'Apl 2012-','date_to': 'May 2016',
        },
        ]
    context = {'myinfo':myinfo,'objective':objective, 'skills': skills, 'education': education, 'work': work,'intern':intern, 'research':research}
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    