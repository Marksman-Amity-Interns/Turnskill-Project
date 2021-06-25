from .models import *
from import_export import resources

class CourseResource(resources.ModelResource):

    class Meta:
        model = course
        import_id_fields = ('course_id',)    