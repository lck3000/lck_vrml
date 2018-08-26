class WRLWriter:
    def write_wrl(text,dir_='test/test.wrl',mode='w+'):
        with open(dir_,mode) as wrl:
            wrl.write(text)

class Node:
    pass

class Group:
    pass

class WorldInfo:
    pass

class Shape:
    pass

class Transform:
    pass

class Appeareance:
    pass

class Material:
    pass

class NavigationInfo:
    pass

class Geometry:
    pass

class Box:
    pass

class Cone:
    pass

class Cylinder:
    pass

class Sphere:
    pass

class Text:
    pass



if __name__ == '__main__':

    text = '''#VRML V2.0 utf8

    Shape {
        geometry Cone {
            bottomRadius 30
            height 50
        }
    }
    '''
    write_wrl(text=text,mode='a+')
