from contextlib import contextmanager


@contextmanager
def managed_file(name):
    try:
        file = open(name, "w")
        yield file
    finally:
        file.close()


with managed_file("./context_manager_decorator/my_file.txt") as file:
    file.write("hello @contextmanager")
