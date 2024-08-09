from rest_framework.pagination import PageNumberPagination


class Small1SetPagination(PageNumberPagination):
    page_query_param ='p'
    page_size =6
    page_size_query_param = 'page_size'
    max_page_size = 6


class Medium1SetPagination(PageNumberPagination):
    page_query_param ='p'
    page_size =9
    page_size_query_param = 'page_size'
    max_page_size = 9

class Large1SetPagination(PageNumberPagination):
    page_query_param ='p'
    page_size =18
    page_size_query_param = 'page_size'
    max_page_size = 18

class Small2SetPagination(PageNumberPagination):
    page_query_param ='p'
    page_size =25
    page_size_query_param = 'page_size'
    max_page_size = 25


class Medium2SetPagination(PageNumberPagination):
    page_query_param ='p'
    page_size =50
    page_size_query_param = 'page_size'
    max_page_size = 50

class Large2SetPagination(PageNumberPagination):
    page_query_param ='p'
    page_size =100
    page_size_query_param = 'page_size'
    max_page_size = 100