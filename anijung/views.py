from django.shortcuts import render

from anijung.models import Judge, Case, Quote


def index(request):
    judges = Judge.objects.exclude(name='?')
    cases = Case.objects.all()
    quotes = Quote.objects.all()

    return render(request, 'index.html', dict(
        judges=judges,
        cases=cases,
        quotes=quotes,
    ))


def judge(request, judge_id):
    j = Judge.objects.get(id=judge_id)

    return render(request, 'judge.html', dict(
        judge=j,
    ))


def case(request, case_id):
    c = Case.objects.get(id=case_id)

    return render(request, 'case.html', dict(
        case=c,
    ))
