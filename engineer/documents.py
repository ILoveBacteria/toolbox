from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from engineer.models import Footprint


@registry.register_document
class FootprintDocument(Document):
    class Index:
        name = 'footprints'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Footprint
        fields = ['title', 'tags', 'url']
