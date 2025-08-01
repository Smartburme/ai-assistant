"""Calculator skill — basic arithmetic."""

def calculate(expression: str) -> str:
    try:
        result = eval(expression, {'__builtins__': {}})
        return str(result)
    except Exception:
        return 'တွက်ချက်မှုအမှားရှိပါသည်'
