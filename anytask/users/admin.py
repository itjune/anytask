# -*- coding: utf-8 -*-

from users.models import UserProfile, UserStatus, UserProfileLog
from django.contrib import admin

def display_color(obj):
    return u'<span style="' \
           u'padding: .25em .4em;' \
           u'font-size: 75%;' \
           u'font-weight: 700;' \
           u'line-height: 1;' \
           u'color: #000;' \
           u'text-align: center;' \
           u'white-space: nowrap;' \
           u'vertical-align: baseline;' \
           u'border-radius: .25rem;' \
           u'background-color:{0}' \
           u'">{1}</span>'.format(obj.color, obj.name)
display_color.short_description = u'Статус'
display_color.allow_tags = True

class UserStatusAdmin(admin.ModelAdmin):
    list_display = (display_color, 'tag', 'type')
    search_fields = ('name',)

    def queryset(self, request):
        qs = super(UserStatusAdmin, self).queryset(request)
        # if request.user.is_superuser:
        #     return qs
        return qs

class UserProfileLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'updated_by', 'update_time')
    search_fields = ('name', 'update_by',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'updated_by', 'update_time')
    filter_horizontal = ('unread_messages', 'deleted_messages', 'send_notify_messages')
    search_fields = ('user__username', 'user_status')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserStatus, UserStatusAdmin)
admin.site.register(UserProfileLog, UserProfileLogAdmin)

from django.contrib.auth import admin as auth_admin
auth_admin.UserAdmin.list_display += ('last_login',)
