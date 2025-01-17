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


class Section(object):
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
        'course': 'str',
        'created': 'str',
        'district': 'str',
        'ext': 'object',
        'grade': 'str',
        'id': 'str',
        'last_modified': 'str',
        'name': 'str',
        'period': 'str',
        'school': 'str',
        'section_number': 'str',
        'sis_id': 'str',
        'students': 'list[str]',
        'subject': 'str',
        'teacher': 'str',
        'teachers': 'list[str]',
        'term_id': 'str'
    }

    attribute_map = {
        'course': 'course',
        'created': 'created',
        'district': 'district',
        'ext': 'ext',
        'grade': 'grade',
        'id': 'id',
        'last_modified': 'last_modified',
        'name': 'name',
        'period': 'period',
        'school': 'school',
        'section_number': 'section_number',
        'sis_id': 'sis_id',
        'students': 'students',
        'subject': 'subject',
        'teacher': 'teacher',
        'teachers': 'teachers',
        'term_id': 'term_id'
    }

    def __init__(self, course=None, created=None, district=None, ext=None, grade=None, id=None, last_modified=None, name=None, period=None, school=None, section_number=None, sis_id=None, students=None, subject=None, teacher=None, teachers=None, term_id=None):  # noqa: E501
        """Section - a model defined in Swagger"""  # noqa: E501

        self._course = None
        self._created = None
        self._district = None
        self._ext = None
        self._grade = None
        self._id = None
        self._last_modified = None
        self._name = None
        self._period = None
        self._school = None
        self._section_number = None
        self._sis_id = None
        self._students = None
        self._subject = None
        self._teacher = None
        self._teachers = None
        self._term_id = None
        self.discriminator = None

        if course is not None:
            self.course = course
        if created is not None:
            self.created = created
        if district is not None:
            self.district = district
        if ext is not None:
            self.ext = ext
        if grade is not None:
            self.grade = grade
        if id is not None:
            self.id = id
        if last_modified is not None:
            self.last_modified = last_modified
        if name is not None:
            self.name = name
        if period is not None:
            self.period = period
        if school is not None:
            self.school = school
        if section_number is not None:
            self.section_number = section_number
        if sis_id is not None:
            self.sis_id = sis_id
        if students is not None:
            self.students = students
        if subject is not None:
            self.subject = subject
        if teacher is not None:
            self.teacher = teacher
        if teachers is not None:
            self.teachers = teachers
        if term_id is not None:
            self.term_id = term_id

    @property
    def course(self):
        """Gets the course of this Section.  # noqa: E501


        :return: The course of this Section.  # noqa: E501
        :rtype: str
        """
        return self._course

    @course.setter
    def course(self, course):
        """Sets the course of this Section.


        :param course: The course of this Section.  # noqa: E501
        :type: str
        """

        self._course = course

    @property
    def created(self):
        """Gets the created of this Section.  # noqa: E501


        :return: The created of this Section.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Section.


        :param created: The created of this Section.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def district(self):
        """Gets the district of this Section.  # noqa: E501


        :return: The district of this Section.  # noqa: E501
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this Section.


        :param district: The district of this Section.  # noqa: E501
        :type: str
        """

        self._district = district

    @property
    def ext(self):
        """Gets the ext of this Section.  # noqa: E501


        :return: The ext of this Section.  # noqa: E501
        :rtype: object
        """
        return self._ext

    @ext.setter
    def ext(self, ext):
        """Sets the ext of this Section.


        :param ext: The ext of this Section.  # noqa: E501
        :type: object
        """

        self._ext = ext

    @property
    def grade(self):
        """Gets the grade of this Section.  # noqa: E501


        :return: The grade of this Section.  # noqa: E501
        :rtype: str
        """
        return self._grade

    @grade.setter
    def grade(self, grade):
        """Sets the grade of this Section.


        :param grade: The grade of this Section.  # noqa: E501
        :type: str
        """
        allowed_values = ["InfantToddler", "Preschool", "PreKindergarten", "TransitionalKindergarten", "Kindergarten", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "PostGraduate", "Ungraded", "Other", ""]  # noqa: E501
        if grade not in allowed_values:
            raise ValueError(
                "Invalid value for `grade` ({0}), must be one of {1}"  # noqa: E501
                .format(grade, allowed_values)
            )

        self._grade = grade

    @property
    def id(self):
        """Gets the id of this Section.  # noqa: E501


        :return: The id of this Section.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Section.


        :param id: The id of this Section.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_modified(self):
        """Gets the last_modified of this Section.  # noqa: E501


        :return: The last_modified of this Section.  # noqa: E501
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Section.


        :param last_modified: The last_modified of this Section.  # noqa: E501
        :type: str
        """

        self._last_modified = last_modified

    @property
    def name(self):
        """Gets the name of this Section.  # noqa: E501


        :return: The name of this Section.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Section.


        :param name: The name of this Section.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def period(self):
        """Gets the period of this Section.  # noqa: E501


        :return: The period of this Section.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Section.


        :param period: The period of this Section.  # noqa: E501
        :type: str
        """

        self._period = period

    @property
    def school(self):
        """Gets the school of this Section.  # noqa: E501


        :return: The school of this Section.  # noqa: E501
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this Section.


        :param school: The school of this Section.  # noqa: E501
        :type: str
        """

        self._school = school

    @property
    def section_number(self):
        """Gets the section_number of this Section.  # noqa: E501


        :return: The section_number of this Section.  # noqa: E501
        :rtype: str
        """
        return self._section_number

    @section_number.setter
    def section_number(self, section_number):
        """Sets the section_number of this Section.


        :param section_number: The section_number of this Section.  # noqa: E501
        :type: str
        """

        self._section_number = section_number

    @property
    def sis_id(self):
        """Gets the sis_id of this Section.  # noqa: E501


        :return: The sis_id of this Section.  # noqa: E501
        :rtype: str
        """
        return self._sis_id

    @sis_id.setter
    def sis_id(self, sis_id):
        """Sets the sis_id of this Section.


        :param sis_id: The sis_id of this Section.  # noqa: E501
        :type: str
        """

        self._sis_id = sis_id

    @property
    def students(self):
        """Gets the students of this Section.  # noqa: E501


        :return: The students of this Section.  # noqa: E501
        :rtype: list[str]
        """
        return self._students

    @students.setter
    def students(self, students):
        """Sets the students of this Section.


        :param students: The students of this Section.  # noqa: E501
        :type: list[str]
        """

        self._students = students

    @property
    def subject(self):
        """Gets the subject of this Section.  # noqa: E501


        :return: The subject of this Section.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Section.


        :param subject: The subject of this Section.  # noqa: E501
        :type: str
        """
        allowed_values = ["english/language arts", "math", "science", "social studies", "language", "homeroom/advisory", "interventions/online learning", "technology and engineering", "PE and health", "arts and music", "other", ""]  # noqa: E501
        if subject not in allowed_values:
            raise ValueError(
                "Invalid value for `subject` ({0}), must be one of {1}"  # noqa: E501
                .format(subject, allowed_values)
            )

        self._subject = subject

    @property
    def teacher(self):
        """Gets the teacher of this Section.  # noqa: E501


        :return: The teacher of this Section.  # noqa: E501
        :rtype: str
        """
        return self._teacher

    @teacher.setter
    def teacher(self, teacher):
        """Sets the teacher of this Section.


        :param teacher: The teacher of this Section.  # noqa: E501
        :type: str
        """

        self._teacher = teacher

    @property
    def teachers(self):
        """Gets the teachers of this Section.  # noqa: E501


        :return: The teachers of this Section.  # noqa: E501
        :rtype: list[str]
        """
        return self._teachers

    @teachers.setter
    def teachers(self, teachers):
        """Sets the teachers of this Section.


        :param teachers: The teachers of this Section.  # noqa: E501
        :type: list[str]
        """

        self._teachers = teachers

    @property
    def term_id(self):
        """Gets the term_id of this Section.  # noqa: E501


        :return: The term_id of this Section.  # noqa: E501
        :rtype: str
        """
        return self._term_id

    @term_id.setter
    def term_id(self, term_id):
        """Sets the term_id of this Section.


        :param term_id: The term_id of this Section.  # noqa: E501
        :type: str
        """

        self._term_id = term_id

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
        if issubclass(Section, dict):
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
        if not isinstance(other, Section):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
