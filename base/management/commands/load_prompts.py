import os
import re
from django.core.management.base import BaseCommand
from base.models import Prompt, Tag

prompt_pattern = '\d+\..'

class Command(BaseCommand):

    @staticmethod
    def create_tag(tag_name):
        tag_obj, created = Tag.objects.get_or_create(
            name=tag_name
        )
        return tag_obj

    @staticmethod
    def create_prompt(prompt_body, tag):
        prompt_obj, created = Prompt.objects.get_or_create(
            body=prompt_body,
        )
        prompt_obj.tag.add(*tag)
        return prompt_obj

    def handle(self, *args, **options):
        command_dir = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(command_dir, 'prompts.txt')
        current_tags = []
        with open(file_name) as r_file:
            data = r_file.readlines()
            for line in data:
                line = line.strip()
                match = re.search(prompt_pattern, line)
                if not match: # either an outlier or a tag
                    if re.search('".+"', line): #if outlier
                        self.create_prompt(line, current_tags)
                    else: #if tag
                        line = line.strip('\ufeff')
                        if line: # filter empty lines
                            if line.isupper(): # is a subcategory
                                line.capitalize()
                            else: # New category
                                current_tags.clear()

                            tag_instance = self.create_tag(line)
                            current_tags.append(tag_instance)
                else:
                    prompt = re.split(prompt_pattern, line)[1]
                    self.create_prompt(prompt, current_tags)