from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


from workshop_app.form import Login_Form, Customer_Form, Workmanager_Form


# Create your views here.
# def front(request):
    # return render(request,'front.html')

def landing_page(request):
    return render(request,'page.html')

def dash(request):
    return render(request,'dash.html')



# registration
def customer_reg(request):
    form1=Login_Form()
    form2=Customer_Form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = Customer_Form(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_customer = True
            user.save()
            user1 = form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('login_view')
    return render(request,'customer_reg.html',{'form1':form1,'form2':form2})


def workmanager_reg(request):
    form1=Login_Form()
    form2= Workmanager_Form()
    if request.method == 'POST':
        form1 = Login_Form(request.POST)
        form2 = Workmanager_Form(request.POST)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_workmanager = True
            user.save()
            user1 = form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('login_view')
    return render(request,'workmanager_reg.html',{'form1':form1,'form2':form2})


def login_view1(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin')
            elif user.is_customer:
                return redirect('customer')
            elif user.is_workmanager:
                return redirect('manager')
        else:
                messages.info(request,'Invalid Creadentials')
    return render(request,'login.html')

def admin(request):
    return render(request,'admin_template/admin.html')

def customer(request):
    return render(request,'customer_template/customer.html')

def manager(request):
    return render(request,'manager_template/manager.html')
         