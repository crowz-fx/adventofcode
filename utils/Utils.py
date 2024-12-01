"""
Global functions to use for ease of running things
"""

import sys
from enum import Enum


class PrintType(Enum):
    INFO = "-->"
    ERROR = "$$>"
    WARN = "??>"
    DONE = "##>"


class Utils:
    def __init__(self):
        pass

    def out(self, message="", type=PrintType.INFO):
        print(f"{type.value} {message}")

    def err(self, message="", type=PrintType.ERROR):
        self.out(type=type, message=message)

    def dun(self, message="", type=PrintType.DONE):
        self.out(type=type, message=message)

    def war(self, message="", type=PrintType.WARN):
        self.out(type=type, message=message)

    def get_file_contents(self, file, open_mode="r"):
        try:
            with open(file, open_mode) as file:
                file_contents = file.readlines()
            return file_contents
        except FileNotFoundError:
            self.err(f"Dude, where the f is the file [{file}]?")
            sys.exit(1)
        except Exception:
            self.err(f"Something else happened when looking/reading file, look up ^^^")
            raise

    def file_contents(self, root_dir, file_name):
        return self.get_file_contents(f"{root_dir}/{file_name}")

    def error_out(self):
        raise RuntimeError(f"{PrintType.ERROR.value} Whoops! -- Look up ^^^")

    def run_solution(
        self,
        root_dir="",
        test_count=1,
        run_tests=True,
        run_input=True,
        part=1,
        solution=(),
    ):
        # run test and validate correct result, if yes run full input
        print()
        self.out(f"Executing solution part [{part}]...")

        if run_tests:
            self.out("Running tests...")
            for i in range(1, test_count + 1):
                self.out(f"Running test [{i}]...")
                test_result_actual = solution(
                    self.file_contents(root_dir, f"test_{i}.txt")
                )
                test_result_expected = int(
                    str(
                        self.file_contents(
                            root_dir, f"part_{part}_test_{i}_result.txt"
                        )[0]
                    )
                    .replace("\n", "")
                    .strip()
                )

                if not test_result_actual:
                    self.err("You need to write the solution!")
                    self.error_out()

                if not test_result_expected:
                    self.err(f"Where is the expected result for test [{i}]?")
                    self.error_out()

                if test_result_actual == test_result_expected:
                    self.dun(f"Test [{i}] passed!")
                else:
                    self.err(
                        f"Test [{i}] failed, expected [{test_result_expected}] but got [{test_result_actual}]!"
                    )
                    self.error_out()

            self.dun("Tests completed!")

        if run_input:
            self.out("Running input...")
            self.dun(
                f"Output from part [{part}] solution [{solution(self.file_contents(root_dir, 'input.txt'))}]"
            )
