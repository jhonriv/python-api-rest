from django.views import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import json

# Create your views here.
class CompanyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = 0):
        result = []
        if (id > 0):
            company = list(Company.objects.filter(id=id).values())
            if (len(company) > 0): result = { "company": company[0] }
            else: result = { "message": "company not found" }
            return JsonResponse(result)
        
        companies = list(Company.objects.values())
        if (len(companies) > 0): result = companies
        return JsonResponse({ "companies": result })
        
    
    def post(self, request):
        data = json.loads(request.body)
        Company.objects.create(name = data['name'], website = data['website'], foundation = data['foundation'])
        return JsonResponse({ "message": "company created" })
    
    def put(self, request, id):
        data = json.loads(request.body)
        company = Company.objects.get(id = id)
        company.name = data['name']
        company.website = data['website']
        company.foundation = data['foundation']
        company.save()
        return JsonResponse({ "message": "company updated" })
    
    def delete(seft, request, id):
        Company.objects.filter(id = id).delete()
        return JsonResponse({ "message": "company deleted"})