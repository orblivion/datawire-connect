import os, sys

_Map = dict
class _List(list):
    def __repr__(self):
        return "[%s]" % ", ".join([str(e) for e in self])

def _println(obj):
    if obj is None:
        sys.stdout.write("null\n")
    else:
        sys.stdout.write("%s\n" % obj)


def main():
    four = (2) + (2);
    _println(str(four));
    half = (1) / (2);
    _println(str(half));
    num = 314;
    den = 100;
    pi = float(num) / float(den);
    _println(str(pi));
    n = -(100);
    x = -(100);


if __name__ == "__main__":
    main()
