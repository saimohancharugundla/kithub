from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Inquiry

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        owner_email = request.POST['owner_mail']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_inquired = Inquiry.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_inquired:
                messages.error(request,'You have already made an inquiry for this book')
                return redirect('/listings/'+listing_id+'/')
            inquiries = Inquiry(listing_id=listing_id,user_id=user_id,name=name,email=email,phone=phone,message=message,listing=listing)
            inquiries.save()
            send_mail(
                'Inquiry for your'+listing,
                'You have an inquiry for'+listing+'. Checkout it!',
                'saimohancharugundla@gmail.com',
                [owner_email],
                fail_silently=False
            )
            messages.success(request,'Yay! Your Inquiry has been made. Owner may get back to you soon!')
            return redirect('/listings/'+listing_id+'/')
