from mysite.survey import models as m
from mysite.survey.forms import adsForm
import datetime
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate ,  login
from mysite.survey.models import sem_6_ads , sem_6_cc , sem_4 , MonthlyWeatherByCity
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout






def log(request):
    username1 = request.POST.get("username", False)
    password1 = request.POST.get("password", False)
    user = authenticate(username=username1, password=password1)
    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['name1'] = username1
            l=0
            count=0
            sem_6_list_ads = sem_6_ads.objects.filter(usn = username1)
            sem_6_list_cc = sem_6_cc.objects.filter(usn = username1)
            sem_4_list = sem_4.objects.filter(usn = username1)
            if(len(sem_6_list_ads)):
                count=1
            elif(len(sem_6_list_cc)):
                count=0
            elif(len(sem_4_list)):
                count=99
            else:
                count=100
            if( count == 1 ):
                for sub in sem_6_list_ads :
                    if sub.done == 0:
                        l=1
                if l == 1 :
                    return render(request,'subject.html',{'subjects':sem_6_list_ads,'name':request.session['name1']})
                else:
                    return redirect("https://ise.pythonanywhere.com/complete")
            elif( count == 0):
                for sub in sem_6_list_cc :
                    if sub.done == 0:
                        l=1
                if l == 1 :
                    return render(request,'subject.html',{'subjects':sem_6_list_cc,'name':request.session['name1']})
                else:
                    return redirect("https://ise.pythonanywhere.com/complete")
            elif( count == 99):
                for sub in sem_4_list :
                    if sub.done == 0:
                        l=1
                if l == 1 :
                    return render(request,'subject.html',{'subjects':sem_4_list,'name':request.session['name1']})
                else:
                    return redirect("https://ise.pythonanywhere.com/complete")
            else:
                return redirect('http://ise.pythonanywhere.com/')
    else:
        return redirect('http://ise.pythonanywhere.com/')

def end(request):
    return render(request,'end1.html',{'name':request.session['name1']})

def out(request):
    logout(request)
    return redirect("https://ise.pythonanywhere.com/")

def form_store(request):
    username = request.session['name1']
    subject_id = request.POST['subname']
    sem_6_list_ads = sem_6_ads.objects.filter(usn = username)
    sem_6_list_cc = sem_6_cc.objects.filter(usn = username)
    sem_4_list = sem_4.objects.filter(usn = username)
    if( len(sem_6_list_ads)):
        count=1

    elif(len(sem_6_list_cc)):
        count=0
    elif(len(sem_4_list)):
        count=99
    if(subject_id == "ads"):
        f = m.ads(usn=request.POST['stuname'],timestamp=datetime.datetime.today(),q1=request.POST['score1'],q2=request.POST['score2'],q3=request.POST['score3'],q4=request.POST['score4'],q5=request.POST['score5'])
        f.save()
        c = m.sem_6_ads.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
        c.done="1"
        c.save()

    elif(subject_id == "cn"):
        f = m.cn(usn=request.POST['stuname'],timestamp=datetime.datetime.today(),q1=request.POST['score1'],q2=request.POST['score2'],q3=request.POST['score3'],q4=request.POST['score4'],q5=request.POST['score5'],q6=request.POST['score6'],q7=request.POST['score7'],q8=request.POST['score8'])
        f.save()
        if( count == 1 ):
            c = m.sem_6_ads.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        elif( count == 0):
            c = m.sem_6_cc.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        else:
            c = m.sem_4.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
    elif(subject_id == "cc"):
        f = m.cc(usn=request.POST['stuname'],timestamp=datetime.datetime.today(),q1=request.POST['score1'],q2=request.POST['score2'],q3=request.POST['score3'],q4=request.POST['score4'],q5=request.POST['score5'],q6=request.POST['score6'],q7=request.POST['score7'],q8=request.POST['score8'])
        f.save()
        if( count == 1 ):
            c = m.sem_6_ads.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        elif( count == 0):
            c = m.sem_6_cc.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        else:
            c = m.sem_4.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
    elif(subject_id == "wp"):
        f = m.wp(usn=request.POST['stuname'],timestamp=datetime.datetime.today(),q1=request.POST['score1'],q2=request.POST['score2'],q3=request.POST['score3'],q4=request.POST['score4'],q5=request.POST['score5'],q6=request.POST['score6'],q7=request.POST['score7'],q8=request.POST['score8'])
        f.save()
        if( count == 1 ):
            c = m.sem_6_ads.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        elif( count == 0):
            c = m.sem_6_cc.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        else:
            c = m.sem_4.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
    elif(subject_id == "psq"):
        f = m.psq(usn=request.POST['stuname'],timestamp=datetime.datetime.today(),q1=request.POST['score1'],q2=request.POST['score2'],q3=request.POST['score3'],q4=request.POST['score4'],q5=request.POST['score5'],q6=request.POST['score6'],q7=request.POST['score7'],q8=request.POST['score8'])
        f.save()
        if( count == 1 ):
            c = m.sem_6_ads.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        elif( count == 0):
            c = m.sem_6_cc.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        else:
            c = m.sem_4.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
    elif(subject_id == "oomd"):
        f = m.oomd(usn=request.POST['stuname'],timestamp=datetime.datetime.today(),q1=request.POST['score1'],q2=request.POST['score2'],q3=request.POST['score3'],q4=request.POST['score4'],q5=request.POST['score5'],q6=request.POST['score6'],q7=request.POST['score7'],q8=request.POST['score8'])
        f.save()
        if( count == 1 ):
            c = m.sem_6_ads.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        elif( count == 0):
            c = m.sem_6_cc.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        else:
            c = m.sem_4.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
    elif(subject_id == "se"):
        f = m.se(usn=request.POST['stuname'],timestamp=datetime.datetime.today(),q1=request.POST['score1'],q2=request.POST['score2'],q3=request.POST['score3'],q4=request.POST['score4'],q5=request.POST['score5'],q6=request.POST['score6'],q7=request.POST['score7'],q8=request.POST['score8'])
        f.save()
        if( count == 1 ):
            c = m.sem_6_ads.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        elif( count == 0):
            c = m.sem_6_cc.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        else:
            c = m.sem_4.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
    elif(subject_id == "tfc"):
        f = m.tfc(usn=request.POST['stuname'],timestamp=datetime.datetime.today(),q1=request.POST['score1'],q2=request.POST['score2'],q3=request.POST['score3'],q4=request.POST['score4'],q5=request.POST['score5'],q6=request.POST['score6'],q7=request.POST['score7'],q8=request.POST['score8'])
        f.save()
        if( count == 1 ):
            c = m.sem_6_ads.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        elif( count == 0):
            c = m.sem_6_cc.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        else:
            c = m.sem_4.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
    elif(subject_id == "ada"):
        f = m.ada(usn=request.POST['stuname'],timestamp=datetime.datetime.today(),q1=request.POST['score1'],q2=request.POST['score2'],q3=request.POST['score3'],q4=request.POST['score4'],q5=request.POST['score5'],q6=request.POST['score6'],q7=request.POST['score7'])
        f.save()
        if( count == 1 ):
            c = m.sem_6_ads.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        elif( count == 0):
            c = m.sem_6_cc.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        else:
            c = m.sem_4.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
    elif(subject_id == "oop"):
        f = m.oop(usn=request.POST['stuname'],timestamp=datetime.datetime.today(),q1=request.POST['score1'],q2=request.POST['score2'],q3=request.POST['score3'],q4=request.POST['score4'],q5=request.POST['score5'],q6=request.POST['score6'],q7=request.POST['score7'],q8=request.POST['score8'])
        f.save()
        if( count == 1 ):
            c = m.sem_6_ads.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        elif( count == 0):
            c = m.sem_6_cc.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        else:
            c = m.sem_4.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
    else:
        f = m.unix(usn=request.POST['stuname'],timestamp=datetime.datetime.today(),q1=request.POST['score1'],q2=request.POST['score2'],q3=request.POST['score3'],q4=request.POST['score4'],q5=request.POST['score5'],q6=request.POST['score6'],q7=request.POST['score7'],q8=request.POST['score8'],q9=request.POST['score9'])
        f.save()
        if( count == 1 ):
            c = m.sem_6_ads.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        elif( count == 0):
            c = m.sem_6_cc.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
        else:
            c = m.sem_4.objects.get(subject_code=request.POST['subname'],usn = request.POST['stuname'])
            c.done="1"
            c.save()
    return redirect("https://ise.pythonanywhere.com/sub")




def sub(request):
    username = request.session['name1']
    l=0
    sem_6_list_ads = sem_6_ads.objects.filter(usn = username)
    sem_6_list_cc = sem_6_cc.objects.filter(usn = username)
    sem_4_list = sem_4.objects.filter(usn = username)
    if( len(sem_6_list_ads)):
        count=1

    elif(len(sem_6_list_cc)):
        count=0
    elif(len(sem_4_list)):
        count=99
    else:
        count=100
    if( count == 1 ):
        for sub in sem_6_list_ads :
            if sub.done == 0:
                l=1
        if l == 1 :
            return render(request,'subject.html',{'subjects':sem_6_list_ads,'name':request.session['name1']})
        else:
            return redirect("https://ise.pythonanywhere.com/complete")
    elif( count == 0):
        for sub in sem_6_list_cc :
            if sub.done == 0:
                l=1
        if l == 1 :
            return render(request,'subject.html',{'subjects':sem_6_list_cc,'name':request.session['name1']})
        else:
            return redirect("https://ise.pythonanywhere.com/complete")
    elif( count == 99):
        for sub in sem_4_list :
            if sub.done == 0:
                l=1
        if l == 1 :
            return render(request,'subject.html',{'subjects':sem_4_list,'name':request.session['name1']})
        else:
            return redirect("https://ise.pythonanywhere.com/complete")
    else:
        return redirect('http://ise.pythonanywhere.com/')

def store(request,product):
    if( product == 'ads'):
        return render(request,'ads.html',{'name':request.session['name1']})
    elif(product == 'wp'):
        return render(request,'wp.html',{'name':request.session['name1']})
    elif(product == 'cc'):
        return render(request,'cc.html',{'name':request.session['name1']})
    elif(product == "cn"):
        return render(request,'post_form_upload.html',{'name':request.session['name1']})
    elif(product == 'psq'):
        return render(request,'psq.html',{'name':request.session['name1']})
    elif(product == 'oomd'):
        return render(request,'oomd.html',{'name':request.session['name1']})
    elif(product == 'se'):
        return render(request,'se.html',{'name':request.session['name1']})
    elif(product == 'tfc'):
        return render(request,'tfc.html',{'name':request.session['name1']})
    elif(product == 'ada'):
        return render(request,'ada.html',{'name':request.session['name1']})
    elif(product == 'unix'):
        return render(request,'unix.html',{'name':request.session['name1']})
    else:
        return render(request,'oop.html',{'name':request.session['name1']})





def base(request):
    return render(request,'base.html')
