from django.db import models

class Utente(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Utente"
        verbose_name_plural = "Utenti"

class Indagine(models.Model):
    titoloIndagine = models.CharField(max_length=20)
    erogatore = models.CharField(max_length=20)
    imgUrl = models.FileField()
    tematica = models.TextField()

    def __str__(self):
        return self.titoloIndagine

    class Meta:
        verbose_name = "Indagine"
        verbose_name_plural = "Indagini"

class Distribuzione(models.Model):
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name="indagini")
    indagine = models.ForeignKey(Indagine, on_delete=models.CASCADE, related_name="utenti")
    terminata = models.BooleanField()

    def __str__(self):
        return "Utente: " + self.utente.__str__() + " Indagine: " + self.indagine.__str__()

    class Meta:
        verbose_name = "Distribuzione"
        verbose_name_plural = "Distribuzioni"


class Questionario(models.Model):
    titolo = models.CharField(max_length=20)
    qualtricsUrl = models.CharField(max_length=250)
    compilato = models.BooleanField()
    indagine = models.ForeignKey(Indagine, on_delete=models.CASCADE, related_name="questionari")

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = "Questionario"
        verbose_name_plural = "Questionari"

class Informazione(models.Model):
    nomeFile = models.CharField(max_length=20)
    fileUrl = models.FileField()
    thumbnailUrl = models.FileField()
    tipoFile = models.CharField(max_length=20)
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE, related_name="informazioni")

    def __str__(self):
        return self.nomeFile

    class Meta:
        verbose_name = "Informazione"
        verbose_name_plural = "Informazioni"



