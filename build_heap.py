# python3

def build_heap(data):
    swaps = []
    n = len(data)
  

    # for i in range(n // 2 -1, -1, -1):
    #     heapify(data, i, n, swaps)


    # return swaps


    for i in range(n // 2 -1, -1, -1):
        j = 1

        while True:
            left_child = 2*j+1
            right_child = 2*j+2
            smallest = j
            
            if left_child < n and data[left_child] < data[smallest]:
                smallest = left_child
            if right_child < n and data[right_child] < data[smallest]:
                smallest = right_child


            if j != smallest:
                swaps.append((j, smallest))
                data[j], data[smallest] = data[smallest], data[j]
                j = smallest

            else:
                break

    return swaps

                

# def heapify(data, i, n, swaps):
#     left_child = 2*i+1
#     right_child = 2*i+2
#     smallest = i

#     if left_child < n and data[left_child] < data[smallest]:
#         smallest = left_child

#     if right_child < n and data[right_child] < data[smallest]:
#         smallest = right_child

#     if smallest != i:

#         data[i], data[smallest] = data[smallest], data[i]

#         swaps.append((i, smallest))

#         heapify(data, smallest, n, swaps)


def main():

    input_method = (input("Enter input method (I for keyboard input, F for file input): "))

    if "I" in input_method:
        n = int(input("enter number of elements: "))
        data = list(map(int, input("enter the elements: ").split()))
    if "F" in input_method:
        filename = input("enter the filename:")
        with open(f"tests/{filename}") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))

    else:
        print("Invalid input method")
        return
    
    assert len(data) == n

   
    swaps = build_heap(data)
    
    print(len(swaps))
    for i, j  in swaps:
        if i > j:
            i, j = j, i

        print(i, j)



if __name__ == "__main__":
    main()
