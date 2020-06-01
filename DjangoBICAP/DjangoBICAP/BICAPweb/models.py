from django.db import models

class Utente(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Distribuzione(models.Model):
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name="distribuzioni")
    indagine = models.ForeignKey(Indagine, on_delete=models.CASCADE, related_name="distribuzioni")
    terminata = models.BooleanField()

class Indagine(models.Model):
    titoloIndagine = models.CharField(max_length=20)
    erogatore = models.CharField(max_length=20)
    imgUrl = models.FileField(upload_to="media/")
    tematica = models.TextField()

class Questionario(models.Model):
    titolo = models.CharField(max_length=20)
    qualtricsUrl = models.CharField(max_length=250)
    compilato = models.BooleanField()
    indagine = models.ForeignKey(Indagine, on_delete=models.CASCADE, related_name="questionari")

class Informazione(models.Model):
    nomeFile = models.CharField(max_length=20)
    fileUrl = models.FileField(upload_to='media/')
    thumbnailUrl = models.FileField(upload_to='media/')
    tipoFile = models.CharField(max_length=20)
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE, related_name="informazioni")

    def __str__(self):
        return self.nomeFile

    class Meta:
        verbose_name = "Informazione"
        verbose_name_plural = "Informazioni"



