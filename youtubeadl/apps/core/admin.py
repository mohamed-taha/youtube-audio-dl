from django.contrib import admin

from djcelery.models import TaskMeta

from youtubeadl.apps.core.models import Ad


@admin.register(TaskMeta)
class TaskMetaAdmin(admin.ModelAdmin):
    readonly_fields = ('result',)

    list_display = (
        'task_id',
        'status',
        'date_done',
        'traceback',
        'result',
    )

    list_filter = (
        'status',
        'date_done',
    )

    search_fields = (
        'task_id',
        'traceback',
        'result',
    )


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('description', 'position', 'created', 'modified')