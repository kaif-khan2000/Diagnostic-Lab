from django.shortcuts import render,HttpResponse
from .models import Test,Value,Application,Record
from django.core import serializers
import datetime
# Create your views here.
def index(request):
    return home(request)

def home(request):
    value = Value.objects.all()[0]
    return render(request,'lab/home.html',{'lab_no':value.lab_no})


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

def record(request):
    return render(request,'lab/record.html')

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
            )

            value.lab_no+=1
            value.save()

            return HttpResponse()

def submitRecord(request):
    if request.method == 'GET':
        lab_no = request.GET.get("lab_no")
        test = request.GET.get("test")

        if request.is_ajax:
            application = Application.objects.get(lab_no = lab_no)
            record = Record.objects.create(
                lab_no = lab_no,
                application = application,
                test = test,
            )

            return HttpResponse()

def check(request,slug):
    slug = int(slug)
    try:
        application = Application.objects.get(lab_no = slug)
        records = Record.objects.filter(lab_no = slug)
        params = {
            'application':application,
            'records':records,
            'length':len(records),
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

        if request.is_ajax:
            record = Record.objects.get(lab_no=lab_no,test=test)
            record.finding = finding
            record.ref = ref
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