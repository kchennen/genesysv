from django.urls import include, path
import core.views as core_views

urlpatterns = (
    path('dataset-snippet/<int:study_id>',
         core_views.DatasetSnippetView.as_view(), name='dataset-snippet'),
    path('filter-snippet/<int:dataset_id>',
         core_views.FilterSnippetView.as_view(), name='filter-snippet'),
    path('attribute-snippet/<int:dataset_id>',
         core_views.AttributeSnippetView.as_view(), name='attribute-snippet'),
    path('search-router/', core_views.SearchRouterView.as_view(), name='search-router'),
    path('base-search/', core_views.BaseSearchView.as_view(), name='base-search'),
    path('base-download/<int:search_log_id>', core_views.BaseDownloadView.as_view(), name='base-download'),
)
