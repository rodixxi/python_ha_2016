#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from grupos_personas import *


class Groups(unittest.TestCase):
    p0 = Person("juan", 18)
    p1 = Person("tito", 34)
    p2 = Person("carlos", 36)
    p3 = Person("jose", 28)

    def test_groups(self):

        # Two Persons class can get together and generate a Group

        g0 = self.p0 + self.p1

        self.assertIsInstance(g0, Group)
        self.assertIn(self.p0, g0)
        self.assertIn(self.p1, g0)
        self.assertEqual(len(g0), 2)

        #  Two Groups are equal if they have the same Persons
        self.assertEqual(Group({self.p0, self.p1}), Group([self.p1, self.p0]))

        self.assertNotEqual(Group({self.p0, self.p1}), Group([self.p2,
                                                              self.p0]))

        # A Group can add another Person and generate a new Group with all
        # the persons of the Group plus the new Person

        g1 = g0 + self.p2

        self.assertIsInstance(g1, Group)
        self.assertIn(self.p0, g1)
        self.assertIn(self.p1, g1)
        self.assertIn(self.p2, g1)
        self.assertEqual(len(g1), 3)

        # You can subtract one person from a group

        g2 = g1 - self.p2

        self.assertIsInstance(g2, Group)
        self.assertIn(self.p0, g2)
        self.assertIn(self.p1, g2)
        self.assertNotIn(self.p2, g2)
        self.assertEqual(len(g2), 2)

        # Two groups can be added and subtracted. In the case of addition the
        # sum generates a group with the persons of the TWO groups without
        # repeating; And in the case of subtract a group is created where only
        # the people of the first group where they are not in the second group.

        g2 = self.p1 + self.p2
        g3 = g1 + g2

        self.assertIsInstance(g3, Group)
        self.assertIn(self.p0, g3)
        self.assertIn(self.p1, g3)
        self.assertIn(self.p2, g3)
        self.assertEqual(len(g3), 3)

        g3 = g1 - g2

        self.assertIsInstance(g3, Group)
        self.assertIn(self.p0, g3)
        self.assertNotIn(self.p1, g3)
        self.assertNotIn(self.p2, g3)
        self.assertEqual(len(g3), 1)

        # Groups are iterative and iterate over persons.

        self.assertIn(self.p0, g3)
        self.assertNotIn(self.p1, g3)

        # The groups have length (number of persons)

        g3 = g3 - self.p0

        self.assertEqual(len(g3), 0)
        self.assertEqual(len(g2), 2)

        # A group is True only if it has any person.

        self.assertTrue(g2)
        self.assertFalse(g3)

        # You can tell if a person is in a group with the operator "in"

        self.assertTrue(self.p1 in g2)
        self.assertFalse(self.p1 in g3)

        # NOT IMPLEMENTED
        # The group has an edad_promedio method that calculates the average
        # age of the group (float) or throws an EmptyGroupError if the group
        # is empty

        # self.assertIsInstance(g2.edad_promedio(), float)
        # self.assertRaises(EmptyGroupError, g3.edad_promedio)

if __name__ == '__main__':
    unittest.main()
