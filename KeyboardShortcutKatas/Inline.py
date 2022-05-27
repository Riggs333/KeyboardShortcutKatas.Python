"""
Inline as much as you can using your IDE keyboard shortcuts.
Run the test at the bottom regularly to check you did not break anything.
"""


def n():
    return False


e = 2


class Inline:

    def a(self):
        return 5

    def practice(self):
        i = 2
        s = 2 - i
        j = (self.b() - self.a() + i)
        m = self.f(3)
        l = m + j
        if n():
            m += 56
        k = lambda: l - Inline().c(e)

        q = 1 - O().create().p
        return 42 + k() + q + Extensions.h(7) + s

    def f(self, G):
        return -3 + G

    def c(self, d: int) -> int:
        return d

    def b(self):
        return 5


class Extensions:

    def h(that: int):
        return that - 7


class O:
    p = 1

    def create(self):
        return O()


def test_answer():
    actual_answer = Inline().practice()
    expected = str(0x2a)
    assert hex(actual_answer) == '0x2a', f"The answer should be {expected}"
