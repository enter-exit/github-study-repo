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
# #
# obj = B()
# obj2 = B.__call__()

# print(obj,obj2)
# print(obj is obj2)
# print('*'*100)
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
#         obj = super().__new__(cls)
#         return obj
#     def __init__(self):
#         print('init-B')
    
# obj = B()
# obj2 = B.__call__()
# print(obj,obj2)
# print(obj is obj2)
from typing import Any


print('*'*100)

class A(type):
    obj = None
    def __new__(cls,*args, **kwargs):
        print('A-new')
        return super().__new__(cls,*args, **kwargs)
    def __init__(self,*args, **kwargs) -> None:
        print('A-init')
        # print(args,kwargs)
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if not self.obj:
            self.obj = self.__new__(self)
        self.__init__(self.obj)
        return self.obj
# B = A('B',(),{})
# B = A.__call__(A,'B',(),{})
class B(metaclass=A):
   def __new__(cls):
       print('B-new')
       return super().__new__(cls)
   def __init__(self, *args, **kwargs) -> None:
       print('B-init')
       
obj = B()
obj2 = B.__call__()
print(obj,obj2)
print(obj is obj2)