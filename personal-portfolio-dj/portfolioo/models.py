from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(_("title"), max_length=50)
    image = models.ImageField(_("image"), upload_to='projects')
    created_by = models.ForeignKey(User,  on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created at"),auto_now_add=True)
    
    

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

