from django.db import models
from django.db import models
from django.utils import timezone
import os

# Create your models here.
class CategoriaJob(models.Model):
    ctj_codigo = models.AutoField(primary_key=True, db_column='ctj_codigo'),
    ctj_nombre = models.CharField(max_length=150)
    ctj_ativo = models.BooleanField(default=True)

    def __str__(self):
        return '%s' %(self.ctj_nombre)
    
    class Meta:
        verbose_name = 'Categoria de trabajo'


class TypeJob(models.Model):
    tp_codigo = models.AutoField(primary_key=True, db_column='tp_codigo')
    tp_nome = models.CharField(max_length=150)
    tp_ativo = models.BooleanField(default=True)

    def __str__(self):
        return '%s' %(self.tp_nome)
    
    class Meta:
        verbose_name = 'Tipo de trabajo'

class Job(models.Model):
    j_codigo = models.AutoField(primary_key=True, db_column='j_codigo')
    j_nombre = models.CharField(max_length=150)
    j_companyname = models.CharField(max_length=150)
    j_url = models.CharField(max_length=150)
    j_description = models.TextField()
    j_email = models.CharField(max_length=80)
    j_position_ordem = models.IntegerField()
    j_position_location = models.CharField(max_length=80)
    
    TypeJob = models.ForeignKey(TypeJob, on_delete=models.CASCADE)
    CategoriaJob = models.ForeignKey(CategoriaJob, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s - %s' % (self.j_nombre, self.j_email, self.j_position_ordem)

    class Meta:
        verbose_name = 'Job'
