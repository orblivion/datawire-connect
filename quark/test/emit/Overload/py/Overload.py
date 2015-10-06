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

class Overload:
    def _init(self):
        self.name = None
    
    
    
    def __init__(self, name):
        self._init()
        (self).name = name
    
    
    def __add__(self, o):
        return o;
    
    
    def __mul__(self, o):
        return self;
    
    
    def test(self):
        o1 = Overload("one");
        o2 = Overload("two");
        o3 = (o1).__add__(o2);
        _println((o3).name);
        o3 = (o1).__mul__(o2)
        _println((o3).name);
        if ((o3) == (o1)):
            _println("YAY!");
        
    


def main():
    o = Overload("test");
    (o).test();


if __name__ == "__main__":
    main()
