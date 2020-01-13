from __future__ import unicode_literals
from django.db import models
from django import forms
import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if 'change' in postData:
            if len(postData[f"{postData['change']}title_input"]) <= 1:
                errors[f"{postData['change']}title_input"]="Title Should be at least 2 characters"
            if len(postData[f"{postData['change']}network_input"]) <= 2:
                errors[f"{postData['change']}network_input"]="Network Should be at least 3 characters"
            if len(postData[f"{postData['change']}release_date_input"]) <= 0:
                errors[f"{postData['change']}release_date_input"]="Release Date Should not be at blank"
            elif len(postData[f"{postData['change']}release_date_input"]) > 0:
                num_string= ''
                year=0
                month=0
                day=0
                year_check= False
                month_check= False
                day_check= False
                now= datetime.datetime.now().strftime("%Y-%m-%d")
                for i in postData[f"{postData['change']}release_date_input"]:
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
                            errors[f"{postData['change']}release_date_input"]= 'This is a future date. Date must be not be after todays date.'
                    else:
                        errors[f"{postData['change']}release_date_input"]= 'This is a future date. Date must be not be after todays date.'    
                else:
                    errors[f"{postData['change']}release_date_input"]= 'This is a future date. Date must be not be after todays date.'
            if len(postData[f"{postData['change']}description_input"]) <= 9:
                errors[f"{postData['change']}description_input"]="Description Should be at least 10 characters"
        return errors



# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    changezz = models.CharField(max_length=255)
    descript = models.TextField()
    rel_date = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now().strftime("%m/%d/%Y"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
