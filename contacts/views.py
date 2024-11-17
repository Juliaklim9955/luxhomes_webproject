from django.shortcuts import render, redirect 
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Contact
from django.core.mail import send_mail


# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        flat_id = request.POST['flat_id']
        flat_title = request.POST['flat_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        question = request.POST['question']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        contact = Contact(flat_id=flat_id, flat_title=flat_title, user_id=user_id, first_name=first_name,
                          last_name=last_name, question=question, city=city, state=state, email=email, phone=phone, 
                          message=message)
        
        ### put all uner # later
        #fetch admin's email:

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email 
        
        #send_mail(
                    #"Subject here",
                    #"Here is the message.",
                    #from email:
                    #"example_from_email@gmail.com",
                    # to email - superuser email:
                    #[admin_email],
                    #fail_silently=False,
                #)
        contact.save()
        messages.success(request, 'You request has been submitted, we will get back to you shortly')
        return redirect('/'+flat_id)


     
