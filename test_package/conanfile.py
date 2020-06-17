import os.path

from conans import ConanFile, CMake


class Hdf5TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ("cmake_paths", "cmake_find_package")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        program = 'test_package'
        if self.settings.os == "Windows":
            program += '.exe'
            test_path = os.path.join(self.build_folder,
                                     str(self.settings.build_type))
        else:
            test_path = '.' + os.sep

        self.run(os.path.join(test_path, program), run_environment=True)
