# encoding: utf-8
# module _xxsubinterpreters
# from (built-in)
# by generator 1.147
"""
This module provides primitive operations to manage Python interpreters.
The 'interpreters' module provides a more convenient interface.
"""
# no imports

# functions

def create(): # real signature unknown; restored from __doc__
    """
    create() -> ID
    
    Create a new interpreter and return a unique generated ID.
    """
    pass

def destroy(id): # real signature unknown; restored from __doc__
    """
    destroy(id)
    
    Destroy the identified interpreter.
    
    Attempting to destroy the current interpreter results in a RuntimeError.
    So does an unrecognized ID.
    """
    pass

def get_current(): # real signature unknown; restored from __doc__
    """
    get_current() -> ID
    
    Return the ID of current interpreter.
    """
    pass

def get_main(): # real signature unknown; restored from __doc__
    """
    get_main() -> ID
    
    Return the ID of main interpreter.
    """
    pass

def is_running(id): # real signature unknown; restored from __doc__
    """
    is_running(id) -> bool
    
    Return whether or not the identified interpreter is running.
    """
    return False

def is_shareable(obj): # real signature unknown; restored from __doc__
    """
    is_shareable(obj) -> bool
    
    Return True if the object's data may be shared between interpreters and
    False otherwise.
    """
    return False

def list_all(): # real signature unknown; restored from __doc__
    """
    list_all() -> [ID]
    
    Return a list containing the ID of every existing interpreter.
    """
    pass

def run_string(id, script, shared): # real signature unknown; restored from __doc__
    """
    run_string(id, script, shared)
    
    Execute the provided string in the identified interpreter.
    
    See PyRun_SimpleStrings.
    """
    pass

# classes

class InterpreterID(object):
    """ A interpreter ID identifies a interpreter and may be used as an int. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class RunFailedError(RuntimeError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000002393B9BEF20>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000002393B9BEFC0>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000002393B9BF060>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000002393B9BF1A0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000002393B9BF2E0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000002393B9BF420>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000002393B9BE2A0>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_xxsubinterpreters', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

