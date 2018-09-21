from django.urls import path
from meryota.views import Index, Cv
from . import views

app_name = 'meryota'
urlpatterns = [
    #path('', Index.as_view()),
    path('', Cv.as_view()),
    path('cv/', Cv.as_view()), 
     # ex: /meryote/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /meryote/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /meryote/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #path('.well-known/acme-challenge/acme-challenge/<slug:slug>', views.acm, name='acm'),
]