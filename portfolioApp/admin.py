from django.contrib import admin
from .models import myproject, herosection, projectcount, copyright, serviceoffer, skills, maplocation,learing_resource,socialmedia_link

# Register your models here.
admin.site.site_header = "Sonam Wangchuk Portfolio"
admin.site.site_title = "Sonam Developer"
admin.site.index_title = "Manage Soanm Administration"


class myprojectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "project_desc",
                    "project_link", "image_link",)


class herosectionAdmin(admin.ModelAdmin):
    list_display = ("hero_greeting", "hero_title",
                    "hero_intro", "hero_img_link",)


class projectcountAdmin(admin.ModelAdmin):
    list_display = ("countdown_title", "countdown",)


class copyrightAdmin(admin.ModelAdmin):
    list_display = ("copyright",)


class serviceOffferAdmin(admin.ModelAdmin):
    list_display = ("iconname", "service_title")


class locationAdmin(admin.ModelAdmin):
    list_display = ("present_location", "location_map_api_link",)


class skillsAdmin(admin.ModelAdmin):
    list_display = ("skill_title", "skills_in_percent",)

class learing_resourceAdmin(admin.ModelAdmin):
    list_display = ('title','resource_link')

admin.site.register(myproject, myprojectAdmin)
admin.site.register(herosection, herosectionAdmin)
admin.site.register(projectcount, projectcountAdmin)
admin.site.register(copyright, copyrightAdmin)
admin.site.register(serviceoffer, serviceOffferAdmin)
admin.site.register(skills, skillsAdmin)
admin.site.register(maplocation, locationAdmin)
admin.site.register(learing_resource,learing_resourceAdmin)
admin.site.register(socialmedia_link)
