def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Returns:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    if hasattr(iterable, '__iter__'):
        ret = iterable[0]
        for elem in iterable[1:]:
            ret = function_to_apply(ret, elem)
        return ret
    else:
        return None
