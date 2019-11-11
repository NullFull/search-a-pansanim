from django.contrib import admin
from django.urls import path
from anijung import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('judge/<int:judge_id>', views.judge, name='judge'),
    path('case/<int:case_id>', views.case, name='case'),
    # path('decision/<int:decision_id>', views.decision, name='decision'),
]
