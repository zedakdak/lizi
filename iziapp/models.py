from django.db import models


# Customer : classe pour le client
# Uniquement avec le champ 'Name' pour permettre la mise au point
# ajoout pour git encore
class Customer(models.Model):
    """
    Cette classe represente le client
    """
    name = models.CharField(max_length=20, blank=True, default='')
    email = models.CharField(max_length=20, blank=True, default='')   

# Classe : classe pour la en-tete de facture
class Invoice(models.Model):
    """
    Classe represente la facture du client
    """
    #import pdb; pdb.set_trace()
    name = models.CharField(max_length=20, blank=True, default='')


class InvoiceItem(models.Model):
    """
    Classe postes de la facture
    """
    invoice = models.ForeignKey(Invoice, related_name='invoiceitems')
    creation_date = models.DateField()

    def __unicode__(self):
        return '%s' % (self.creation_date)


