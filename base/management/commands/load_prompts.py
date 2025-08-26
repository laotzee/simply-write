import os
import re
from django.core.management.base import BaseCommand
from base.models import Prompt, Tag

prompt_pattern = r'\d+\. '
outlier_prompt = r'[\'"“]'

class Command(BaseCommand):

    @staticmethod
    def count_iterr(iterr, reverse=False):
        """Create a new list of tuples containing the length of the item, and the item itself sorted by length"""
        counted_iterr = [(len(item), item) for item in iterr]
        counted_iterr.sort(reverse=reverse, key=lambda item: item[0])
        return counted_iterr

    @staticmethod
    def create_tag(tag_name):
        tag_obj, created = Tag.objects.get_or_create(
            name=tag_name
        )
        return tag_obj

    @staticmethod
    def create_prompt(prompt_body, tag_instances):
        prompt_obj, created = Prompt.objects.get_or_create(
            body=prompt_body,
        )
        prompt_obj.tag.add(*tag_instances)
        return prompt_obj

    def handle(self, *args, **options):
        command_dir = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(command_dir, 'prompts.txt')
        current_tags = []
        with open(file_name) as r_file:
            data = r_file.readlines()
            for raw_line in data:
                line = raw_line.strip()
                line = line.strip('\ufeff')
                if re.search(prompt_pattern, line):
                    prompt = line.split('. ', maxsplit=1)[1]
                    prompt_instance = self.create_prompt(prompt, current_tags)
                elif re.search(outlier_prompt, line):
                    prompt_instance = self.create_prompt(line, current_tags)
                else:
                    if line: # filter blanks
                        tag_instance = self.create_tag(line.capitalize())
                        if line.isupper() and len(current_tags) == 1: # Sub cat of the current cat
                            current_tags.append(tag_instance)
                        elif line.isupper() and len(current_tags) > 1: # Another sub category of the current cat
                            current_tags[1] = tag_instance
                        else: # Completely new cat
                            current_tags.clear()
                            current_tags.append(tag_instance)