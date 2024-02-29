from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import*

# Create your views here.
def index(request):
    return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')  # Replace 'home' with your desired redirect URL after login
        else:
            # Invalid login credentials
            messages.error(request, "Invalid email or password.")
            return redirect('login')  # Replace 'login' with your login URL name

    else:
        return render(request, 'login.html')
       

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone_no = request.POST['phone_no']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validate password
        try:
            validate_password(password)
        except ValidationError as e:
            messages.error(request, " ".join(e.messages))
            return redirect('signup')

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')
        
        # Password validation passed, create user
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password)
        user.save()

        # Create associated Customer object
        Customer.objects.create(user=user, phone_no=phone_no) 

        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('login')
    else:
        return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')
def products(request):
    return render(request, 'products.html')