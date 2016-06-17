from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):
    return JsonResponse({
        'event': request.META['HTTP_X_GITHUB_EVENT'],
    })
