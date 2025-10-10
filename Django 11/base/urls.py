from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from api.models import CategoryResource, TaskResource
from tastypie.api import Api

api = Api(api_name='v1')
category_resource = CategoryResource()
task_resource = TaskResource()

api.register(category_resource)
api.register(task_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),  # доступно по /todo/
    path('', RedirectView.as_view(url='/accounts/', permanent=False)),       # доступно по /

    # path('api/', include(category_resource.urls)),
    # path('api/', include(task_resource.urls)),
    path('api/', include(api.urls)),
    # base/urls.py
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

]


