# -*- coding: utf-8 -*=
from __future__ import unicode_literals
from twaddr.autocomplete import get_autocomplete_handler


def test_autocomplete():
    ac = get_autocomplete_handler()
    assert ac.query('市政北七路')[0] == '市政北七路'
    assert ac.query('台中港路') == []
