from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    sum = serializers.DecimalField(max_digits=50, decimal_places=2)
    name = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()