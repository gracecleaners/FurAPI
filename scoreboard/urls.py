from django.urls import path
from .views import ScoreList, get_top_scores, get_scores_above_threshold, ScoresBelowThresholdView, get_scores_in_range

urlpatterns = [
    path('scores/', ScoreList.as_view(), name='score-list'),
    path('scores/top/<int:top_n>/', get_top_scores, name='top-scores'),
    path('scores/above/<float:threshold>/', get_scores_above_threshold, name='scores-above-threshold'),
    path('scores/below/<float:threshold>/', ScoresBelowThresholdView.as_view(), name='scores-below-threshold'),
    path('scores/vgb/<int:start>/<int:end>/', get_scores_in_range, name='scores-in-range'),
]
