# hdt_document_test.py
# Author: Thomas MINIER - MIT License 2017-2018
from hdt import HDTDocument
import unittest

path = "tests/test.hdt"
document = HDTDocument(path)
nbTotalTriples = 132


class TestHDTDocument(unittest.TestCase):

    def test_file_path(self):
        self.assertEqual(document.get_file_path(), path)

    def test_total_triples(self):
        self.assertEqual(document.get_total_triples(), nbTotalTriples)

    def test_nb_subjects(self):
        self.assertEqual(document.get_nb_subjects(), 4)

    def tests_nb_predicates(self):
        self.assertEqual(document.get_nb_predicates(), 3)

    def tests_nb_objects(self):
        self.assertEqual(document.get_nb_objects(), 112)

    def tests_nb_shared(self):
        self.assertEqual(document.get_nb_shared(), 0)

    def test_read_document(self):
        (triples, cardinality) = document.search_triples("", "", "")
        self.assertEqual(cardinality, nbTotalTriples)
        self.assertEqual(len(triples), cardinality)
        for subj, pred, obj in triples:
            self.assertNotEqual(subj, None)
            self.assertNotEqual(pred, None)
            self.assertNotEqual(obj, None)

    def test_read_document_limit(self):
        nbItems = 0
        (triples, cardinality) = document.search_triples("", "", "", limit=10)
        self.assertEqual(cardinality, nbTotalTriples)
        self.assertEqual(len(triples), nbTotalTriples)
        for subj, pred, obj in triples:
            nbItems += 1
            self.assertNotEqual(subj, None)
            self.assertNotEqual(pred, None)
            self.assertNotEqual(obj, None)
        self.assertEqual(nbItems, 10)

    def test_read_document_offset(self):
        nbItems = 0
        (triples, cardinality) = document.search_triples("", "", "", offset=10)
        self.assertEqual(cardinality, nbTotalTriples)
        self.assertEqual(len(triples), nbTotalTriples)
        for subj, pred, obj in triples:
            nbItems += 1
            self.assertNotEqual(subj, None)
            self.assertNotEqual(pred, None)
            self.assertNotEqual(obj, None)
        self.assertEqual(nbItems, cardinality - 10)
