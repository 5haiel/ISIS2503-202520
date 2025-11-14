import csv
from django.core.management.base import BaseCommand
from users.models import Usuario

class Command(BaseCommand):
    help = "Import usuarios from CSV"

    def handle(self, *args, **kwargs):
        path = "datos/usuarios.csv"  # adjust if needed

        with open(path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)

            count = 0
            for row in reader:
                Usuario.objects.create(
                    nombre=row["nombre"],
                    correo=row["correo"],
                    telefono=row["telefono"],
                    direccion_entrega=row["direccion_entrega"],
                    ciudad=row["ciudad"],
                    codigo_postal=row["codigo_postal"],
                    pais=row["pais"],
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f"Usuarios imported: {count}"))
