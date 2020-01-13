from __future__ import unicode_literals
from django.db import models
from django.shortcuts import redirect
from django import forms
import datetime
import re

class AddressManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if 'change' in postData and postData['change'] == 'register_':
            if len(postData[f"{postData['change']}house_apt_input"]) <= 0:
                errors[f"{postData['change']}house_apt_input"]="House/Apt # field should not be blank."

            if len(postData[f"{postData['change']}street_address_input"]) <= 0:
                errors[f"{postData['change']}street_address_input"]="Street Address field should not be blank."
            
            if len(postData[f"{postData['change']}city_input"]) <= 0:
                errors[f"{postData['change']}city_input"]="City field should not be blank."
            
            if len(postData[f"{postData['change']}state_province_input"]) <= 0:
                errors[f"{postData['change']}state_province_input"]="State/Province field should not be blank."
            
            if len(postData[f"{postData['change']}zipcode_input"]) <= 0:
                errors[f"{postData['change']}zipcode_input"]="Zip Code field should not be blank."

            if len(postData[f"{postData['change']}country_input"]) <= 0:
                errors[f"{postData['change']}country_input"]="Country field should not be blank."

class UserManager(models.Manager):
    def basic_validator(self, postData):
        birthday_count=0
        EMAIL_REGEX = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
        errors = {}
        if 'change' in postData and postData['change'] == 'register_':
            print('hi')
            if len(postData[f"{postData['change']}email_input"]) <= 0:
                errors[f"{postData['change']}email_input"]="Email addressfield should not be blank."
            elif not EMAIL_REGEX.match(postData[f"{postData['change']}email_input"]):
                errors[f"{postData['change']}email_input"]="Email address is an invalid format"
            
            if len(postData[f"{postData['change']}username_input"]) <= 0:
                errors[f"{postData['change']}username_input"]="Username field should not be blank."
            
            if len(postData[f"{postData['change']}first_name_input"]) <= 0:
                errors[f"{postData['change']}first_name_input"]="First name field should not be blank."
            
            if len(postData[f"{postData['change']}last_name_input"]) <= 0:
                errors[f"{postData['change']}last_name_input"]="Last name field should not be blank."
            
            if len(postData[f"{postData['change']}password_input"]) <= 0:
                errors[f"{postData['change']}password_input"]="Password field should not be blank."

            if len(postData[f"{postData['change']}password_con_input"]) <= 0:
                errors[f"{postData['change']}password_con_input"]="Password Conformation field should not be blank."
            
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
            if len(postData[f"{postData['change']}email_input"]) <= 0:
                errors[f"{postData['change']}email_input"]="Email address field should not be blank."
            elif not EMAIL_REGEX.match(postData[f"{postData['change']}email_input"]):
                errors[f"{postData['change']}email_input"]="Email address is an invalid format."
                        
            if len(postData[f"{postData['change']}username_input"]) <= 0:
                errors[f"{postData['change']}username_input"]="Username field should not be blank."

            if len(postData[f"{postData['change']}password_input"]) <= 0:
                errors[f"{postData['change']}password_input"]="Password field should not be blank"
            else:
                for userz in all_users:
                    if postData[f"{postData['change']}email_input"] == userz.email_address and postData[f"{postData['change']}password_input"] == userz.password:
                        pass
                    elif postData[f"{postData['change']}email_input"] == userz.email_address and postData[f"{postData['change']}password_input"] != userz.password:
                        errors[f"{postData['change']}password_input"]="Password Does not match Users records"
                    else:
                        errors[f"{postData['change']}email_input"]="Email address does not belong to our database"
        return errors

class Address(models.Model):
    street_number = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    user_level = models.IntegerField(default=1, auto_created=True)
    email_address = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    u_address_id = models.ForeignKey(Address, related_name='u_user_id')
    phone_number = models.IntegerField()
    profile_description = models.TextField(default='', auto_created=True)
    birthdate = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now().strftime("%m-%d-%Y"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Artist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shop(models.Model):
    s_address_object = models.ForeignKey(Address, related_name='s_ad_shop_object')
    s_artist_object = models.ForeignKey(Artist, related_name='s_ar_shop_object')
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    m_user_object = models.ForeignKey(User, related_name='m_message_object')
    m_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TattooPost(models.Model):
    t_user_object = models.ForeignKey(User, related_name='t_u_tattoo_post_object')
    t_artist_object = models.ForeignKey(Artist, related_name='t_a_tattoo_post_object')    
    t_title = models.CharField(max_length=255)
    t_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    c_user_object = models.ForeignKey(User, related_name='c_u_comment_object')
    c_message_object = models.ForeignKey(Message, related_name='c_m_comment_object', null=True, blank=True)
    c_tattoo_post_object = models.ForeignKey(TattooPost, related_name='c_t_p_comment_object', null=True, blank=True)
    c_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FileImage(models.Model):
    f_tattoo_post_object = models.ForeignKey(Artist, related_name='f_file_image_object')
    tattoo_image = models.ImageField(upload_to='static/img/', default='static/img/no-img.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)