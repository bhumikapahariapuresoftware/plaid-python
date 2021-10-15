"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from plaid.model.deductions import Deductions
    from plaid.model.earnings import Earnings
    from plaid.model.employee import Employee
    from plaid.model.employment_details import EmploymentDetails
    from plaid.model.income_breakdown import IncomeBreakdown
    from plaid.model.net_pay import NetPay
    from plaid.model.pay_period_details import PayPeriodDetails
    from plaid.model.paystub_details import PaystubDetails
    from plaid.model.paystub_employer import PaystubEmployer
    from plaid.model.paystub_ytd_details import PaystubYTDDetails
    globals()['Deductions'] = Deductions
    globals()['Earnings'] = Earnings
    globals()['Employee'] = Employee
    globals()['EmploymentDetails'] = EmploymentDetails
    globals()['IncomeBreakdown'] = IncomeBreakdown
    globals()['NetPay'] = NetPay
    globals()['PayPeriodDetails'] = PayPeriodDetails
    globals()['PaystubDetails'] = PaystubDetails
    globals()['PaystubEmployer'] = PaystubEmployer
    globals()['PaystubYTDDetails'] = PaystubYTDDetails


class Paystub(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'deductions': (Deductions,),  # noqa: E501
            'doc_id': (str,),  # noqa: E501
            'earnings': (Earnings,),  # noqa: E501
            'employee': (Employee,),  # noqa: E501
            'employer': (PaystubEmployer,),  # noqa: E501
            'net_pay': (NetPay,),  # noqa: E501
            'pay_period_details': (PayPeriodDetails,),  # noqa: E501
            'income_breakdown': ([IncomeBreakdown],),  # noqa: E501
            'ytd_earnings': (PaystubYTDDetails,),  # noqa: E501
            'employment_details': (EmploymentDetails,),  # noqa: E501
            'paystub_details': (PaystubDetails,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'deductions': 'deductions',  # noqa: E501
        'doc_id': 'doc_id',  # noqa: E501
        'earnings': 'earnings',  # noqa: E501
        'employee': 'employee',  # noqa: E501
        'employer': 'employer',  # noqa: E501
        'net_pay': 'net_pay',  # noqa: E501
        'pay_period_details': 'pay_period_details',  # noqa: E501
        'income_breakdown': 'income_breakdown',  # noqa: E501
        'ytd_earnings': 'ytd_earnings',  # noqa: E501
        'employment_details': 'employment_details',  # noqa: E501
        'paystub_details': 'paystub_details',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, deductions, doc_id, earnings, employee, employer, net_pay, pay_period_details, income_breakdown, ytd_earnings, *args, **kwargs):  # noqa: E501
        """Paystub - a model defined in OpenAPI

        Args:
            deductions (Deductions):
            doc_id (str): An identifier of the document referenced by the document metadata.
            earnings (Earnings):
            employee (Employee):
            employer (PaystubEmployer):
            net_pay (NetPay):
            pay_period_details (PayPeriodDetails):
            income_breakdown ([IncomeBreakdown]):
            ytd_earnings (PaystubYTDDetails):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            employment_details (EmploymentDetails): [optional]  # noqa: E501
            paystub_details (PaystubDetails): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.deductions = deductions
        self.doc_id = doc_id
        self.earnings = earnings
        self.employee = employee
        self.employer = employer
        self.net_pay = net_pay
        self.pay_period_details = pay_period_details
        self.income_breakdown = income_breakdown
        self.ytd_earnings = ytd_earnings
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
