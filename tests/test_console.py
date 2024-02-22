#!/usr/bin/python3
"""
This module contain tests for console
"""
import unittest
from io import StringIO
from unittest.mock import patch, Mock, mock_open
from console import HBNBCommand
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Test HBNBCommand classs"""

    def setUp(self):
        self.cmd = HBNBCommand()

    def test_do_quit_exist(self):
        """test do_quit metod"""
        with self.assertRaises(SystemExit, msg=f'quit should quit'):
            self.cmd.onecmd('quit')

    def test_do_EOF_exist(self):
        """test do_EOF method"""
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit, msg='EOF should exit the console'):
                self.cmd.onecmd('EOF')
                self.assertEqual(f.getvalue(), '\n')


    def test_emptyline_exist(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('\n')
            self.assertEqual(f.getvalue(),'')

    def test_do_create_with_no_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('create')
            self.assertEqual(f.getvalue(), '** class name missing **\n', msg=f'create should print ** class name missing followed by new line!')

    def test_do_create_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('create pla')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n", msg=f'create should print ** class does\'nt exist ** followed by a new line if given invalid class name')

    def test_do_create_with_valid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            with patch.object(BaseModel,'save', new=Mock()) as mock_saved:
                self.cmd.onecmd('create BaseModel')
                mock_saved.assert_called()
                self.assertNotEqual(f.getvalue(), '\n')

    def test_do_create_with_parameters(self):
        with patch.object(BaseModel,'add_attributes', new=Mock()) as add_attributes_mock:
            with patch('sys.stdout', new=StringIO()) as f:
                with patch.object(BaseModel, 'save', new=Mock()) as save_mock:
                    self.cmd.onecmd('create BaseModel para=1 pa1 para2="HELLO"')
                    add_attributes_mock.assert_called_with(para=1, para2="HELLO")
                    save_mock.assert_called_once()

    def test_do_show_with_no_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('show')
            self.assertEqual(f.getvalue(), '** class name missing **\n')

    def test_do_show_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('show pla')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
    
    def test_do_show_with_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('show BaseModel')
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_show_with_non_existent_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.__init__.storage.find_by_id', new=Mock()) as find_by_id_mock:
                find_by_id_mock.return_value = None
                self.cmd.onecmd('show BaseModel plapla')
                find_by_id_mock.assert_called_once_with("plapla", BaseModel)
                self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_do_show_with_existent_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.__init__.storage.find_by_id', new=Mock()) as find_by_id_mock:
                returned_instance = BaseModel(id='plapla')
                find_by_id_mock.return_value = returned_instance
                self.cmd.onecmd('show BaseModel plapla')
                self.assertEqual(f.getvalue(),str(returned_instance)+"\n")

    def test_do_destroy_with_no_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('destroy')
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_destroy_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('destroy pla')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
            
    def test_do_destroy_with_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('destroy BaseModel')
            self.assertEqual(f.getvalue(), "** instance id missing **\n")

    def test_do_destroy_with_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('destroy BaseModel plp')
            self.assertEqual(f.getvalue(), '** no instance found **\n')

    def test_do_destroy_with_valid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.__init__.storage.find_by_id', new=Mock()) as mock_find:
                with patch('models.__init__.storage.delete', new=Mock()) as mock_delete:
                    with patch('models.__init__.storage.save', new=Mock()) as mock_save:
                        instance = BaseModel(id="123-123")
                        mock_find.return_value = instance
                        self.cmd.onecmd('destroy BaseModel 123-123')
                        mock_delete.assert_called_once_with(instance)
                        mock_save.assert_called_once()
    
    def test_do_all_with_invalid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('all pla')
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_all_with_valid_class_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.__init__.storage.all', new=Mock()) as all_mock:
                result = {
                    'BaseModel.123-123': BaseModel(id='123-123')
                }
                all_mock.return_value = result
                self.cmd.onecmd('all BaseModel')
                all_mock.assert_called_once_with(BaseModel)
                self.assertEqual(f.getvalue(), f"{[str(result['BaseModel.123-123'])]}\n")
    
    def test_do_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            with patch('models.__init__.storage.count', new=Mock()) as count_mock:
                count_mock.return_value = 5
                self.cmd.onecmd('count BaseModel')
                count_mock.assert_called_once_with(BaseModel)
                self.assertEqual(f.getvalue(), '5\n')


if __name__ == '__main__':
    unittest.main()
