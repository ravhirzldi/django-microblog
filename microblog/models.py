from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

# Third Parties Libraries
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

# Create your models here.
class PublishedManager(models.Manager):
    # This class is to change query commands
    # From Post.objects.all() to Post.Published()
    # So it will only showing all published content only
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                    .filter(status='published').order_by('-created')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User)
    header_img = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    body = RichTextUploadingField('body')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    tags = TaggableManager()
    
    objects = models.Manager()
    published = PublishedManager()
    
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # If slug failed to created it will be automatically created after you save
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        
    def photo_url(self):
        if self.header_img and hasattr(self.header_img, 'url'):
            return self.header_img.url
        
    
    # Reversing URl to post_detail so get URL like,
    # ../(year)/(month)/(day)/slug
    def get_absolute_url(self):
        return reverse('post_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])
    
    