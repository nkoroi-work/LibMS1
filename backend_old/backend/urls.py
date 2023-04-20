"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from tables import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    re_path(r'^api/books/$', views.books_list),
    re_path(r'^api/books/([0-9])$', views.books_detail),
    re_path(r'^api/book_authors/$', views.book_authors_list),
    re_path(r'^api/book_authors/([0-9])$', views.book_authors_detail),
    re_path(r'^api/book_copies/$', views.book_copies_list),
    re_path(r'^api/book_copies/([0-9])$', views.book_copies_detail),
    re_path(r'^api/publishers/$', views.publishers_list),
    re_path(r'^api/publishers/([0-9])$', views.publishers_detail),
    re_path(r'^api/library_branches/$', views.library_branches_list),
    re_path(r'^api/library_branches/([0-9])$', views.library_branches_detail),
    re_path(r'^api/borrowers/$', views.borrowers_list),
    re_path(r'^api/borrowers/([0-9])$', views.borrowers_detail),
    re_path(r'^api/book_loans/$', views.book_loans_list),
    re_path(r'^api/book_loans/([0-9])$', views.book_loans_detail),

]
