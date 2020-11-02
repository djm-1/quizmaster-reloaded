from django.shortcuts import render
import uuid
#create views here

def index(request):
    id=uuid.uuid4()
    context={'id':id}
    return render(request,'home.html',context)


