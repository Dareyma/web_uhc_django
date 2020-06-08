from django.shortcuts import render
from django.views import View

from django.urls import reverse_lazy
import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

# from gestion.models import Juega
# Está comentado dado que me da fallo y estoy tocando cosas de permisos

class PartidaInvoicePdfView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('pdf/partida_pdf.html')
            context = {
                'juega': Juega.objects.get(pk=self.kwargs['pk'])
                }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('gestion:partidas'))
