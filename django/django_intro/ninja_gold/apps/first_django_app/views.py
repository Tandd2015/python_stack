from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import random
import datetime
# Create your views here.
def index(request):
    if 'loop' not in request.session:
        request.session['loop']= []
    else:
        request.session['loop']= request.session['loop']

    if 'log_holder' not in request.session:
        request.session['log_holder']=[]
    else:
        request.session['log_holder']= request.session['log_holder']

    if 'color_holder' not in request.session:
        request.session['color_holder']=[]
    else:
        request.session['color_holder']=request.session['color_holder']

    if 'win_lose' not in request.session:
        request.session['win_lose']= False
    else:
        request.session['win_lose']= request.session['win_lose']

    return render(request, 'first_django_app/index.html')

def function_one(request):
    request.session.clear()
    return redirect('/')

def function_two(request):
    if request.method == "GET":
        request.session.pop('count')
        for i in range(15,-1,-1):
            new1= '%s%d' % ('log', i)
            new2= '%s%d' % ('color', i)
            request.session.pop(new1, None)
            request.session.pop(new2, None)
        request.session.pop('count')
        request.session['count'] = 0
        request.session['log%s'%request.session['count']] = request.session['log']
        request.session.pop('log_holder')
        request.session.pop('color_holder')
        request.session['log_holder'] = []
        request.session['color_holder'] = []
        request.session.pop('sumGold')
        request.session['sumGold']= 0
        if request.session['count'] == 0 and 'moreGold' not in request.session:
            if request.session['sumGold'] >= 0:
                request.session['color%s' % request.session['count']] = "text-success"
            else:
                request.session['color%s' % request.session['count']] = "text-danger"
        else:
            if request.session['moreGold'] >= 0:
                request.session['color%s' % request.session['count']] = "text-success"
            else:
                request.session['color%s' % request.session['count']] = "text-danger"
        request.session.update()
    print('hello')
    return redirect('/')

def function_three(request):
    if request.method == 'POST':
        request.session['win_lose'] = False
        if request.POST['action'] == 'farm':
            request.session['value'] = "farm"
            request.session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")

            if 'sumGold' not in request.session:
                request.session['sumGold'] = random.randrange(10, 21)
                request.session['log'] = f"Earned {request.session['sumGold']} golds from the {request.session['value']}! ({request.session['daTime']})"
            else:
                request.session['moreGold'] = random.randrange(10, 21)
                request.session['sumGold'] += request.session['moreGold']
                request.session['log'] = f"Earned {request.session['moreGold']} golds from the {request.session['value']}! ({request.session['daTime']})"

            if 'count' not in request.session:
                request.session['count'] = 0
                request.session['log%s' % request.session['count']] = request.session['log']
                request.session['color%s' % request.session['count']]= "text-success"
                request.session['color_holder'].append(request.session['color%s' % request.session['count']])
                request.session['log_holder'].append(request.session['log%s' % request.session['count']])
            elif request.session['count'] > 14 and request.session['sumGold'] < 499:
                request.session['end_color']= "text-danger"
                request.session['win_lose'] = True
                messages.add_message(request, messages.ERROR, "You Lost. Try Again")
                redirect('/')
            elif request.session['count'] <= 15 and request.session['sumGold'] > 499:
                request.session['end_color']= "text-success"
                request.session['win_lose'] = True
                function_two(request) 
                messages.add_message(request, messages.ERROR, "You Win. Try Again")    
            else:
                request.session['count'] += 1
                request.session['color%s' % request.session['count']]= "text-success"
                request.session['log%s' % request.session['count']] = request.session['log']
                request.session['color_holder'].append(request.session['color%s' % request.session['count']])
                request.session['log_holder'].append(request.session['log%s' % request.session['count']])           
            print(request.session['log_holder'])
            print(request.session['color_holder'])
            print(request.session['count'])
            print(request.session['win_lose'])
        
        elif request.POST['action'] == 'cave':
            request.session['value'] = "cave"
            request.session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
            
            if 'sumGold' not in request.session:
                request.session['sumGold'] = random.randint(5, 11)
                request.session['log'] = f"Earned {request.session['sumGold']} golds from the {request.session['value']}! ({request.session['daTime']})"
            else:
                request.session['moreGold'] = random.randint(5, 11)
                request.session['sumGold'] += request.session['moreGold']
                request.session['log'] = f"Earned {request.session['moreGold']} golds from the {request.session['value']}! ({request.session['daTime']})"

            if 'count' not in request.session:
                request.session['count'] = 0
                request.session['log%s' % request.session['count']] = request.session['log']
                request.session['color%s' % request.session['count']]= "text-success"
                request.session['color_holder'].append(request.session['color%s' % request.session['count']])
                request.session['log_holder'].append(request.session['log%s' % request.session['count']])
            elif request.session['count'] > 14 and request.session['sumGold'] < 499:
                request.session['end_color']= "text-danger"
                request.session['win_lose'] = True
                messages.add_message(request, messages.ERROR, "You Lost. Try Again")
                function_two(request)
            elif request.session['count'] <= 15 and request.session['sumGold'] > 499:
                request.session['end_color']= "text-success"
                request.session['win_lose'] = True
                function_two(request) 
                messages.add_message(request, messages.ERROR, "You Win. Try Again")    
            else:
                request.session['count'] += 1
                request.session['color%s' % request.session['count']]= "text-success"
                request.session['log%s' % request.session['count']] = request.session['log']
                request.session['color_holder'].append(request.session['color%s' % request.session['count']])
                request.session['log_holder'].append(request.session['log%s' % request.session['count']])     
            print(request.session['log_holder'])
            print(request.session['color_holder'])
            print(request.session['count'])
            print(request.session['win_lose'])
        
        elif request.POST['action'] == 'house':
            
            request.session['value'] = "house"
            request.session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
            
            if 'sumGold' not in request.session:
                request.session['sumGold'] = random.randint(2, 6)
                request.session['log'] = f"Earned {request.session['sumGold']} golds from the {request.session['value']}! ({request.session['daTime']})"
            else:
                request.session['moreGold'] = random.randint(2, 6)
                request.session['sumGold'] += request.session['moreGold']
                request.session['log'] = f"Earned {request.session['moreGold']} golds from the {request.session['value']}! ({request.session['daTime']})"
            
            if 'count' not in request.session:
                request.session['count'] = 0
                request.session['log%s' % request.session['count']] = request.session['log']
                request.session['color%s' % request.session['count']]= "text-success"
                request.session['color_holder'].append(request.session['color%s' % request.session['count']])
                request.session['log_holder'].append(request.session['log%s' % request.session['count']])
            elif request.session['count'] > 14 and request.session['sumGold'] < 499:
                request.session['end_color']= "text-danger"
                request.session['win_lose'] = True
                messages.add_message(request, messages.ERROR, "You Lost. Try Again")
                function_two(request)
            elif request.session['count'] <= 15 and request.session['sumGold'] > 499:
                request.session['end_color']= "text-success"
                request.session['win_lose'] = True
                function_two(request) 
                messages.add_message(request, messages.ERROR, "You Win. Try Again")    
            else:
                request.session['count'] += 1
                request.session['color%s' % request.session['count']]= "text-success"
                request.session['log%s' % request.session['count']] = request.session['log']
                request.session['color_holder'].append(request.session['color%s' % request.session['count']])
                request.session['log_holder'].append(request.session['log%s' % request.session['count']])           
            print(request.session['log_holder'])
            print(request.session['color_holder'])
            print(request.session['count'])
            print(request.session['win_lose'])
        
        else:
            request.session['value'] = "casino"
            request.session['daTime'] = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
            
            if 'sumGold' not in request.session:
                request.session['sumGold'] = random.randint(-50, 51)
            
                if request.session['sumGold'] >= 0:
                    request.session['log'] = f"Earned {request.session['sumGold']} golds from the {request.session['value']}! ({request.session['daTime']})"
                else: 
                    request.session['log'] = f"Entered a {request.session['value']} and lost {request.session['sumGold']} golds... Ouch.. ({request.session['daTime']})"
            else:
                request.session['moreGold'] = random.randint(-50, 51)
                request.session['sumGold'] += request.session['moreGold']
                if request.session['moreGold'] >= 0:
                    request.session['log'] = f"Earned {request.session['moreGold']} golds from the {request.session['value']}! ({request.session['daTime']})"
                else: 
                    request.session['log'] = f"Entered a {request.session['value']} and lost {request.session['moreGold']} golds... Ouch.. ({request.session['daTime']})"

            if 'count' not in request.session:
                request.session['count'] = 0
                request.session['log%s' % request.session['count']] = request.session['log']
                request.session['color%s' % request.session['count']]= "text-success"
                request.session['color_holder'].append(request.session['color%s' % request.session['count']])
                request.session['log_holder'].append(request.session['log%s' % request.session['count']])
            elif request.session['count'] > 14 and request.session['sumGold'] < 499:
                request.session['end_color']= "text-danger"
                request.session['win_lose'] = True
                messages.add_message(request, messages.ERROR, "You Lost. Try Again")
                function_two(request)
            elif request.session['count'] <= 15 and request.session['sumGold'] > 499:
                request.session['win_lose'] = True
                function_two(request) 
                messages.add_message(request, messages.ERROR, "You Win. Try Again")    
            else:
                request.session['count'] += 1
                if request.session['count'] == 0 and 'moreGold' not in request.session:
                    if request.session['sumGold'] >= 0:
                        request.session['color%s' % request.session['count']] = "text-success"
                    else:
                        request.session['color%s' % request.session['count']] = "text-danger"
                else:
                    if request.session['moreGold'] >= 0:
                        request.session['color%s' % request.session['count']] = "text-success"
                    else:
                        request.session['color%s' % request.session['count']] = "text-danger"
                request.session['log%s' % request.session['count']] = request.session['log']
                request.session['color_holder'].append(request.session['color%s' % request.session['count']])
                request.session['log_holder'].append(request.session['log%s' % request.session['count']])
                # elif session['count'] <= 15 and session['sumGold'] > 499:
                #     function_two("log", "color") 
                #     messages.add_message(request, messages.ERROR, "You Win. Try Again")               
                print(request.session['log_holder'])
                print(request.session['color_holder'])
                print(request.session['count'])
                print(request.session['win_lose'])
                print(request.POST)
                print(request.POST['action'])
    return redirect('/')
