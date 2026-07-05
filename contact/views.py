from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import ContactMessage

def contact_combined(request):
    """
    Simple view that saves contact messages to database
    Supports both normal POST and AJAX POST
    """
    if request.method == 'POST':
        # Get form data
        fullname = request.POST.get('fullname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
        # Validation
        if not fullname or not email or not subject or not message:
            error_msg = 'Please fill all required fields (*)'
            
            # Check if AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'message': error_msg
                }, status=400)
            else:
                messages.error(request, error_msg)
                return redirect('contact:contact')
        
        # Save to database
        ContactMessage.objects.create(
            name=fullname,
            email=email,
            phone=phone or '',
            subject=subject,
            message=message
        )
        
        success_msg = f'Thank you {fullname}! Your message has been received. We will contact you soon.'
        
        # Check if AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': success_msg
            })
        else:
            messages.success(request, success_msg)
            return redirect('contact:contact')
    
    # GET request - show the form
    return render(request, 'contact/contact.html')