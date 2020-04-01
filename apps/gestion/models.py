from django.db import models

class Ano(models.Model):
    ano = models.IntegerField(unique=True)
    comienzo = models.DateTimeField()
    final = models.DateTimeField()

    class Meta:
        verbose_name = 'Año'
        verbose_name_plural = 'Años'

    def __str__(self):
        return str(self.comienzo)

class Temporada(models.Model):
    nombre = models.CharField(max_length=20)
    # Foránea
    ano = models.OneToOneField(Ano, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Temporada'
        verbose_name_plural = 'Temporadas'

    def __str__(self):
        return str(self.nombre)

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Nacionalidad'
        verbose_name_plural = 'Nacionalidades'

    def __str__(self):
        return self.pais

class Jugador(models.Model):
    foto = models.ImageField(upload_to='img')
    nombre = models.CharField(max_length=50)
    pj = models.IntegerField(default=0)
    victorias = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # Foráneas
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, related_name='nacionalidad', null=True, blank=True)

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        ordering = ['victorias']

    def __str__(self):
        return self.nombre


class Partida(models.Model):
    dia = models.DateField(max_length=20)
    hora_inic = models.TimeField(max_length=5)
    hora_fin = models.TimeField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    #Foránea
    temporada =  models.ForeignKey(Temporada, on_delete=models.SET_NULL, related_name='temporada', null=True, blank=True)

    class Meta:
        verbose_name = 'Partida'
        verbose_name_plural = 'Partidas'
        ordering = ['dia']

    def __str__(self):
        return self.dia

class Juega(models.Model):
    kills = models.IntegerField(default=0)
    equipo = models.CharField(max_length=50, unique=True)
    ganador = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # Foráneas
    jugador = models.ManyToManyField(Jugador)
    partida = models.ManyToManyField(Partida)

    class Meta:
        verbose_name = 'Juega'
        verbose_name_plural = 'Juega'
        ordering = ['kills']

    def __str__(self):
        return self.equipo