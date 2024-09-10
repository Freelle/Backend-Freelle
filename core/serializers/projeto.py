from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.models import Projeto

from uploader.models import Image
from uploader.serializers import ImageSerializer


class ProjetoSerializer(ModelSerializer):
    image_project_attachment_key = SlugRelatedField(
        source="image_project",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    image_project = ImageSerializer(
        required=False,
        read_only=True
    )
    class Meta:
        model = Projeto
        fields = "__all__"

class ProjetoDetailSerializer(ModelSerializer):
    class Meta:
        model = Projeto
        fields = "__all__"
        depth = 1

class ProjetoListSerializer(ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'descricao', 'status', 'categoria']