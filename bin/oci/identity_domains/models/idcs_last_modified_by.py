# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdcsLastModifiedBy(object):
    """
    The User or App who modified the Resource

    **SCIM++ Properties:**
    - idcsSearchable: true
    - multiValued: false
    - mutability: readOnly
    - required: false
    - returned: default
    - type: complex
    """

    #: A constant which can be used with the type property of a IdcsLastModifiedBy.
    #: This constant has a value of "User"
    TYPE_USER = "User"

    #: A constant which can be used with the type property of a IdcsLastModifiedBy.
    #: This constant has a value of "App"
    TYPE_APP = "App"

    def __init__(self, **kwargs):
        """
        Initializes a new IdcsLastModifiedBy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this IdcsLastModifiedBy.
        :type value: str

        :param ref:
            The value to assign to the ref property of this IdcsLastModifiedBy.
        :type ref: str

        :param type:
            The value to assign to the type property of this IdcsLastModifiedBy.
            Allowed values for this property are: "User", "App", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param display:
            The value to assign to the display property of this IdcsLastModifiedBy.
        :type display: str

        :param ocid:
            The value to assign to the ocid property of this IdcsLastModifiedBy.
        :type ocid: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'type': 'str',
            'display': 'str',
            'ocid': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'type': 'type',
            'display': 'display',
            'ocid': 'ocid'
        }

        self._value = None
        self._ref = None
        self._type = None
        self._display = None
        self._ocid = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this IdcsLastModifiedBy.
        The ID of the SCIM resource that represents the User or App who modified this Resource

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this IdcsLastModifiedBy.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this IdcsLastModifiedBy.
        The ID of the SCIM resource that represents the User or App who modified this Resource

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this IdcsLastModifiedBy.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        Gets the ref of this IdcsLastModifiedBy.
        The URI of the SCIM resource that represents the User or App who modified this Resource

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this IdcsLastModifiedBy.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this IdcsLastModifiedBy.
        The URI of the SCIM resource that represents the User or App who modified this Resource

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this IdcsLastModifiedBy.
        :type: str
        """
        self._ref = ref

    @property
    def type(self):
        """
        Gets the type of this IdcsLastModifiedBy.
        The type of resource, User or App, that modified this Resource

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "User", "App", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this IdcsLastModifiedBy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IdcsLastModifiedBy.
        The type of resource, User or App, that modified this Resource

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this IdcsLastModifiedBy.
        :type: str
        """
        allowed_values = ["User", "App"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def display(self):
        """
        Gets the display of this IdcsLastModifiedBy.
        The displayName of the User or App who modified this Resource

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this IdcsLastModifiedBy.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this IdcsLastModifiedBy.
        The displayName of the User or App who modified this Resource

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this IdcsLastModifiedBy.
        :type: str
        """
        self._display = display

    @property
    def ocid(self):
        """
        Gets the ocid of this IdcsLastModifiedBy.
        The OCID of the SCIM resource that represents the User or App who modified this Resource

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - returned: default
         - type: string
         - uniqueness: none


        :return: The ocid of this IdcsLastModifiedBy.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this IdcsLastModifiedBy.
        The OCID of the SCIM resource that represents the User or App who modified this Resource

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - returned: default
         - type: string
         - uniqueness: none


        :param ocid: The ocid of this IdcsLastModifiedBy.
        :type: str
        """
        self._ocid = ocid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other