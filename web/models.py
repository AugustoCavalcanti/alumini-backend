from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=128)


class Turma(models.Model):
    nome = models.CharField(max_length=128)
    curso = models.ForeignKey(Curso, related_name='turmas', blank=False, on_delete=models.CASCADE)
    ano = models.IntegerField(max_length=4)
    semestre = models.IntegerField(max_length=1)
    paraninfo = models.CharField(max_length=128)
    patrono = models.CharField(max_length=128)
    foto = models.URLField(null=True, blank=True, max_length=300)

    def __str__(self):
        return self.nome


class Habilidade(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    curso = models.ForeignKey(Curso, related_name='habilidades', blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Formando(models.Model):
    nome = models.CharField(max_length=128)
    ocupacao = models.CharField(max_length=128)
    formacao = models.CharField(max_length=128)
    foto = models.URLField(null=True, blank=True, max_length=300)
    redes_socias = models.URLField(null=True, blank=True)
    destaque = models.CharField(max_length=128)
    local = models.CharField(max_length=128)
    frase_de_efeito = models.CharField(max_length=300)
    turma = models.ForeignKey(Turma, related_name='egressos', on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidade, related_name='egressos', blank=True, max_length=5)
    curso = models.ForeignKey(Curso,related_name='egressos', blank=False, on_delete=models.CASCADE)
    ano = models.IntegerField(max_length=4)
    semestre = models.IntegerField(max_length=1)

    def __str__(self):
        return self.nome
