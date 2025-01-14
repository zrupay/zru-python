from .request import APIRequest
from .resources import ProductResource, PlanResource, TaxResource, ShippingResource, CouponResource, \
    TransactionResource, SubscriptionResource, AuthorizationResource, SaleResource, ClientResource, \
    WalletResource, TransferResource, CurrencyResource, GatewayResource, PayDataResource
from .objects import Product, Plan, Tax, Shipping, Coupon, Transaction, Subscription, Authorization, Sale, \
    Client, Wallet, Transfer, Currency, Gateway, PayData
from .notification import NotificationData


def class_decorator(cls, resource):
    """
    Allows initializes an object without the resource variable
    :param cls: Object item class
    :param resource: Resource used to initializes the object
    :return: Function that only receive the json_dict value
    """
    cls.resource = resource

    def init(json_dict):
        return cls(json_dict, resource)

    try:
        init.get = cls.get
    except:
        pass

    return init


class ZRUClient(object):
    """
    ZRUClient - class used to manage the communication with ZRU API
    """
    def __init__(self, key, secret_key):
        """
        Initializes the zru library
        :param key: key to connect with API
        :param secret_key: secret_key to connect with API
        """
        self.api_request = APIRequest(key, secret_key)

        self.product = ProductResource(self.api_request)
        self.plan = PlanResource(self.api_request)
        self.tax = TaxResource(self.api_request)
        self.shipping = ShippingResource(self.api_request)
        self.coupon = CouponResource(self.api_request)
        self.transaction = TransactionResource(self.api_request)
        self.subscription = SubscriptionResource(self.api_request)
        self.authorization = AuthorizationResource(self.api_request)
        self.sale = SaleResource(self.api_request)
        self.client = ClientResource(self.api_request)
        self.wallet = WalletResource(self.api_request)
        self.transfer = TransferResource(self.api_request)
        self.currency = CurrencyResource(self.api_request)
        self.gateway = GatewayResource(self.api_request)
        self.pay_data = PayDataResource(self.api_request)

        self.Product = class_decorator(Product, self.product)
        self.Plan = class_decorator(Plan, self.plan)
        self.Tax = class_decorator(Tax, self.tax)
        self.Shipping = class_decorator(Shipping, self.shipping)
        self.Coupon = class_decorator(Coupon, self.coupon)
        self.Transaction = class_decorator(Transaction, self.transaction)
        self.Subscription = class_decorator(Subscription, self.subscription)
        self.Authorization = class_decorator(Authorization, self.authorization)
        self.Sale = class_decorator(Sale, self.sale)
        self.Client = class_decorator(Client, self.client)
        self.Wallet = class_decorator(Wallet, self.wallet)
        self.Transfer = class_decorator(Transfer, self.transfer)
        self.Currency = class_decorator(Currency, self.currency)
        self.Gateway = class_decorator(Gateway, self.gateway)
        self.PayData = class_decorator(PayData, self.pay_data)

        self.NotificationData = class_decorator(NotificationData, self)
