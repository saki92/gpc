from django.http import HttpResponse
from django.template import loader
import datetime
from django.shortcuts import render_to_response

def ip(request):
	return render_to_response('gpa.html')

def calc(request):
	global final
	final=[]	
	t="hi all"
	global lis
	lis=[{'sem':'1','dep':'ece','sub':'english','credit':'4'},\
             {'sem':'1','dep':'ece','sub':'maths','credit':'4'},\
             {'sem':'1','dep':'ece','sub':'physics','credit':'3'},\
	     {'sem':'1','dep':'ece','sub':'chemistry','credit':'3'},\
	     {'sem':'1','dep':'ece','sub':'Engneering-graphics','credit':'5'},\
	     {'sem':'1','dep':'ece','sub':'FOC','credit':'3'},\
	     {'sem':'1','dep':'ece','sub':'computer-lab','credit':'2'},\
	     {'sem':'1','dep':'ece','sub':'engneering-lab','credit':'2'},\
	     {'sem':'2','dep':'ece','sub':'english2','credit':'4'},\
	     {'sem':'2','dep':'ece','sub':'maths2','credit':'4'},\
	     {'sem':'2','dep':'ece','sub':'physics2','credit':'3'},\
	     {'sem':'2','dep':'ece','sub':'chemistry2','credit':'3'},\
	     {'sem':'2','dep':'ece','sub':'EDC','credit':'4'},\
	     {'sem':'2','dep':'ece','sub':'BCM','credit':'4'},\
	     {'sem':'2','dep':'ece','sub':'EDC-lab','credit':'2'},\
	     {'sem':'2','dep':'ece','sub':'physics-lab','credit':'2'},\
	     {'sem':'2','dep':'ece','sub':'chemistry-lab','credit':'2'},\
	     {'sem':'1','dep':'it','sub':'english','credit':'4'},\
	     {'sem':'1','dep':'it','sub':'maths','credit':'4'},\
	     {'sem':'1','dep':'it','sub':'physics','credit':'3'},\
	     {'sem':'1','dep':'it','sub':'chemistry','credit':'3'},\
	     {'sem':'1','dep':'it','sub':'engneering-drawing','credit':'5'},\
	     {'sem':'1','dep':'it','sub':'FOC','credit':'3'},\
	     {'sem':'1','dep':'it','sub':'engneering-lab','credit':'2'},\
	     {'sem':'1','dep':'it','sub':'computer-lab','credit':'2'},\
	     {'sem':'2','dep':'it','sub':'english2','credit':'4'},\
	     {'sem':'2','dep':'it','sub':'maths2','credit':'4'},\
	     {'sem':'2','dep':'it','sub':'physics2','credit':'3'},\
	     {'sem':'2','dep':'it','sub':'chemistry2','credit':'3'},\
	     {'sem':'2','dep':'it','sub':'EDC','credit':'4'},\
	     {'sem':'2','dep':'it','sub':'bcm','credit':'4'},\
	     {'sem':'2','dep':'it','sub':'phy-lab','credit':'2'},\
	     {'sem':'2','dep':'it','sub':'chem-lab','credit':'2'},\
	     {'sem':'2','dep':'it','sub':'edc-lab','credit':'2'}]
	if 'sem' and 'dep' in request.GET:
		sem=request.GET['sem']
		dep=request.GET['dep']
		for l in lis:
			if l['sem']==sem and l['dep']==dep:
				final.append(l)
	return render_to_response('table.html',{'list':final})


def value(request): 
	j=0
	i=0
	lis=['s','a','b','c','d','e','u']
	dic={'s':10,'a':9,'b':8,'c':7,'d':6,'e':5,'u':0}
	for d in final:
		a=d['sub']
		c=d['credit']
		c=float(c)
		s=c+j
		j=s
		if a in request.GET:
			grade=request.GET[a]
			if grade in lis:
				g=dic[grade]
				g=float(g)
				p=c*g
				t=p+i
				i=t
				pr=t/s
				gpa=float(pr)
				gpa="%.2f"%gpa
			else:
				gpa="Enter a proper Grade for %s"%a
				break
	gpa=float(gpa)	
	if gpa>9.00:
		cmt="Get lost Nerd!"
	else:
		cmt=""
	return render_to_response('final.html',{'lst':gpa,'cmt':cmt})	
