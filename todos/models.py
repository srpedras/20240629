from django.db import models

# Create your models here.


#criando a tabela Todo
class Todo(models.Model):
    titulo = models.CharField(verbose_name='Titulo da Tarefa',max_length=150, null=False, blank=False)
    dtCriacao = models.DateTimeField(verbose_name='TData da Criação',auto_now_add=True, null=False, blank=False)
    dtFinalizado = models.DateTimeField(verbose_name='Data da Finalização',null=True, blank=True)
