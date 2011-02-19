#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(1, os.path.abspath('.'))

import polib


class TestFunctions(unittest.TestCase):

    def test_pofile_and_mofile1(self):
        """
        Test bad usage of pofile/mofile. 
        """
        data = u'''# test for pofile/mofile with string buffer
msgid ""
msgstr ""
"Project-Id-Version: django\n"

msgid "foo"
msgstr "bar"
'''
        po = polib.pofile(data)
        self.assertTrue(isinstance(po, polib.POFile))
        self.assertEqual(po.encoding, 'utf-8')
        self.assertEqual(po[0].msgstr, u"bar")

    def test_pofile_and_mofile2(self):
        """
        Test that the pofile function returns a POFile instance.
        """
        po = polib.pofile('tests/test_utf8.po')
        self.assertTrue(isinstance(po, polib.POFile))

    def test_pofile_and_mofile3(self):
        """
        Test  that the mofile function returns a MOFile instance.
        """
        mo = polib.mofile('tests/test_utf8.mo')
        self.assertTrue(isinstance(mo, polib.MOFile))

    def test_pofile_and_mofile4(self):
        """
        Test that check_for_duplicates is passed to the instance.
        """
        po = polib.pofile('tests/test_iso-8859-15.po', check_for_duplicates=True)
        self.assertTrue(po.check_for_duplicates == True)

    def test_pofile_and_mofile5(self):
        """
        Test that detect_encoding works as expected.
        """
        po = polib.pofile('tests/test_iso-8859-15.po')
        self.assertTrue(po.encoding == 'ISO_8859-15')

    def test_pofile_and_mofile6(self):
        """
        Test that encoding is default_encoding when detect_encoding is False.
        """
        po = polib.pofile('tests/test_noencoding.po', autodetect_encoding=False)
        self.assertTrue(po.encoding == 'utf-8')

    def test_pofile_and_mofile7(self):
        """
        Test that encoding is ok when encoding is explicitely given.
        """
        po = polib.pofile('tests/test_iso-8859-15.po', autodetect_encoding=False, encoding='iso-8859-15')
        self.assertTrue(po.encoding == 'iso-8859-15')

    def test_detect_encoding1(self):
        """
        Test that given enconding is returned when file has no encoding defined.
        """
        self.assertEqual(polib.detect_encoding('tests/test_noencoding.po'), 'utf-8')

    def test_detect_encoding2(self):
        """
        Test with a .pot file.
        """
        self.assertEqual(polib.detect_encoding('tests/test_merge.pot'), 'utf-8')

    def test_detect_encoding3(self):
        """
        Test with an utf8 .po file.
        """
        self.assertEqual(polib.detect_encoding('tests/test_utf8.po'), 'UTF-8')

    def test_detect_encoding4(self):
        """
        Test with utf8 data (no file).
        """
        self.assertEqual(polib.detect_encoding(open('tests/test_utf8.po','r').read()), 'UTF-8')

    def test_detect_encoding5(self):
        """
        Test with utf8 .mo file.
        """
        self.assertEqual(polib.detect_encoding('tests/test_utf8.mo', True), 'UTF-8')

    def test_detect_encoding6(self):
        """
        Test with iso-8859-15 .po file.
        """
        self.assertEqual(polib.detect_encoding('tests/test_iso-8859-15.po'), 'ISO_8859-15')

    def test_detect_encoding7(self):
        """
        Test with iso-8859-15 .mo file.
        """
        self.assertEqual(polib.detect_encoding('tests/test_iso-8859-15.mo', True), 'ISO_8859-15')

    def test_escape(self):
        """
        Tests the escape function.
        """
        self.assertEqual(
            polib.escape('\\t and \\n and \\r and " and \\ and \\\\'),
            '\\\\t and \\\\n and \\\\r and \\" and \\\\ and \\\\\\\\'
        )

    def test_unescape(self):
        """
        Tests the unescape function.
        """
        self.assertEqual(
            polib.unescape('\\\\t and \\\\n and \\\\r and \\\\" and \\\\\\\\'),
            '\\t and \\n and \\r and \\" and \\\\'
        )


class TestBaseFile(unittest.TestCase):
    """
    Tests for the _BaseFile class.
    """

    def test_append1(self):
        pofile = polib.pofile('tests/test_pofile_helpers.po')
        entry = polib.POEntry(msgid="Foo", msgstr="Bar", msgctxt="Some context")
        pofile.append(entry)
        self.assertTrue(entry in pofile)

    def test_append2(self):
        def add_duplicate():
            pofile = polib.pofile('tests/test_pofile_helpers.po', check_for_duplicates=True)
            pofile.append(polib.POEntry(msgid="and", msgstr="y"))
        self.assertRaises(ValueError, add_duplicate)

    def test_insert1(self):
        pofile = polib.pofile('tests/test_pofile_helpers.po')
        entry = polib.POEntry(msgid="Foo", msgstr="Bar", msgctxt="Some context")
        pofile.insert(0, entry)
        self.assertEqual(pofile[0], entry)

    def test_insert2(self):
        def add_duplicate():
            pofile = polib.pofile('tests/test_pofile_helpers.po', check_for_duplicates=True)
            pofile.insert(0, polib.POEntry(msgid="and", msgstr="y"))
        self.assertRaises(ValueError, add_duplicate)

    def test_metadata_as_entry(self):
        pofile = polib.pofile('tests/test_fuzzy_header.po')
        lines  = open('tests/test_fuzzy_header.po').readlines()[2:]
        self.assertEqual(unicode(pofile.metadata_as_entry()), "".join(lines))

    def test_find1(self):
        pofile = polib.pofile('tests/test_pofile_helpers.po')
        entry = pofile.find('and')
        self.assertEqual(entry.msgstr, u'y')

    def test_find2(self):
        pofile = polib.pofile('tests/test_pofile_helpers.po')
        entry = pofile.find('pacote', by="msgstr")
        self.assertEqual(entry, None)

    def test_find3(self):
        pofile = polib.pofile('tests/test_pofile_helpers.po')
        entry = pofile.find('package', include_obsolete_entries=True)
        self.assertEqual(entry.msgstr, u'pacote')

    def test_find4(self):
        pofile = polib.pofile('tests/test_utf8.po')
        entry1 = pofile.find('test context', msgctxt='@context1')
        entry2 = pofile.find('test context', msgctxt='@context2')
        self.assertEqual(entry1.msgstr, u'test context 1')
        self.assertEqual(entry2.msgstr, u'test context 2')

    def test_save1(self):
        pofile = polib.POFile()
        self.assertRaises(IOError, pofile.save)

    def test_save2(self):
        tmpfile = tempfile.mkstemp()[1]
        pofile = polib.POFile()
        pofile.save(tmpfile)
        pofile.save()
        self.assertTrue(os.path.isfile(tmpfile))

    def test_ordered_metadata(self):
        pofile = polib.pofile('tests/test_fuzzy_header.po')
        lines  = open('tests/test_fuzzy_header.po').readlines()[2:]
        mdata  = [
            ('Project-Id-Version', u'PACKAGE VERSION'),
            ('Report-Msgid-Bugs-To', u''),
            ('POT-Creation-Date', u'2010-02-08 16:57+0100'),
            ('PO-Revision-Date', u'YEAR-MO-DA HO:MI+ZONE'),
            ('Last-Translator', u'FULL NAME <EMAIL@ADDRESS>'),
            ('Language-Team', u'LANGUAGE <LL@li.org>'),
            ('MIME-Version', u'1.0'),
            ('Content-Type', u'text/plain; charset=UTF-8'),
            ('Content-Transfer-Encoding', u'8bit')
        ]
        self.assertEqual(pofile.ordered_metadata(), mdata)

    def test_unicode1(self):
        pofile  = polib.pofile('tests/test_merge_after.po')
        expected = codecs.open('tests/test_merge_after.po', encoding='utf8').read()
        self.assertEqual(unicode(pofile), unicode(expected))

    def test_unicode2(self):
        pofile  = polib.pofile('tests/test_iso-8859-15.po')
        expected = codecs.open('tests/test_iso-8859-15.po', encoding='iso-8859-15').read()
        self.assertEqual(unicode(pofile), unicode(expected))

    def test_str(self):
        pofile  = polib.pofile('tests/test_iso-8859-15.po')
        expected = open('tests/test_iso-8859-15.po').read()
        self.assertEqual(str(pofile), expected)

    def test_wrapping(self):
        pofile  = polib.pofile('tests/test_wrap.po', wrapwidth=50)
        expected = r'''# test wrapping
msgid ""
msgstr ""

msgid "This line will not be wrapped"
msgstr ""

msgid ""
"Some line that contain special characters \" and"
" that \t is very, very, very long...: %s \n"
msgstr ""

msgid ""
"Some line that contain special characters "
"\"foobar\" and that contains whitespace at the "
"end          "
msgstr ""
'''
        self.assertEqual(str(pofile), expected)

    def test_sort(self):
        a1 = polib.POEntry(msgid='a1', occurrences=[('b.py', 1), ('b.py', 3)])
        a2 = polib.POEntry(msgid='a2')
        a3 = polib.POEntry(msgid='a1', occurrences=[('b.py', 1), ('b.py', 3)], obsolete=True)
        b1 = polib.POEntry(msgid='b1', occurrences=[('b.py', 1), ('b.py', 3)])
        b2 = polib.POEntry(msgid='b2', occurrences=[('d.py', 3), ('b.py', 1)])
        c1 = polib.POEntry(msgid='c1', occurrences=[('a.py', 1), ('b.py', 1)])
        c2 = polib.POEntry(msgid='c2', occurrences=[('a.py', 1), ('a.py', 3)])
        pofile = polib.POFile()
        pofile.append(b1)
        pofile.append(a3)
        pofile.append(a2)
        pofile.append(a1)
        pofile.append(b2)
        pofile.append(c1)
        pofile.append(c2)
        pofile.sort()
        expected = u'''# 
msgid ""
msgstr ""

msgid "a2"
msgstr ""

#: a.py:1 a.py:3
msgid "c2"
msgstr ""

#: a.py:1 b.py:1
msgid "c1"
msgstr ""

#: b.py:1 b.py:3
msgid "a1"
msgstr ""

#: b.py:1 b.py:3
msgid "b1"
msgstr ""

#: d.py:3 b.py:1
msgid "b2"
msgstr ""

#~ msgid "a1"
#~ msgstr ""
'''
        self.assertEqual(unicode(pofile), expected)

class TestPoFile(unittest.TestCase):
    """
    Tests for MoFile class.
    """

    def test_save_as_mofile(self):
        """
        Test for the POFile.save_as_mofile() method.
        """
        reffiles = ['tests/test_utf8.po', 'tests/test_iso-8859-15.po']
        for reffile in reffiles:
            tmpfile1 = tempfile.mkstemp()[1]
            tmpfile2 = tempfile.mkstemp()[1]
            po = polib.pofile(reffile)
            po.save_as_mofile(tmpfile1)
            subprocess.call(['msgfmt', '--no-hash', '-o', tmpfile2, reffile])
            try:
                self.assertEqual(open(tmpfile1).read(), open(tmpfile2).read())
            finally:
                os.remove(tmpfile1)
                os.remove(tmpfile2)

    def test_merge(self):
        refpot = polib.pofile('tests/test_merge.pot')
        po = polib.pofile('tests/test_merge_before.po')
        po.merge(refpot)
        expected_po = polib.pofile('tests/test_merge_after.po')
        self.assertEqual(po, expected_po)

    def test_percent_translated(self):
        po = polib.pofile('tests/test_pofile_helpers.po')
        self.assertEqual(po.percent_translated(), 50)
        po = polib.POFile()
        self.assertEqual(po.percent_translated(), 100)

    def test_translated_entries(self):
        po = polib.pofile('tests/test_pofile_helpers.po')
        self.assertEqual(len(po.translated_entries()), 6)

    def test_untranslated_entries(self):
        po = polib.pofile('tests/test_pofile_helpers.po')
        self.assertEqual(len(po.untranslated_entries()), 4)

    def test_fuzzy_entries(self):
        po = polib.pofile('tests/test_pofile_helpers.po')
        self.assertEqual(len(po.fuzzy_entries()), 2)

    def test_obsolete_entries(self):
        po = polib.pofile('tests/test_pofile_helpers.po')
        self.assertEqual(len(po.obsolete_entries()), 4)


class TestMoFile(unittest.TestCase):
    """
    Tests for MoFile class.
    """
    def test_dummy_methods(self):
        """
        This is stupid and just here for code coverage.
        """
        mo = polib.MOFile()
        self.assertEqual(mo.percent_translated(), 100)
        self.assertEqual(mo.translated_entries(), mo)
        self.assertEqual(mo.untranslated_entries(), [])
        self.assertEqual(mo.fuzzy_entries(), [])
        self.assertEqual(mo.obsolete_entries(), [])

    def test_save_as_pofile(self):
        """
        Test for the MOFile.save_as_pofile() method.
        """
        tmpfile = tempfile.mkstemp()[1]
        mo = polib.mofile('tests/test_utf8.mo', wrapwidth=78)
        mo.save_as_pofile(tmpfile)
        try:
            self.assertEqual(open(tmpfile).read(), open('tests/test_save_as_pofile.po').read())
        finally:
            os.remove(tmpfile)

if __name__ == '__main__':
    unittest.main()
