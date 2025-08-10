from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def onboarding(request):
    if request.method == 'POST':
        # Collect form data
        category = request.POST.get('category')
        service = request.POST.get('service')
        service_description = request.POST.get('service_description')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Construct email message
        full_message = (
            f"Category: {category}\n"
            f"Service: {service}\n"
            f"Service Description: {service_description}\n"
            f"Email: {email}\n"
            f"Phone: {phone}"
        )

        # Send email
        send_mail(
            subject="New Onboarding Submission",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        messages.success(request, "Thank you for completing the onboarding! We will be in touch soon.")
        return redirect('home')
    return render(request, 'onboarding.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Construct the message
        full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

        # Send email
        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        messages.success(request, "Thank you for contacting us! We will get back to you soon.")
        return render(request, 'contact.html')
    
    return render(request, 'contact.html')
