# from django.http import JsonResponse
# # Create your views here.
# def estudantes(request):
#     if request.method == 'GET':
#             estudante = {
#                 'id':'2',
#                 'nome':'senai'
#             }
#     return JsonResponse(estudante)
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer, MatriculaSerializer,ListaMatriculasEstudanteSerializer,ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

