from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.modelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'completed')
        # Todo class에 설정해 놓은 내용을 가져와서 json 형식으로 어떤 것들을 보내줄지 설정. db column과 같음.