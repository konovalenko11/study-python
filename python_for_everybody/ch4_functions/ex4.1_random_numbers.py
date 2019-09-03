import random

t = []

for i in range(10):
    t.append(i)
    print("Iteration [{}]: RandRange - [{:.2f}]".format(i, random.randrange(1, 10)))
    print("Iteration [{}]: Randint   - [{:.2f}]".format(i, random.randint(1, 10)))
    print("Iteration [{}]: Choice    - [{:.2f}]".format(i, random.choice(t)))

    print("Iteration [{}]: t - [{}]".format(i, t))
    print("----------")

