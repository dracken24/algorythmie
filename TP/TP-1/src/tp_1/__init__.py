from tp_1.benchmark import benchmark
from tp_1.datastructure import datastructure 

def main() -> None:
    # print("Hello from tp-1!")
    data = datastructure(int)
    container_01 = benchmark(data.static_array)
    container_02 = benchmark(data.dynamic_array)
    container_03 = benchmark(data.singly_linked_list)
    container_04 = benchmark(data.doubly_linked_list)

    # test get
    insert_1000 = [i for i in range(1000)]
    # insert_10000 = [i for i in range(10000)]
    # insert_100000 = [i for i in range(100000)]
    # insert_1000000 = [i for i in range(1000000)]
    # insert_10000000 = [i for i in range(10000000)]
    # insert_100000000 = [i for i in range(100000000)]
    # insert_1000000000 = [i for i in range(1000000000)]

    # test insert head
    print("static array insert head      : " + str(container_01.test_insert_head(insert_1000)))
    print("dynamic array insert head     : " + str(container_02.test_insert_head(insert_1000)))
    print("singly linked list insert head: " + str(container_03.test_insert_head(insert_1000)))
    print("doubly linked list insert head: " + str(container_04.test_insert_head(insert_1000)))

    # test insert mid
    print("static array insert mid      : " + str(container_01.test_insert_mid(insert_1000)))
    print("dynamic array insert mid     : " + str(container_02.test_insert_mid(insert_1000)))
    print("singly linked list insert mid: " + str(container_03.test_insert_mid(insert_1000)))
    print("doubly linked list insert mid: " + str(container_04.test_insert_mid(insert_1000)))

# if __name__ == "__main__":
main()
