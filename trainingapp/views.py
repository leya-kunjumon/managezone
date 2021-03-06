from django. contrib import messages
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render, redirect
from trainingapp.models import *
from datetime import datetime,date
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from io import BytesIO
from django.core.files import File
from django.conf import settings
import qrcode
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate
from django.core.files.storage import FileSystemStorage
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.

def login(request):
    des = designation.objects.get(designation_name='manager')
    des1 = designation.objects.get(designation_name='trainer')
    des2 = designation.objects.get(designation_name='trainee')
    des3 = designation.objects.get(designation_name='accounts')

    if request.method == 'POST':
        
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
                request.session['SAdm_id'] = user.id
                return redirect( 'Admin_Dashboard')
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['m_designation_id'] = member.designation_id
                request.session['m_fullname'] = member.fullname
                request.session['m_id'] = member.id
                return render(request, 'dashsec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des1.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['tr_designation_id'] = member.designation_id
                request.session['tr_fullname'] = member.fullname
                request.session['tr_team_id'] = member.team_id
                request.session['tr_id'] = member.id
                return render(request, 'tr_sec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des2.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['te_designation_id'] = member.designation_id
                request.session['te_fullname'] = member.fullname
                request.session['te_id'] = member.id
                request.session['te_team_id'] = member.team_id
                return render(request, 'traineesec.html', {'member': member})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des3.id).exists():
                member = user_registration.objects.get(
                email=request.POST['email'], password=request.POST['password'])
                request.session['acc_designation_id'] = member.designation_id
                request.session['acc_fullname'] = member.fullname
                request.session['acc_id'] = member.id
                return render(request, 'accountsec.html', {'member': member})
        else:
                context = {'msg': 'Invalid username or password'}
                return render(request, 'login.html', context)
    return render(request,'login.html')       



    
        # if request.method == 'POST':
        #     username = request.POST.get('email', None)
        #     password = request.POST.get('password', None)
        #     user = authenticate(email=username, password=password)
        #     if user:
        #         login(request, user)
        #         return redirect('Admin_Dashboard')
        #     else:
        #           context = {'msg': 'Invalid username or password'}
        #           return render(request, 'login.html',context)
        # if request.method == 'POST':
        #     email  = request.POST['email']
        #     password = request.POST['password']
        #     user = authenticate(email=email, password=password)
        #     if user is not None:
        #             request.session['SAdm_id'] = user.id
        #             return redirect('Admin_Dashboard')

        #     else:
        #         context = {'msg': 'Invalid username or password'}
        #         return render(request, 'login.html', context)
    

def manager_logout(request):
    if 'm_id' in request.session:  
        request.session.flush()
        return redirect('login')
    else:
        return redirect('login') 

def index(request):
    return render(request,'software_training/training/index.html')
    
def Trainings(request):
    return render(request,'software_training/training/training.html')

#******************Manager*****************************

def Manager_Dashboard(request):
    return render(request,'software_training/training/manager/manager_Dashboard.html')

def Manager_trainer(request):
    return render(request,'software_training/training/manager/manager_trainer.html')

def manager_team(request):
    return render(request,'software_training/training/manager/manager_team.html')

def manager_current_team(request):
    return render(request,'software_training/training/manager/manager_current_team.html')

def Manager_current_task(request):
    return render(request,'software_training/training/manager/manager_current_task.html')

def manager_current_assigned(request):
    return render(request,'software_training/training/manager/manager_current_assigned.html')

def manager_current_trainees(request):
    return render(request,'software_training/training/manager/manager_current_trainees.html')

def manager_current_empdetails(request):
    return render(request,'software_training/training/manager/manager_current_empdetails.html')

def manager_current_attendance(request):
    return render(request,'software_training/training/manager/manager_current_attendance.html')

def manager_current_attendance_list(request):
    return render(request,'software_training/training/manager/manager_current_attendance_list.html')

def manager_current_task_list(request):
    return render(request,'software_training/training/manager/manager_current_task_list.html')

def manager_current_task_details(request):
    return render(request,'software_training/training/manager/manager_current_task_details.html')
    
def manager_previous_team(request):
    return render(request,'software_training/training/manager/manager_previous_team.html')

def Manager_previous_task(request):
    return render(request,'software_training/training/manager/Manager_previous_task.html')

def manager_previous_assigned(request):
    return render(request,'software_training/training/manager/manager_previous_assigned.html')

def manager_previous_trainees(request):
    return render(request,'software_training/training/manager/manager_previous_trainees.html')

def manager_previous_empdetails(request):
    return render(request,'software_training/training/manager/manager_previous_empdetails.html')

def manager_previous_attendance(request):
    return render(request,'software_training/training/manager/manager_previous_attendance.html')

def manager_previous_attendance_list(request):
    return render(request,'software_training/training/manager/manager_previous_attendance_list.html')

def manager_previous_task_list(request):
    return render(request,'software_training/training/manager/manager_previous_task_list.html')

def manager_previous_task_details(request):
    return render(request,'software_training/training/manager/manager_previous_task_details.html')

def manager_trainee(request):
    return render(request,'software_training/training/manager/manager_trainee.html')

def Manager_trainees_details(request):
    return render(request,'software_training/training/manager/Manager_trainees_details.html')

def Manager_trainees_attendance(request):
    return render(request,'software_training/training/manager/Manager_trainees_attendance.html')

def Manager_reported_issues(request):
    return render(request,'software_training/training/manager/manager_reported_issues.html')

def manager_trainerreportissue(request):
    return render(request,'software_training/training/manager/manager_trainerreportissue.html')

def manager_trainer_unsolvedissue(request):
    return render(request,'software_training/training/manager/manager_trainer_unsolvedissue.html')

def manager_trainer_solvedissue(request):
    return render(request,'software_training/training/manager/manager_trainer_solvedissue.html')

def manager_traineereportissue(request):
    return render(request,'software_training/training/manager/manager_traineereportissue.html')

def manager_trainee_unsolvedissue(request):
    return render(request,'software_training/training/manager/manager_trainee_unsolvedissue.html')

def manager_trainee_solvedissue(request):
    return render(request,'software_training/training/manager/manager_trainee_solvedissue.html')

def manager_report_issue(request):
    return render(request,'software_training/training/manager/manager_report_issue.html')

def manager_reported_issue(request):
    return render(request,'software_training/training/manager/manager_reported_issue.html')

def manager_trainee_solvedissue(request):
    return render(request,'software_training/training/manager/manager_trainee_solvedissue.html')

def Manager_attendance(request):
    return render(request,'software_training/training/manager/manager_attendance.html') 

def manager_trainee_attendance(request):
    return render(request,'software_training/training/manager/manager_trainee_attendance.html') 

def manager_trainer_attendance(request):
    return render(request,'software_training/training/manager/manager_trainer_attendance.html') 

def manager_trainer_attendance_table(request):
    return render(request,'software_training/training/manager/manager_trainer_attendance_table.html') 

def manager_trainee_attendance_table(request):
    return render(request,'software_training/training/manager/manager_trainee_attendance_table.html') 

def manager_applyleave(request):
    return render(request,'software_training/training/manager/manager_applyleave.html') 

def manager_applyleavsub(request):
    return render(request,'software_training/training/manager/manager_applyleavsub.html')

def manager_requestedleave(request):
    return render(request,'software_training/training/manager/manager_requestedleave.html')

def manager_trainer_leave(request):
    return render(request,'software_training/training/manager/manager_trainer_leave.html')

def manager_trainers_leavelist(request):
    return render(request,'software_training/training/manager/manager_trainers_leavelist.html')

def manager_trainer_leavestatus(request):
    return render(request,'software_training/training/manager/manager_trainer_leavestatus.html')

def manager_trainee_leave(request):
    return render(request,'software_training/training/manager/manager_trainee_leave.html')

def manager_trainee_leavelist(request):
    return render(request,'software_training/training/manager/manager_trainee_leavelist.html')

def manager_trainee_leavestatus(request):
    return render(request,'software_training/training/manager/manager_trainee_leavestatus.html')

def manager_new_team(request):
    return render(request,'software_training/training/manager/manager_new_team.html')

def manager_new_teamcreate(request):
    return render(request,'software_training/training/manager/manager_new_teamcreate.html')

def manager_newtrainees(request):
    return render(request,'software_training/training/manager/manager_newtrainees.html')

    
#******************Trainer*****************************
def trainer_applyleave(request):
    return render(request, 'software_training/training/trainer/trainer_applyleave.html')

def trainer_applyleave_form(request):
    return render(request, 'software_training/training/trainer/trainer_applyleave_form.html')

def trainer_traineesleave_table(request):
    return render(request, 'software_training/training/trainer/trainer_traineesleave_table.html')

def trainer_reportissue(request):
    return render(request, 'software_training/training/trainer/trainer_reportissue.html')

def trainer_reportissue_form(request):
    return render(request, 'software_training/training/trainer/trainer_reportissue_form.html')

def trainer_reportedissue_table(request):
    return render(request, 'software_training/training/trainer/trainer_reportedissue_table.html')
    
def trainer_myreportissue_table(request):
    return render(request, 'software_training/training/trainer/trainer_myreportissue_table.html')
    
def trainer_attendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance.html')

def trainer_attendance_trainees(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees.html')

def trainer_attendance_trainer(request):
    return render(request, 'software_training/training/trainer/trainer_attendance_trainer.html')

def trainer_attendance_trainer_viewattendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainer_viewattendance.html')

def trainer_attendance_trainer_viewattendancelist(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainer_viewattendancelist.html')

def trainer_attendance_trainees_viewattendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees_viewattendance.html')

def trainer_attendance_trainees_viewattendancelist(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees_viewattendancelist.html')

def trainer_attendance_trainees_addattendance(request):
    return render(request,'software_training/training/trainer/trainer_attendance_trainees_addattendance.html')

def trainer_dashboard(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
           tr_id = request.session['tr_id']
        z = user_registration.objects.filter(id=tr_id)
        return render(request,'software_training/training/trainer/trainer_dashboard.html',{'z': z})
    else:
        return redirect('/')
        
def trainer_imagechange(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
           tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id).filter(fullname=tr_fullname)
        return render(request,'software_training/training/trainer/trainer_imagechange.html',{'z':z})
    else:
        return redirect('/')
        
def trainerimagechange(request,id):
    if request.method == 'POST':
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        abc.save()
        return redirect('trainer_imagechange')
    return render(request, 'trainer_imagechange.html') 

def trainer_passwordchange(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
           tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id).filter(fullname=tr_fullname)
        if request.method=='POST':
            abc = user_registration.objects.get(id=tr_id)
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'software_training/training/trainer/trainer_dashboard.html', {'z':z})
    
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
            return render(request,'software_training/training/trainer/trainer_passwordchange.html',{'z':z})
        return render(request,'software_training/training/trainer/trainer_passwordchange.html',{'z':z})
    else:
        return redirect('/')
        
def trainer_logout(request):
    if 'tr_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 
    

def trainer_topic(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        return render(request,'software_training/training/trainer/trainer_topic.html',{'z': z})
    else:
        return redirect('/')

def trainer_addtopic(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
           tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        crt = create_team.objects.filter(create_team_trainer=tr_fullname,create_team_status=0)
        mem = topic()
        if request.method == 'POST':
            mem.topic_team_id = request.POST['select']
            mem.topic_topic = request.POST['topic']
            mem.topic_startdate = request.POST['start']
            mem.topic_enddate = request.POST['end']
            mem.topic_status = 0
            mem.topic_trainer_id = tr_id 
            mem.save()
            return render(request,'software_training/training/trainer/trainer_addtopic.html',{'crt':crt,'mem': mem,'z':z})
        return render(request,'software_training/training/trainer/trainer_addtopic.html',{'crt':crt,'mem': mem,'z':z})
    else:
        return redirect('/')

def trainer_viewtopic(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
    
        z = user_registration.objects.filter(id=tr_id)
        mem = topic.objects.filter(topic_trainer=tr_id).order_by('-id')
        return render(request,'software_training/training/trainer/trainer_viewtopic.html',{'mem':mem,'z':z})
    else:
        return redirect('/')

def trainer_team(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
    
        z = user_registration.objects.filter(id=tr_id)
        return render(request,'software_training/training/trainer/trainer_team.html',{'z':z})
    else:
        return redirect('/')

def trainer_currentteam(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
           tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id).filter(fullname=tr_fullname)
        tm = create_team.objects.filter(create_team_trainer=tr_fullname).filter(create_team_status=0).order_by('-id')
        return render(request,'software_training/training/trainer/trainer_current_team_list.html',{'z':z,'tm':tm})
    else:
        return redirect('/')
def attenperform(request,id):
    if request.method == 'POST':
        abc = create_team.objects.get(id=id)
        abc.create_team_progress = request.POST['sele']
        abc.save()
    return redirect('trainer_currentteam')

def trainer_currenttrainees(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation_name='trainee')
        mem = user_registration.objects.filter(
            designation_id=des.id).filter(team_id=d).order_by('-id')
        return render(request,'software_training/training/trainer/trainer_current_trainees_list.html',{'z':z,'mem':mem})
    else:
        return redirect('/')

def trainer_currenttraineesdetails(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
    
        z = user_registration.objects.filter(id=tr_id)
        mem = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=mem.team.id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels = [i.workperformance,i.attitude,i.creativity]
            data = [i.workperformance,i.attitude,i.creativity]
        return render(request,'software_training/training/trainer/trainer_current_tainees_details.html', {'mem': mem, 'tre': tre, 'z': z ,'labels': labels,'data': data,})
    else:
        return redirect('/')

def trainer_currentattentable(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        mem = user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=mem
            atten = attendance.objects.filter(attendance_date__gte=std,attendance_date__lte=edd,attendance_user=user).order_by('-id')
        return render(request,'software_training/training/trainer/trainer_current_atten_table.html',{'mem': mem, 'z': z,'atten':atten})
    else:
        return redirect('/')

def trainer_currentperform(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        mem = user_registration.objects.get(id=id)
        if request.method == 'POST':
            mem.attitude = request.POST['sele1']
            mem.creativity = request.POST['sele2']
            mem.workperformance = request.POST['sele3']
            mem.save()
            return render(request,'software_training/training/trainer/trainer_current_perform.html',{'mem': mem, 'z': z})
        return render(request,'software_training/training/trainer/trainer_current_perform.html',{'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_currentattenadd(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
    
        z = user_registration.objects.filter(id=tr_id)
        mem = user_registration.objects.get(id=id)
        atten = attendance()
        if request.method == 'POST':
            atten.attendance_date = request.POST['date']
            atten.attendance_user  = mem
            atten.attendance_status = request.POST['pres']
            atten.save()
            return render(request,'software_training/training/trainer/trainer_current_atten_add.html',{'mem': mem, 'atten': atten, 'z': z})
        return render(request,'software_training/training/trainer/trainer_current_atten_add.html',{'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_previousteam(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
           tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id).filter(fullname=tr_fullname)
        tm = create_team.objects.filter(create_team_trainer=tr_fullname).filter(create_team_status = 1).order_by('-id')
        return render(request,'software_training/training/trainer/trainer_previous_team_list.html',{'z':z,'tm':tm})
    else:
        return redirect('/')

def trainer_previoustrainees(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation_name='trainee')
        mem = user_registration.objects.filter(designation_id=des.id).filter(team_id=d)
        return render(request,'software_training/training/trainer/trainer_previous_trainess_list.html',{'z':z,'mem':mem})
    else:
        return redirect('/')

def trainer_previoustraineesdetails(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        mem = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=mem.team_id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels = [i.workperformance,i.attitude,i.creativity]
            data = [i.workperformance,i.attitude,i.creativity]
        print(data)
        return render(request,'software_training/training/trainer/trainer_previous_trainees_details.html',{'mem': mem, 'tre': tre, 'z': z ,'labels': labels,'data': data,})
    else:
        return redirect('/')

def trainer_previousattentable(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        mem = user_registration.objects.get(id=id)
        att = attendance.objects.filter( attendance_user=mem.id).order_by('-id')
        return render(request,'software_training/training/trainer/trainer_previous_atten_table.html',{'z':z,'att':att})
    else:
        return redirect('/')

def trainer_previousperfomtable(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        num = user_registration.objects.get(id=id)
        return render(request,'software_training/training/trainer/trainer_previous_performtable.html',{'z':z,'num':num})
    else:
        return redirect('/')

def trainer_current_attendance(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        mem = user_registration.objects.get(id=id)
        return render(request,'software_training/training/trainer/trainer_current_attendance.html',{'z':z,'mem':mem})
    else:
        return redirect('/')


def trainer_Task(request) :
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        return render(request,'software_training/training/trainer/trainer_task.html',{'z' :z})
    else:
        return redirect('/')
    
def trainer_teamlist(request) :
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
            tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        tam = create_team.objects.filter(create_team_trainer=tr_fullname,create_team_status = 0).order_by('-id')
        des = designation.objects.get(designation_name='trainee')
        cut = user_registration.objects.filter(designation_id=des.id)
        return render(request,'software_training/training/trainer/trainer_teamlist.html',{'z' :z,'tam': tam, 'cut': cut})
    else:
        return redirect('/')

def trainer_taskpage(request,id) :
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
            tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        d = create_team.objects.get(id=id)
        return render(request, 'software_training/training/trainer/trainer_taskfor.html',{'d': d, 'z': z})
    else:
        return redirect('/')
    
def trainer_givetask(request,id) :
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
            tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation_name='trainee')
        var = user_registration.objects.filter(team_id=d).filter(designation_id=des.id)
        if request.method == 'POST':
            list= request.POST.get('list')
            name = request.POST.get('taskname')
            desc = request.POST.get('description')
            files= request.FILES['files']
            start= request.POST.get('start')
            end = request.POST.get('end')
            task_status = 0
            team_name = id
            vars = trainer_task(trainer_task_user_id=list,trainer_task_taskname=name,trainer_task_description=desc,trainer_task_files=files,trainer_task_startdate=start,
                     trainer_task_enddate=end,trainer_task_status=task_status,trainer_task_team_name_id =team_name)
            vars.save()
            return render(request, 'software_training/training/trainer/trainer_givetask.html', {'z': z, 'var': var})
        else:
            return render(request,'software_training/training/trainer/trainer_givetask.html',{'z': z, 'var': var})
    else:
        return redirect('/')
    
def trainer_taskgivenpage(request,id) :
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
            tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        d = create_team.objects.get(id=id)
        c = trainer_task.objects.filter(trainer_task_team_name_id=d.id)
        des = designation.objects.get(designation_name='trainee')
        mem1 = user_registration.objects.filter(designation_id=des.id).filter(team_id=d).order_by('-id')
        mem = user_registration.objects.filter(designation_id=des.id).filter(team_id=d).values_list('id')
        tsk = trainer_task.objects.filter(trainer_task_team_name_id=d.id).filter(trainer_task_user__in=mem).order_by('-id')
        return render(request,'software_training/training/trainer/trainer_taskgiven.html',{'mem': mem,'mem1': mem1, 'tsk': tsk, 'z': z})
    else:
        return redirect('/')
    
# def trainer_task_completed_teamlist(request):
#     if 'tr_id' in request.session:
#         if request.session.has_key('tr_id'):
#             tr_id = request.session['tr_id']
#         if request.session.has_key('tr_fullname'):
#             tr_fullname = request.session['tr_fullname']
#         else:
#            tr_fullname = "dummy"
#         z = user_registration.objects.filter(id=tr_id).filter(fullname=tr_fullname)
#         tam = create_team.objects.filter(create_team_trainer=tr_fullname,create_team_status= 1).order_by('-id')
#         des = designation.objects.get(designation_name='trainee')
#         cut = user_registration.objects.filter(designation_id=des.id)
#         return render(request, 'software_training/training/trainer/trainer_task_completed_teamlist.html',{'z': z, 'cut':cut, 'tam':tam})
#     else:
#         return redirect('/')
# def trainer_task_completed_team_tasklist(request,id):
#     if 'tr_id' in request.session:
#         if request.session.has_key('tr_id'):
#             tr_id = request.session['tr_id']
#         else:
#            tr_fullname = "dummy"
#         z = user_registration.objects.filter(id=tr_id)
#         tsk = trainer_task.objects.filter(trainer_task_team_name=id).order_by('-id')
#         return render(request, 'software_training/training/trainer/trainer_task_completed_team_tasklist.html',{'z': z, 'tsk':tsk})
#     else:
#         return redirect('/')
def trainer_task_previous_teamlist(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
            tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id).filter(fullname=tr_fullname)
        tam = create_team.objects.filter(create_team_trainer=tr_fullname,create_team_status= 1).order_by('-id')
        des = designation.objects.get(designation_name='trainee')
        cut = user_registration.objects.filter(designation_id=des.id)
        return render(request, 'software_training/training/trainer/trainer_task_previous_teamlist.html',{'z': z, 'cut':cut, 'tam':tam})
    else:
        return redirect('/')
def trainer_task_previous_team_tasklist(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        tsk = trainer_task.objects.filter(trainer_task_team_name_id=id).order_by('-id')
        return render(request, 'software_training/training/trainer/trainer_task_previous_team_tasklist.html',{'z': z, 'tsk':tsk})
    else:
        return redirect('/')

def trainer_trainees(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
   
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
            tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        cut = create_team.objects.filter(create_team_trainer=tr_fullname).values_list('id',flat=True)
        print(cut)
        des = designation.objects.get(designation_name='trainee')
        user = user_registration.objects.filter(designation_id=des.id,team_id__in=cut)
        return render(request, 'software_training/training/trainer/trainer_current_trainees.html',{'z':z,'n': user})
    else:
        return redirect('/')
        
def trainer_traineesdetails(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
            tr_fullname = request.session['tr_fullname']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        mem = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=mem.team.id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels = [i.workperformance,i.attitude,i.creativity]
            data = [i.workperformance,i.attitude,i.creativity]
        return render(request, 'software_training/training/trainer/trainer_traineesdetails.html',{'mem': mem, 'tre': tre, 'z': z ,'labels': labels,'data': data,})
    else:
        return redirect('/')

def trainer_current_attendance_view(request,id):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        else:
           tr_fullname = "dummy"
        z = user_registration.objects.filter(id=tr_id)
        mem = user_registration.objects.get(id=id)
        return render(request,'software_training/training/trainer/trainer_current_attendance_view.html',{'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_paymentlist(request):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
            tr_fullname = request.session['tr_fullname']
        if request.session.has_key('tr_designation_id'):
            tr_designation_id = request.session['tr_designation_id']
        else:
            m_id = "dummy"
        z = user_registration.objects.filter(designation_id=tr_designation_id).filter(fullname=tr_fullname).filter(id=tr_id)
        acc=acntspayslip.objects.filter(acntspayslip_user_id=tr_id).all().order_by('-id')
        return render(request, 'software_training/training/trainer/trainer_paymentlist.html', {'acc': acc,'z':z})
    else:
        return redirect('/')

def trainer_payment_viewslip(request,id,tid):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
            tr_fullname = request.session['tr_fullname']
        if request.session.has_key('tr_designation_id'):
            tr_designation_id = request.session['tr_designation_id']
        else:
            m_id = "dummy"
        z= user_registration.objects.filter(designation_id=tr_designation_id).filter(fullname=tr_fullname).filter(id=tr_id)
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        names = acntspayslip.objects.all()
        return render(request, 'software_training/training/trainer/trainer_payment_viewslip.html', {'z': z,'user':user,'acc':acc})
    else:
        return redirect('/')

def trainer_payment_print(request,id,tid):
    if 'tr_id' in request.session:
        if request.session.has_key('tr_id'):
            tr_id = request.session['tr_id']
        if request.session.has_key('tr_fullname'):
            tr_fullname = request.session['tr_fullname']
        if request.session.has_key('tr_designation_id'):
            tr_designation_id = request.session['tr_designation_id']
        else:
            m_id = "dummy"
        z = user_registration.objects.filter(designation_id=tr_designation_id).filter(fullname=tr_fullname).filter(id=tr_id)
        mem = user_registration.objects.filter(id=tr_id)   
        user = user_registration.objects.get(id=tid)
        acc = acntspayslip.objects.get(id=id)
        return render(request, 'software_training/training/trainer/trainer_payment_print.html', {'z': z,'user':user,'acc':acc,'mem': mem})
    else:
        return redirect('/')


def pdf(request,id,tid):
    date = datetime.now()   
    acc = acntspayslip.objects.get(id=id)
    user = user_registration.objects.get(id=tid)
    template_path = 'software_training/training/trainer/trainer_payment_pdf.html'
    context = {'acc': acc,'user':user,
    'media_url':settings.MEDIA_URL,
    'date':date
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


    
#******************  Trainee  *****************************

def trainee_dashboard_trainee(request):
    return render(request,'software_training/training/trainee/trainee_dashboard_trainee.html')
    
def trainee_task(request):
   return render(request,'software_training/training/trainee/trainee_task.html')   

def trainee_task_list(request):
    return render(request,'software_training/training/trainee/trainee_task_list.html')

def trainee_task_details(request):
    return render(request,'software_training/training/trainee/trainee_task_details.html')

def trainee_completed_taskList(request):
   return render(request,'software_training/training/trainee/trainee_completed_taskList.html')

def trainee_completedTask(request):
    return render(request,'software_training/training/trainee/trainee_completedTask.html')

def trainee_completed_details(request):
    return render(request,'software_training/training/trainee/trainee_completed_details.html')

def trainee_topic(request):
    return render(request, 'software_training/training/trainee/trainee_topic.html')

def trainee_currentTopic(request):
    return render(request, 'software_training/training/trainee/trainee_currentTopic.html')
    
def trainee_previousTopic(request):
    return render(request, 'software_training/training/trainee/trainee_previousTopic.html')

def trainee_reported_issue(request):
    return render(request, 'software_training/training/trainee/trainee_reported_issue.html')
   
def trainee_report_reported(request):
    return render(request, 'software_training/training/trainee/trainee_report_reported.html')
  
def trainee_report_issue(request):
    return render(request, 'software_training/training/trainee/trainee_report_issue.html')

def trainee_applyleave_form(request):
    return render(request, 'software_training/training/trainee/trainee_applyleave_form.html')  

def trainee_applyleave_card(request):
     return render(request, 'software_training/training/trainee/trainee_applyleave_cards.html')
    
def trainee_appliedleave(request):
     return render(request, 'software_training/training/trainee/trainee_appliedleave.html')
    
def Attendance(request):
   return render(request,'software_training/training/trainee/trainees_attendance.html')
    
def trainees_attendance_viewattendance(request):
    return render(request,'software_training/training/trainee/trainees_attendance_viewattendance.html')
 
def trainees_attendance_viewattendancelist(request):
   return render(request,'software_training/training/trainee/trainees_attendance_viewattendancelist.html')
   
def trainee_payment(request):
   return render(request,'software_training/training/trainee/trainee_payment.html')
   
def trainee_payment_addpayment(request):
   return render(request,'software_training/training/trainee/trainee_payment_addpayment.html')
  
def trainee_payment_viewpayment(request):
     return render(request,'software_training/training/trainee/trainee_payment_viewpayment.html')

#****************************  Admin- view  ********************************

def Admin_Dashboard(request):
    return render(request,'software_training/training/admin/admin_Dashboard.html')

def Admin_categories(request):
    return render(request,'software_training/training/admin/admin_categories.html') 

def Admin_emp_categories(request):
    return render(request,'software_training/training/admin/admin_emp_categories.html')  

def Admin_courses(request):
    return render(request,'software_training/training/admin/admin_courses.html')

def Admin_emp_course_list(request):
    return render(request,'software_training/training/admin/admin_emp_course_list.html')

def Admin_emp_course_details(request):
    return render(request,'software_training/training/admin/admin_emp_course_details.html')

def Admin_emp_profile(request):
    return render(request,'software_training/training/admin/admin_emp_profile.html')

def Admin_emp_attendance(request):
    return render(request,'software_training/training/admin/admin_emp_attendance.html')

def Admin_emp_attendance_show(request):
    return render(request,'software_training/training/admin/admin_emp_attendance_show.html')

def Admin_task(request):
    return render(request,'software_training/training/admin/admin_task.html')

def Admin_givetask(request):
    return render(request,'software_training/training/admin/admin_givetask.html')

def Admin_current_task(request):
    return render(request,'software_training/training/admin/admin_current_task.html')

def Admin_previous_task(request):
    return render(request,'software_training/training/admin/admin_previous_task.html')

def Admin_registration_details(request):
    return render(request,'software_training/training/admin/admin_registration_details.html')  

def Admin_attendance(request):
    return render(request,'software_training/training/admin/admin_attendance.html') 

def Admin_attendance_show(request):
    return render(request,'software_training/training/admin/admin_attendance_show.html')

def Admin_reported_issues(request):
    return render(request,'software_training/training/admin/admin_reported_issues.html') 

def Admin_emp_reported_detail(request):
    return render(request,'software_training/training/admin/admin_emp_reported_detail.html')

def Admin_emp_reported_issue_show(request):
    return render(request,'software_training/training/admin/admin_emp_reported_issue_show.html')

def Admin_manager_reported_detail(request):
    return render(request,'software_training/training/admin/admin_manager_reported_detail.html')

def Admin_manager_reported_issue_show(request):
    return render(request,'software_training/training/admin/admin_manager_reported_issue_show.html')

def Admin_add(request):
    return render(request,'software_training/training/admin/admin_add.html') 

def Admin_addcategories(request):
    return render(request,'software_training/training/admin/admin_addcategories.html') 

def Admin_categorieslist(request):
    return render(request,'software_training/training/admin/admin_categorieslist.html') 

def Admin_addcourse(request):
    return render(request,'software_training/training/admin/admin_addcourse.html') 

def Admin_addnewcourse(request):
    return render(request,'software_training/training/admin/admin_addnewcourse.html') 

def Admin_addnewcategories(request):
    return render(request,'software_training/training/admin/admin_addnewcategories.html') 

def Admin_courselist(request):
    return render(request,'software_training/training/admin/admin_courselist.html') 

def Admin_coursedetails(request):
    return render(request,'software_training/training/admin/admin_coursedetails.html') 

#******************accounts****************

def accounts_Dashboard(request):
    return render(request, 'software_training/training/account/accounts_Dashboard.html')

def accounts_registration_details(request):
    return render(request, 'software_training/training/account/accounts_registration_details.html')

def accounts_payment_details(request):
    return render(request, 'software_training/training/account/account_payment_details.html')

def accounts_payment_salary(request):
    return render(request, 'software_training/training/account/account_payment_salary.html')

def accounts_payment_view(request):
    return render(request, 'software_training/training/account/account_payment_view.html')

def accounts_report_issue(request):
    return render(request, 'software_training/training/account/account_report_issue.html')

def accounts_report(request):
    return render(request, 'software_training/training/account/account_report.html')

def accounts_reported_issue(request):
    return render(request, 'software_training/training/account/account_reported_issue.html')

def accounts_acntpay(request):
    return render(request, 'software_training/training/account/accounts_acntpay.html')

def accounts_employee(request):
    return render(request, 'software_training/training/account/accounts_employee.html')

def accounts_emp_dep(request):
    return render(request, 'software_training/training/account/accounts_emp_dep.html')

def accounts_emp_list(request):
    return render(request, 'software_training/training/account/accounts_emp_list.html')

def accounts_emp_details(request):
    return render(request, 'software_training/training/account/accounts_emp_details.html')

def accounts_add_bank_acnt(request):
    return render(request, 'software_training/training/account/accounts_add_bank_acnt.html')

def accounts_bank_acnt_details(request):
    return render(request, 'software_training/training/account/accounts_bank_acnt_details.html')

def accounts_salary_details(request):
    return render(request, 'software_training/training/account/accounts_salary_details.html')

def accounts_expenses(request):
    return render(request, 'software_training/training/account/accounts_expenses.html')

def accounts_expenses_viewEdit(request):
    return render(request, 'software_training/training/account/accounts_expenses_viewEdit.html')

def accounts_expenses_viewEdit_Update(request):
    return render(request, 'software_training/training/account/accounts_expenses_viewEdit.html')

def accounts_expense_newTransaction(request):
    return render(request, 'software_training/training/account/accounts_expense_newTransaction.html')

def accounts_paydetails(request):
    return render(request, 'software_training/training/account/accounts_paydetails.html')

def accounts_print(request):
    return render(request, 'software_training/training/account/accounts_print.html')

def accounts_payment(request):
    return render(request,'software_training/training/account/accounts_payment.html')

def accounts_payment_dep(request):
    return render(request, 'software_training/training/account/accounts_payment_dep.html')

def accounts_payment_list(request):
    return render(request, 'software_training/training/account/accounts_payment_list.html')

def accounts_payment_details(request):
    return render(request, 'software_training/training/account/accounts_payment_details.html')

def accounts_payment_detail_list(request):
    return render(request, 'software_training/training/account/accounts_payment_detail_list.html')

def accounts_payslip(request):
    return render(request, 'software_training/training/account/accounts_payslip.html')