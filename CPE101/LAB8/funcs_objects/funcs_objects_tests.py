#Raymond Lenz
#Sussan Einakian 
#Section 9 
#Lab 8
import unittest
import objects as o
import funcs_objects as f
class TestCases(unittest.TestCase):
    def test_point(self):
        p=o.Point(2,3)
        self.assertTrue(p.x==2)
        self.assertTrue(p.y==3)
        pass


    def test_circle(self):
        c=o.Circle(o.Point(2,3),4)
        p=o.Point(2,3)
        self.assertTrue(p==c.cpnt)
        self.assertTrue(c.rad==4)
        pass

   # Add other testing functions
    def test_dist(self):
        p1=o.Point(1,0)
        p2=o.Point(2,0)
        self.assertEqual(f.distance(p1,p2),1)
        p3=o.Point(1,1)
        p4=o.Point(2,2)
        self.assertAlmostEqual(f.distance(p3,p4),1.414213562373095)
        p5=o.Point(0,0)
        p6=o.Point(5,5)
        self.assertEqual(f.distance(p5,p6),7.0710678118654755)
        pass
    def test_circles_overlap(self):
        c1=o.Circle(o.Point(0,0),5)
        c2=o.Circle(o.Point(3,3),3)
        self.assertTrue(f.circles_overlap(c1,c2))
        c3=o.Circle(o.Point(0,0),1)
        c4=o.Circle(o.Point(5,5),1)
        self.assertFalse(f.circles_overlap(c3,c4))
        self.assertTrue(f.circles_overlap(c2,c4))
        pass
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
