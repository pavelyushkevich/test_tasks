import unittest
from task1 import DictCompare

class TestDictCompare(unittest.TestCase):

    def test_compare(self):
        dict1 = {
            'a' : {
                'a1' : 1,
                'a2' : 2,
            },
            'b' : {
		'b1': {
		    'b11' : 1,
		    'b12' : 2,
		},
            }
        }

        dict2 = {
            'a' : {
		'a1' : 3,
		'a2' : 2,
            },
            'b' : {
		'b1': {
		    'b11' : 5,
		    'b12' : 2,
		},
            }
        }
        my_compare = DictCompare()
        res = my_compare.compare(dict1, dict2)
        
        self.assertEqual(res, {'a': {'a1': 3}, 'b': {'b1': {'b11': 5}}} )

    def test_compare_with_different_values(self):
        dict1 = {
            'a' : {
                'a1' : 1,
                'a2' : 2,
            },
            'b' : {
		'b1': {
		    'b11' : 1,
		    'b12' : 2,
		},
            }
        }

        dict2 = {
            'a' : 2,
            'b' : {
		'b1': {
		    'b11' : 5,
		    'b12' : 2,
		},
            }
        }
        my_compare = DictCompare()
        res = my_compare.compare(dict1, dict2)
        
        self.assertEqual(res, {'a': 2, 'b': {'b1': {'b11': 5}}} )

unittest.main()
