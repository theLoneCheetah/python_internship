from django.utils.deprecation import MiddlewareMixin
from .models import RequestLog

# перехват запроса для записи в базу данных
class RequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # получение IP клиента с другого устройства, последний адрес при работе обратного прокси
        remote_addr = request.META.get('HTTP_X_FORWARDED_FOR')
        print(remote_addr)
        if remote_addr:
            remote_addr = remote_addr.split(',')[0].strip()
        else:
            # при его отсутствии получение IP непосредственно обратившегося устройства или прокси
            remote_addr = request.META.get('REMOTE_ADDR', '')
        
        # сохранение информации о запросе в базу данных
        RequestLog.objects.create(
            method=request.method,
            path=request.path,
            remote_addr=remote_addr,
            query_params=request.GET.urlencode(),
        )
        return None
