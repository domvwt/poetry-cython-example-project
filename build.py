import os
from pathlib import Path
from distutils.command.build_ext import build_ext
from distutils.core import Distribution
from Cython.Build import cythonize

# Define the source directory for the project
source_dir = Path("src")
# Set the compilation and linking arguments, include directories, and libraries
compile_args = []
link_args = []
include_dirs = []
libraries = []


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
        compiler_directives={"binding": True, "language_level": 3},
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
