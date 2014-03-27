from ert.util import Matrix
from ert_tests import ExtendedTestCase

class MatrixTest(ExtendedTestCase):
    def test_matrix(self):
        m = Matrix(2, 3)

        self.assertEqual(m.rows(), 2)
        self.assertEqual(m.columns(), 3)

        self.assertEqual(m[(0, 0)], 0)

        m[(1, 1)] = 1.5
        self.assertEqual(m[(1, 1)], 1.5)

        m[1,0] = 5
        self.assertEqual(m[1, 0], 5)

        with self.assertRaises(TypeError):
            m[5] = 5

        with self.assertRaises(IndexError):
            m[2, 0] = 0

        with self.assertRaises(IndexError):
            m[0, 3] = 0

    def test_matrix_set(self):
        m1 = Matrix(2,2)
        m1.setAll(99)
        self.assertEqual( 99 , m1[0,0] )
        self.assertEqual( 99 , m1[1,1] )
        m2 = Matrix(2,2 , value = 99)
        self.assertEqual(m1,m2)

    
    def test_matrix_scale(self):
        m = Matrix(2,2 , value = 1)
        m.scaleColumn(0 , 2)
        self.assertEqual(2 , m[0,0])
        self.assertEqual(2 , m[1,0])
        
        with self.assertRaises(IndexError):
            m.scaleColumn(10 , 99)


    def test_matrix_equality(self):
        m = Matrix(2, 2)
        m[0, 0] = 2
        m[1, 1] = 4

        s = Matrix(2, 3)
        s[0, 0] = 2
        s[1, 1] = 4

        self.assertNotEqual(m, s)

        r = Matrix(2, 2)
        r[0, 0] = 2
        r[1, 1] = 3

        self.assertNotEqual(m, r)

        r[1, 1] = 4

        self.assertEqual(m, r)


        
