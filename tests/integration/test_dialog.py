from assistant.core.nlp_engine import NLPEngine
from assistant.core.dialog_manager import DialogManager

def test_dialog():
    dlg = DialogManager(NLPEngine())
    assert 'Hello' in dlg.process('u', 'hello')
