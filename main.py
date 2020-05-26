import random


class Element:
    name = None
    data = None
    expected = None

    def __init__(self, name, data, expected):
        self.data = data
        self.expected = expected
        self.name = name

    def __repr__(self):
        return f'XXX [name={self.name}, data={self.data}, expected={self.expected}]'


class Perceptron:
    _w = None
    _train_limit = None
    _train_times = None

    def __init__(self, train_limit):
        self._train_limit = train_limit
        self._train_times = 0

    def __repr__(self):
        return f'Perceptron [w={self._w}, train_times={self._train_times}]'

    @staticmethod
    def _activate(x):
        return 1 if x > 0 else 0

    def _process_player(self, player):
        sum_ = 0
        for i in range(len(player.data)):
            sum_ += player.data[i] * self._w[i]
        return self._activate(sum_)

    def train(self, mass):
        # TODO Validate if mass input has the same "in_" size
        data_size = len(mass[0].data)

        self._w = [random.randint(0, 1) for _ in range(data_size)]
        self._train_times = 0

        while True:
            self._train_times += 1
            error = False
            for player in mass:
                value = self._process_player(player)
                if value != player.expected:
                    error = True

                    if value == 0:
                        for i in range(data_size):
                            self._w[i] = player.data[i]

                    elif value == 1:
                        for i in range(data_size):
                            self._w[i] -= player.data[i]
                            self._w[i] = abs(self._w[i])

            if not error or self._train_times == self._train_limit:
                return error, self._train_times

    def test(self, player):
        return self._process_player(player)


def main():
    neymar = Element(
        name='Neymar',
        data=[1, 0, 0],
        expected=0
    )
    messi = Element(
        name='Messi',
        data=[1, 0, 1],
        expected=0
    )
    barichello = Element(
        name='Barrichello',
        data=[1, 1, 0],
        expected=1
    )
    massa = Element(
        name='Massa',
        data=[1, 1, 1],
        expected=1
    )

    train_mass = [neymar, messi, barichello, massa]

    perceptron = Perceptron(train_limit=1000)
    perceptron.train(train_mass)

    for player in train_mass:
        value = perceptron.test(player)
        print(f'Player {player.name} has {value} class value')


if __name__ == '__main__':
    main()
