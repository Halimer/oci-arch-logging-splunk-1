# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalClusterNetworkConfiguration(object):
    """
    The details of a network address configuration in an external cluster.
    """

    #: A constant which can be used with the network_type property of a ExternalClusterNetworkConfiguration.
    #: This constant has a value of "AUTOCONFIG"
    NETWORK_TYPE_AUTOCONFIG = "AUTOCONFIG"

    #: A constant which can be used with the network_type property of a ExternalClusterNetworkConfiguration.
    #: This constant has a value of "DHCP"
    NETWORK_TYPE_DHCP = "DHCP"

    #: A constant which can be used with the network_type property of a ExternalClusterNetworkConfiguration.
    #: This constant has a value of "STATIC"
    NETWORK_TYPE_STATIC = "STATIC"

    #: A constant which can be used with the network_type property of a ExternalClusterNetworkConfiguration.
    #: This constant has a value of "MIXED"
    NETWORK_TYPE_MIXED = "MIXED"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalClusterNetworkConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_number:
            The value to assign to the network_number property of this ExternalClusterNetworkConfiguration.
        :type network_number: int

        :param network_type:
            The value to assign to the network_type property of this ExternalClusterNetworkConfiguration.
            Allowed values for this property are: "AUTOCONFIG", "DHCP", "STATIC", "MIXED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type network_type: str

        :param subnet:
            The value to assign to the subnet property of this ExternalClusterNetworkConfiguration.
        :type subnet: str

        """
        self.swagger_types = {
            'network_number': 'int',
            'network_type': 'str',
            'subnet': 'str'
        }

        self.attribute_map = {
            'network_number': 'networkNumber',
            'network_type': 'networkType',
            'subnet': 'subnet'
        }

        self._network_number = None
        self._network_type = None
        self._subnet = None

    @property
    def network_number(self):
        """
        Gets the network_number of this ExternalClusterNetworkConfiguration.
        The network number.


        :return: The network_number of this ExternalClusterNetworkConfiguration.
        :rtype: int
        """
        return self._network_number

    @network_number.setter
    def network_number(self, network_number):
        """
        Sets the network_number of this ExternalClusterNetworkConfiguration.
        The network number.


        :param network_number: The network_number of this ExternalClusterNetworkConfiguration.
        :type: int
        """
        self._network_number = network_number

    @property
    def network_type(self):
        """
        Gets the network_type of this ExternalClusterNetworkConfiguration.
        The network type.

        Allowed values for this property are: "AUTOCONFIG", "DHCP", "STATIC", "MIXED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The network_type of this ExternalClusterNetworkConfiguration.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """
        Sets the network_type of this ExternalClusterNetworkConfiguration.
        The network type.


        :param network_type: The network_type of this ExternalClusterNetworkConfiguration.
        :type: str
        """
        allowed_values = ["AUTOCONFIG", "DHCP", "STATIC", "MIXED"]
        if not value_allowed_none_or_none_sentinel(network_type, allowed_values):
            network_type = 'UNKNOWN_ENUM_VALUE'
        self._network_type = network_type

    @property
    def subnet(self):
        """
        Gets the subnet of this ExternalClusterNetworkConfiguration.
        The subnet for the network.


        :return: The subnet of this ExternalClusterNetworkConfiguration.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """
        Sets the subnet of this ExternalClusterNetworkConfiguration.
        The subnet for the network.


        :param subnet: The subnet of this ExternalClusterNetworkConfiguration.
        :type: str
        """
        self._subnet = subnet

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other