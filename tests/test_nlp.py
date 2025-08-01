from assistant.core.nlp_engine import NLPEngine

def test_intent_classification():
    nlp = NLPEngine()
    assert nlp.classify_intent('Hello') == 'greet'
