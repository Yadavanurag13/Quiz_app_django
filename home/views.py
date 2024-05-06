from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import random
# Create your views here.

def home(request):

    context = {'categories': Category.objects.all()}

    if(request.GET.get('category')):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request, 'home.html', context)


def quiz(request):
    return render(request, 'quiz.html')


# {
#     'status': True
#     'data': [
#        {payload}
#     ]
# }
def get_quiz(request):
    try:
        Question_objs = (Question.objects.all())

        #if we want to access the data for foreign key we have to use double __
        if request.GET.get('category'):
            Question_objs = Question.objects.filter(category__category_name__icontains=request.GET.get('category'))

        #if any category is not given directly return it in form of list 
        Question_objs = list(Question_objs)

        data = []
        random.shuffle(Question_objs)

        for Question_obj in Question_objs:
            data.append({
                'category': Question_obj.category.category_name,
                'question': Question_obj.question,
                'marks': Question_obj.marks,
                'ans': Question_obj.get_answer()
            })

        payload = {
            'status': 200,
            'data': data
        }

        return JsonResponse(payload)
    except Exception as e:
        print(e)
    return JsonResponse({
        'status': 500,
        'data': "Something went wrong"
    })