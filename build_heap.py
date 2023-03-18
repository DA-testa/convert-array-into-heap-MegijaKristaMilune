# python3

def build_heap(data):
    swaps = []
    n = len(data)
  
    for i in range(n // 2 -1, -1, -1):
        heap(data, i, n, swaps)
    return swaps

 def heap(data, i, n, swaps):
    pos_left = 2*i+1
    pos_right = 2*i+2
    last = i

    if pos_left < n and data[pos_left] < data[i]:
        last = pos_left

    if pos_right < n and data[pos_right] < data[last]:
        last = pos_right

    if last != i:

        data[i], data[last] = data[last], data[i]

        swaps.append((i, last))

        heap(data, last, n, swaps)


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
