from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

def acm(request):
    return HttpResponse("YI7ivk3q0YIK7E1GSpWjaC2kwvDJ4lGeKi8k9AGvHrs.97bDFrJbO2m1sKFAlAXa9D5w5gDpo_iGGgeOZORtKKo")

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    myinfo = {
        'name': 'Ryota Bannai', 
        'email': 'cy12161@shibauta-it.ac', 
        'phone':'+13236139942',
        'GPA': '3.38',
        }
    objection = ''
    skills_cplanguage = ['C','Python(Fluent)','Javascript(Fluent)','Node.js','PHP(Fluent)']
    skills_research = ['Coding NLP, GA','Numpy','matplotlib','coffe','Data Cleansing','Mysql']
    skills_other =['Git', 'Typing- ave. 85/wpm, max. 118/wpm (as of Sep, 2018) according to Typeracer']
    skills = {
        'skills_cplanguage':skills_cplanguage, 
        'skills_research':skills_research, 
        'skills_other':skills_other
        }
    work = [
        {'corp':'GREE inc., Tokyo',
        'position':'Customer Service- for GREE provided Games', 
        'details':[
            'Market Researching on other competitors\' games, such as target segments, and contributed to make strategies.',
            'Monitoring an abuse and a violation to the game usage from users and other abnormal activities, such as a record of huge payment.'], 
        'date_from':'Feb 2015-',
        'date_to': 'May 2015'
        }, 
        {'corp':'Plate inc., Tokyo', 
        'position':'System Engineer', 
        'details':[
            'Project: Employees\' Salary Caliculation System Development and Maintainance with PHP and FuelPHP',
            'Project: A self-testing system for Products by using Selenium WebDriver - Test-Driven Development',
            'Project: Meeting Room Booking System for employees with Google Calender like functions, such as draggable, plan repeat. etc.',
            'Senimor: Gave a Node.js step by step turorial seminor for System Engineer department'
        ], 
        'date_from':'May 2015-',
        'date_to': 'May 2016'
        }
        ]
    intern = [
        {'corp':'Columbia West College, Los Angeles',
        'position':'Programmer', 
        'details':[
            'Development of Advertizing Landing Webpages in four different languages and being used in multiple counties'], 
        'date_from':'Jun 2018-',
        'date_to': 'Present'
        }
        ]    
    research = [
        {'name':'An Artificial Chef',
        'subtitle': 'Automatic creation of cuisine recipes with Neural Network and genetic algorithm',
        'details':[
            '',
            ], 
        'date':'2016'
        }
        ]
    education = [
        {'name': 'Shibaura Institute of Techonology, Japan',
        'specification':'Engineering and Design, Robotics and Information Course', 
        'details':['Study information design, software design, and mechatronics design, and learn about mechatronics, motion control, and similar fields.',],
        'date_from':'Apl 2012-','date_to': 'May 2016',
        },
        {'name': 'Columbia West College, Los Angeles', 
        'specification':'ESL', 
        'details':[
            'The best student of month out of 300 students in Nob. 2017',
            '163% improvement of TOEFL score since the first test '],
        'date_from':'Jul 2016-','date_to': 'Present'}]

    context = {'myinfo':myinfo,'objection':objection, 'skills': skills, 'education': education, 'work': work,'intern':intern, 'research':research}
    return render(request, 'meryota/index.html', context)