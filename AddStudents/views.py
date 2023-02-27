from django.shortcuts import render,redirect
from AddStudents.models import Students

# Create your views here.
def home(request):
    mylist = Students.objects.all()
    if (mylist!=''):
        return render(request,'home.html',{'mylist':mylist})
    else:
        return render(request,'home.html')

def addData(request):
    if request.method=='POST':
        rollno=request.POST['rollno']
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        mobile=request.POST['mobile']
        course=request.POST['course']

        data=Students()
        data.Rollno=rollno
        data.Name=name
        data.Address=address
        data.Email=email
        data.Mobile=mobile
        data.Course=course
        data.save()
        mylist = Students.objects.all()
        return redirect('home')
    return render(request,'home.html',{'mylist':mylist, 'pageType':'add'})


def editData(request,id):
    mydata=Students.objects.get(id=id)
    mylist=Students.objects.all()
    context = {
        'getdata':mydata,
        'mylist':mylist,
        'pageType':'edit'
    }
    return render(request,'home.html',context)


def updateData(request,id):
    mydata=Students.objects.get(id=id)
    if request.method=='POST':
        rollno=request.POST['rollno']
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        mobile=request.POST['mobile']
        course=request.POST['course']

        mydata.Rollno=rollno
        mydata.Name=name
        mydata.Address=address
        mydata.Email=email
        mydata.Mobile=mobile
        mydata.Course=course
        mydata.save()
        return redirect('home')


def deleteData(request,id):
    mydata=Students.objects.get(id=id)
    mydata.delete()
    return redirect('home')

def cancel(request):
    return redirect('home')