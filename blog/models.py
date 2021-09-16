from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


##################################################################
class Subject(models.Model):
    subjectName = models.CharField(max_length=30)
    createdDate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="defaultSubject.jpg")

    def __str__(self):
        return f'{self.subjectName}'



##################################################################
class Article(models.Model):
    articleSubject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default="defaultArticle.jpg")  #blank=True, null=True
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:articleDetail', kwargs={'pk': self.pk})
 
##################################################################
class Comment(models.Model):
    relatedPost = models.ForeignKey(Article,on_delete=models.CASCADE)
    commentAuthor = models.CharField(max_length=50)
    commentContent = models.CharField(max_length=1000)
    commentDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.commentContent
    class Meta:
        ordering = ['-commentDate']
