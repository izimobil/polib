#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest

sys.path.insert(1, os.path.abspath('.'))

import polib


class TestFunctions(unittest.TestCase):

    def test_pofile_and_mofile1(self):
        """
        Test bad usage of pofile/mofile. 
        """
        def bad_call():
            polib.pofile('not_a_file.txt')
        self.assertRaises(OSError, bad_call)

    def test_pofile_and_mofile2(self):
        """
        Test that the pofile function returns a POFile instance.
        """
        po = polib.pofile('tests/test_utf8.po')
        self.failUnless(isinstance(po, polib.POFile))

    def test_pofile_and_mofile3(self):
        """
        Test  that the mofile function returns a MOFile instance.
        """
        mo = polib.mofile('tests/test_utf8.mo')
        self.failUnless(isinstance(mo, polib.MOFile))

    def test_pofile_and_mofile4(self):
        """
        Test that check_for_duplicates is passed to the instance.
        """
        po = polib.pofile('tests/test_iso-8859-15.po', check_for_duplicates=True)
        self.failUnless(po.check_for_duplicates == True)

    def test_pofile_and_mofile5(self):
        """
        Test that detect_encoding works as expected.
        """
        po = polib.pofile('tests/test_iso-8859-15.po')
        self.failUnless(po.encoding == 'ISO_8859-15')

    def test_pofile_and_mofile6(self):
        """
        Test that encoding is default_encoding when detect_encoding is False.
        """
        po = polib.pofile('tests/test_noencoding.po', autodetect_encoding=False)
        self.failUnless(po.encoding == 'utf-8')

    def test_pofile_and_mofile7(self):
        """
        Test that encoding is ok when encoding is explicitely given.
        """
        po = polib.pofile('tests/test_iso-8859-15.po', autodetect_encoding=False, encoding='iso-8859-15')
        self.failUnless(po.encoding == 'iso-8859-15')

    def test_detect_encoding1(self):
        """
        Test that given enconding is returned when file has no encoding defined.
        """
        self.failUnlessEqual(polib.detect_encoding('tests/test_noencoding.po'), 'utf-8')

    def test_detect_encoding2(self):
        """
        Test with a .pot file.
        """
        self.failUnlessEqual(polib.detect_encoding('tests/test_merge.pot'), 'utf-8')

    def test_detect_encoding3(self):
        """
        Test with an utf8 .po file.
        """
        self.failUnlessEqual(polib.detect_encoding('tests/test_utf8.po'), 'UTF-8')

    def test_detect_encoding4(self):
        """
        Test with utf8 data (no file).
        """
        self.failUnlessEqual(polib.detect_encoding(open('tests/test_utf8.po','r').read()), 'UTF-8')

    def test_detect_encoding5(self):
        """
        Test with utf8 .mo file.
        """
        self.failUnlessEqual(polib.detect_encoding('tests/test_utf8.mo', True), 'UTF-8')

    def test_detect_encoding6(self):
        """
        Test with iso-8859-15 .po file.
        """
        self.failUnlessEqual(polib.detect_encoding('tests/test_iso-8859-15.po'), 'ISO_8859-15')

    def test_detect_encoding7(self):
        """
        Test with iso-8859-15 .mo file.
        """
        self.failUnlessEqual(polib.detect_encoding('tests/test_iso-8859-15.mo', True), 'ISO_8859-15')

    def test_escape(self):
        """
        Tests the escape function.
        """
        self.failUnlessEqual(
            polib.escape('\\t and \\n and \\r and " and \\ and \\\\'),
            '\\\\t and \\\\n and \\\\r and \\" and \\\\ and \\\\\\\\'
        )

    def test_unescape(self):
        """
        Tests the unescape function.
        """
        self.failUnlessEqual(
            polib.unescape('\\\\t and \\\\n and \\\\r and \\\\" and \\\\\\\\'),
            '\\t and \\n and \\r and \\" and \\\\'
        )


if __name__ == '__main__':
    unittest.main()
