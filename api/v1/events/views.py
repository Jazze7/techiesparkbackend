from rest_framework.response import Response 
from rest_framework.decorators import api_view

from web.models import Event
from api.v1.events.serializers import EventSerializer
from api.v1.events.pagination import StandardResultsSetPagination

@api_view(["GET"])
def event(request):

    instances=Event.objects.all()

    # search for events
    q=request.GET.get('q')
    if q:
        instances=instances.filter(title__icontains=q)
    context={
        "request":request,
    }

    # pagination
    paginator=StandardResultsSetPagination()
    paginated_result=paginator.paginate_queryset(instances, request)


    serializer=EventSerializer(paginated_result,many=True,context=context)
    if instances:
        response_data={
            "status_code": 3000,
            "count": paginator.page.paginator.count,
            "links":{
                "next":paginator.get_next_link(),
                "previous":paginator.get_previous_link(),
            },
            "data": serializer.data
        }
        return  Response (response_data)
    else:
        response_data={
            "status_code": 6001,
            "data": "No data available"
        }
        return  Response (response_data)



# single events view
@api_view(["GET"])
def individual_event(request,pk):
    
    instances=Event.objects.filter(pk=pk)
    context={
        "request":request,
    }
    serializer=EventSerializer(instances,many=True,context=context)
    if instances:
        response_data={
            "status_code": 3000,
            "data": serializer.data
        }
        return  Response (response_data)
    else:
        response_data={
            "status_code": 6001,
            "data": "No data available"
        }
        return  Response (response_data)
