from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Rename the Django project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str,
                            help='Add new project name')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # rename the project

        file_to_rename = ['demo/settings.py', 'demo/wsgi.py', 'manage.py']
        folder_to_rename = 'demo'

        for f in file_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('demo', new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)

        # console output success

        self.stdout.write(self.style.SUCCESS(
            'project has ben renamed to %a' % new_project_name))
