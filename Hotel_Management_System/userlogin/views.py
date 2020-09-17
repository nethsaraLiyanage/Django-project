from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer , Admin , Employee
from .models import generateRandomeNum
from .models import foodItem, utilCost, ingrediants
from django.contrib.auth.models import auth
from django.shortcuts import redirect
from random import randint
from .forms import custmoneForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

#random num gen

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

# Create your views here.

def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')
    

def signUp(request):
    return render(request, 'Signup.html')


def admin(request):
    return render(request, 'Dashboard.html')


def forgetpassword(request):
    return render(request, 'Forgot_password_1.html')


def forgetpw2(request):
    return render(request, 'Forgot_password_2.html')


def fogetPw3(request):
    return render(request, 'Forgot_password_3.html')


def customerLogout(request):
    return render(request, 'login.html')


def addEmployees(request):
    return render(request, 'AddEmployee.html')


def employeerepo(request):
    return render(request, 'AttendenceReport.html')


def foodreport(request):
    return render(request, 'FoodReport.html')
    
def foodprofit(request):
    return render(request, 'FoodProfitability.html')

def myprofile(request):
    print("sesseionvalue : " + request.session['userid'])
    cus1 = Customer.objects.get(cusid=request.session['userid'])
    return render(request, 'User_profile.html' , {'customer' : cus1} )

# login function
def vertifyLogin(request):
    
    Email = request.POST['loginEmail']
    Password = request.POST['loginPw']

    print(Password)

    cusExist = Customer.objects.filter(email=Email).exists()

    if cusExist == True:
        #auth.login(request, customer)
        customer = Customer.objects.get(email=Email)
        if customer.password == Password:
            request.session['userid'] = customer.cusid
            print("Customer valid")
            return render(request, 'index.html', {'userid': customer.cusid , 'userEmail' : customer.email})
        else:
            request.session['userid'] = None
            return redirect('login')
    else:
        adminExist = Admin.objects.filter(adminid=Email).exists()
        if adminExist == True:
            admin = Admin.objects.get(adminid=Email)
            if admin.password == Password:
                request.session['eid'] = admin.adminid
                print("admin valid")
                return render(request, 'Dashboard.html')
            else:
                request.session['userid'] = None
                return redirect('login')
    




   

            
    #     admin = auth.authenticate(adminid=Email, password = Password)
    #     print("add checked")
    #     if admin is not None:
    #     auth.login(request, admin)
        

    # print("function skiped")
    # return render(request, 'login.html')

# Signup function
def signUpVer(request):

    rand = generateRandomeNum() 


    custId = "CUS" + rand.fiveNums()
    print("custId" + custId)
    Email = request.POST['signEmail']
    Password = request.POST['signPW']
    ConPw = request.POST['signConfermPw']
    fname = request.POST['signFname']
    lname = request.POST['signLname']

    if ConPw != Password:
        return render(request, 'login.html')

    # elif Customer.objects.filter(email=Email).exists:
    #     return render(request, 'login.html')

    # elif Customer.objects.filter(cusid=custId).exists:
    #     return render(request, 'login.html')

    else:
        customer = Customer(cusid=custId, email=Email,
                            password=Password, f_name=fname, l_name=lname)
        customer.save()
        print("Saved Customer")
        return render(request, 'index.html')




def updateCus(request , id_cus):
    
    cus = Customer.objects.get(cus_index = id_cus)
    print(id_cus)
    cus.email = request.POST['Edit_Email']
    cus.cusnic = request.POST['Edit_Nic']
    cus.address_l1 = request.POST['AddressLineOne']
    cus.address_l2 = request.POST['Edit_AddLine2']
    cus.postcode = request.POST['Edit_PCode']
    cus.f_name = request.POST['Edit_Fname']
    cus.l_name = request.POST['Edit_Lname']
    uploaded_File = request.FILES['cusImg']
    cus.img = uploaded_File.name
    print(uploaded_File.name)
    print(uploaded_File.size)
    fs = FileSystemStorage()
    fs.save(uploaded_File.name , uploaded_File)



    cus.save()
    cus = Customer.objects.get(cusid=request.session['userid'])
    return render(request, 'User_profile.html', {'customer': cus, 'media_url': settings.MEDIA_URL})



def adduser(request):

    rand = generateRandomeNum()

    addEmpEID = "EMP" + rand.fiveNums()
    print("custId" + addEmpEID)

    addEmpFname = request.GET['addEmpFname']
    addEmpLname = request.GET['addEmpLname']
    addEmpNIC = request.GET['addEmpNIC']
    #addEmpMale = request.GET['addEmpMale']
    addEmpEmail = request.GET['addEmpEmail']

    addEmpPhone = request.GET['addEmpPhone']
    addEpLineOne = request.GET['addEpLineOne']
    addEpLineTwo = request.GET['addEpLineTwo']
    addEmpcity = request.GET['addEmpcity']
    addEmpPCode = request.GET['addEmpPCode']
    addempDateOfJoin = request.GET['addempDateOfJoin']
    addempSal = request.GET['addempSal']
    addempOTRate = request.GET['addempOTRate']

    employee = Employee(empid=addEmpEID, f_name=addEmpFname,
                        l_name=addEmpLname, empnic=addEmpNIC, gender='Male',    email=addEmpEmail, phone=addEmpPhone,
                        address_l1=addEpLineOne, address_l2=addEpLineTwo, postcode=addEmpPCode, reg_date=addempDateOfJoin, basic_sal=addempSal,
                        ot_rate=addempOTRate)
    employee.save()
    print("Saved Customer")
    emp = Employee.objects.all()
    return render(request, 'EmployeeList.html', {'employees': emp})





def fullemployee(request, id_emp):
    emp = Employee.objects.get(emp_index=id_emp)
    return render(request, 'ViewEmployee.html', {'employee': emp})


def editemp(request):

    #eid = request.GET['Edit_eid']
    addEmpFname = request.GET['Edit_E_Fname']
    addEmpLname = request.GET['Edit_E_Lname']
    addEmpNIC = request.GET['Edit_E_nic']
    #addEmpMale = request.GET['addEmpMale']
    addEmpEmail = request.GET['Edit_E_email']

    addEmpPhone = request.GET['Edit_E_phone']
    addEpLineOne = request.GET['Edit_E_assL1']
    addEpLineTwo = request.GET['Edit_E_assL2']
    addEmpcity = request.GET['Edit_E_city']
    addEmpPCode = request.GET['Edit_Epost_code']
    #addempDateOfJoin = request.GET['Edit_Appdate']
    addempSal = request.GET['Edit_Bsal']
    addempOTRate = request.GET['Edit_OTrate']

    employee = Employee(empid='EMP98245', f_name=addEmpFname,
                        l_name=addEmpLname, empnic=addEmpNIC, gender='Male',    email=addEmpEmail, phone=addEmpPhone,
                        address_l1=addEpLineOne, address_l2=addEpLineTwo, postcode=addEmpPCode, basic_sal=addempSal,
                        ot_rate=addempOTRate)

    return render(request, 'ViewEmployee.html', {'employee': employee})

def saveFoodItem(request):
    date = request.POST['date']
    dishName = request.POST['dishName']
    ing1id = request.POST['ing1id']
    ing1name = request.POST['ing1name']
    ing1qty = request.POST['ing1qty']
    ing1cost = request.POST['ing1cost']
    ing2id = request.POST['ing2id']
    ing2name = request.POST['ing2name']
    ing2qty = request.POST['ing2qty']
    ing2cost = request.POST['ing2cost']
    ing3id = request.POST['ing3id']
    ing3name = request.POST['ing3name']
    ing3qty = request.POST['ing3qty']
    ing3cost = request.POST['ing3cost']
    ing4id = request.POST['ing4id']
    ing4name = request.POST['ing4name']
    ing4qty = request.POST['ing4qty']
    ing4cost = request.POST['ing4cost']
    ing5id = request.POST['ing5id']
    ing5name = request.POST['ing5name']
    ing5qty = request.POST['ing5qty']
    ing5cost = request.POST['ing5cost']
    prep = request.POST['prep']
    gas = request.POST['gas']
    elec = request.POST['elec']
    water = request.POST['water']
    costmarg = request.POST['costmarg']
    totcost = request.POST['totcost']
    sprice = request.POST['sprice']
    netprof = request.POST['netprof']

    foodId = random_with_N_digits(9)

    fooditrm = foodItem(
        foodItemId = foodId,
        date = date,
        dishName = dishName,
        salesPrice = sprice,
        totalCost = totcost,
        costMargin = costmarg,
        netProfit = netprof
    )

    fooditrm.save()

    ingrid1 = ingrediants(
        ingId = ing1id,
        foodId = foodId,
        ingName = ing1name,
        qty = ing1qty,
        cost = ing1cost
    )
    ingrid1.save()

    ingrid2 = ingrediants(
        ingId = ing2id,
        foodId = foodId,
        ingName = ing2name,
        qty = ing2qty,
        cost = ing2cost
    )
    ingrid2.save()

    ingrid3 = ingrediants(
        ingId = ing3id,
        foodId = foodId,
        ingName = ing3name,
        qty = ing3qty,
        cost = ing3cost
    )
    ingrid3.save()

    ingrid4 = ingrediants(
        ingId = ing4id,
        foodId = foodId,
        ingName = ing4name,
        qty = ing4qty,
        cost = ing4cost
    )
    ingrid4.save()

    ingrid5 = ingrediants(
        ingId = ing5id,
        foodId = foodId,
        ingName = ing5name,
        qty = ing5qty,
        cost = ing5cost
    )
    ingrid5.save()

    utilct = utilCost(
        utilId = random_with_N_digits(9),
        foodId = foodId,
        preparations = prep,
        gas = gas,
        elec = elec,
        water = water,
        total = totcost
    )
    utilct.save()

    return render(request,"FoodProfitability.html")

