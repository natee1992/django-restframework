import json

from django.views.generic.base import View
from django.http.response import HttpResponse

from .models import Music


# class MusicListView(View):
#     '''
#     通过django的view获取商品列表页
#     '''

#     def get(self, request):
#         json_list = []
#         musics = Music.objects.all()[:10]
#         for music in musics:
#             json_dict = {}
#             json_dict['song'] = music.song
#             json_dict['singer'] = music.singer
#             json_list.append(json_dict)
#         return HttpResponse(json.dumps(json_list),content_type='application/json')

# from django.forms.models import model_to_dict


# class MusicListView(View):
#     '''
#     通过django的view获取商品列表页
#     '''

#     def get(self, request):
#         json_list = []
#         musics = Music.objects.all()[:10]
#         for music in musics:
#             json_dict = model_to_dict(music)
#             json_list.append(json_dict)
#         return HttpResponse(json.dumps(json_list), content_type='application/json')

from django.core import serializers
from django.http.response import JsonResponse


class MusicListView(View):
    '''
    通过django的view获取商品列表页
    '''

    def get(self, request):
        musics = Music.objects.all()[:10]
        json_data = serializers.serialize('json', musics)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
