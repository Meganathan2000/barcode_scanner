from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from log_in import models as log_models
from django.http import JsonResponse
# def my_view(request):
#     context = {
#         'div_content': 'This is the content inside the <div> tag.',
#     }
#     return render(request, 'ucb_barcode_scanning.html', context)


class BarcodeScanner(TemplateView):
    template_path='ucb_barcode_scanning.html'
    def get(self,request,*args,**kwargs):
        try:
            context ={}
            return render(request, 'ucb_barcode_scanning.html', context)
        except Exception as e:
            print(e)
            
class StoreBarcode(View):
    def post(self,request,*args,**kwargs):
        try:
            print(request.POST)
            pdict = request.POST
            barcoede = log_models.data(barcode=pdict['scanned_barcode'])
            barcoede.save()
            barcoedls = list(log_models.data.objects.all().values_list('barcode',flat=True))
            return JsonResponse({'status':'getting','barcode_ls':barcoedls})
        except Exception as e:
            print(e)