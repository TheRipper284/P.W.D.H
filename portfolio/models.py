from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descripción')
    image = models.ImageField(upload_to='images/', verbose_name='Imagen')
    url = models.URLField(verbose_name = 'Url de proyecto', null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'
                                    , null = True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización',
                                    null = True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']
