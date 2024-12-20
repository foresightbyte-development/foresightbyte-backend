from accounts.models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import View
from django.http import JsonResponse


# Create your views here.

from firebase_admin import auth, firestore
# Initialize Firestore
from demo.settings import db

from django.contrib.auth import logout

def registration(request):
    if request.method == 'POST':
        try:
            # Extract user details from POST request
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']

            # Create the user in Firebase Authentication
            user = auth.create_user(
                email=email,
                password=password,
                display_name=name
            )

            # Store additional user details in Firestore
            db.collection('users').document(user.uid).set({
                'name': name,
                'email': email,
                'uid': user.uid,
            })

            # Send a success response
            return redirect('login')
            # return JsonResponse({'message': 'User registered successfully', 'uid': user.uid}, status=201)

        except Exception as e:
            # Handle errors (e.g., duplicate email, invalid input)
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'registration.html')


def login(request):
    email=request.POST.get('email')
    pasw=request.POST.get('password')
    try:
        # if there is no error then signin the user with given email and password
        user=auth.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"a_mainchat.html",{"email":email})
 

from django.http import JsonResponse
from django.contrib.auth import logout

def clear_session(request):
    if request.method == "POST":
        # Clear the Django session
        request.session.flush()  # Remove all session data
        logout(request)  # Log out the user if using Django authentication
        return JsonResponse({'message': 'Session cleared'}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)



# def login(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         user = auth.sign_in_with_email_and_password(email, password)
#         try:
#             # Query Firestore to verify user credentials
#             users_ref = db.collection('users')
#             query = users_ref.where('email', '==', email).stream()

#             login_successful = False  # Flag to track successful login

#             for user in query:
#                 user_data = user.to_dict()
#                 if user_data.get('password') == password:  # Replace with hashed password check
#                     # Store UID and username in the session
#                     request.session['uid'] = user.id
#                     request.session['username'] = user_data.get('username', 'Guest')
#                     login_successful = True
#                     break  # Exit the loop since login is successful

#             if login_successful:
#                 return redirect('chatui')  # Redirect only if login is successful
#             else:
#                 messages.error(request, "Invalid credentials")
#                 return redirect('login')

#         except Exception as e:
#             messages.error(request, f"An error occurred: {e}")
#             return redirect('login')  # Redirect in case of an error

#     return render(request, 'login.html')




def logout_view(request):
    logout(request)  # Clear all session data
    return redirect('login')  # Redirect to the login page


# def login(request):
#     if request.method == 'POST':
#         try:
#             # Extract email and password from the POST request
#             email = request.POST['email']
#             password = request.POST['password']


#             print('email',email)
#             print('password',password)

#             # Sign in the user with Firebase
#             user = auth.get_user_by_email(email)
            
#             # Check Firestore for user details (optional)
#             user_doc = db.collection('users').document(user.uid).get()
#             if user_doc.exists:
#                 user_data = user_doc.to_dict()
#             else:
#                 user_data = {'message': 'No additional user data found in Firestore.'}

#             # You could also generate a custom token for additional operations
#             custom_token = auth.create_custom_token(user.uid)

#             print('custom_token',custom_token)

#             # Send a success response with user data and custom token
#             return JsonResponse({
#                 'message': 'Login successful',
#                 'user_data': user_data,
#                 'custom_token': custom_token.decode('utf-8'),
#             }, status=200)

#         except Exception as e:
#             # Handle errors (e.g., invalid credentials or user not found)
#             return JsonResponse({'error': str(e)}, status=401)

#     return render(request, 'login.html')

