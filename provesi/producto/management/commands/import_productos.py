import csv
from django.core.management.base import BaseCommand
from producto.models import Producto

class Command(BaseCommand):
    help = "Import productos from CSV"

    def handle(self, *args, **kwargs):
        path = "provesi/datos/productos.csv"

        with open(path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)

            count = 0
            for row in reader:
                Producto.objects.create(
                    nombre=row["nombre"],
                    sku=row["sku"]
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f"Productos imported: {count}"))
