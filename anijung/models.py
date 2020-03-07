from django.db import models as m


class Company(m.Model):
    name = m.CharField(max_length=30)


class Judge(m.Model):
    name = m.CharField(max_length=20)
    company = m.ForeignKey(Company, null=True, on_delete=m.CASCADE)
    position = m.CharField(max_length=40)  # TODO : 이 아이도 별도 모델로


class Case(m.Model):
    title = m.CharField(max_length=200)
    desc = m.TextField(null=True, blank=True)


class Decision(m.Model):
    no = m.CharField(max_length=20)
    case = m.ForeignKey(Case, on_delete=m.CASCADE, null=True, related_name='decisions')
    court = m.CharField(max_length=30)  # TODO : 이 아이도 별도 모델로
    place = m.CharField(max_length=20)  # TODO : 위 아이랑 묶어서 별도 모델로
    round = m.CharField(max_length=20)
    result = m.TextField()
    source = m.URLField(null=True)
    judge = m.ForeignKey(Judge, related_name='decisions', on_delete=m.CASCADE, null=True)  # TODO : 여러 판사 지원
    # judges = m.ManyToManyField(Judge, related_name='decisions')


class Quote(m.Model):
    # case = m.ForeignKey(Case, on_delete=m.CASCADE, null=True, blank=True)
    decision = m.ForeignKey(Decision, on_delete=m.CASCADE, null=True, blank=True)
    quote = m.CharField(max_length=300)
    source = m.URLField(null=True, blank=True)
