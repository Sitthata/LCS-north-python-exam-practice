def main():
    print_triangle(5)


def print_matrix(n: int) -> None:
    counter = 1
    for i in range(n):
        for j in range(n):
            if j >= i:
                print(counter, end="\t")
                counter += 1
            else:
                print(0, end="\t")
        print()


def print_triangle(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print(j, end="\t")
        print()

if __name__ == "__main__":
    main()
