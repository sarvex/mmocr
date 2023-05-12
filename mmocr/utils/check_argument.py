# Copyright (c) OpenMMLab. All rights reserved.


def is_3dlist(x):
    """check x is 3d-list([[[1], []]]) or 2d empty list([[], []]) or 1d empty
    list([]).

    Notice:
        The reason that it contains 1d or 2d empty list is because
        some arguments from gt annotation file or model prediction
        may be empty, but usually, it should be 3d-list.
    """
    if not isinstance(x, list):
        return False
    return True if len(x) == 0 else all(is_2dlist(sub_x) for sub_x in x)


def is_2dlist(x):
    """check x is 2d-list([[1], []]) or 1d empty list([]).

    Notice:
        The reason that it contains 1d empty list is because
        some arguments from gt annotation file or model prediction
        may be empty, but usually, it should be 2d-list.
    """
    if not isinstance(x, list):
        return False
    return True if len(x) == 0 else all(isinstance(item, list) for item in x)


def is_type_list(x, type):

    if not isinstance(x, list):
        return False

    return all(isinstance(item, type) for item in x)


def is_none_or_type(x, type):

    return isinstance(x, type) or x is None


def equal_len(*argv):
    assert argv

    num_arg = len(argv[0])
    return all(len(arg) == num_arg for arg in argv)


def valid_boundary(x, with_score=True):
    num = len(x)
    if num < 8:
        return False
    if num % 2 == 0 and (not with_score):
        return True
    return bool(num % 2 == 1 and with_score)
