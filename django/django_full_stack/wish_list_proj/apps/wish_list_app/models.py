from django.db import models
import datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if 'change' in postData and postData['change'] == 'register_': 
            if len(postData[f"{postData['change']}name_input"]) <= 3:
                errors[f"{postData['change']}name_input"]="name should be at least 3 characters"
            
            if len(postData[f"{postData['change']}username_input"]) <= 3:
                errors[f"{postData['change']}username_input"]="username should be at least 3 characters"
            
            if len(postData[f"{postData['change']}password_input"]) <= 10:
                errors[f"{postData['change']}password_input"]="Password must be at least 10 characters length"

            if len(postData[f"{postData['change']}password_con_input"]) <= 10:
                errors[f"{postData['change']}password_con_input"]="Password Conformation must be at least 10 characters length"
            
            if postData[f"{postData['change']}password_input"] != postData[f"{postData['change']}password_con_input"]:
                errors[f"{postData['change']}password_match"]="Password and Password Conformation must Match"
        elif 'change' in postData and postData['change'] == 'login_':
            all_users = User.objects.all()
            if len(postData[f"{postData['change']}username_input"]) <= 3:
                errors[f"{postData['change']}username_input"]="username should be at least 3 characters"
            
            if len(postData[f"{postData['change']}password_input"]) <= 10:
                errors[f"{postData['change']}password_input"]="Password must be at least 10 characters length"
            else:
                for userz in all_users:
                    if postData[f"{postData['change']}username_input"] == userz.username and postData[f"{postData['change']}password_input"] == userz.password:
                        pass
                    elif postData[f"{postData['change']}username_input"] == userz.username and postData[f"{postData['change']}password_input"] != userz.password:
                        errors[f"{postData['change']}password_input"]="Password Does not match Users records"
                    else:
                        errors[f"{postData['change']}username_input"]="username does not belong to our database"   
        elif 'change' in postData and postData['change'] == 'product_':
            if len(postData[f"{postData['change']}item_input"]) <= 3:
                errors[f"{postData['change']}item_input"]="username should be at least 3 characters"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255) 
    username  = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hireday = models.DateTimeField(auto_now_add=False, default=datetime.datetime.now().strftime("%m-%d-%Y"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Item(models.Model):
    name = models.CharField(max_length=255)
    items_list_object = models.ForeignKey(User, related_name='users_list_object', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()