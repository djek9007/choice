from rest_framework import serializers

from role.models import Role, RegionRole, DistrictRole, OrganizationRole


class RoleSerializer(serializers.ModelSerializer):
    """Серилайзер для таблицы ролей"""

    class Meta:
        model = Role
        fields = ('id', 'name',)



class RegionRoleSerializer(serializers.ModelSerializer):
    """Сериалайзер  для администраторов Области/города"""

    class Meta:
        model = RegionRole
        fields = ('id',
                  'user',
                  'role',
                  'region_role',

                  )


class DistrictRoleSerializer(serializers.ModelSerializer):
    """Сериалайзер для администраторов района"""
    class Meta:
        model = DistrictRole
        fields = ('id',
                  'user',
                  'role',
                  'region_role',
                  'district_role',

                  )

class OrganizationRoleSerializer(serializers.ModelSerializer):
    """Сериалайзер для администраторов организации"""
    class Meta:
        model = OrganizationRole
        fields = ('id',
                  'user',
                  'role',
                  'region_role',
                  'district_role',
                  'locality_role',
                  'organizations',

                  )
