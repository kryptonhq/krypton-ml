import importlib.util
import os
import sys
from typing import Callable


def load_module(module_path: str, callable_path: str) -> Callable:
    """
    Load a module from a file path and return a callable object.

    :param module_path: The file path to the Python module
    :param callable_path: The dot-separated path to the callable within the module
    :return: The callable object
    """

    # Split the callable path into package, module, and callable parts
    parts = callable_path.split(".")
    package_name = parts[0]
    module_name = parts[1]
    callable_name = ".".join(parts[2:])

    # Construct the full path to the package
    package_path = os.path.join(module_path, package_name)

    # Add the package path to sys.path temporarily
    sys.path.insert(0, module_path)

    try:
        # Import the module
        module = importlib.import_module(f"{package_name}.{module_name}")

        # Get the callable from the module
        obj = module
        for part in parts[2:]:
            obj = getattr(obj, part)

        return obj

    except ImportError:
        raise ImportError(
            f"Could not import module {package_name}.{module_name} from {package_path}"
        )
    except AttributeError:
        raise AttributeError(
            f"Could not find callable '{callable_name}' in module {package_name}.{module_name}"
        )
    finally:
        # Remove the temporarily added path
        sys.path.pop(0)
