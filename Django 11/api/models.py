from tastypie.resources import ModelResource
from todo.models import Category, Task
from tastypie.authorization import Authorization



class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'tasks'
        allowed_methods = ['get', 'post', 'put', 'delete']
        excludes = ['created', 'updated']
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        return bundle

    def dehydrate_name(self, bundle):
        return bundle.data["name"].upper()



