from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("home",views.home,name="home"),
    path("applications/<slug>",views.application,name="application"),
    path("records",views.record,name="record"),
    path("test_ajax",views.testAjax,name="testAjax"),
    path("addTest",views.addTest,name="addTest"),
    path("submitApplication",views.submitApplication,name="submitApplication"),
    path("submitRecord",views.submitRecord,name="submitRecord"),
    path("check/<slug>",views.check,name="check"),
    path('registerValues',views.registerValues,name="registerValues"),
    path('submitCheck/<slug>',views.submitCheck,name="submitCheck"),
    path('viewPage/<slug>',views.viewPage,name="viewPage"),
]
