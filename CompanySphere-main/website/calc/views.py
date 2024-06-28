'''from django.shortcuts import render
from django.http import HttpResponse
from calc.models import Posts
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def login(request):
    return render(request,'login.html',{})
def index(request):
    return render(request,'index.html',{})
def add_post(request):
    comment=request.POST.get('comment').split(',')
    tags=request.POST.get('tags').split(',')
    user_details={'name':request.POST.get('name')}
    post=Posts(post_title=request.POST.get('post_title',post_description=request.POST.get('post_description'),comment=comment,tags=tags,user_details=user_details))
    post.save()
    return HttpResponse('Inserted')


def update_post(request,id):
    pass
def delete_post(request,id):
    pass
def read_post(request,id):
    post=Posts.objects.get(_id=ObjectId(id))
    stringval='name:'+post.user_details['name']
    return HttpResponse(stringval)
def read_post_all(request,id):
    posts=Posts.objects.all()
    for post in posts
    pass '''
# views.py

'''from django.shortcuts import render
from .models import YourModel

def your_view(request):
    data = YourModel.objects.all()
    return render(request, 'google.html', {'data': data})'''
# views.py

'''from django.shortcuts import render
from pymongo import MongoClient
from gridfs import GridFS
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        hashed_password = make_password(password)
        user = User(username=username, email=email, password=hashed_password)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username).first()
        if user:
            if check_password(password, user.password):
                # Successful login logic
                return redirect('index.html')
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        else:
            return render(request, 'login.html', {'error': 'User does not exist'})
    return render(request, 'login.html')
'''

'''def index(request):
    return render(request,'index.html',{})
from .models import Microsoft
from django.shortcuts import render

from django.shortcuts import render
from pymongo import MongoClient
# views.py

from django.shortcuts import render
from pymongo import MongoClient
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .models import FreshersData  # Assuming you have a model for freshers data

# views.py
from chartjs.views.lines import BaseLineChartView
from .models import FreshersData

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return years as labels for the x-axis."""
        return ['Year 1', 'Year 2', 'Year 3']

    def get_providers(self):
        """Return the name of the dataset."""
        return ["Number of Freshers"]

    def get_data(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['data']
        data_collection = db['micro']
        
        # Initialize lists to store freshers count for each year
        freshers_counts = []
        
        # Fetch data from MongoDB
        data = list(data_collection.find())
        
        # Extract freshers count for each year from MongoDB documents
        for entry in data:
            freshers_counts.append([
                entry['number_of_freshers1'],
                entry['number_of_freshers2'],
                entry['number_of_freshers3']
            ])

        client.close()
        return freshers_counts



class LineChartView(TemplateView):
    template_name = 'microsoft.html'

line_chart = LineChartView.as_view()
line_chart_json = LineChartJSONView.as_view()'''

'''def pie_chart_view(request):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['data']
    data_collection = db['micro']
    data = list(data_collection.find())  # Convert cursor to list for easier manipulation
    # Print the fetched data for debugging
    #print(data)
    from django.shortcuts import render




    # Close the MongoDB connection
    client.close()

    # Render the template with data
    return render(request, 'microsoft.html', {'data': data})'''


''''freshers_data = hiring_collection.find_one()  # Assuming you have only one document
    labels = ['Year 1', 'Year 2', 'Year 3']
    data = [
        freshers_data['number_of_freshers1'],
        freshers_data['number_of_freshers2'],
        freshers_data['number_of_freshers3'],
    ]
    context = {
        'labels': labels,
        'data': data,
    }
    return render(request, 'microsoft.html', context)'''

'''def pie_chart_view(request):
    client = MongoClient('mongodb://localhost:27017/')  # Update connection string as needed
    db = client['data']  # Use your database name
    hiring_collection = db['micro']

    freshers_data = list(hiring_collection.find())
      # Retrieve data from MongoDB
    #print(hiring_data)
    client.close()
     #FreshersData.objects.all()  # Assuming you have only one document in the collection
    labels = ['Year 1', 'Year 2', 'Year 3']
    data = [
        freshers_data.number_of_freshers1,
        freshers_data.number_of_freshers2,
        freshers_data.number_of_freshers3,
    ]
    context = {
        'labels': labels,
        'data': data,
    }
    return render(request, 'microsoft.html', context)'''

'''def data(request):
    client = MongoClient('mongodb://localhost:27017/')  # Update connection string as needed
    db = client['data']  # Use your database name
    hiring_collection = db['micro']

    hiring_data = list(hiring_collection.find())
      # Retrieve data from MongoDB
    print(hiring_data)
    client.close()


    # Pass the correct context variable name to the template
    return render(request, 'microsoft.html', {'data': hiring_data})

'''
# views.py inside the 'calc' app
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

 #views.py

from pymongo import MongoClient
from django.shortcuts import render
from pymongo import MongoClient
from django.shortcuts import render

def your_view(request):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')  # Update connection string as needed

    # Select the appropriate database
    db = client['data']  # Use your database name

    # Select the collection and retrieve data
    data_collection = db['goog']
    
    data = list(data_collection.find())  # Convert cursor to list for easier manipulation

    # Close the MongoDB connection
    client.close()

    # Render the template with data
    return render(request, 'google.html', {'data': data})


def your_view1(request):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')  # Update connection string as needed

    # Select the appropriate database
    db = client['data']  # Use your database name

    # Select the collection and retrieve data
    data_collection = db['micro']
    
    data = list(data_collection.find())  # Convert cursor to list for easier manipulation

    # Close the MongoDB connection
    client.close()

    # Render the template with data
    return render(request, 'microsoft.html', {'data': data})


def your_view2(request):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')  # Update connection string as needed

    # Select the appropriate database
    db = client['data']  # Use your database name

    # Select the collection and retrieve data
    data_collection = db['ibm']
    
    data = list(data_collection.find())  # Convert cursor to list for easier manipulation

    # Close the MongoDB connection
    client.close()

    # Render the template with data
    return render(request, 'ibm.html', {'data': data})

def your_view3(request):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')  # Update connection string as needed

    # Select the appropriate database
    db = client['data']  # Use your database name

    # Select the collection and retrieve data
    data_collection = db['tcs']
    
    data = list(data_collection.find())  # Convert cursor to list for easier manipulation

    # Close the MongoDB connection
    client.close()

    # Render the template with data
    return render(request, 'tcs.html', {'data': data})

def your_view4(request):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')  # Update connection string as needed

    # Select the appropriate database
    db = client['data']  # Use your database name

    # Select the collection and retrieve data
    data_collection = db['walmart']
    data = list(data_collection.find())  # Convert cursor to list for easier manipulation

    # Close the MongoDB connection
    client.close()

    # Render the template with data
    return render(request, 'walmart.html', {'data': data})
def your_view5(request):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')  # Update connection string as needed

    # Select the appropriate database
    db = client['data']  # Use your database name

    # Select the collection and retrieve data
    data_collection = db['wipro']
    
    data = list(data_collection.find())  # Convert cursor to list for easier manipulation

    # Close the MongoDB connection
    client.close()

    # Render the template with data
    return render(request, 'wipro.html', {'data': data})