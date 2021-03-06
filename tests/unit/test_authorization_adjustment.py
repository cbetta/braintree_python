from tests.test_helper import *
from datetime import datetime
from braintree.authorization_adjustment import AuthorizationAdjustment

class TestAuthorizationAdjustment(unittest.TestCase):
    def test_constructor(self):
        attributes = {
            "amount": "-20.00",
            "timestamp": datetime(2017, 7, 12, 1, 2, 3),
            "success": True,
        }

        authorization_adjustment = AuthorizationAdjustment(attributes)

        self.assertEqual(authorization_adjustment.amount, Decimal("-20.00"))
        self.assertEqual(authorization_adjustment.timestamp, datetime(2017, 7, 12, 1, 2, 3))
        self.assertEqual(authorization_adjustment.success, True)

    def test_constructor_with_amount_as_None(self):
        attributes = {
            "amount": None,
            "timestamp": datetime(2017, 7, 12, 1, 2, 3),
            "success": True,
        }

        authorization_adjustment = AuthorizationAdjustment(attributes)

        self.assertEqual(authorization_adjustment.amount, None)
        self.assertEqual(authorization_adjustment.timestamp, datetime(2017, 7, 12, 1, 2, 3))
        self.assertEqual(authorization_adjustment.success, True)

    def test_constructor_without_amount(self):
        attributes = {
            "timestamp": datetime(2017, 7, 12, 1, 2, 3),
            "success": True,
        }

        authorization_adjustment = AuthorizationAdjustment(attributes)

        self.assertEqual(authorization_adjustment.timestamp, datetime(2017, 7, 12, 1, 2, 3))
        self.assertEqual(authorization_adjustment.success, True)
