from django.contrib import admin
from .models import Wilaya, Etablissement, CentreExam, Exam, Candidat, Resultat

admin.site.register(Wilaya)
admin.site.register(Etablissement)
admin.site.register(CentreExam)
admin.site.register(Exam)
admin.site.register(Candidat)
admin.site.register(Resultat)
