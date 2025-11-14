import csv
from django.core.management.base import BaseCommand
from orders.models import Orders
from users.models import Usuario
from producto.models import Producto

class Command(BaseCommand):
    help = "Import orders from CSV"

    def handle(self, *args, **kwargs):
        path = "datos/ordenes.csv"

        with open(path, newline='', encoding="utf-8") as f:
            reader = csv.DictReader(f)

            count = 0
            for row in reader:
                try:
                    producto = Producto.objects.get(pk=row["producto_id"])
                    usuario = Usuario.objects.get(pk=row["usuario_id"])

                    Orders.objects.create(
                        cantidad=row["cantidad"],
                        ubicacion=row["ubicacion"],
                        estado=row["estado"],
                        producto=producto,
                        usuario=usuario
                    )
                    count += 1

                except Producto.DoesNotExist:
                    self.stdout.write(self.style.ERROR(
                        f"Producto ID {row['producto_id']} no existe — fila saltada."
                    ))

                except Usuario.DoesNotExist:
                    self.stdout.write(self.style.ERROR(
                        f"Usuario ID {row['usuario_id']} no existe — fila saltada."
                    ))

        self.stdout.write(self.style.SUCCESS(f"Orders imported: {count}"))
