from models import *
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class StoryAdmin(admin.ModelAdmin):
    def object(self, story):
        """
        Return the speech act's object
        
        Overrides the model's attribute in order to give it a gettext-able name.
        """
        return story.object
    # This is the closest I got in giving a verbose_name to the GenericForeignKey
    object.short_description = _('object')
    
    list_display = ('__unicode__', 'object', 'created_at', 'updated_at',)
    list_filter = ('speech_act',)
    search_fields = ('content',)
    ordering = ('created_at',)

admin.site.register(Story, StoryAdmin)
