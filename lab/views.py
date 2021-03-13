from django.shortcuts import render,HttpResponse,redirect
from .models import Test,Value,Application,Record,Device,Profile
from django.core import serializers
import datetime
# Create your views here.
def index(request):
    return home(request)

def home(request):
    value = Value.objects.all()[0]
    profiles = Profile.objects.all()
    return render(request,'lab/home.html',{'lab_no':value.lab_no,'profiles':profiles})


def application(request,slug):
    params = {
        'new':"",
        'checked':"",
    }
    if slug == "checked":
        params['checked'] = 'active'
        applications = Application.objects.filter(checked = True).order_by('-recieved_on')[:20]
        params['applications'] = applications
    else:
        params['new'] = 'active'
        applications = Application.objects.filter(checked = False)
        params['applications'] = applications
    return render(request,'lab/application.html',params)

def search(request):
    if request.method == "GET":
        query = request.GET.get("search")
        applications = Application.objects.filter(name__icontains = query)
        applications = applications.union(Application.objects.filter(age__contains = query))
        applications = applications.union(Application.objects.filter(lab_no__contains = query))
        return render(request,'lab/search.html',{'applications':applications})
    return HttpResponse("404- Not Found")

def testAjax(request):
    if request.method == 'GET':
        query = request.GET.get("search")
        if request.is_ajax:
            tests = Test.objects.filter(test__icontains = query)[:10]
            data = serializers.serialize('json',tests)
            return HttpResponse(data,content_type='application/json')

def addTest(request):
    if request.method == 'GET':
        query = request.GET.get("test")
        print(query)
        if request.is_ajax:
            test = []
            test.append(Test.objects.get(test = query))
            data = serializers.serialize('json',test)
            return HttpResponse(data,content_type='application/json')

def submitApplication(request):

    if request.method == 'GET':
        name = request.GET.get("name")
        age = request.GET.get("age")
        sex = request.GET.get("sex")
        cost= request.GET.get("cost")
        ref_by = request.GET.get('ref_by')
        date = datetime.date.today()
        if request.is_ajax:
            value = Value.objects.all()[0]
            application = Application.objects.create(
                name = name,
                age = int(age),
                sex = sex,
                recieved_on = date,
                cost = cost,
                lab_no = value.lab_no,
                ref_by = ref_by
            )

            value.lab_no+=1
            value.save()

            return HttpResponse()

def submitRecord(request):
    if request.method == 'GET':
        lab_no = request.GET.get("lab_no")
        test = request.GET.get("test")
        rangeValue = Test.objects.get(test = test).range1
        if request.is_ajax:
            application = Application.objects.get(lab_no = lab_no)
            price = Test.objects.get(test=test).price
            record = Record.objects.create(
                lab_no = lab_no,
                application = application,
                test = test,
                price = price,
                ref = rangeValue
            )

            return HttpResponse()

def check(request,slug):
    slug = int(slug)
    try:
        application = Application.objects.get(lab_no = slug)
        records = Record.objects.filter(lab_no = slug)
        devices = Device.objects.all()
        
        params = {
            'application':application,
            'records':records,
            'length':len(records),
            'devices':devices,
        }
        return render(request,'lab/check.html',params)
    except:
        return HttpResponse("404 - Page Not Found")

def registerValues(request):
    if request.method == 'GET':
        lab_no = request.GET.get('lab_no')
        test = request.GET.get('test')
        finding = request.GET.get('finding')
        ref = request.GET.get('ref')
        note = request.GET.get('note')
        device = request.GET.get('device')

        if request.is_ajax:
            record = Record.objects.get(lab_no=lab_no,test=test)
            record.finding = finding
            record.ref = ref
            record.note = note
            record.device = device
            record.save()
            return HttpResponse()

def submitCheck(request,slug):
    application1 = Application.objects.get(lab_no = slug)
    application1.checked = True
    application1.save()
    return application(request,"checked")

def viewPage(request,slug):
    application = Application.objects.get(lab_no = slug)
    records = Record.objects.filter(lab_no = slug)
    params = {
        'application':application,
        'records':records,
    }
    return render(request,'lab/viewPage.html',params)

def billing(request,slug):
    application = Application.objects.get(lab_no = slug)
    records = Record.objects.filter(lab_no = slug)
    total = 0
    for record in records:
        total += record.price
    params = {
        'application':application,
        'records':records,
        'total':total,
    }
    return render(request,'lab/billing.html',params)


def profileSearch(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if request.is_ajax:
            profile = Profile.objects.get(name=query)
            tests = Test.objects.filter(profile = profile)
            data = serializers.serialize('json',tests)
            return HttpResponse(data,content_type='application/json')

def profileadmin(request):
    profile = Profile.objects.all()
    return render(request,'lab/profileadmin.html',{'profiles':profile})


#from now starts code for profile page

def addProfile(request):
    if request.method == 'GET':
        profile = request.GET.get("profile")
        try:
            Profile.objects.create(name=profile)
        except:
            pass
        return redirect('/profileadmin')

def deleteProfile(request):
    if request.method == 'GET' and request.is_ajax:
        slug = request.GET.get('name')
        Profile.objects.get(name=slug).delete()
    return HttpResponse()

def getTests(request):
    if request.method=="GET" and request.is_ajax:
        profile_name = request.GET.get('name')
        profile = Profile.objects.get(name=profile_name)
        tests = Test.objects.filter(profile=profile)
        data = serializers.serialize('json',tests)
        return HttpResponse(data,content_type='application/json')

def addTest2(request):
    if request.method=="GET":
        test = request.GET.get('test')
        profile_name = request.GET.get('profile')
        price = int(request.GET.get('price'))
        range1 = request.GET.get('range')
        profile = Profile.objects.get(name=profile_name)
        Test.objects.create(test = test,price=price,profile=profile,range1=range1)
        return redirect('/profileadmin')

def deleteTest(request):
    if request.method=="GET" and request.is_ajax:
        name = request.GET.get('name')
        Test.objects.get(test=name).delete()
        return HttpResponse()