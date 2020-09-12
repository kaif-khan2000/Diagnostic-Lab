from django.contrib import admin
from django.urls import path,include
from . import views

admin.site.site_title = "ShriyaDiagnostics Administration"
admin.site.site_header = "ShriyaDiagnostics Administration"
urlpatterns = [
    path("",views.index,name="index"),
    path("home",views.home,name="home"),
    path("applications/<slug>",views.application,name="application"),
    path("search",views.search,name="search"),
    path("test_ajax",views.testAjax,name="testAjax"),
    path("addTest",views.addTest,name="addTest"),
    path("submitApplication",views.submitApplication,name="submitApplication"),
    path("submitRecord",views.submitRecord,name="submitRecord"),
    path("check/<slug>",views.check,name="check"),
    path('registerValues',views.registerValues,name="registerValues"),
    path('submitCheck/<slug>',views.submitCheck,name="submitCheck"),
    path('viewPage/<slug>',views.viewPage,name="viewPage"),
    path('billing/<slug>',views.billing,name="billing"),
    path('profileSearch',views.profileSearch,name="profileSearch"),
    path('profileadmin',views.profileadmin,name='profileadmin'),
    path('addProfile',views.addProfile,name='addProfile'),
    path('deleteProfile',views.deleteProfile,name='deleteProfile'),
    path('getTests',views.getTests,name='getTests'),
    path('addTest2',views.addTest2,name='addTest2'),
    path('deleteTest',views.deleteTest,name='deleteTest'),
]
