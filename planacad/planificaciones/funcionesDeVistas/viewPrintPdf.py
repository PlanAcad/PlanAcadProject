from django.http import FileResponse
from django.views import View

class ViewPdfLibroRojo(View):
    def get(self, request, *args, **kwargs):
        filename = 'planificaciones/pdf/LIBRO-ROJO-DE-CONFEDI-Estandares-de-Segunda-Generacion-para-Ingenieria-2018-VFPublicada.pdf'
        response = FileResponse(open(filename, 'rb'), content_type='application/pdf')
        return response

class ViewPdfVerbosBloom(View):
    def get(self, request, *args, **kwargs):
        filename = 'planificaciones/pdf/Verbos-de-la-Taxonomia-de-Bloom.pdf'
        response = FileResponse(open(filename, 'rb'), content_type='application/pdf')
        return response