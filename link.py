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
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __repr__(self):
        return f'({self.head}, {self.tail})'

def get_link(lst):
    '''
    >>> get_link(None)
    >>> get_link((1, 2, 3))
    (1, (2, (3, None)))
    '''
    if not lst:
        return None
    link = None
    for i in lst[::-1]:
        link = Link(i, link)
    return link

def reverse_link(link):
    '''
    >>> reverse_link(get_link((1, 2, 3)))
    (3, (2, (1, None)))
    '''
    prv, cur, nxt = None, link, link.tail if link else None
    while cur:
        pprv = prv
        prv, cur, nxt = cur, nxt, nxt.tail if nxt else None
        prv.tail = pprv
    return prv
