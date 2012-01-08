import unittest
import pascal_add, pascal_rows_half

import unittest

class PascalTest( unittest.TestCase ):

    def test_pascal( self ):
	self.assertEqual( pascal_add.first_ten(), pascal_rows_half.first_ten() )
	print "PASSED ADD/ROWS_HALF"

if __name__ == '__main__':
    unittest.main()

