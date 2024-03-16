class GeneratorIterator:
    def __iter__(self):
        return self

    def __next__(self):
        return (x for x in range(5))

iterator = GeneratorIterator()

for gen in iterator:
    for value in gen:
        print(value)

