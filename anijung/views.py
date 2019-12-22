from django.shortcuts import render

from anijung.models import Judge, Case


def index(request):
    judges = Judge.objects.all()[:21]
    cases = Case.objects.all()[:21]

    return render(request, 'index.html', dict(
        judges=judges,
        cases=cases,
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
