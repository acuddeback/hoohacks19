# Import DRF
from rest_framework import serializers

# Import models
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )

# Student


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=True)

    class Meta:
        model = Student
        fields = (
            'pk',
            'user',
            'inCollege',
            'college',
            'major',
            'secondMaj',
            'minor',
            'secondMin',
            'hometown',
            'interests',
            'bio',
            'gradYear'
        )

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        student = Student.objects.update_or_create(user=user,
                                                   inCollege=validated_data.pop(
                                                       'inCollege'),
                                                   college=validated_data.pop(
                                                       'college'),
                                                   major=validated_data.pop(
                                                       'major'),
                                                   secondMaj=validated_data.pop(
                                                       'secondMaj'),
                                                   minor=validated_data.pop(
                                                       'minor'),
                                                   secondMin=validated_data.pop(
                                                       'secondMin'),
                                                   hometown=validated_data.pop(
                                                       'hometown'),
                                                   interests=validated_data.pop(
                                                       'interests'),
                                                   bio=validated_data.pop(
                                                       'bio'),
                                                   gradYear=validated_data.pop(
                                                       'gradYear')),
        return student

# School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            'pk',
            'name',
            'actCode',
            'state',
            'address',
            'website',
            'acceptanceRate',
            'gRatio',
            'fsRatio',
            'classSize',
            'imgUrl'
        )

# Ratio


class RatioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratio
        fields = (
            'pk',
            'numer',
            'denom',
        )

# Ratio


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = (
            'pk',
            'name',
        )
