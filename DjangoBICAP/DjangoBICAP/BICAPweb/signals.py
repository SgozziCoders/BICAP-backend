from BICAPweb.models import *
from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from preview_generator.manager import PreviewManager
import os


@receiver(m2m_changed, sender=Indagine.gruppi.through)
def CreateDistribuzione(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        senderObjects = instance.gruppi.all()
        indagine = instance
        utenti = []
        for gruppo in senderObjects:
            idGruppo = gruppo.id
            utenti += Utente.objects.all().filter(gruppi=idGruppo)
        if action == 'post_add':
            for utente in utenti:
            # Controllo che il record utente-indagine non sia già presente 
                if len(Distribuzione.objects.filter(utente=utente, indagine=indagine)) == 0:
                    Distribuzione.objects.get_or_create(utente=utente, indagine=indagine, terminata=False)
        if action == 'post_remove':
            distribuzioni = Distribuzione.objects.all()
            for utente in utenti:
                distribuzioni = distribuzioni.exclude(utente=utente)
            distribuzioni.delete()


@receiver(post_save, sender=InformazioneIndagine)
def create_thumb(sender, instance, **kwargs):
    if(instance.thumbnailUrl.name == ''):
        filepath = instance.fileUrl.file.name
        cache_path = settings.MEDIA_ROOT + '/thumb'
        manager = PreviewManager(cache_path, create_folder=True)
        FullPathToimage = manager.get_jpeg_preview(filepath)
        instance.thumbnailUrl.name = '/thumb/' + os.path.basename(FullPathToimage)
        instance.save()