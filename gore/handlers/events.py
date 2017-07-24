import json

from django.http import JsonResponse
from marshmallow import Schema, fields

from gore.models import Event


class EventSchema(Schema):
    class Meta:
        fields = ('id', 'message', 'culprit', 'level', 'type', 'timestamp', 'project_id')


class ProjectSchema(Schema):
    class Meta:
        fields = ('id', 'slug', 'name')


class EventDetailSchema(Schema):
    project = fields.Nested(ProjectSchema)
    data = fields.Method(serialize='get_data')

    class Meta:
        fields = ('id', 'message', 'culprit', 'level', 'type', 'timestamp', 'project', 'data')

    def get_data(self, instance):
        return instance.data_dict


def get_event_list(request):
    if not request.user.is_authenticated():
        return JsonResponse({'error': 'not authenticated'}, status=401)
    qs = Event.objects.all().defer('data').order_by('-id')
    return list(EventSchema().dump(qs, many=True).data)


def get_event_detail(request, id):
    if not request.user.is_authenticated():
        return JsonResponse({'error': 'not authenticated'}, status=401)
    event = Event.objects.get(pk=id)
    data = EventDetailSchema().dump(event).data
    return data
