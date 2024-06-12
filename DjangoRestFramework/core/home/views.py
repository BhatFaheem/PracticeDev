from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person


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


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def person(request):
    if request.method == "GET":
        objs = Person.objects.all()
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
