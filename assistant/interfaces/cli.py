"""Simple CLI interface."""

import argparse
from assistant.core.nlp_engine import NLPEngine
from assistant.core.dialog_manager import DialogManager

def main():
    parser = argparse.ArgumentParser(description='AI Assistant CLI')
    parser.add_argument('--model', default='data/knowledge/faq.json')
    args = parser.parse_args()

    nlp = NLPEngine()
    dlg = DialogManager(nlp)

    print('CLI Assistant စတင်သုံးနိုင်ပါပြီ — "exit" ထွက်ရန်')
    while True:
        user = input('>> ')
        if user.strip().lower() == 'exit':
            break
        print(dlg.process('anon', user))

if __name__ == '__main__':
    main()
