from django.shortcuts import render,HttpResponseRedirect
from .models import quiz,leaderboard
from .forms import RegisterForm
import uuid
from django.contrib import messages
from django.core.paginator import Paginator
#from datetime import datetime
#back-end code for contest-hosting
#trick
con_id=uuid.uuid4()
contest=con_id
# tricky end
def store_id(request):
    if request.user.is_authenticated:
        global con_id
        con_id = request.POST.get('con_id')
        #print(str(con_id))
        return HttpResponseRedirect('/quiz/host')
    else:
        messages.warning(request,'Signup or login first to continue')
        return HttpResponseRedirect('/')

def question_view(request):
    if request.user.is_authenticated:
        quizobj= quiz.objects.filter(contest_id=con_id)
        num= quizobj.count()
        context={'quizobj':quizobj,'con_id':con_id,'num':num}
        return render(request,'host.html',context)
    else:
        messages.warning(request,'Signup or login first to continue')
        return HttpResponseRedirect('/')
    

def add_question(request):
    if request.user.is_authenticated:
        new_quiz_obj=quiz(contest_id=con_id,question=request.POST['question'],
                    option_1=request.POST['option_1'],option_2=request.POST['option_2'],
                    option_3=request.POST['option_3'],option_4=request.POST['option_4'],
                    answer=request.POST['answer'])
        new_quiz_obj.save()
        return HttpResponseRedirect('/quiz/host')
    else:
        messages.warning(request,'Signup or login first to continue')
        return HttpResponseRedirect('/')

def delete_question(request,id):
    if request.user.is_authenticated:
        quiz_del = quiz.objects.get(id=id)
        quiz_del.delete()
        return HttpResponseRedirect('/quiz/host')
    else:
        messages.warning(request,'Signup or login first to continue')
        return HttpResponseRedirect('/')

def host_return(request):
    if request.user.is_authenticated:
        context={'con_id':con_id}
        return render(request,'hostfinal.html',context)
    else:
        messages.warning(request,'Signup or login first to continue')
        return HttpResponseRedirect('/')

#end of back-end code for hosting contest




#start of back-end code for participating in contest

#user registration
def register(response):
    if response.method == "POST":
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'Sign up successful! You may log in now')
        return HttpResponseRedirect('/')
    else:
        form=RegisterForm()

    return render(response,'signup.html',{'form':form})

#startquiz page
def getid(request):
    if request.user.is_authenticated:
        global contest 
        contest = request.POST.get('con_id_enter')
        return HttpResponseRedirect('/quiz/quizpage/')
    else:
        messages.warning(request,'Signup or login first to continue')
        return HttpResponseRedirect('/')

def quizpage(request):
    if request.user.is_authenticated:
        quiz_obj=quiz.objects.filter(contest_id=contest)
        total=quiz_obj.count()
        user_score=0
        right_ans=0
        wrong_ans=0
        unattempted=0
        user_answer=[]
        if request.method == 'POST':
            for qn in quiz_obj:
                if request.POST.get(str(qn.id),False) != False:
                    given_ans=request.POST[str(qn.id)]
                    if given_ans==qn.answer:
                        right_ans+=1
                        user_answer.append(given_ans)
                    else:
                        wrong_ans+=1
                        user_answer.append(given_ans)
                else:
                    unattempted+=1 
                    user_answer.append('--Not answered--')
            user_score=right_ans
            new_participant=leaderboard(contest_id=contest,
                    participant_name=request.user.get_username(),
                    score=user_score)
            new_participant.save()
            # print(right_ans)
            # print(wrong_ans)
            # print(unattempted)
            params={'right':right_ans,'wrong':wrong_ans,'nil':unattempted,
                    'user_answer':user_answer,'quiz_obj': quiz_obj,'total':total}
            return render(request,'score.html',params)
        context={'quiz_obj': quiz_obj,'total':total}
        return render(request, 'quizpage.html', context)
    else:
        messages.warning(request,'Signup or login first to continue')
        return HttpResponseRedirect('/')



def show_leaderboard(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            leader_id=request.POST.get('id_view')
            # print(leader_id)
            leader_obj=leaderboard.objects.filter(contest_id=leader_id).order_by('-score')
            # for i in leader_obj:
            #      print (i.participant_name)
            #      print(i.score)
            context={'ranking':leader_obj}
            return render(request,'ranking.html',context)
        else:
            return render(request,'leaderboard.html')
    else:
        messages.warning(request,'Signup or login first to continue')
        return HttpResponseRedirect('/')


#end of back-end code for participating in contest


#contact us
def contact_us(request):
    return render(request,'contactus.html')
    