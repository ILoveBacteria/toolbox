from django.urls import path

from engineer import views


urlpatterns = [
    path('footprint/', views.FootprintListView.as_view(), name='footprint_list'),
    path('footprint/<int:pk>/', views.FootprintDetailView.as_view(), name='footprint_detail'),
    path('footprint/extractor/', views.FootprintExtractor.as_view(), name='footprint_extractor'),
    path("vocab/", views.vocab_view, name="vocab"),
    path("vocab/update/", views.update_vocab, name="update_vocab"),
    path('add/', views.add_vocab_view, name='add_vocab'),
    path('list/', views.vocab_list_view, name='vocab_list'),
    path('update/', views.update_vocab_view, name='update_vocab'),
    path('edit/<int:vocab_id>/', views.edit_vocab_view, name='edit_vocab'),
    path('delete/<int:vocab_id>/', views.delete_vocab_view, name='delete_vocab'),
]
