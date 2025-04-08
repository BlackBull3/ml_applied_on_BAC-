from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wilaya/<int:pk>', views.WilayaView.as_view(), name='wilaya-detail-view'),
    path('wilaya/add', views.WilayaCreate.as_view(), name='wilaya-create-view'),
    path('wilaya/', views.WilayaList.as_view(), name='wilaya-list-view'),
    path('wilaya/update/<int:pk>', views.WilayaUpdate.as_view(), name='wilaya-update'),
    path('wilaya/delete/<int:pk>', views.WilayaDelete.as_view(), name='wilaya-delete'),
    path('etablissement/add', views.EtablissementCreate.as_view(), name='etablissement-create-view'),
    path('etablissement/<slug:pk>', views.EtablissementView.as_view(), name='etablissement-detail-view'),
    path('etablissement/', views.EtablissementList.as_view(), name='etablissement-list-view'),
    path('etablissement/update/<slug:pk>', views.EtablissementUpdate.as_view(), name='etablissement-update'),
    path('etablissement/delete/<slug:pk>', views.EtablissementDelete.as_view(), name='etablissement-delete'),
]