from django.utils.deprecation import MiddlewareMixin

# перехват запроса для записи в базу данных
class RequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # сохранение инфомрации о запросе в базу данных
        RequestLog.objects.create(
            method=request.method,
            path=request.path,
            remote_addr=request.META.get('REMOTE_ADDR', ''),
            query_params=request.GET.urlencode(),
        )
        return None
