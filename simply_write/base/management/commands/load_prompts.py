import csv
import os
from django.core.management.base import BaseCommand
from base.models import Prompt, Tag

class Command(BaseCommand):
    def handle(self, *args, **options):
        command_dir = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(command_dir, 'prompts.csv')
        with open(file_name) as r_file:
            data = csv.DictReader(r_file)
            for line in data:
                tags = line['Tone'].strip().split('|')
                prompt = line['Prompt']
                tag_objects = []
                for tag in tags:
                    tag_obj, created = Tag.objects.get_or_create(
                        name=tag.strip()
                    )
                    tag_objects.append(tag_obj)
                new_prompt = Prompt.objects.create(
                    body=prompt,
                )
                new_prompt.tag.set(tag_objects)