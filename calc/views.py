from django.shortcuts import render, redirect

Firstname = ""
Lastname = ""

def home(request):
  return render(request,'home.html',{'name':'Sreya'})
def test1(request):
  return render(request,'test1.html',{'name':'Sreya'})
def r1(request):
  return render(request,'r1.html',{'name':'Sreya'})
# Create your views here.

def add(request):
  global Firstname, Lastname

  Firstname=str(request.POST['first'])
  Lastname=str(request.POST['last'])
  val3 = "WELCOME " + Firstname + " " + Lastname

  print(f"Val3 is: {val3}")

  return render(request,'dashboard.html',{'friend':val3})
  

def dashboard(request):
  global Firstname, Lastname

  print(f"Firstname is: {Firstname}")
  print(f"Lastname is: {Lastname}")

  if Firstname and Lastname:
      message = f"WELCOME {Firstname} {Lastname}"
      return render(request, 'dashboard.html', {'friend': message})
  else:
    return render(request,'dashboard.html')

# views.py

# from .forms import QuestionForm
# from django.http import HttpResponseRedirect
# from urllib.parse import quote

# def question_view(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             selected_option = form.cleaned_data['question']
#             # encoded_option = quote(selected_option)
#             return HttpResponseRedirect(f'test1?response={selected_option}')
#             return redirect('test1')
#     else:
#         form = QuestionForm()

#     return render(request, 'r1.html', {'form': form})

# def success_view(request):
#     response = request.GET.get('response', 'No response')
#     return render(request, 'test1.html', {'response': response})

# views.py

from .forms import SurveyForm
def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            question_1_response = form.cleaned_data['optimum_learning']
            question_2_response = form.cleaned_data['assesments']
            return render(request, 'test1.html', {'q1': question_1_response, 'q2': question_2_response})
            return redirect('test1')
    else:
        form = SurveyForm()

    return render(request, 'r1.html', {'form': form})

def success_view(request):
    q1 = request.GET.get('optimum_learning', 'No response')
    q2 = request.GET.get('assesments', 'No response')
    return render(request, 'test1.html', {'q1': q1, 'q2': q2})