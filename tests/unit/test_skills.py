from assistant.skills.calculator import calculate

def test_calculator():
    assert calculate('1+1') == '2'
