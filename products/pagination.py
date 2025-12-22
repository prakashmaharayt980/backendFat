from rest_framework.pagination import PageNumberPagination

class ProductsPagination(PageNumberPagination):
    page_size = 3                 # Default items per page
    page_size_query_param = 'page_size'
    max_page_size = 3
