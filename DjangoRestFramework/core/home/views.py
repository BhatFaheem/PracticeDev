from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer, LoginSerializer, RegisterSerializer
from .models import Person
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth.models import User


class RegisterAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                {"status": False, "message": serializer.errors},
                status.HTTP_400_BAD_REQUEST,
            )
        serializer.save()
        return Response(
            {"status": True, "message": "User Created Successfully"},
            status.HTTP_201_CREATED,
        )


@api_view(["GET", "POST"])
def index(request):
    courses = {
        "course_name": "python",
        "learn": ["Django", "Flask", "FastAPi"],
        "course_provider": "Scalar",
    }
    if request.method == "GET":
        print("We used a Get Method")
        return Response(courses)
    if request.method == "POST":
        data = request.data
        # print(data)
        print("We used a POST Method")
        return Response(courses)


@api_view(["POST"])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.data
        print(data)
        return Response({"message": "Success"})
    return Response(serializer.errors)


class PersonAPI(APIView):
    def get(self, request):
        objs = Person.objects.filter(color__isnull=False)
        serializer = PersonSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = Person.objects.get(id=data["id"])
        serializer = PersonSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        obj = Person.objects.get(id=data["id"])
        obj.delete()
        return Response({"message": "Person Deleted Successfully"})


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def person(request):
    if request.method == "GET":
        objs = Person.objects.filter(color__isnull=False)
        serializer = PersonSerializer(objs, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PUT":
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PATCH":
        data = request.data
        obj = Person.objects.get(id=data["id"])
        serializer = PersonSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id=data["id"])
        obj.delete()
        return Response({"message": "Person Deleted Successfully"})


class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get("search")
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__startswith=search)
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
