from rest_framework import serializers
from.models import Super

class SuperSerializer (serializers.ModelSerializer):
    class Meta:
        fields=['id','name','alter_ego','primary_ability','secondary_ability', 'cathphrase','super_type']