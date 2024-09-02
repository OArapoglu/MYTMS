from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @method_decorathor(cache_page(60*15))
    def week_tasks(self, request, year, week):
        tasks = Task.objects.filter(

        )







