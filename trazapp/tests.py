from django.test import TestCase

from .models import RegistroActividad


class RegistroActividadModelTests(TestCase):
    def test_registro_actividad_se_puede_importar_desde_models(self):
        self.assertTrue(hasattr(RegistroActividad, "_meta"))
