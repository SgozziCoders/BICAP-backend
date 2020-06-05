from BICAPweb.models import *
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


@receiver(m2m_changed, sender=Indagine.gruppi.through)
def CreateDistribuzione(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add':
        senderObjects = instance.gruppi.all()
        indagine = instance
        utenti = []
        for gruppo in senderObjects:
            idGruppo = gruppo.id
            utenti += Utente.objects.all().filter(gruppi=idGruppo)
        for utente in utenti:
            # Controllo che il recordo utente.indagine non sia già presente 
            if len(Distribuzione.objects.filter(utente=utente, indagine=indagine)) == 0:
                Distribuzione.objects.get_or_create(utente=utente, indagine=indagine, terminata=False)

    if action == 'post_remove':
        senderObjects = instance.gruppi.all()
        indagine = instance
        utenti = []
        for gruppo in senderObjects:
            idGruppo = gruppo.id
            utenti += Utente.objects.all().filter(gruppi=idGruppo)
        distribuzioni = Distribuzione.objects.all()
        for utente in utenti:
            distribuzioni = distribuzioni.exclude(utente=utente)
        distribuzioni.delete()

