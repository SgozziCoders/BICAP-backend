import os
import mimetypes

from django.db.models.signals import m2m_changed, post_save, post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
from preview_generator.manager import PreviewManager
from BICAPweb.models import *


""" 
Metodo usato per gestire(creare e/o eliminare) i record della tabella 
Distribuzione che è la tabella che collega un utente ad un indagine.
"""
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


""" 
Meotodo richiamato dopo il salvataggio di una modifica o della creazione di un
InformazioneIndagine.
Questo metodo si occupa di ottenere e salvare il mime type e di creare una 
thumbnail.
"""        
@receiver(post_save, sender=InformazioneIndagine)
def post_save_InformazioneIndagine(sender, instance, **kwargs):
    post_save_informazione_helper(sender, instance)


""" 
Meotodo richiamato dopo il salvataggio di una modifica o della creazione di un
InformazioneQuestionario.
Questo metodo si occupa di ottenere e salvare il mime type e di creare una 
thumbnail se necessario.
""" 
@receiver(post_save, sender=InformazioneQuestionario)
def post_save_InformazioneQuestionario(sender, instance, **kwargs):
    post_save_informazione_helper(sender, instance)


"""
Metodo richiamato da post_save_InformazioneQuestionario e 
post_save_InformazioneIndagine che si occupa di ottenere e salvare il mime type
e di creare una thumbnail se necessario.
"""
def post_save_informazione_helper(sender, instance): 
    if instance.thumbnailUrl.name == '' or instance.tipoFile == '':
        if instance.tipoFile == '':
            set_tipoFile(sender, instance)
        if instance.thumbnailUrl.name == '':
            create_thumb(sender, instance)      
        instance.save()


"""
Metodo che ricava il tipo di mime dal nome del file caricato
"""
def set_tipoFile(sender, instance):
    instance.tipoFile = mimetypes.guess_type(instance.fileUrl.name)[0]


"""
Metodo che crea una thumbnail a partire da un file
"""
def create_thumb(sender, instance):
    #Se il file è un audio gli assegno una thumbnail prefatta
    if 'audio' in instance.tipoFile:
        instance.thumbnailUrl.name = '/thumb/audio.png'
    else:
        filepath = instance.fileUrl.file.name
        cache_path = settings.MEDIA_ROOT + '/thumb'
        manager = PreviewManager(cache_path, create_folder=True)
        FullPathToimage = manager.get_jpeg_preview(filepath)
        instance.thumbnailUrl.name = '/thumb/' + os.path.basename(FullPathToimage)


""" 
Metodo richiamato prima del salvataggio di una modifica ma anche prima della 
creazione di un InformazioneQuestionario.
Questo metodo si occupa di resettare il campo thumbnail e tipofile se è stato
caricato un file diverso da quello già presente nell'InformazioneQuestionario
presa in considerazione
""" 
@receiver(pre_save, sender=InformazioneQuestionario)
def pre_save_InformazioneQuestionario(sender, instance, **kwargs):
    reset_tipofile_and_thumbnail(sender, instance)

""" 
Metodo richiamato prima del salvataggio di una modifica ma anche prima della 
creazione di un InformazioneIndagine.
Questo metodo si occupa di resettare il campo thumbnail e tipofile se è stato
caricato un file diverso da quello già presente nell'InformazioneIndagine
presa in considerazione
""" 
@receiver(pre_save, sender=InformazioneIndagine)
def pre_save_InformazioneIndagine(sender, instance, **kwargs):
    reset_tipofile_and_thumbnail(sender, instance)


"""
Metodo per resettare il campo thumbnail e tipofile se necessario
"""
def reset_tipofile_and_thumbnail(sender, instance):
    old_Informazione = 	sender.objects.filter(pk=instance.pk).first()
    if old_Informazione != None and old_Informazione.fileUrl != instance.fileUrl:
        if instance.thumbnailUrl.name != '' or instance.tipoFile != '':          
            instance.tipoFile = ''
            instance.thumbnailUrl.name = ''
            instance.save()