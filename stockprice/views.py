import requests
from django.conf import settings
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CompanyList
from .models import HistoricalData
from .serializers import StockSerializer


class StockListView(viewsets.ModelViewSet):
    serializer_class = StockSerializer

    # Below commented code will be used later for rendering the response to HTML
    '''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base.html'

    def list(self, request):
        if self.request.query_params.get("company", None):
            comp = self.request.query_params.get("company")
            company_id = CompanyList.objects.get(name=comp).id  # TODO: Handle when company not exist
            query_set = HistoricalData.objects.filter(companyId=company_id).order_by('-date')[:100]
        else:
            query_set = HistoricalData.objects.all().order_by('-date')[:100]
        return Response({'stocks': query_set})
    '''

    def get_queryset(self):
        comp = self.request.query_params.get("company", None)
        start_date = self.request.query_params.get("start", None)
        end_date = self.request.query_params.get("end", None)

        condition = {}

        if comp:
            try:
                company = CompanyList.objects.get(name=comp)
            except CompanyList.DoesNotExist:
                return CompanyList.objects.none()
            condition['companyId'] = company.id
        if start_date and end_date:
            condition['date__gte'] = start_date
            condition['date__lte'] = end_date

        return HistoricalData.objects.filter(**condition)


@api_view(('GET',))
def populate_data(request):
    if request.method == "GET":
        api_key = settings.API_KEY
        r = requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL,GOOG,"
                         "AMZN?apikey=%s" % api_key)
        if r.status_code == 200:
            data = r.json()
            for d in data['historicalStockList']:
                company, created = CompanyList.objects.get_or_create(name=d['symbol'])
                save_data(company.id, d['historical'])
            return Response("Requested data has been consumed.", status=status.HTTP_200_OK)
        else:
            return Response({"error": "Request Failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)


def save_data(comp_id, data):
    for i in data:
        i['companyId'] = comp_id
        HistoricalData(**i).save()
