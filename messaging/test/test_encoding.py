# -*- coding: utf-8 -*-
import unittest

from messaging.pdu import PDU

class TestEncodingFunctions(unittest.TestCase):

    def setUp(self):
        self.pdu = PDU()

    def test_encoding_7bit_message_with_msmc(self):
        number = "+34616585119"
        text = "hola"
        csca = "+34646456456"
        expected = "07914346466554F611000B914316565811F90000AA04E8373B0C"

        pdu = self.pdu.encode_pdu(number, text, csca=csca)[0]
        self.assertEqual(pdu[1], expected)

    def test_encoding_7bit_message_without_msmc(self):
        number = "+34616585119"
        text = "hola"
        expected = "0011000B914316565811F90000AA04E8373B0C"

        pdu = self.pdu.encode_pdu(number, text)[0]
        self.assertEqual(pdu[1], expected)

    def test_encoding_7bit_to_store_message(self):
        number = "+34123456"
        csca = "+34987654"
        text = "hey there"
        expected = "0591438967450100089143214365000009E8721E444797E565"

        pdu = self.pdu.encode_pdu(number, text, csca=csca, store=True)[0]
        self.assertEqual(pdu[1], expected)

    def test_encoding_ucs2_message_with_smsc(self):
        number = "+34616585119"
        text = u'あ叶葉'
        csca = '+34646456456'
        expected = "07914346466554F611000B914316565811F90008AA06304253F68449"

        pdu = self.pdu.encode_pdu(number, text, csca=csca)[0]
        self.assertEqual(pdu[1], expected)

    def test_encoding_ucs2_message_without_smsc(self):
        number = "+34616585119"
        text = u'あ叶葉'
        expected = "0011000B914316565811F90008AA06304253F68449"

        pdu = self.pdu.encode_pdu(number, text)[0]
        self.assertEqual(pdu[1], expected)

    def test_encoding_ucs2_message_without_smsc_2(self):
        text = "Русский"
        number = "655345678"
        expected = "001100098156355476F80008AA1C00D000A000D1008300D1008100D1008100D000BA00D000B800D000B9"

        pdu = self.pdu.encode_pdu(number, text)[0]
        self.assertEqual(pdu[1], expected)

    def test_encoding_multipart_7bit(self):
        # text encoded with umts-tools
        text = "Or walk with Kings - nor lose the common touch, if neither foes nor loving friends can hurt you, If all men count with you, but none too much; If you can fill the unforgiving minute With sixty seconds' worth of distance run, Yours is the Earth and everything thats in it, And - which is more - you will be a Man, my son"
        number = "655345678"
        expected = [
            "005100098156355476F80000AAA00500038803019E72D03DCC5E83EE693A1AB44CBBCF73500BE47ECB41ECF7BC0CA2A3CBA0F1BBDD7EBB41F4777D8C6681D26690BB9CA6A3CB7290F95D9E83DC6F3988FDB6A7DD6790599E2EBBC973D038EC06A1EB723A28FFAEB340493328CC6683DA653768FCAEBBE9A07B9A8E06E5DF7516485CA783DC6F7719447FBF41EDFA18BD0325CDA0FCBB0E1A87DD",
            "005100098156355476F80000AAA005000388030240E6349B0DA2A3CBA0BADBFC969FD3F6B4FB0C6AA7DD757A19744DD3D1A0791A4FCF83E6E5F1DB4D9E9F40F7B79C8E06BDCD20727A4E0FBBC76590BCEE6681B2EFBA7C0E4ACF41747419540CCBE96850D84D0695ED65799E8E4EBBCF203A3A4C9F83D26E509ACE0205DD64500B7447A7C768507A0E6ABFE565500B947FD741F7349B0D129741",
            "005100098156355476F80000AA14050003880303C2A066D8CD02B5F3A0F9DB0D",
        ]
        for i, (pdu_len, pdu) in enumerate(self.pdu.encode_pdu(number, text, rand_id=136)):
            self.assertEqual(expected[i], pdu)

