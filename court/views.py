from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from .models import *
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from court.forms import *
from court.models import *



def login_user(request):
	if request.user.is_authenticated:
		print("Logged in")
		return redirect("/userdash/")
	else:
		print("Not logged in")

	if request.method == 'POST':
		form = loginform(request.POST)
		if form.is_valid():
			username = request.POST.get('Username')
			print(username)
			password = request.POST.get('Password')
			print(password)
			user = authenticate(username=username, password=password)
			if user:
				print("yesssssssssssssssss")
				login(request,user)
				return redirect("/userdash/")

	else:
		form = loginform()
		print("not")
	return render(request, 'signin.html', {"form": form})



@login_required
def user_logout(request):
	logout(request)
	return redirect('/signin/')

from django.shortcuts import get_list_or_404, get_object_or_404
# def inputform(request):
#     alldata = CaseType.objects.all()
	
#     check =[]
#     for types in alldata:
#         check.append(types.Casetypes)
#     # ff = request.POST['item_id']
#     # print(ff)

#     # data=['CWP','CRM-M','COCP']
#     # for i in data:
#     #     print(i)
#     #     # f=formDetails(Casetypes=i)
#     #     # f.save()
#     return render(request, 'inputform.html',{'alldata':check})
from django.conf import settings

def inputform(request):
	alldata = CaseType.objects.all()
	Year_ = Year.objects.all()
	InternelCategory_ = InternelCategory.objects.all()
	alldprt = Department.objects.all()
	Commission = Commissions.objects.all()
	Constituional = ConstituionalBodies.objects.all()
	Boardsand = BoardsandCorporations.objects.all()
	if request.method == 'POST':
		Caset_ypes = get_object_or_404(alldata, Casetypes=request.POST.get('item_id'))
		case_number = request.POST['Case_Number']
		Years_id_ypes = get_object_or_404(Year_, Years=request.POST.get('Years_id'))
		InternelCategorys = get_object_or_404(InternelCategory_, InternelCategorya=request.POST.get('category_id'))

		Internal_Custom = request.POST['Internal_Category_Custom']
		dprtmnt = get_object_or_404(alldprt, Departmens=request.POST.get('alldprts_id'))

		Commission_ids = request.POST['Commission_id']
		Constituional_id = request.POST['Constituional_id']
		Boardsand_id = request.POST['Boardsand_id']
		Post = request.POST['Post']
		Advertisement = request.POST['Advertisement']
		Cat = request.POST['Cat']
		status = request.POST['final_status']
		addfilecopy = request.FILES['Cop_Final_Reply']
		prayer = request.POST['Prayer']
		Issue_Involved = request.POST['Issue_Involved']
		Law_Officer = request.POST['Law_Officer_conducting']
		Next_Date = request.POST['Next_Date']
		Others = request.FILES['Others']
		last = request.FILES["docfile"]
	
		

		idss = str(Caset_ypes)+'-'+str(case_number)+'-'+str(Years_id_ypes)
		profile = userinfo(userid=idss,casetype=Caset_ypes,caseNo=case_number,year_value=Years_id_ypes,InternelCategorys=InternelCategorys,
			InternelCustom=Internal_Custom,dprtmnt=dprtmnt,commis=Commission_ids,bodies=Constituional_id,Boards=Boardsand_id
			,post=Post,Advertisements_year=Advertisement,cat=Cat,status=status,copy=addfilecopy,prayer=prayer,issue=Issue_Involved,
			law=Law_Officer,nextdate=Next_Date,lastorder=last)
		profile.save()   


		fs = FileSystemStorage()
		filename = fs.save(addfilecopy.name,addfilecopy)
		filename = fs.save(Others.name,Others)
		obj = othersdoc.objects.create(
		userid =  userinfo.objects.get(userid=idss),
		othersodcs = Others,
		copy = addfilecopy,
		lastorder = last )

	return render(request, 'inputform.html', {'alldata':alldata,'Years':Year_,'InternelCategory':InternelCategory_
		,'alldprts':alldprt,'Commission_':Commission,'Constituional':Constituional,'Boardsand':Boardsand})

def readfile(request):
	import pandas as pd

	df = pd.read_excel (r'list of departmetns (1).xlsx')
	ss = df['Home Department']
	for ee in ss:
		print(ee)
		sw = Department(Departmens=ee)
		# sw.save()
	return HttpResponse("ffsdghfsg")


def Otherfile(request):
	import pandas as pd
	if request.method == 'POST':
		otherdocu = request.FILES["otherfile"]
		userid = 'COCP-dssa-2017' 
		fs = FileSystemStorage()
		filename = fs.save(otherdocu.name,otherdocu)
		obj = othersdoc.objects.create(
		userid =  userinfo.objects.get(userid=userid),
		othersodcs = otherdocu)
	return render(request, 'other.html')