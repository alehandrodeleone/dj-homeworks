from django.db import models

class Tag(models.Model):
    
    name = models.CharField(max_length=50, verbose_name='Название')
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        
    def __str__(self):
        return self.name

class Article(models.Model):

    titles = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    images = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, related_name='articles', through='Scope')
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']
        
    def __str__(self):
        return self.title
    
    
class Scope(models.Model):
    
    articles = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной')
    
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
    
