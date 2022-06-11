from attrdict import AttrDict

if __name__ == '__main__':
    d = AttrDict(x=1, y=2, z=[3, 4, 5])
    assert d.x == 1 and d.y == 2 and sum(d.z) == 12

    d = AttrDict({'a': 3, 'b': 4}, c=5)
    assert d.a == 3 and d.b == 4 and d.c == 5

    d = AttrDict(dict(
        a=1,
        b='x',
        c=[1, 2, 3],
        d=dict(
            e=4,
            f=5,
            g=dict(
                h=6,
                i=7,
                j=AttrDict(
                    k='a',
                    l='b'
                )
            )
        )
    ))
    assert d.a == 1 and d.b == 'x' and d.c[1] == 2
    assert d.d.e == 4 and d.d.g.i == 7 and d.d.g.j.l == 'b'

    _d = d.__dict__
    assert not isinstance(_d, AttrDict) and isinstance(_d, dict)

    d = AttrDict(a=1, b='x')
    assert repr(d) == "<AttrDict a: 1, b: 'x'>", repr(d)
