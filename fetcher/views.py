from django.views.generic.list import ListView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework as filters

from .models import Video
from .serializers import VideoSerializer
from videofetcher.pagination import PaginationMixin

class VideoListAPI(APIView, PaginationMixin):
    """
    It returns a paginated response of video queryset containing
    ordered by decreasing publication date(Latest First order).
    """
    pagination_class = PageNumberPagination
    serializer_class = VideoSerializer
    
    def get(self, request, format=None):
        videos = Video.objects.all().order_by('-published_on')         
        page = self.paginate_queryset(videos)

        if page is not None:    
            serializers = VideoSerializer(page, many=True)
            return self.get_paginated_response(serializers.data)

        serializers = VideoSerializer(videos, many = True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

class VideoListGenericAPI(generics.ListAPIView):
    """
    Implementation of Dashboard API. It can filter out the queryset on basis of 
    channel name and title. Ordering would be done on basis published on or 
    created on date.
    """
    queryset = Video.objects.all().order_by('-published_on')
    serializer_class = VideoSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filter_fields = {
      'channel': ['iexact'],
      'title':['icontains'],
      'description':['icontains']
   }
    ordering_fields = ['published_on', 'created_on']

class VideoList(ListView):
    """
    Youtube Clone home page conatining list of youtube videos.
    """
    model = Video
    paginate_by = 16
    context_object_name = 'videos' 
    template_name = 'fetcher/youtube.html'

    def get_queryset(self, *args, **kwargs):
        videos = super(VideoList, self).get_queryset(*args, **kwargs)
        videos = videos.order_by("-created_on")
        search_key = self.request.GET.get('search')
        if search_key:
            videos = videos.filter(title__icontains = search_key)
        return videos

    def get_context_data(self, **kwargs):
        context = super(VideoList, self).get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search','')
        return context