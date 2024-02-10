from django.shortcuts import render, redirect
from .models import Receipe

def receipes(request):
    context = {}

    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_field = request.FILES.get('receipe_field')

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_field=receipe_field,
        )

        return redirect('receipes')

    queryset = Receipe.objects.all()

    if request.GET.get('search'):
      queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
      

    context['receipes'] = queryset

    return render(request, 'receipes.html', context)


def delete_receipe(request, id):
  queryset = Receipe.objects.get(id = id)
  queryset.delete()
  return redirect('receipes')


def update_receipe(request, id):
  context = {}
  queryset = Receipe.objects.get(id = id)

  if request.method == "POST":
    data = request.POST

    receipe_name = data.get('receipe_name')
    receipe_description = data.get('receipe_description')
    receipe_field = request.FILES.get('receipe_field')

    queryset.receipe_name = receipe_name
    queryset.receipe_description = receipe_description

    if receipe_field:
      queryset.receipe_field = receipe_field
    
    queryset.save()
    return redirect('receipes')

  context['receipe'] = queryset
  return render(request, 'update_receipes.html', context)