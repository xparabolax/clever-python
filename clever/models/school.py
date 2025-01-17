# coding: utf-8

"""
    Clever API

    The Clever API  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from clever.models.location import Location  # noqa: F401,E501
from clever.models.principal import Principal  # noqa: F401,E501


class School(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created': 'str',
        'district': 'str',
        'ext': 'object',
        'high_grade': 'str',
        'id': 'str',
        'last_modified': 'str',
        'location': 'Location',
        'low_grade': 'str',
        'mdr_number': 'str',
        'name': 'str',
        'nces_id': 'str',
        'phone': 'str',
        'principal': 'Principal',
        'school_number': 'str',
        'sis_id': 'str',
        'state_id': 'str'
    }

    attribute_map = {
        'created': 'created',
        'district': 'district',
        'ext': 'ext',
        'high_grade': 'high_grade',
        'id': 'id',
        'last_modified': 'last_modified',
        'location': 'location',
        'low_grade': 'low_grade',
        'mdr_number': 'mdr_number',
        'name': 'name',
        'nces_id': 'nces_id',
        'phone': 'phone',
        'principal': 'principal',
        'school_number': 'school_number',
        'sis_id': 'sis_id',
        'state_id': 'state_id'
    }

    def __init__(self, created=None, district=None, ext=None, high_grade=None, id=None, last_modified=None, location=None, low_grade=None, mdr_number=None, name=None, nces_id=None, phone=None, principal=None, school_number=None, sis_id=None, state_id=None):  # noqa: E501
        """School - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._district = None
        self._ext = None
        self._high_grade = None
        self._id = None
        self._last_modified = None
        self._location = None
        self._low_grade = None
        self._mdr_number = None
        self._name = None
        self._nces_id = None
        self._phone = None
        self._principal = None
        self._school_number = None
        self._sis_id = None
        self._state_id = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if district is not None:
            self.district = district
        if ext is not None:
            self.ext = ext
        if high_grade is not None:
            self.high_grade = high_grade
        if id is not None:
            self.id = id
        if last_modified is not None:
            self.last_modified = last_modified
        if location is not None:
            self.location = location
        if low_grade is not None:
            self.low_grade = low_grade
        if mdr_number is not None:
            self.mdr_number = mdr_number
        if name is not None:
            self.name = name
        if nces_id is not None:
            self.nces_id = nces_id
        if phone is not None:
            self.phone = phone
        if principal is not None:
            self.principal = principal
        if school_number is not None:
            self.school_number = school_number
        if sis_id is not None:
            self.sis_id = sis_id
        if state_id is not None:
            self.state_id = state_id

    @property
    def created(self):
        """Gets the created of this School.  # noqa: E501


        :return: The created of this School.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this School.


        :param created: The created of this School.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def district(self):
        """Gets the district of this School.  # noqa: E501


        :return: The district of this School.  # noqa: E501
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this School.


        :param district: The district of this School.  # noqa: E501
        :type: str
        """

        self._district = district

    @property
    def ext(self):
        """Gets the ext of this School.  # noqa: E501


        :return: The ext of this School.  # noqa: E501
        :rtype: object
        """
        return self._ext

    @ext.setter
    def ext(self, ext):
        """Sets the ext of this School.


        :param ext: The ext of this School.  # noqa: E501
        :type: object
        """

        self._ext = ext

    @property
    def high_grade(self):
        """Gets the high_grade of this School.  # noqa: E501


        :return: The high_grade of this School.  # noqa: E501
        :rtype: str
        """
        return self._high_grade

    @high_grade.setter
    def high_grade(self, high_grade):
        """Sets the high_grade of this School.


        :param high_grade: The high_grade of this School.  # noqa: E501
        :type: str
        """
        allowed_values = ["InfantToddler", "Preschool", "PreKindergarten", "TransitionalKindergarten", "Kindergarten", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "PostGraduate", "Ungraded", "Other", ""]  # noqa: E501
        if high_grade not in allowed_values:
            raise ValueError(
                "Invalid value for `high_grade` ({0}), must be one of {1}"  # noqa: E501
                .format(high_grade, allowed_values)
            )

        self._high_grade = high_grade

    @property
    def id(self):
        """Gets the id of this School.  # noqa: E501


        :return: The id of this School.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this School.


        :param id: The id of this School.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_modified(self):
        """Gets the last_modified of this School.  # noqa: E501


        :return: The last_modified of this School.  # noqa: E501
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this School.


        :param last_modified: The last_modified of this School.  # noqa: E501
        :type: str
        """

        self._last_modified = last_modified

    @property
    def location(self):
        """Gets the location of this School.  # noqa: E501


        :return: The location of this School.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this School.


        :param location: The location of this School.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def low_grade(self):
        """Gets the low_grade of this School.  # noqa: E501


        :return: The low_grade of this School.  # noqa: E501
        :rtype: str
        """
        return self._low_grade

    @low_grade.setter
    def low_grade(self, low_grade):
        """Sets the low_grade of this School.


        :param low_grade: The low_grade of this School.  # noqa: E501
        :type: str
        """
        allowed_values = ["InfantToddler", "Preschool", "PreKindergarten", "TransitionalKindergarten", "Kindergarten", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "PostGraduate", "Ungraded", "Other", ""]  # noqa: E501
        if low_grade not in allowed_values:
            raise ValueError(
                "Invalid value for `low_grade` ({0}), must be one of {1}"  # noqa: E501
                .format(low_grade, allowed_values)
            )

        self._low_grade = low_grade

    @property
    def mdr_number(self):
        """Gets the mdr_number of this School.  # noqa: E501


        :return: The mdr_number of this School.  # noqa: E501
        :rtype: str
        """
        return self._mdr_number

    @mdr_number.setter
    def mdr_number(self, mdr_number):
        """Sets the mdr_number of this School.


        :param mdr_number: The mdr_number of this School.  # noqa: E501
        :type: str
        """

        self._mdr_number = mdr_number

    @property
    def name(self):
        """Gets the name of this School.  # noqa: E501


        :return: The name of this School.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this School.


        :param name: The name of this School.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nces_id(self):
        """Gets the nces_id of this School.  # noqa: E501


        :return: The nces_id of this School.  # noqa: E501
        :rtype: str
        """
        return self._nces_id

    @nces_id.setter
    def nces_id(self, nces_id):
        """Sets the nces_id of this School.


        :param nces_id: The nces_id of this School.  # noqa: E501
        :type: str
        """

        self._nces_id = nces_id

    @property
    def phone(self):
        """Gets the phone of this School.  # noqa: E501


        :return: The phone of this School.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this School.


        :param phone: The phone of this School.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def principal(self):
        """Gets the principal of this School.  # noqa: E501


        :return: The principal of this School.  # noqa: E501
        :rtype: Principal
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this School.


        :param principal: The principal of this School.  # noqa: E501
        :type: Principal
        """

        self._principal = principal

    @property
    def school_number(self):
        """Gets the school_number of this School.  # noqa: E501


        :return: The school_number of this School.  # noqa: E501
        :rtype: str
        """
        return self._school_number

    @school_number.setter
    def school_number(self, school_number):
        """Sets the school_number of this School.


        :param school_number: The school_number of this School.  # noqa: E501
        :type: str
        """

        self._school_number = school_number

    @property
    def sis_id(self):
        """Gets the sis_id of this School.  # noqa: E501


        :return: The sis_id of this School.  # noqa: E501
        :rtype: str
        """
        return self._sis_id

    @sis_id.setter
    def sis_id(self, sis_id):
        """Sets the sis_id of this School.


        :param sis_id: The sis_id of this School.  # noqa: E501
        :type: str
        """

        self._sis_id = sis_id

    @property
    def state_id(self):
        """Gets the state_id of this School.  # noqa: E501


        :return: The state_id of this School.  # noqa: E501
        :rtype: str
        """
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        """Sets the state_id of this School.


        :param state_id: The state_id of this School.  # noqa: E501
        :type: str
        """

        self._state_id = state_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(School, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, School):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
