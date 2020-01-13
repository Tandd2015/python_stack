from __future__ import unicode_literals
from django.db import models
from django.shortcuts import redirect
from django import forms
import datetime
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        birthday_count=0
        EMAIL_REGEX = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
        errors = {}
        if 'change' in postData and postData['change'] == 'register_' or postData['change'] == 'edit_':
            print('hi')
            if len(postData[f"{postData['change']}email_input"]) <= 1:
                errors[f"{postData['change']}email_input"]="Email address should is required"
            elif not EMAIL_REGEX.match(postData[f"{postData['change']}email_input"]):
                errors[f"{postData['change']}email_input"]="Email address is an invalid format"
            
            if len(postData[f"{postData['change']}first_name_input"]) <= 2:
                errors[f"{postData['change']}first_name_input"]="First name should be at least 2 characters"
            
            if len(postData[f"{postData['change']}last_name_input"]) <= 2:
                errors[f"{postData['change']}last_name_input"]="Last name should be at least 2 characters"
            
            if len(postData[f"{postData['change']}password_input"]) <= 7:
                errors[f"{postData['change']}password_input"]="Password must be at least 7 characters length"

            if len(postData[f"{postData['change']}password_con_input"]) <= 7:
                errors[f"{postData['change']}password_con_input"]="Password Conformation must be at least 7 characters length"
            
            if postData[f"{postData['change']}password_input"] != postData[f"{postData['change']}password_con_input"]:
                errors[f"{postData['change']}password_match"]="Password and Password Conformation must Match"
            
            if len(postData[f"{postData['change']}birthday_input"]) <= 0:
                errors[f"{postData['change']}birthday_input"]="Birthday Day Should not be at blank"
            elif len(postData[f"{postData['change']}birthday_input"]) == 8:
                num_string= ''
                year=0
                month=0
                day=0
                year_check= False
                month_check= False
                day_check= False
                now= datetime.datetime.now().strftime("%Y-%m-%d")
                for i in postData[f"{postData['change']}birthday_input"]:
                    if str.isdigit(i):
                        num_string+=i
                        if len(num_string) == 4:
                            year=num_string
                            num_string=''
                            year_check=True
                        if len(num_string) == 2 and year_check == True and month_check == False:
                            month=num_string
                            num_string=''
                            month_check=True
                        if len(num_string) == 2 and year_check == True and month_check == True:
                            day=num_string
                            num_string=''
                            day_check=True
                        if day_check == True:
                            now_num_string= ''
                            now_year=0
                            now_month=0
                            now_day=0
                            now_year_check= False
                            now_month_check= False
                            now_day_check= False
                            for n in now:
                                if str.isdigit(n):
                                    now_num_string+=n
                                    if len(now_num_string) == 4:
                                        now_year=now_num_string
                                        now_num_string=''
                                        now_year_check=True
                                    if len(now_num_string) == 2 and now_year_check == True and now_month_check == False:
                                        now_month=now_num_string
                                        now_num_string=''
                                        now_month_check=True
                                    if len(now_num_string) == 2 and now_year_check == True and now_month_check == True:
                                        now_day=now_num_string
                                        now_num_string=''
                                        now_day_check=True
                                    if now_day_check == True:
                                        pass
                                else:
                                    pass
                    else:
                        pass
                if year <= now_year:
                    if month <= now_month:
                        if day <= now_day:
                            pass
                        else:
                            errors[f"{postData['change']}birthday_input"]= 'This is a future date. Date must be not be after todays date.'
                    else:
                        errors[f"{postData['change']}birthday_input"]= 'This is a future date. Date must be not be after todays date.'    
                else:
                    errors[f"{postData['change']}birthday_input"]= 'This is a future date. Date must be not be after todays date.'
        elif 'change' in postData and postData['change'] == 'login_':
            all_users = User.objects.all()
            print('helllllllooooooo')
            if len(postData[f"{postData['change']}email_input"]) <= 1:
                errors[f"{postData['change']}email_input"]="Email address should is required"
            elif not EMAIL_REGEX.match(postData[f"{postData['change']}email_input"]):
                errors[f"{postData['change']}email_input"]="Email address is an invalid format"

            if len(postData[f"{postData['change']}password_input"]) <= 7:
                errors[f"{postData['change']}password_input"]="Password must be at least 7 characters length"
            else:
                for userz in all_users:
                    if postData[f"{postData['change']}email_input"] == userz.email_address and postData[f"{postData['change']}password_input"] == userz.password:
                        pass
                    elif postData[f"{postData['change']}email_input"] == userz.email_address and postData[f"{postData['change']}password_input"] != userz.password:
                        errors[f"{postData['change']}password_input"]="Password Does not match Users records"
                    else:
                        errors[f"{postData['change']}email_input"]="Email address does not belong to our database"
        elif 'change' in postData and postData['change'] == 'quoter_':
            if len(postData[f"{postData['change']}author_name_input"]) <= 3:
                errors[f"{postData['change']}author_name_input"]="Author name should be at least 3 characters"
            
            if len(postData[f"{postData['change']}quote_input"]) <= 10:
                errors[f"{postData['change']}quote_input"]="Quotes must be at least 10 characters length"
        elif 'change' in postData and postData['change'] == 'liker_':
            p = Like.objects.last()
            # p.likers_quote_id
            # print(p.likers_user_id_id)
            # for like in all_likes: 
                # print(like.likers_quote_id.quote_message,'message') 
                # print(like.likers_quote_id.id,'id') 
                # print(like.one_like_check,'check')
                # print(like.likers_quote_id.users_quote_id_id)
                # print(like.likers_quote_id.users_quote_id_id)
                # if p.likers_quote_id.id == like.likers_quote_id.id:
                    # print(p.likers_quote_id.id ,"and so it begins",like.likers_quote_id.id)
        return errors
class User(models.Model):
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255)
    birthday = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now().strftime("%m-%d-%Y"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Quote(models.Model):
    quote_message = models.TextField(default="No Quote")
    #users_who_liked                                       #all_quotes
    users_quote_id = models.ForeignKey(User, related_name="quotes_id", default=0)
    author_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Like(models.Model):
    likers_quote_id = models.ForeignKey(Quote, related_name="likes_id")
    likers_user_id = models.ForeignKey(User, related_name="users_like_id", default=0)
    likers_check= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()