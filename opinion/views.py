from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from .forms import OpinionForm, AnswerForm
from .models import OpinionBox


@login_required
def index(request):
    opins = OpinionBox.objects.filter(user=request.user)
    return render(request, 'index.html', {
        'opins': opins
    })


@login_required
def add_one(request):
    if request.method == 'POST':
        form = OpinionForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.user = request.user
            opinion.save()
            return redirect(reverse('opinion:index'))
    else:
        form = OpinionForm()
    return render(request, "addopinion.html", {'form': form})


@login_required
def detail(request, id):
    if request.method == 'POST':
        form = AnswerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.opinion_box_id = id
            answer.save()
            return redirect(reverse('opinion:detail', args=[id]))
    else:
        form = AnswerForm()
    try:
        opinion_obj = OpinionBox.objects.get(id=id, user=request.user)
    except OpinionBox.DoesNotExist:
        raise Http404
    answers = opinion_obj.answerbox_set.all()
    return render(request, 'details.html', {'opinion_obj': opinion_obj, 'answers': answers, 'form': form})
