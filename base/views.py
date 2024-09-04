from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm

def home(request):
    success_message = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            email_message = EmailMessage(
                subject=f"Form Submission: {subject} from {name}",
                body=message,
                from_email="form-response@example.com",
                to=["test.mailtrap1234@gmail.com"],
                reply_to=[email]
            )
            try:
                print("Attempting to send email...")
                email_message.send()
                print("Email sent successfully!")
                success_message = "Your message has been sent successfully!"
            except Exception as e:
                print(f"Failed to send email: {e}")
                success_message = "There was an error sending your message. Please try again later."
    else:
        form = ContactForm()

    return render(request, 'base/home.html', {'form': form, 'success_message': success_message})

def projects(request):
    return render(request, 'base/projects.html')

def brandguide(request):
    return render(request, 'base/brand-guide.html')

def bobabar(request):
    return render(request, 'base/boba-bar.html')

def campsitecompanions(request):
    return render(request, 'base/campsite-companions.html')

def communicationscertificate(request):
    return render(request, 'base/communications-certificate.html')

def potterycompanyrebrand(request):
    return render(request, 'base/pottery-company-rebrand.html')

def crochet(request):
    return render(request, 'base/crochet-project.html')

def imagesources(request):
    return render(request, 'base/image-sources.html')

def bobabarlandingpage(request):
    return render(request, 'base/boba-bar-landing-page.html')

def campsitecompanionslandingpage(request):
    return render(request, 'base/campsite-companions-landing-page.html')

# custom 404
def custom_404(request, exception):
    return render(request, '404.html', status=404)