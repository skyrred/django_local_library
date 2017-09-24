from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import permalink

class Post(models.Model):
	title = models.CharField(max_length = 255)
	slug = models.SlugField(unique = True , max_length=255)
	url = models.CharField(max_length = 500 , default= False)
	description = models.CharField(max_length = 200)
	content = models.TextField()
	published = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'%s' % self.title
	#def get_absolute_url(self):
		#return reverse('blog_pst', args=[self.slug])
	@permalink
	def get_absolute_url(self):
		return ("blog_post" ,None ,{'slug':self.slug})
#	def get_url(self):
		#return reverse("blog.views.post" , args = self.slug)
#def get_absolute_url(self):
		#global slg
		#slg = self.slug
		#return reverse('blog.views.post',args = slg)
class Meta:
	ordering = ['-created']
class Post2(models.Model):
	title = models.CharField(max_length = 255)
	slug = models.SlugField(unique = True , max_length=255)
	url = models.CharField(max_length = 500)
	description = models.CharField(max_length = 200)
	content = models.TextField()
	published = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return u'%s' % self.title
	@permalink
	def get_absolute_url(self):
		return ("blog_view_post" ,None,{'slug':self.slug})

class Meta:
	ordering = ['-created']





# Create your models here.
