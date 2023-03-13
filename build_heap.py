# python3


def build_heap(data):
    swaps = []
  

    for i in range(len(data) // 2 -1, -1, -1);
        heapify(data, i, len(data), swaps)


    return swaps


def heapify(data, i, n, swaps):
    left_child = 2*i+1
    right_child = 2*i+2
    smallest = i

    if left_child < n and data[left_child] < data[smallest]:
        smallest = left_child

    if right_child < n and data[right_child] < data[smallest]:
        smallest = right_child

    if smallest != i:

        data[i], data[smallest] = data[smallest], data[i]

        swaps.append((i, smallest))

        heapify(data, smallest, n, swaps)


def main():
    
   input_method = input("Enter input method (I for keyboard input, F for file input): ")

   if input_method == "I":
        n = int(input("Enter number of elements: "))
        data = list(map(int, input("Enter the elements: ").split()))
    
    elif input_method == "F":
        filename = input("enter the filename:")
        with open(filename, "r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))

    else:
        print("Invalid input method")
        return


    assert len(data) == n

   
    swaps = build_heap(data)

 

    # output all swaps
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])


if __name__ == "__main__":
    main()
