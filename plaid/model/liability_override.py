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
    from plaid.model.address import Address
    from plaid.model.pslf_status import PSLFStatus
    from plaid.model.student_loan_repayment_model import StudentLoanRepaymentModel
    from plaid.model.student_loan_status import StudentLoanStatus
    globals()['Address'] = Address
    globals()['PSLFStatus'] = PSLFStatus
    globals()['StudentLoanRepaymentModel'] = StudentLoanRepaymentModel
    globals()['StudentLoanStatus'] = StudentLoanStatus


class LiabilityOverride(ModelNormal):
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
            'type': (str,),  # noqa: E501
            'purchase_apr': (float,),  # noqa: E501
            'cash_apr': (float,),  # noqa: E501
            'balance_transfer_apr': (float,),  # noqa: E501
            'special_apr': (float,),  # noqa: E501
            'last_payment_amount': (float,),  # noqa: E501
            'minimum_payment_amount': (float,),  # noqa: E501
            'is_overdue': (bool,),  # noqa: E501
            'origination_date': (str,),  # noqa: E501
            'principal': (float,),  # noqa: E501
            'nominal_apr': (float,),  # noqa: E501
            'interest_capitalization_grace_period_months': (float,),  # noqa: E501
            'repayment_model': (StudentLoanRepaymentModel,),  # noqa: E501
            'expected_payoff_date': (str,),  # noqa: E501
            'guarantor': (str,),  # noqa: E501
            'is_federal': (bool,),  # noqa: E501
            'loan_name': (str,),  # noqa: E501
            'loan_status': (StudentLoanStatus,),  # noqa: E501
            'payment_reference_number': (str,),  # noqa: E501
            'pslf_status': (PSLFStatus,),  # noqa: E501
            'repayment_plan_description': (str,),  # noqa: E501
            'repayment_plan_type': (str,),  # noqa: E501
            'sequence_number': (str,),  # noqa: E501
            'servicer_address': (Address,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'type': 'type',  # noqa: E501
        'purchase_apr': 'purchase_apr',  # noqa: E501
        'cash_apr': 'cash_apr',  # noqa: E501
        'balance_transfer_apr': 'balance_transfer_apr',  # noqa: E501
        'special_apr': 'special_apr',  # noqa: E501
        'last_payment_amount': 'last_payment_amount',  # noqa: E501
        'minimum_payment_amount': 'minimum_payment_amount',  # noqa: E501
        'is_overdue': 'is_overdue',  # noqa: E501
        'origination_date': 'origination_date',  # noqa: E501
        'principal': 'principal',  # noqa: E501
        'nominal_apr': 'nominal_apr',  # noqa: E501
        'interest_capitalization_grace_period_months': 'interest_capitalization_grace_period_months',  # noqa: E501
        'repayment_model': 'repayment_model',  # noqa: E501
        'expected_payoff_date': 'expected_payoff_date',  # noqa: E501
        'guarantor': 'guarantor',  # noqa: E501
        'is_federal': 'is_federal',  # noqa: E501
        'loan_name': 'loan_name',  # noqa: E501
        'loan_status': 'loan_status',  # noqa: E501
        'payment_reference_number': 'payment_reference_number',  # noqa: E501
        'pslf_status': 'pslf_status',  # noqa: E501
        'repayment_plan_description': 'repayment_plan_description',  # noqa: E501
        'repayment_plan_type': 'repayment_plan_type',  # noqa: E501
        'sequence_number': 'sequence_number',  # noqa: E501
        'servicer_address': 'servicer_address',  # noqa: E501
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
    def __init__(self, type, purchase_apr, cash_apr, balance_transfer_apr, special_apr, last_payment_amount, minimum_payment_amount, is_overdue, origination_date, principal, nominal_apr, interest_capitalization_grace_period_months, repayment_model, expected_payoff_date, guarantor, is_federal, loan_name, loan_status, payment_reference_number, pslf_status, repayment_plan_description, repayment_plan_type, sequence_number, servicer_address, *args, **kwargs):  # noqa: E501
        """LiabilityOverride - a model defined in OpenAPI

        Args:
            type (str): The type of the liability object, either `credit` or `student`. Mortgages are not currently supported in the custom Sandbox.
            purchase_apr (float): The purchase APR percentage value. For simplicity, this is the only interest rate used to calculate interest charges. Can only be set if `type` is `credit`.
            cash_apr (float): The cash APR percentage value. Can only be set if `type` is `credit`.
            balance_transfer_apr (float): The balance transfer APR percentage value. Can only be set if `type` is `credit`. Can only be set if `type` is `credit`.
            special_apr (float): The special APR percentage value. Can only be set if `type` is `credit`.
            last_payment_amount (float): Override the `last_payment_amount` field. Can only be set if `type` is `credit`.
            minimum_payment_amount (float): Override the `minimum_payment_amount` field. Can only be set if `type` is `credit` or `student`.
            is_overdue (bool): Override the `is_overdue` field
            origination_date (str): The date on which the loan was initially lent, in ISO 8601 (YYYY-MM-DD) format. Can only be set if `type` is `student`.
            principal (float): The original loan principal. Can only be set if `type` is `student`.
            nominal_apr (float): The interest rate on the loan as a percentage. Can only be set if `type` is `student`.
            interest_capitalization_grace_period_months (float): If set, interest capitalization begins at the given number of months after loan origination. By default interest is never capitalized. Can only be set if `type` is `student`.
            repayment_model (StudentLoanRepaymentModel):
            expected_payoff_date (str): Override the `expected_payoff_date` field. Can only be set if `type` is `student`.
            guarantor (str): Override the `guarantor` field. Can only be set if `type` is `student`.
            is_federal (bool): Override the `is_federal` field. Can only be set if `type` is `student`.
            loan_name (str): Override the `loan_name` field. Can only be set if `type` is `student`.
            loan_status (StudentLoanStatus):
            payment_reference_number (str): Override the `payment_reference_number` field. Can only be set if `type` is `student`.
            pslf_status (PSLFStatus):
            repayment_plan_description (str): Override the `repayment_plan.description` field. Can only be set if `type` is `student`.
            repayment_plan_type (str): Override the `repayment_plan.type` field. Can only be set if `type` is `student`. Possible values are: `\"extended graduated\"`, `\"extended standard\"`, `\"graduated\"`, `\"income-contingent repayment\"`, `\"income-based repayment\"`, `\"interest only\"`, `\"other\"`, `\"pay as you earn\"`, `\"revised pay as you earn\"`, or `\"standard\"`.
            sequence_number (str): Override the `sequence_number` field. Can only be set if `type` is `student`.
            servicer_address (Address):

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

        self.type = type
        self.purchase_apr = purchase_apr
        self.cash_apr = cash_apr
        self.balance_transfer_apr = balance_transfer_apr
        self.special_apr = special_apr
        self.last_payment_amount = last_payment_amount
        self.minimum_payment_amount = minimum_payment_amount
        self.is_overdue = is_overdue
        self.origination_date = origination_date
        self.principal = principal
        self.nominal_apr = nominal_apr
        self.interest_capitalization_grace_period_months = interest_capitalization_grace_period_months
        self.repayment_model = repayment_model
        self.expected_payoff_date = expected_payoff_date
        self.guarantor = guarantor
        self.is_federal = is_federal
        self.loan_name = loan_name
        self.loan_status = loan_status
        self.payment_reference_number = payment_reference_number
        self.pslf_status = pslf_status
        self.repayment_plan_description = repayment_plan_description
        self.repayment_plan_type = repayment_plan_type
        self.sequence_number = sequence_number
        self.servicer_address = servicer_address
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
