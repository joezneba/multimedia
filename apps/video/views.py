import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models as mod

# Create your views here.
''' Muestra la página de inicio con todos los videos '''
#@login_required()
def index(request):
    ctx = {}
    datos = mod.Video.objects.filter(Q(activo=True)
                                     & Q(tipo_video_id__activo=True)
                                     & Q(categoria_id__activo=True)).order_by('pk').reverse()
    paginator = Paginator(datos, 12)
    page = request.GET.get('page')

    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    cat = obtenerCategorias()
    tipo_video = obtenerTipoVideos()

    ctx['videos'] = videos
    ctx['categorias'] = cat
    ctx['tipo_video'] = tipo_video
    return render(request, 'video/catalogo.html', ctx)

''' Reproductor de video '''
#@login_required()
def reproductor(request, id_video):
    ctx = {}
    video = mod.Video.objects.get(pk=id_video)
    cat = obtenerCategorias()
    tipo_video = obtenerTipoVideos()
    ctx['video'] = video
    ctx['categorias'] = cat
    ctx['tipo_video'] = tipo_video

    return render(request, 'video/reproductor.html',ctx)

''' Devuelve todas las categorías de videos activas '''
def obtenerCategorias():
    cat = mod.Categoria.objects.filter(activo=True).order_by('nombre_categoria')
    return cat

''' Mostrar videos según la categoría seleccionada '''
#@login_required()
def filtroCategorias(request, id_categoria):
    ctx = {}
    videos = mod.Video.objects.filter(Q(activo=True) & Q(categoria_id=id_categoria)).order_by('nombre')
    cat_actual = mod.Categoria.objects.get(pk = id_categoria)
    cat = obtenerCategorias()
    tipo_video = obtenerTipoVideos()
    ctx['videos'] = videos
    ctx['categorias'] = cat
    ctx['categoria_actual'] = cat_actual
    ctx['tipo_video'] = tipo_video
    return render(request, 'video/catalogo.html', ctx)

''' Devuelve los tipos de videos activos '''
def obtenerTipoVideos():
    tipo = mod.TipoVideo.objects.filter(activo=True).order_by('nombre')
    return tipo

''' Búsqueda de videos por nombre '''
def buscarVideo(request):
    busqueda = request.GET['nombre']
    if len(busqueda)>0 :
        if request.is_ajax():
            video = mod.Video.objects.filter(nombre__startswith=busqueda.title()).values('nombre', 'pk')
            return HttpResponse(json.dumps(list(video)), content_type='application/json')
        else:
            return HttpResponse('Solo Ajax')
    else:
        return HttpResponse(json.dumps(list()), content_type='application/json')
