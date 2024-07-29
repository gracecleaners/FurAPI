from rest_framework import generics
from .models import Score
from .serializers import ScoreSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class ScoresBelowThresholdView(APIView):
    def get(self, request, threshold):
        try:
            threshold = float(threshold)
        except ValueError:
            return Response({"error": "Invalid threshold value"}, status=status.HTTP_400_BAD_REQUEST)

        scores = Score.objects.filter(survive_seconds__lt=threshold).order_by('-survive_seconds')
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_top_scores(request, top_n):
    top_scores = Score.objects.all().order_by('-survive_seconds')[:top_n]
    serializer = ScoreSerializer(top_scores, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_scores_above_threshold(request, threshold):
    scores = Score.objects.filter(survive_seconds__gt=threshold).order_by('-survive_seconds')
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_scores_in_range(request, start, end):
    scores = Score.objects.all().order_by('-survive_seconds')[start:end]
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)
