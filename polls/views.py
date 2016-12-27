from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = { 'question': question }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    return HttpResponse("あなたが探しているのは%sの結果ですね。" % question_id)

def vote(request, question_id):
    return HttpResponse("あなたは質問%sに投票しました。" % question_id)
