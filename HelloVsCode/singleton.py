from abc import ABCMeta

# import functools

# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]

# class Singleton(object):
#     _instance = None
#     def __new__(class_, *args, **kwargs):
#         if not isinstance(class_._instance, class_):
#             class_._instance = object.__new__(class_, *args, **kwargs)
#         return class_._instance

# THIS WORKS
# def singleton(class_):
#     instances = {}
#     def getinstance(*args, **kwargs):
#         if class_ not in instances:
#             instances[class_] = class_(*args, **kwargs)
#         return instances[class_]
#     return getinstance

# THIS WORKS
# def singleton(class_):
#     class class_w(class_):
#         _instance = None

#         def __new__(class_, *args, **kwargs):
#             if class_w._instance is None:
#                 class_w._instance = super(class_w, class_).__new__(
#                     class_
#                 )
#                 # class_w._instance = super(class_w, class_).__new__(
#                     # class_, *args, **kwargs
#                 # )
#                 class_w._instance._sealed = False
#             return class_w._instance

#         def __init__(self, *args, **kwargs):
#             if self._sealed:
#                 return
#             super(class_w, self).__init__(*args, **kwargs)
#             self._sealed = True

#     class_w.__name__ = class_.__name__
#     return class_w

# THIS WORKS
# def singleton(cls):
#     cls.__call__ = lambda self: self
#     return cls()


# FINAL 1. THIS WORKS
#       With this we can add "@singleton" decorator to each of the derived class
#       We can't add to the base class
# https://github.com/siddheshsathe/handy-decorators/blob/master/src/decorators.py
# def singleton(cls):
# #     """
# #     Handy decorator for creating a singleton class
# #     Description:
# #         - Decorate your class with this decorator
# #         - If you happen to create another instance of the same class, it will return the previously created one
# #         - Supports creation of multiple instances of same class with different args/kwargs
# #         - Works for multiple classes
# #     Use:
# #         >>> from decorators import singleton
# #         >>>
# #         >>> @singleton
# #         ... class A:
# #         ...     def __init__(self, *args, **kwargs):
# #         ...         pass
# #     """
#     previous_instances = {}
#     @functools.wraps(cls)
#     def wrapper(*args, **kwargs):
#         if cls in previous_instances and previous_instances.get(cls, None).get('args') == (args, kwargs):
#             return previous_instances[cls].get('instance')
#         else:
#             previous_instances[cls] = {
#                 'args': (args, kwargs),
#                 'instance': cls(*args, **kwargs)
#             }
#             return previous_instances[cls].get('instance')
#     return wrapper

# FINAL 2. THIS WORKS
#       With this, we can just make the base class as Singleton and all derived class automatically
#       becomes singleton
class Singleton(ABCMeta):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
