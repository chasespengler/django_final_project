from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from onlinecourse.views import CourseListView, registration_request, login_request, logout_request, CourseDetailView, enroll

app_name = 'onlinecourse'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=CourseListView.as_view(), name='index'),
    path('registration/', registration_request, name='registration'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    # ex: /onlinecourse/5/
    path('<int:pk>/', CourseDetailView.as_view(), name='course_details'),
    # ex: /enroll/5/
    path('<int:course_id>/enroll/', enroll, name='enroll'),

    # <HINT> Create a route for submit view
    path('<int:course_id>/submit/', ...),

    # <HINT> Create a route for show_exam_result view
    path('course/<int:course_id>/submission/<int:submission_id>/result/', ...),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
