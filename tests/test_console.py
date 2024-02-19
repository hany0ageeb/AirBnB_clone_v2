#!/usr/bin/python3
"""
This module contain tests for console
"""
import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """defines test cases for console"""
    def test_quit_present(self):
        """tests do_quit present"""
        # setup
        instance = HBNBCommand()
        with self.assertRaises(SystemExit):
            instance.onecmd("quit")

    def test_EOF_present(self):
        """test EOF exist"""
        # setup
        instance = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as f:
            instance.onecmd('EOF')
        self.assertEqual(f.getvalue(), '\n')

    def test_emptyline_present(self):
        """Test empty line is present"""
        instance = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as f:
            with patch.object(instance, 'emptyline') as empt:
                instance.onecmd("\n")
            empt.assert_called_once()
            self.assertEqual(f.getvalue(), '')

    def test_create_BaseModel_is_present(self):
        """test create BaseModel is present"""
        with patch('builtins.open', mock_open(read_data="{}")):
            instance = HBNBCommand()
            with patch('sys.stdout', new=StringIO()) as f:
                with patch('uuid.uuid4', return_value='123-123'):
                    instance.onecmd("create BaseModel")
                    self.assertEqual(f.getvalue(), '123-123\n')
