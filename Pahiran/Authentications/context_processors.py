from Authentications.models import CompanyDetails

def company_details(request):
    company_info = CompanyDetails.objects.first()  # fetch the first company
    return {
        'company_info': company_info,
    }