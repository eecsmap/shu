# run python3 -m doctest link.py
 
class Link:
    '''
    >>> link = Link(1, None)
    >>> link
    (1, None)
    >>> link = Link(2, link)
    >>> link
    (2, (1, None))
    '''

def get_link(lst):
    '''
    >>> get_link(None)
    >>> get_link((1, 2, 3))
    (1, (2, (3, None)))
    '''

def reverse_link(link):
    '''
    >>> reverse_link(get_link((1, 2, 3)))
    (3, (2, (1, None)))
    '''
