from rest_framework import serializers
from books import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Books
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Departments
        fields = "__all__"
