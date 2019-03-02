# First external includes
from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

# Import all responses needed
from .responses import *

# Import Models
from .models import *

# Import Serializers
from .serializers import *


# User Set
class StudentViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    model = Student

    '''
    __________________________________________________  Delete
     url: DELETE : <WEBSITE>/api/student/pk
     function: Deletes a student
    __________________________________________________
    '''

    def delete(self, request, format=None, pk=None):
        if pk is None:
            return missing_id_response()
        else:
            try:
                result = self.model.objects.get(pk=pk)
                result.delete()
            except self.model.DoesNotExist:
                return object_not_found_response()
            except IntegrityError:
                return object_is_foreign_key_response()

            return successful_delete_response()

    '''
    __________________________________________________  get
     url: GET : <WEBSITE>/api/student/
     function: Returns list of all student

     url: GET : <WEBSITE>/api/student/pk
     function: returns details on one student
    __________________________________________________
    '''

    def get(self, request, format=None, pk=None):
        # print(pk)
        is_many = True
        if pk is None:
            result = self.model.objects.all()
        else:
            try:
                result = self.model.objects.get(pk=pk)
                # print(result)
                is_many = False
            except self.model.DoesNotExist:
                return object_not_found_response()

        serializer = self.serializer_class(result, many=is_many)
        return successful_create_response(serializer.data)

    '''
    __________________________________________________  Post
     url: POST : <WEBSITE>/api/student/
     Body:
     {
        "user":{
            "username":"test",
            "first_name": "Chad",
            "last_name": "Baily",
            "email":"test@test2.com"
        },
        "address":"1912 Stadium Road Charlottesville Va",
        "canSell": false
    }
    function: Creates a student and user. Associates user to student
    __________________________________________________
    '''

    def post(self, request, format=None, pk=None):
        if pk is None:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return invalid_serializer_response(serializer.errors)

            serializer.save()
            return successful_create_response(request.data)
        else:
            return colliding_id_response()

    '''
    __________________________________________________  Put
     url: PUT : <WEBSITE>/api/student/pk
     function: Updates a student
    __________________________________________________
    '''

    def put(self, request, format=None, pk=None):
        if pk is None:
            return missing_id_response()
        else:
            try:
                result = self.model.objects.get(pk=pk)
            except self.model.DoesNotExist:
                return object_not_found_response()

            serializer = self.serializer_class(result, data=request.data)

            if not serializer.is_valid():
                return invalid_serializer_response(serializer.errors)

            serializer.save()
            return successful_edit_response(serializer.data)


# School Set
class SchoolViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    model = School

    '''
    __________________________________________________  Delete
     url: DELETE : <WEBSITE>/api/school/pk
     function: Deletes a school
    __________________________________________________
    '''

    def delete(self, request, format=None, pk=None):
        if pk is None:
            return missing_id_response()
        else:
            try:
                result = self.model.objects.get(pk=pk)
                result.delete()
            except self.model.DoesNotExist:
                return object_not_found_response()
            except IntegrityError:
                return object_is_foreign_key_response()

            return successful_delete_response()

    '''
    __________________________________________________  get
     url: GET : <WEBSITE>/api/school/
     function: Returns list of all school

     url: GET : <WEBSITE>/api/school/pk
     function: returns details on one school
    __________________________________________________
    '''

    def get(self, request, format=None, pk=None):
        # print(pk)
        is_many = True
        if pk is None:
            result = self.model.objects.all()
        else:
            try:
                result = self.model.objects.get(pk=pk)
                # print(result)
                is_many = False
            except self.model.DoesNotExist:
                return object_not_found_response()

        serializer = self.serializer_class(result, many=is_many)
        return successful_create_response(serializer.data)

    '''
    __________________________________________________  Post
     url: POST : <WEBSITE>/api/school/
     Body:
     {
        "user":{
            "username":"test",
            "first_name": "Chad",
            "last_name": "Baily",
            "email":"test@test2.com"
        },
        "address":"1912 Stadium Road Charlottesville Va",
        "canSell": false
    }
    function: Creates a student and user. Associates user to student
    __________________________________________________
    '''

    def post(self, request, format=None, pk=None):
        if pk is None:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return invalid_serializer_response(serializer.errors)

            serializer.save()
            return successful_create_response(request.data)
        else:
            return colliding_id_response()

    '''
    __________________________________________________  Put
     url: PUT : <WEBSITE>/api/school/pk
     function: Updates a school
    __________________________________________________
    '''

    def put(self, request, format=None, pk=None):
        if pk is None:
            return missing_id_response()
        else:
            try:
                result = self.model.objects.get(pk=pk)
            except self.model.DoesNotExist:
                return object_not_found_response()

            serializer = self.serializer_class(result, data=request.data)

            if not serializer.is_valid():
                return invalid_serializer_response(serializer.errors)

            serializer.save()
            return successful_edit_response(serializer.data)


# major Set
class MajorViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    model = Major

    '''
    __________________________________________________  Delete
     url: DELETE : <WEBSITE>/api/major/pk
     function: Deletes a major
    __________________________________________________
    '''

    def delete(self, request, format=None, pk=None):
        if pk is None:
            return missing_id_response()
        else:
            try:
                result = self.model.objects.get(pk=pk)
                result.delete()
            except self.model.DoesNotExist:
                return object_not_found_response()
            except IntegrityError:
                return object_is_foreign_key_response()

            return successful_delete_response()

    '''
    __________________________________________________  get
     url: GET : <WEBSITE>/api/major/
     function: Returns list of all major

     url: GET : <WEBSITE>/api/major/pk
     function: returns details on one major
    __________________________________________________
    '''

    def get(self, request, format=None, pk=None):
        # print(pk)
        is_many = True
        if pk is None:
            result = self.model.objects.all()
        else:
            try:
                result = self.model.objects.get(pk=pk)
                # print(result)
                is_many = False
            except self.model.DoesNotExist:
                return object_not_found_response()

        serializer = self.serializer_class(result, many=is_many)
        return successful_create_response(serializer.data)

    '''
    __________________________________________________  Post
     url: POST : <WEBSITE>/api/major/
     Body:
     {
        "user":{
            "username":"test",
            "first_name": "Chad",
            "last_name": "Baily",
            "email":"test@test2.com"
        },
        "address":"1912 Stadium Road Charlottesville Va",
        "canSell": false
    }
    function: Creates a student and user. Associates user to student
    __________________________________________________
    '''

    def post(self, request, format=None, pk=None):
        if pk is None:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return invalid_serializer_response(serializer.errors)

            serializer.save()
            return successful_create_response(request.data)
        else:
            return colliding_id_response()

    '''
    __________________________________________________  Put
     url: PUT : <WEBSITE>/api/major/pk
     function: Updates a major
    __________________________________________________
    '''

    def put(self, request, format=None, pk=None):
        if pk is None:
            return missing_id_response()
        else:
            try:
                result = self.model.objects.get(pk=pk)
            except self.model.DoesNotExist:
                return object_not_found_response()

            serializer = self.serializer_class(result, data=request.data)

            if not serializer.is_valid():
                return invalid_serializer_response(serializer.errors)

            serializer.save()
            return successful_edit_response(serializer.data)


# Ratio Set
class RatioViewSet(viewsets.ModelViewSet):
    renderer_classes = (JSONRenderer, )
    queryset = Ratio.objects.all()
    serializer_class = RatioSerializer
    model = Ratio

    '''
    __________________________________________________  Delete
     url: DELETE : <WEBSITE>/api/ratio/pk
     function: Deletes a ratio
    __________________________________________________
    '''

    def delete(self, request, format=None, pk=None):
        if pk is None:
            return missing_id_response()
        else:
            try:
                result = self.model.objects.get(pk=pk)
                result.delete()
            except self.model.DoesNotExist:
                return object_not_found_response()
            except IntegrityError:
                return object_is_foreign_key_response()

            return successful_delete_response()

    '''
    __________________________________________________  get
     url: GET : <WEBSITE>/api/ratio/
     function: Returns list of all ratio

     url: GET : <WEBSITE>/api/ratio/pk
     function: returns details on one ratio
    __________________________________________________
    '''

    def get(self, request, format=None, pk=None):
        # print(pk)
        is_many = True
        if pk is None:
            result = self.model.objects.all()
        else:
            try:
                result = self.model.objects.get(pk=pk)
                # print(result)
                is_many = False
            except self.model.DoesNotExist:
                return object_not_found_response()

        serializer = self.serializer_class(result, many=is_many)
        return successful_create_response(serializer.data)

    '''
    __________________________________________________  Post
     url: POST : <WEBSITE>/api/ratio/
     Body:
     {
        "user":{
            "username":"test",
            "first_name": "Chad",
            "last_name": "Baily",
            "email":"test@test2.com"
        },
        "address":"1912 Stadium Road Charlottesville Va",
        "canSell": false
    }
    function: Creates a student and user. Associates user to student
    __________________________________________________
    '''

    def post(self, request, format=None, pk=None):
        if pk is None:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return invalid_serializer_response(serializer.errors)

            serializer.save()
            return successful_create_response(request.data)
        else:
            return colliding_id_response()

    '''
    __________________________________________________  Put
     url: PUT : <WEBSITE>/api/ratio/pk
     function: Updates a ratio
    __________________________________________________
    '''

    def put(self, request, format=None, pk=None):
        if pk is None:
            return missing_id_response()
        else:
            try:
                result = self.model.objects.get(pk=pk)
            except self.model.DoesNotExist:
                return object_not_found_response()

            serializer = self.serializer_class(result, data=request.data)

            if not serializer.is_valid():
                return invalid_serializer_response(serializer.errors)

            serializer.save()
            return successful_edit_response(serializer.data)
