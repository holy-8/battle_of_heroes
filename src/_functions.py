def clamp(_num: int | float,
          _min: int | float,
          _max: int | float):
    """
    Returns _num if _num in range(_min, _max), otherwise returns _min or _max.
    """
    if _num > _max:
        return _max

    if _num < _min:
        return _min

    return _num
