from django.urls import path,include
from . import views

app_name="kickboxing_app"

urlpatterns=[
    path("",views.index,name='index'),
    path("plan/",views.IndexPlanView.as_view(),name="plan_index"),
    path("plan/<int:pk>/",views.DetailPlanView.as_view(),name="plan_detail"),
    path('plan/create/',views.CreatePlanView.as_view(),name="plan_create"),
    path("plan/<int:pk>/update/",views.UpdatePlanView.as_view(),name="plan_update"),
    path("plans/<int:pk>/done-confirm/", views.DoneConfirmView.as_view(), name="plan_done_confirm"),
    path("plan/<int:pk>/delete/",views.DeletePlanConfirmView.as_view(),name="plan_delete"),
    


]