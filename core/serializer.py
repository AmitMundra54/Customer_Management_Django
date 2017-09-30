import json

from rest_framework import serializers
from core.models import User, Address, Organisation, Role, Department, PhoneNumber


class AddressReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('city', 'state','postal_code')


class OrganisationReadSerializer(serializers.ModelSerializer):
    organisationAddress = AddressReadSerializer(many=True)

    class Meta:
        model = Organisation
        fields = ('name','type','organisationAddress')


class DepartmentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'description')


class ContactReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('phone_number',)


class RoleReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('title','description')


class UserReadSerializer(serializers.ModelSerializer):
    organisation = OrganisationReadSerializer(many=True)
    department = DepartmentReadSerializer(many=True)
    address = AddressReadSerializer(many=True)
    user_contact_no = ContactReadSerializer(many=True)
    role = RoleReadSerializer(many=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name','gender','date_of_birth','organisation','department','personal_email',
                  'address','role','designation','user_contact_no',)

    def create(self, validated_data):
        print "validateVAL",validated_data

        address = validated_data.pop('address')
        address_dict = dict(address[0])

        organisation = validated_data.pop('organisation')
        organisation_dict = dict(organisation[0])
        contact = validated_data.pop('user_contact_no')
        contact_dict = dict(contact[0])
        print "FFFF----------------",contact_dict,contact_dict['phone_number']
        print "organisation",organisation_dict
        department = validated_data.pop('department')
        department_dict = dict(department[0])

        role = validated_data.pop('role')
        role_dict = dict(role[0])
        print "roler",role
        user = User.objects.create(**validated_data)
        # print "RRRRRRR",user,type(user)
        contact_obj = PhoneNumber.objects.create(user=user,
                                             phone_number = contact_dict['phone_number'])
        contact_obj.user = user

        department_obj = Department.objects.create(user=user,
                                                   name=department_dict['name'],
                                                   description = department_dict['description'])
        department_obj.user = user
        address_obj = Address.objects.create(user=user,
                                             city=address_dict['city'],
                                             state = address_dict['state'],
                                             postal_code = address_dict['postal_code']
                                            )
        address_obj.user = user
        organisation_obj = Organisation.objects.create(user=user,

                                                    name=organisation_dict['name'],
                                                    type=organisation_dict['type']
                                                   )
        organisation_obj.user = user
        role_obj = Role.objects.create(user=user,
                                       title=role_dict['title'],
                                       description=role_dict['description'])
        role_obj.user = user

        return self.to_representation(user)


    def update(self, instance, validated_data):
        print "Instance",instance
        print "validateddata",validated_data

