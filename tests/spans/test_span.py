from __future__ import unicode_literals

import pytest



@pytest.fixture
def doc(en_nlp):
    return en_nlp('This is a sentence. This is another sentence. And a third.')


def test_sent_spans(doc):
    sents = list(doc.sents)
    assert sents[0].start == 0
    assert sents[0].end == 5
    assert len(sents) == 3
    assert sum(len(sent) for sent in sents) == len(doc)
