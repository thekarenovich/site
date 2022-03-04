from django.http import HttpResponse
from bboard.models import Bb

'''
def index(request):
    return HttpResponse("Здесь будет выведен список объявлений.")
'''

def index(request):
    s = 'Список объявлений\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')


