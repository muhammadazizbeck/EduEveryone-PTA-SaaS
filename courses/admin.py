from django.contrib import admin
from courses.models import Lesson,Course,Submission
from django.utils.html import format_html

# Register your models here.
class LessonInline(admin.TabularInline):
    """
    Course sahifasida darslarni (Lesson) jadval shaklida ko‘rsatish va
    tezda qo‘shish / tahrirlash imkonini beradi.
    """
    model = Lesson
    extra = 0  # qo‘shimcha bo‘sh qatordan voz kechish
    fields = ("order", "title", "video", "assignment_file")
    readonly_fields = ()  # xohlasangiz video/assignment ni readonly qiling

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "level",
        "author",
        "lesson_count",
        "created_at",
        "thumbnail",
    )
    list_filter = ("level", "created_at")
    search_fields = ("title", "description", "author__full_name", "author__email")
    ordering = ("level", "title")
    inlines = [LessonInline]

    # darslar sonini ko‘rsatish
    @admin.display(description="Darslar")
    def lesson_count(self, obj):
        return obj.lessons.count()

    # rasmni kichik ko‘rinishda (60 px) chiqarish
    @admin.display(description="Rasm")
    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="60" />', obj.image.url)
        return "—"
    
class SubmissionInline(admin.TabularInline):
    """
    Lesson sahifasida o‘quvchi topshiriqlarini (Submission) ko‘rsatish.
    """
    model = Submission
    extra = 0
    fields = ("student", "file", "grade", "submitted_at", "feedback")
    readonly_fields = ("submitted_at",)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course__level", "course")
    search_fields = ("title", "course__title")
    ordering = ("course", "order")
    inlines = [SubmissionInline]

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("lesson", "student", "grade", "submitted_at", "short_feedback")
    list_filter = ("grade", "lesson__course__level", "lesson")
    search_fields = ("student__full_name", "student__email", "lesson__title")
    ordering = ("-submitted_at",)
    readonly_fields = ("submitted_at",)

    @admin.display(description="Feedback")
    def short_feedback(self, obj):
        return (obj.feedback[:50] + "...") if obj.feedback else "—"