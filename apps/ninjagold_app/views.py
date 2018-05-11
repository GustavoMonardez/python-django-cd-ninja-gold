from django.shortcuts import render, HttpResponse, redirect
from time import strftime, gmtime
import datetime
import random

def index(request):
    if not "gold" in request.session:
        request.session["gold"] = 0    
    return render(request, "ninjagold_app/index.html")

def process(request,building):
    if building == "farm":
        request.session["building"] = "farm"
        request.session["play"] = random.randrange(10,20)
        request.session["gold"] +=  request.session["play"]
    elif building == "cave":
        request.session["building"] = "cave"
        request.session["play"] = random.randrange(5,10)
        request.session["gold"] +=  request.session["play"]
    elif building == "house":
        request.session["building"] = "house"
        request.session["play"] = random.randrange(2,5)
        request.session["gold"] +=  request.session["play"]
    elif building == "casino":
        request.session["building"] = "casino"
        request.session["play"] = random.randrange(-50,50)
        request.session["gold"] +=  request.session["play"]
    # time
    time = datetime.datetime.now()    
    time = time.strftime("%I:%M %p, %b %d %Y")
    # packaging
    activity = {}
    if request.session["play"] < 0:
        activity = {"content":"Entered a casino and lost "+str(abs(request.session["play"]))+" golds...Ouch ("+time+")",
        "class":"red"}
    else:
         activity = {"content":"Earned "+str(request.session["play"])+" golds from the "+ building + "! ("+time+")",
        "class":"green"}
    if not "activities" in request.session:
        temp = [activity]
        request.session["activities"] = temp
    else:
        temp = request.session["activities"]
        temp.append(activity)
        request.session["activities"] = temp

    return redirect("/")

def reset(request):
    request.session.flush()
    return redirect("/")