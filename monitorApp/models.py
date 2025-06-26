from django.db import models

class Detecta(models.Model):
    id_detecta = models.AutoField(primary_key=True)
    total = models.IntegerField()
    oras = models.DateTimeField()

    def __str__(self):
        return f"Detecta {self.id_detecta} at {self.oras} (Total: {self.total})"

class Class(models.Model):
    id_class = models.AutoField(primary_key=True)
    naran_class = models.CharField(max_length=20, choices=[
        ("SVU", "SVU"),
        ("motor", "motor"),
        ("kareta", "kareta"),
        ("tricycle", "tricycle"),
        ("bemo", "bemo"),
        ("taxi", "taxi"),
        ("truck","truck"),
    ])

    def __str__(self):
        return self.naran_class

class DetailDetail(models.Model):
    id_detecta = models.ForeignKey(Detecta, on_delete=models.CASCADE)
    id_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = (('id_detecta', 'id_class'),)

    def __str__(self):
        return f"Detecta {self.id_detecta.id_detecta} - Class {self.id_class.naran_class}: {self.quantity}" 
