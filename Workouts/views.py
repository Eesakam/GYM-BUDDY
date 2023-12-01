from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Workout,Category
from django.urls import reverse
from .forms import CategoryEditForm
# Create your views here.
def index(request):

  return render(request,"Workouts/index.html")


def ajax_workout(request):
  all_workouts = Workout.objects.all()
  data = []
  for w in all_workouts:
    w_count = w.category_count()
    w_data = {
      "title":w.title,
      "id": w.id,
      "w_count":w_count,
      "url": reverse('Workouts:works_view', args=[w.id])
    }
    data.append(w_data)
  return JsonResponse({"data":data,"w_count":w_count})


def works_view(request,id):
  all_workout = Category.objects.filter(Workout=id)
  form = CategoryEditForm()
  return render(request,"Workouts/works.html",{"all_workout":all_workout,"form":form})


def ajax_works_view(request,id):
  all_workout = Category.objects.filter(Workout=id)
  data = []
  for d in all_workout:
    deets = {
      "Workout_name":d.Workout_name,
      "Muscle_group":d.Muscle_group,
      "Rep1":d.Rep1,
      "Weight1":d.Weight1,
      "Rep2":d.Rep2,
      "Weight2":d.Weight2,
      "Rep3":d.Rep3,
      "Weight3":d.Weight3,
      "C_time":d.C_time,
      "id":d.id
    }
    data.append(deets)
  return JsonResponse({"data":data})


def update_workout_state(request,id):
    obj = Category.objects.get(pk=id)
    if request.is_ajax():
        new_Workout_name = request.POST.get("Workout_name")
        new_Muscle_group = request.POST.get("Muscle_group")
        new_Rep1 = request.POST.get("Rep1")
        new_Weight1 = request.POST.get("Weight1")
        new_Rep2 = request.POST.get("Rep2")
        new_Weight2 = request.POST.get("Weight2")
        new_Rep3 = request.POST.get("Rep1")
        new_Weight3 = request.POST.get("Weight3")
        
        obj.Workout_name = new_Workout_name
        obj.Muscle_group = new_Muscle_group
        obj.Rep1 = new_Rep1
        obj.Weight1 = new_Weight1
        obj.Rep2 = new_Rep2
        obj.Weight2 = new_Weight2
        obj.Rep3 = new_Rep3
        obj.Weight3 = new_Weight3
        obj.save()
       
    return JsonResponse({"Workout_name": new_Workout_name, 
                            "Muscle_group": new_Muscle_group,
                            "Rep1": new_Rep1,
                             "Weight1": new_Weight1, 
                             "Rep2": new_Rep2, 
                             "Weight2": new_Weight2, 
                             "Rep3": new_Rep3, 
                             "Weight3": new_Weight3,
                            })