from django.http import JsonResponse
from worldboss.models import UploadedData

def get_vote_counts(request, id):
    try:
        spawn = UploadedData.objects.get(id=id)
        response = {
            'success': True,
            'thumbs_up': spawn.thumbs_up,
            'thumbs_down': spawn.thumbs_down,
        }
        return JsonResponse(response)
    except UploadedData.DoesNotExist:
        response = {'success': False, 'message': 'Spawn does not exist'}
        return JsonResponse(response)
