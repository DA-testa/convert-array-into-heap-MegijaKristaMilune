# python3

def build_heap(data):
    swaps = []
    n = len(data)
  

    for i in range(n // 2 -1, -1, -1):
        heap(data, i, n, swaps)
    return swaps
                

def heap(data, i, n, swaps):
    left_child = 2*i+1
    right_child = 2*i+2
    smallest = i

    if left_child < n and data[left_child] < data[i]:
        smallest = left_child

    if right_child < n and data[right_child] < data[smallest]:
        smallest = right_child

    if smallest != i:

        data[i], data[smallest] = data[smallest], data[i]

        swaps.append((i, smallest))

        heap(data, smallest, n, swaps)


def main():

    input_method = (input("enter input method I/F: "))

    if "I" in input_method:
        n = int(input("enter number of elements: "))
        data = list(map(int, input("enter the elements: ").split()))

    if "F" in input_method:
        filename = input("enter the filename:")
        
        with open(f"tests/{filename}") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))


    
    assert len(data) == n

   
    swaps = build_heap(data)
    
    print(len(swaps))
    for i, j  in swaps:


        print(i, j)



if __name__ == "__main__":
    main()
