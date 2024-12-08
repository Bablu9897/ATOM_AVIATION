import csv
from blog.models import BlogPost
import pandas as pd
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import blog posts from a CSV file'

    def add_arguments(self, parser):
        """
            Add logic to add argument for passing the csv file
        """
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        """
            populate the database with the same data from data/blog_post.csv
            Style the output so that errors are shown in red and a successfull import is in green.
        """
        csv_file = kwargs['csv_file']

        # Option 1: Using pandas to read the CSV
        try:
            data = pd.read_csv(csv_file)
            for index, row in data.iterrows():
                # You can adjust this part to match your model fields
                BlogPost.objects.create(
                    title=row['title'],  # Adjust column name based on your CSV file
                    content=row['content'],
                    country=row['country']
                )
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(data)} rows"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error importing CSV: {e}"))

        