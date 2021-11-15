def yield_fun(function_to_apply, iterable):
    for elem in iterable:
        yield function_to_apply(elem)

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Returns:
        An iterable.
        None if the iterable can not be used by the function.
    # """
    if hasattr(iterable, '__iter__'):
        return yield_fun(function_to_apply, iterable)
    else:
        return None
    

    



x = [1, 2, 3, 4, 5]
# print("TEST")

# ft_map(lambda dum: dum + 1, None)
# # map(lambda dum: dum + 1, None)
# ft_map(lambda dum: dum + 1, [1, 2])
# ft_map(lambda dum: dum + 1, (1, 2))
# ft_map(lambda dum: dum + 1, "iquefgh")