from pathlib import Path
from distutils.command.build_ext import build_ext
from distutils.core import Distribution
from Cython.Build import cythonize


# fmt: off
source_dir = Path("src") # Define the source directory for the project

compile_args = []  # Additional command-line arguments to pass to the C compiler when building the extension module
link_args = []     # Additional command-line arguments to pass to the linker when building the extension module
include_dirs = []  # List of additional directories to search for header files when building the extension module
libraries = []     # List of additional libraries to link against when building the extension module

compiler_directives = {
    "binding": False,                      # Generate Python bindings for C/C++ libraries
    "linetrace": False,                    # Enable line tracing in the generated C code
    "language_level": 3,                   # Specify the version of Python to use
    "boundscheck": False,                  # Enable or disable runtime bounds checking on array and memory access
    "wraparound": False,                   # Enable or disable wrapping of array indices around when they exceed the bounds of the array
    "cdivision": True,                     # Enable C-style division instead of Python-style division
    "infer_types": True,                   # Enable type inference to generate more optimized C code
    "nonecheck": False,                    # Enable or disable runtime checks for None values
    "initializedcheck": False,             # Enable or disable runtime checks for uninitialized variables
    "optimize.unpack_method_calls": True,  # Unpack method calls into direct C function calls to improve performance
}
# fmt: on


def find_pyx_files(root_dir):
    """Find all .pyx files in the given root directory."""
    return [str(path) for path in Path(root_dir).glob("**/*.pyx")]


def build():
    # Find all .pyx files in the source directory
    pyx_files = find_pyx_files(source_dir)

    # Compile the .pyx files to create extension modules
    ext_modules = cythonize(
        pyx_files,
        include_path=include_dirs,
        compiler_directives=compiler_directives,
        force=True,  # Force the recompilation, even if timestamps are up-to-date
        build_dir="build",
        nthreads=0,
    )

    # Create a distribution object with the required metadata
    distribution = Distribution({"name": "adders", "ext_modules": ext_modules})
    distribution.package_dir = str(source_dir)

    # Instantiate the build_ext command to compile the extension modules
    cmd = build_ext(distribution)
    cmd.ensure_finalized()
    cmd.run()

    # Copy the compiled extension modules back to the source directory
    for output in cmd.get_outputs():
        output_path = Path(output)
        relative_extension = output_path.relative_to(cmd.build_lib)
        destination = source_dir / relative_extension
        output_path.rename(destination)


if __name__ == "__main__":
    build()
