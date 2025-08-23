from django import template
register = template.Library()

def _group_thousands(n: int) -> str:
    s = f"{n:,}"                 # 90,000,000
    return s.replace(",", "\u202F")  # 90 000 000 (فاصله باریکِ بدون‌شکست)

@register.filter
def toman_pretty(value):
    """نمایش کامل با جداکننده هزار: 90000000 -> '90 000 000'"""
    try:
        n = int(float(value))
    except (TypeError, ValueError):
        return value
    return _group_thousands(n)

@register.filter
def toman_compact(value, digits=1):
    """نمایش خلاصه: 90000000 -> '90 میلیون'؛ digits اعشار را کنترل می‌کند."""
    try:
        n = int(float(value))
    except (TypeError, ValueError):
        return value

    units = [(10**9, "میلیارد"), (10**6, "میلیون"), (10**3, "هزار")]
    for factor, name in units:
        if n >= factor:
            v = n / factor
            s = f"{int(v)}" if float(v).is_integer() else f"{v:.{int(digits)}f}"
            return f"{s} {name}"
    return _group_thousands(n)
