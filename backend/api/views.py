from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BranchSerializer
from .models import Branch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

class apiOverview(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['ifsc']
    ordering = ['ifsc']
    search_fields = ['address', 'bank_id', 'branch', 'city', 'district', 'ifsc', 'state']
    pagination_class = LimitOffsetPagination
    

