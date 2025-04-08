from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
import decimal

class Wilaya(models.Model):

    # Fields
    code = models.PositiveIntegerField(help_text='Code de la Wilaya', verbose_name='Code Wilaya', primary_key=True, 
        validators=[MinValueValidator(1), MaxValueValidator(15)])
    nom = models.CharField(max_length=200, help_text='Nom de la Wilaya', verbose_name='Nom', null=True, blank=True)

    class Meta:
        ordering = ['-code']

    # Methods
    def get_absolute_url(self):
        return reverse('wilaya-detail-view', args=[str(self.code)])

    def __str__(self):
        return str(self.code) + ' --- ' + self.nom


class Etablissement(models.Model):

    # Fields
    code = models.CharField(max_length=45, help_text='Code de l\'Etablissement', verbose_name='Code', primary_key=True)
    wilaya = models.ForeignKey('Wilaya', help_text='Wilaya de l\'Etablissement', verbose_name='Wilaya', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-code']

    # Methods
    def get_absolute_url(self):
        return reverse('etablissement-detail-view', args=[str(self.code)])


class CentreExam(models.Model):

    # Fields
    code = models.CharField(max_length=45, help_text='Code du Centre d\'Examen', verbose_name='Code', primary_key=True)
    wilaya = models.ForeignKey('Wilaya', help_text='Wilaya du Centre d\'Examen', verbose_name='Wilaya', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-code']

    # Methods
    def get_absolute_url(self):
        return reverse('centreexam-detail-view', args=[str(self.code)])

class Exam(models.Model):

    # Fields
    id = models.CharField(max_length=100, help_text='ID Examen', verbose_name='ID', primary_key=True)
    code = models.CharField(max_length=45, help_text='Code Examen', verbose_name='Code')
    serie = models.CharField(max_length=45, help_text='Serie Examen', verbose_name='Serie')

    class Meta:
        ordering = ['serie','code']
        constraints = [
            models.UniqueConstraint(
                fields=["code", "serie"], name="unique_code_serie"
            )
        ]

    # Methods
    def get_absolute_url(self):
        return reverse('exam-detail-view', args=[str(self.id)])

class Candidat(models.Model):

    # Fields
    id = models.CharField(max_length=100, help_text='ID Candidat', verbose_name='ID', primary_key=True)
    num_dossier = models.CharField(max_length=45, help_text='Numero dossier du candidat', verbose_name='Numero Dossier')
    annee = models.PositiveBigIntegerField(help_text='Annee de candidature', verbose_name='Annee',
        validators=[MinValueValidator(2000), MaxValueValidator(2035)])

    nom = models.CharField(max_length=245, help_text='Nom du candidat', verbose_name='Nom')
    prenom = models.CharField(max_length=245, help_text='Prenom du candidat', verbose_name='Prenom')
    date_naissance = models.DateField(null=True, blank=True, help_text='Date de naissance', verbose_name='Date de naissance')
    nni = models.CharField(max_length=10, help_text='NNI du candidat', verbose_name='NNI')
    
    APTITUDE_CHOICES = (
        ('I', 'Inapte'),
        ('A', 'Apte'),
    )

    TYPE_CANDIDAT_CHOICES = (
        ('CL', 'CL'),
        ('CP', 'CP'),
        ('OF', 'OF'),
    )

    aptitude = models.CharField(
        max_length=10,
        choices=APTITUDE_CHOICES,
        blank=True,
        null=True,
        help_text='Aptitude du candidat', 
        verbose_name='Aptitude'
    )

    type_candidature = models.CharField(
        max_length=10,
        choices=TYPE_CANDIDAT_CHOICES,
        blank=True,
        null=True,
        help_text='Type de Candidature', 
        verbose_name='Type de Candidature'
    )

    etablissement = models.ForeignKey('Etablissement', help_text='Etablissement du candidat', verbose_name='Etablissement', on_delete=models.SET_NULL, null=True)
    centre_exam = models.ForeignKey('CentreExam', help_text='Centre Examen du candidat', verbose_name='Centre Examen', on_delete=models.SET_NULL, null=True)

    TYPE_GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    sexe = models.CharField(
        max_length=1,
        choices=TYPE_GENDER_CHOICES,
        blank=True,
        null=True,
        help_text='Genre', 
        verbose_name='Genre'
    )

    class Meta:
        ordering = ['annee','num_dossier']
        constraints = [
            models.UniqueConstraint(
                fields=["annee", "num_dossier"], name="unique_annee_num_dossier"
            )
        ]

    # Methods
    def get_absolute_url(self):
        return reverse('candidat-detail-view', args=[str(self.id)])

class Resultat(models.Model):

    # Fields
    examen = models.ForeignKey('Exam', help_text='Examen', verbose_name='Examen', on_delete=models.CASCADE)
    candidat = models.ForeignKey('Candidat', help_text='Candidat', verbose_name='Candidat', on_delete=models.CASCADE)
    moyenne = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        validators=[
            MinValueValidator(decimal.Decimal(0)),
            MaxValueValidator(decimal.Decimal(20)),
        ],
    )
    decision = models.CharField(max_length=245)
    class Meta:
        ordering = ['examen','candidat']
        constraints = [
            models.UniqueConstraint(
                fields=["examen", "candidat"], name="unique_examen_candidat"
            )
        ]

    # Methods
    def get_absolute_url(self):
        return reverse('centreexam-detail-view', args=[str(self.code)])