from django.contrib.auth.models import User, Group
from django.http import JsonResponse, HttpResponse, Http404, request
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from first.models import WebPage, topics
from first.serializers import UserSerializer, GroupSerializer, WebPageSerializer, TopicSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @csrf_exempt
    def users_list(request):
        """
        List all code snippets, or create a new snippet.
        """
        if request.method == 'GET':
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def users_detail(request, pk):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = UserSerializer(user, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            user.delete()
            return HttpResponse(status=204)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# class WebPageViewSet(viewsets.ModelViewSet):
#     """
#         API endpoint that allows users to be viewed or edited.
#         """
#     queryset = WebPageSerializer.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#     @csrf_exempt
#     def users_list(request):
#         """
#         List all code snippets, or create a new snippet.
#         """
#         if request.method == 'GET':
#             user = User.objects.all()
#             serializer = UserSerializer(user, many=True)
#             return JsonResponse(serializer.data, safe=False)
#
#         elif request.method == 'POST':
#             data = JSONParser().parse(request)
#             serializer = UserSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status=201)
#             return JsonResponse(serializer.errors, status=400)
#
#     @csrf_exempt
#     def users_detail(request, pk):
#         """
#         Retrieve, update or delete a code snippet.
#         """
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return HttpResponse(status=404)
#
#         if request.method == 'GET':
#             serializer = UserSerializer(user)
#             return JsonResponse(serializer.data)
#
#         elif request.method == 'PUT':
#             data = JSONParser().parse(request)
#             serializer = UserSerializer(user, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data)
#             return JsonResponse(serializer.errors, status=400)
#
#         elif request.method == 'DELETE':
#             user.delete()
#             return HttpResponse(status=204)


class WebPageDetailViewSet(APIView):
    def get(self, request, pk, format=None):
        webPage = self.get_object(pk)
        serializer = WebPageSerializer(webPage)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return WebPage.objects.get(pk=pk)
        except WebPage.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = WebPageSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WebPageViewSet(APIView):
    def get(self, request, format=None):
        web_pages_objects = WebPage.objects.all()
        serializer = WebPageSerializer(web_pages_objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WebPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopicViewSet(APIView):
    def get(self, request, format=None):
        topics_objects = topics.objects.all()
        serializer = TopicSerializer(topics_objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
