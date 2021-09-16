from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # ABOUT US
    path('', views.aboutView, name = "about" ),
    # SUBJECTS
    path('subjects/', views.subjectsView.as_view(), name = "subjects" ),
    path('subjects/create/', views.subjectCreateView.as_view(success_url="/subjects/"), name = "subjectCreate" ),
    path('subjects/subjectArticles/<int:pk>', views.subjectArticlesListView.as_view(), name = "subjectArticles" ),
    # ARTICLES
    path('articles/detail/<int:pk>/', views.articleDetailView.as_view(), name = "articleDetail" ),
    path('articles/create/<int:pk>', views.articleCreateView.as_view(), name = "articleCreate" ),
    path('articles/delete/<int:pk>/', views.articleDeleteView.as_view(), name = "articleDelete" ),
    path('articles/update/<int:pk>/', views.ArticleUpdateView.as_view(), name = "articleUpdate" ),
    # AUTHOR
    path('authorarticles/<str:username>', views.authorArticlesView.as_view(), name = "authorArticles" ),
    path('authors/', views.authorsListView.as_view(), name = "authors" ),

]

