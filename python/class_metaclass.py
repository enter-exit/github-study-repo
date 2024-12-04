# print('1'.center(100,'-'))
# class A(type):
#     obj = None
#     def __new__(cls, *args, **kwargs):
#         print('new')
#         return super().__new__(cls,*args,**kwargs)
#
#     def __init__(self,*args,**kwargs):
#         print('init')
#
#     def __call__(self, *args, **kwargs):
#         if not self.obj:
#             self.obj = self.__new__(self)
#         self.__init__(self.obj)
#         return self.obj
#
#
# # B = A('B',(),{})
# # B = A.__call__(A,'B',(),{})
# class B(metaclass=A):
#     def __new__(cls, *args, **kwargs):
#         print('new-B')
#         return super().__new__(cls)
#     def __init__(self):
#         print('init-B')
#
# obj = B()
# obj2 = B.__call__()
#
# print(obj,obj2)
# print(obj is obj2)
from struct import pack_into

# print('2'.center(100,'-'))
# class A(type):
#     obj = None
#     def __new__(cls, *args, **kwargs):
#         print('new-A')
#         return super().__new__(cls,*args,**kwargs)
#     def __init__(self,*args,**kwargs):
#         print('init-A')
#     def __call__(self, *args, **kwargs):
#         if not self.obj:
#             self.obj = self.__new__(self)
#         self.__init__(self.obj)
#         return self.obj
# # B = A('B',(),{})
# # B = A.__call__(A,'B',(),{})
# class B(metaclass=A):
#     def __new__(cls, *args, **kwargs):
#         print('new-B')
#         return super().__new__(cls)
#     def __init__(self):
#         print('init-B')
#
# obj = B()
# obj2 = B.__call__()
# print(obj,obj2)
# print(obj is obj2)

print('3'.center(100,'-'))
class A(type):
    obj = None
    def __new__(cls, *args, **kwargs):
        print('A-new')
        return super().__new__(cls,*args,**kwargs)

    def __init__(self,*args,**kwargs):
        print('A-init')
    def __call__(self, *args, **kwargs):
        if not self.obj:
            self.obj = self.__new__(self)
        self.__init__(self.obj)
        return self.obj
# B = A('B',(),{})
# B = A.__call__(A,'B',(),{})
class B(metaclass=A):
    def __new__(cls, *args, **kwargs):
        print('B-new')
        return super().__new__(cls,*args,**kwargs)
    def __init__(self):
        print('B-init')

obj = B()
obj2 = B.__call__()
print(obj,obj2)
print(obj is obj2)























