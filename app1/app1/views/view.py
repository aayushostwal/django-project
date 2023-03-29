import time

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


def internal_function_1():
    time.sleep(2)


def internal_function_2():
    time.sleep(4)


class MyAPIView(APIView):

    def get(self, request: Request, *args, **kwargs) -> Response:
        internal_function_1()
        internal_function_2()
        return Response({"success": True}, status=200)
