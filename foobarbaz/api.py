from foobarbaz.models import ModelItem
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource

class ModelItem(ModelResource):
    class Meta:
        queryset = ModelItem.objects.all()
        resource_name = 'item'
        allowed_methods = ['get', 'post', 'put']
        authorization = DjangoAuthorization()

    def obj_create(self, bundle, **kwargs):
        return super(ModelItem, self).obj_create(bundle, user=bundle.request.user)
