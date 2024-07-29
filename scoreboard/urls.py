from django.urls import path
from .views import ScoreList, get_top_scores, ScoresAboveThresholdView, ScoresBelowThresholdView, get_scores_in_range

urlpatterns = [
    path('scores/', ScoreList.as_view(), name='score-list'),
    path('scores/top/<int:top_n>/', get_top_scores, name='top-scores'),
    path('scores/above_threshold/<float:threshold>/', ScoresAboveThresholdView.as_view(), name='scores-above-threshold'),
    path('scores/below_threshold/<float:threshold>/', ScoresBelowThresholdView.as_view(), name='scores-below-threshold'),
    path('scores/range/<int:start>/<int:end>/', get_scores_in_range, name='scores-in-range'),
]
