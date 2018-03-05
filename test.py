from unittest import TestCase
import random

from allow import allow


class MyException(Exception):
    pass


class TestAllow(TestCase):
    def testNoExceptionRaised(self):
        with allow(Exception):
            pass

    def testNoExceptionsAllowed(self):
        with self.assertRaises(Exception):
            with allow():
                raise Exception

    def testAllowsException_onOneExceptionAllowed(self):
        with allow(MyException):
            raise MyException

    def testAllowsException_onMultipleExceptionsAllowed(self):
        allowed = [MyException, RuntimeError, KeyboardInterrupt]
        with allow(*allowed):
            raise random.choice(allowed)
