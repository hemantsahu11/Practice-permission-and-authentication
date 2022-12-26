from django.contrib import admin
# from .models import Teacher, Student
# from guardian.admin import GuardedModelAdmin
# Register your models here.


# @admin.register(Teacher)
# class TeacherModelAdmin(GuardedModelAdmin):
#     list_display = ('id', 'name', 'email', 'subject',)

    # def has_module_permission(self, request):
    #     if super().has_module_permission(request):   # if staff user or user has permission then only he can view Teacher model on screen
    #         return True
    #
    # def has_permission(self, request, obj, action):
    #     opts = self.opts
    #     code_name = f'{action}_{opts.model_name}'
    #     if obj:
    #         return request.user.has_perm(f'{opts.app_label}.{code_name}', obj)
    #     else:
    #         return True
    #
    # def has_view_permission(self, request, obj=None):
    #     return self.has_permission(request, obj, 'view')
    #
    # def has_change_permission(self, request, obj=None):
    #     return self.has_permission(request, obj, 'change')
    #
    # def has_delete_permission(self, request, obj=None):
    #     return self.has_permission(request, obj, 'delete')


# @admin.register(Student)
# class StudentModelAdmin(GuardedModelAdmin):
#     list_display = ('id', 'name', 'email', 'teacher', )
#
#
# admin.site.register(Teacher, TeacherModelAdmin)
# admin.site.register(Student, StudentModelAdmin)
