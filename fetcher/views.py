from .models import Video
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VideoSerializer
from videofetcher.pagination import PaginationMixin
from rest_framework.pagination import PageNumberPagination

class VideoListAPI(APIView, PaginationMixin):
    pagination_class = PageNumberPagination

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        videos = Video.objects.all().order_by('-published_on')
        
        search = request.query_params.get('search')
        if search:
            videos = videos.filter(title__icontains = search)
            
        page = self.paginate_queryset(videos)

        if page is not None:    
            serializers = VideoSerializer(page, many=True)
            return self.get_paginated_response(serializers.data)

        serializers = VideoSerializer(videos, many = True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)