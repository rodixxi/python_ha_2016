def div(a, b):
    return a/b


class TestDiv(TestCase):
    def setUp(self):
        self.a = random.randint(1, 100)
        self.b = random.randint(1, 100)

    def test_div_comun(self):
        self.assertEquals(div(self.a, self.b), a/b)

    def test_div_0(self):
        with self.assertRaises("No dividas por 0 ctm!!!"):
            div(self.a, 0)

