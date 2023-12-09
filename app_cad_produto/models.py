from django.db import models

class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    codigo = models.TextField(max_length=99999)
    descricao = models.TextField(max_length=99999)
    quantidade = models.TextField(max_length=99999)