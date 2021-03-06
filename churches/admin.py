from django.contrib import admin
from .models import Church, Church_denomination, Bg_color, Color, Text_color, Border_color, Hover_color, Footer_color, Hover_border_color, Hover_text_color, Theme_of_the_year,Weekly_theme, Daily_word, Schedule, Announcement, Home_cell, Church_group, Church_member, Church_choir, Hymn,  Hymn_of_the_week, Video, Sermon, Photo


admin.site.register(Church)
admin.site.register(Church_denomination)
admin.site.register(Bg_color)
admin.site.register(Hover_color)
admin.site.register(Hover_text_color)
admin.site.register(Hover_border_color)
admin.site.register(Footer_color)
admin.site.register(Border_color)
admin.site.register(Color)
admin.site.register(Text_color)
admin.site.register(Theme_of_the_year)
admin.site.register(Weekly_theme)
admin.site.register(Daily_word)
admin.site.register(Schedule)
admin.site.register(Announcement)
admin.site.register(Home_cell)
admin.site.register(Church_group)
admin.site.register(Church_member)
admin.site.register(Church_choir)
admin.site.register(Sermon)
admin.site.register(Hymn)
admin.site.register(Hymn_of_the_week)
admin.site.register(Video)
admin.site.register(Photo)
