def tower(index, fromPole, toPole, withPole):
    if index >= 1:
        tower(index-1, fromPole, withPole, toPole)
        moveTo(fromPole, toPole)
        tower(index-1, withPole, toPole, fromPole)


def moveTo(fromPole, toPole):
    print(f"Move {fromPole} to {toPole}")


tower(3, "A", "B", "C")
