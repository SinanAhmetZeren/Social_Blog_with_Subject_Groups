# from blogproject import user
from django.urls import reverse
from .models import Subject, Article, Comment
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User


################# ABOUT #######################
def aboutView(request):
    return render(request, 'blog/about.html', {'title': 'About'})


################# SUBJECTS #######################
# -------------------------------------------------- #
#--------- LISTING ALL SUBJECTS ON MAIN PAGE --------#
class subjectsView(ListView):
    model = Subject
    template_name = 'blog/subjects_View.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'subjects'
    ordering = ['-createdDate']
    # paginate_by = 10

# -------------------------------------------------- #
#--------- CREATE NEW SUBJECT -----------------------#
class subjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ['image', 'subjectName']

# -------------------------------------------------- #
#----- DISPLAY ALL ARTICLES OF GIVEN SUBJECT --------#
class subjectArticlesListView(ListView):
    model = Article
    template_name = 'blog/subject_articles.html' 
    context_object_name = 'articles'
    # paginate_by = 10
     
    def get_queryset(self):
        subject = get_object_or_404(Subject, id=self.kwargs.get('pk'))
        return Article.objects.filter(articleSubject=subject) .order_by('-date_posted')




################# ARTICLES #######################

# -------------------------------------------------- #
# ----- DISPLAY SINGLE ARTICLE DETAILS --------------#
class articleDetailView(DetailView):
    model = Article

# -------------------------------------------------- #
# ---------- CREATE NEW ARTICLE  ------------------- #
class articleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = [ 'articleSubject','title', 'content', 'image']

    def form_valid(self, form):
        form.instance.articleSubject = get_object_or_404(Subject, id=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        return super().form_valid(form)

# -------------------------------------------------- #
# ----------------------- DELETE ARTICLE  -----------#
class articleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/subjects/'

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


# -------------------------------------------------- #
#------------------------ UPDATE ARTICLE  -----------#
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['articleSubject', 'title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False



################# AUTHOR #######################

# -------------------------------------------------- #
# -------- DISPLAY ALL ARTICLES OF AUTHOR ---------- #

class authorArticlesView(ListView):
    model = Article
    template_name = 'blog/author_articles.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'articles'
    # paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(author=user).order_by('-date_posted')


# -------------------------------------------------- #
# -------------- DISPLAY ALL AUTHORS --------------- #

class authorsListView(ListView):
    model = User
    template_name = "blog/authors.html"
    context_object_name= "users"

    # def get_queryset(self): 
    #     return User.objects.filter(User.article_set)


    # # def get_queryset(self):
    # #     return Scenario.objects.filter(
    # #         scenarioAuthor=self.request.user
    # #     ).order_by('-date_posted')