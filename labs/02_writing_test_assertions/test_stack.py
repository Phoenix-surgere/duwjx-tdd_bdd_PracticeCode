from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    """Test cases for Stack"""

    def setUp(self):
        """Setup before each test"""
        self.stack = Stack()

    def tearDown(self):
        """Tear down after each test"""
        self.stack = None

    def test_push(self):
        """Test pushing an item into the stack"""
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)

    def test_pop(self):
        """Test popping an item of off the stack"""
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.peek(), 1)

    def test_peek(self):
        """Test peeking at the top the stack"""
        self.stack.push(89)
        self.assertEqual(self.stack.peek(), 89)
        self.stack.push(45)
        self.assertEqual(self.stack.peek(), 45)


    def test_is_empty(self):
        """Test if the stack is empty"""
        self.assertEqual(self.stack.is_empty(), 1)
        self.stack.push(5)
        self.assertEqual(self.stack.is_empty(), 0)

