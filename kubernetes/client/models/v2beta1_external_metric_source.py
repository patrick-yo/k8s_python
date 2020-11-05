# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.16
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V2beta1ExternalMetricSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'metric_name': 'str',
        'metric_selector': 'V1LabelSelector',
        'target_average_value': 'str',
        'target_value': 'str'
    }

    attribute_map = {
        'metric_name': 'metricName',
        'metric_selector': 'metricSelector',
        'target_average_value': 'targetAverageValue',
        'target_value': 'targetValue'
    }

    def __init__(self, metric_name=None, metric_selector=None, target_average_value=None, target_value=None, local_vars_configuration=None):  # noqa: E501
        """V2beta1ExternalMetricSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metric_name = None
        self._metric_selector = None
        self._target_average_value = None
        self._target_value = None
        self.discriminator = None

        self.metric_name = metric_name
        if metric_selector is not None:
            self.metric_selector = metric_selector
        if target_average_value is not None:
            self.target_average_value = target_average_value
        if target_value is not None:
            self.target_value = target_value

    @property
    def metric_name(self):
        """Gets the metric_name of this V2beta1ExternalMetricSource.  # noqa: E501

        metricName is the name of the metric in question.  # noqa: E501

        :return: The metric_name of this V2beta1ExternalMetricSource.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this V2beta1ExternalMetricSource.

        metricName is the name of the metric in question.  # noqa: E501

        :param metric_name: The metric_name of this V2beta1ExternalMetricSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and metric_name is None:  # noqa: E501
            raise ValueError("Invalid value for `metric_name`, must not be `None`")  # noqa: E501

        self._metric_name = metric_name

    @property
    def metric_selector(self):
        """Gets the metric_selector of this V2beta1ExternalMetricSource.  # noqa: E501


        :return: The metric_selector of this V2beta1ExternalMetricSource.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._metric_selector

    @metric_selector.setter
    def metric_selector(self, metric_selector):
        """Sets the metric_selector of this V2beta1ExternalMetricSource.


        :param metric_selector: The metric_selector of this V2beta1ExternalMetricSource.  # noqa: E501
        :type: V1LabelSelector
        """

        self._metric_selector = metric_selector

    @property
    def target_average_value(self):
        """Gets the target_average_value of this V2beta1ExternalMetricSource.  # noqa: E501

        targetAverageValue is the target per-list value of global metric (as a quantity). Mutually exclusive with TargetValue.  # noqa: E501

        :return: The target_average_value of this V2beta1ExternalMetricSource.  # noqa: E501
        :rtype: str
        """
        return self._target_average_value

    @target_average_value.setter
    def target_average_value(self, target_average_value):
        """Sets the target_average_value of this V2beta1ExternalMetricSource.

        targetAverageValue is the target per-list value of global metric (as a quantity). Mutually exclusive with TargetValue.  # noqa: E501

        :param target_average_value: The target_average_value of this V2beta1ExternalMetricSource.  # noqa: E501
        :type: str
        """

        self._target_average_value = target_average_value

    @property
    def target_value(self):
        """Gets the target_value of this V2beta1ExternalMetricSource.  # noqa: E501

        targetValue is the target value of the metric (as a quantity). Mutually exclusive with TargetAverageValue.  # noqa: E501

        :return: The target_value of this V2beta1ExternalMetricSource.  # noqa: E501
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        """Sets the target_value of this V2beta1ExternalMetricSource.

        targetValue is the target value of the metric (as a quantity). Mutually exclusive with TargetAverageValue.  # noqa: E501

        :param target_value: The target_value of this V2beta1ExternalMetricSource.  # noqa: E501
        :type: str
        """

        self._target_value = target_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V2beta1ExternalMetricSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2beta1ExternalMetricSource):
            return True

        return self.to_dict() != other.to_dict()
