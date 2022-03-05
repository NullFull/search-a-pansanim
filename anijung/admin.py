from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Case, Judge, Decision, Quote, Company


class QuoteInline(NestedStackedInline):
    model = Quote
    extra = 0


class DecisionInline(NestedStackedInline):
    model = Decision
    extra = 0
    inlines = [QuoteInline]


class CaseAdmin(NestedModelAdmin):
    inlines = [DecisionInline]


class JudgeAdmin(NestedModelAdmin):
    inlines = [DecisionInline]


admin.site.register(Case, CaseAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Quote)
admin.site.register(Company)
