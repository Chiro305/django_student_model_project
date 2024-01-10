from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "studentid",
        "student_name",
        "gender",
        "dob",
        "photo",
        "address",
        "grades",

    ]

admin.site.register(Student,StudentAdmin)