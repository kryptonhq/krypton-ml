def load_module(callable_path: str) -> callable:
    """
    Load a module from a callable path
    :param callable_path:
    :return: callable object
    """
    module_name, callable_name = callable_path.rsplit(".", 1)
    module = __import__(module_name, fromlist=[callable_name])
    return getattr(module, callable_name)