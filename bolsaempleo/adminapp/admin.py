from django.contrib import admin
from .models import Job, CategoriaJob, TypeJob
from reversion.admin import VersionAdmin
# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    search_fields = ['j_nombre']
    list_display = (
        'j_nombre',
        'j_companyname',
        'j_email',
        'j_position_ordem',
    )
    def has_add_permission(self, request):
        return request.user.username == 'yona'

    def has_delete_permission(self, request, obj=None):
        return request.user.username == 'yona'
    
    def has_change_permission(self, request, obj=None):
        return request.user.username == 'yona'
    

@admin.register(CategoriaJob)
class CategoriaJobAdmin(admin.ModelAdmin):
    search_fields = ['ctj_nombre']
    list_display = (
        'ctj_nombre',
        'ctj_ativo'
    )
    def has_add_permission(self, request):
        return request.user.username == 'yona'

    def has_delete_permission(self, request, obj=None):
        return request.user.username == 'yona'
    
    def has_change_permission(self, request, obj=None):
        return request.user.username == 'yona'


@admin.register(TypeJob)
class TypeJobAdmin(admin.ModelAdmin):
    search_fields = ['tp_nome']
    list_display = (
        'tp_nome',
        'tp_ativo'
    )
    def has_add_permission(self, request):
        return request.user.username == 'yona'

    def has_delete_permission(self, request, obj=None):
        return request.user.username == 'yona'
    
    def has_change_permission(self, request, obj=None):
        return request.user.username == 'yona'

