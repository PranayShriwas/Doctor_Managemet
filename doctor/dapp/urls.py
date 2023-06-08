from django.urls import path
from dapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # user url
    path('', views.userlogin),
    path('login_reg/', views.login_reg),
    path('usersignup/', views.usersignup),
    path('user_signup/', views.user_signup),

    # doctor url
    path('docsignup/', views.docsignup),
    path('doc_signup/', views.doc_signup),
    path('table/', views.table),
    path('delete/<int:uid>/', views.delete),
    path('update/<int:uid>/', views.update),
    path('ureg/', views.ureg)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
