from django.urls import path
from . import views
urlpatterns = [
    path('host/',views.question_view,name='host'),
    path('addqn/',views.add_question,name='addqn'),
    path('delqn/<int:id>/',views.delete_question,name='delqn'),
    path('contestid/',views.store_id,name='contestid'),
    path('hostreturn/',views.host_return,name='hostreturn'),
    path('getid/',views.getid,name='getid'),
    path('quizpage/',views.quizpage,name='quizpage'),
    path('leaderboard/',views.show_leaderboard,name='leaderboard'),
    path('contactus/',views.contact_us,name='contactus'),
]
