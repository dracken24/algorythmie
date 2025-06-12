'''
===============================================================================    */
---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---    */
              -------------------------------------------------                    */
               PROJET: <TP1>          PAR: Dracken24                               */
              -------------------------------------------------                    */
               CREATED: 12-6th-2025                                                */
               MODIFIED BY: Dracken24                                              */
               LAST MODIFIED: 12-6th-2025                                          */
              -------------------------------------------------                    */
               FILE: __init__.py                                                   */
              -------------------------------------------------                    */
---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---    */
===============================================================================    */
'''

from tp_1.benchmark import benchmark
from tp_1.datastructure import datastructure 

def main() -> None:
    # print("Hello from tp-1!")
    data = datastructure(int)

    test_with_1000(data)
    test_with_10000(data)
    test_with_100000(data)

# ------------------------------------------------------------------- #
# -----------------------------TESTS--------------------------------- #
# ------------------------------------------------------------------- #

# --------------------------1000 Elements---------------------------- #

def test_with_1000(data: datastructure) -> None:
    static_array = benchmark(data.static_array)
    dynamic_array = benchmark(data.dynamic_array)
    singly_linked_list = benchmark(data.singly_linked_list)
    doubly_linked_list = benchmark(data.doubly_linked_list)

    insert_1000 = [i for i in range(1000)]


    print("******************** TEST WITH 1000 ELEMENTS *******************")

    print("\n----------------------------------------------------------------")
    print("-----------------------Get 1000---------------------------------")
    print("----------------------------------------------------------------")
    # test get
    print("static array       get 1000: " + str(static_array.test_get(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      get 1000: " + str(dynamic_array.test_get(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list get 1000: " + str(singly_linked_list.test_get(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list get 1000: " + str(doubly_linked_list.test_get(insert_1000)))

    print("\n----------------------------------------------------------------")
    print("-----------------------Insert head 1000-------------------------")
    print("----------------------------------------------------------------")
    # test insert head
    print("static array       insert head 1000: " + str(static_array.test_insert_head(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      insert head 1000: " + str(dynamic_array.test_insert_head(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list insert head 1000: " + str(singly_linked_list.test_insert_head(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list insert head 1000: " + str(doubly_linked_list.test_insert_head(insert_1000)))

    print("\n----------------------------------------------------------------")
    print("-----------------------Insert mid 1000--------------------------")
    print("----------------------------------------------------------------")
    # test insert mid
    print("static array       insert mid 1000: " + str(static_array.test_insert_mid(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      insert mid 1000: " + str(dynamic_array.test_insert_mid(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list insert mid 1000: " + str(singly_linked_list.test_insert_mid(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list insert mid 1000: " + str(doubly_linked_list.test_insert_mid(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")

    print("\n----------------------------------------------------------------")
    print("-----------------------Insert tail 1000-------------------------")
    print("----------------------------------------------------------------")
    # test insert tail
    print("static array       insert tail 1000: " + str(static_array.test_insert_tail(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      insert tail 1000: " + str(dynamic_array.test_insert_tail(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list insert tail 1000: " + str(singly_linked_list.test_insert_tail(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list insert tail 1000: " + str(doubly_linked_list.test_insert_tail(insert_1000)))

    print("\n----------------------------------------------------------------")
    print("-----------------------Delete head 1000-------------------------")
    print("----------------------------------------------------------------")
    # test delete head
    print("static array       delete head 1000: " + str(static_array.test_delete_head(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      delete head 1000: " + str(dynamic_array.test_delete_head(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list delete head 1000: " + str(singly_linked_list.test_delete_head(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list delete head 1000: " + str(doubly_linked_list.test_delete_head(insert_1000)))

    print("\n----------------------------------------------------------------")
    print("-----------------------Delete mid 1000--------------------------")
    print("----------------------------------------------------------------")
    # test delete mid
    print("static array       delete mid 1000: " + str(static_array.test_delete_mid(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      delete mid 1000: " + str(dynamic_array.test_delete_mid(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list delete mid 1000: " + str(singly_linked_list.test_delete_mid(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list delete mid 1000: " + str(doubly_linked_list.test_delete_mid(insert_1000)))

    print("\n----------------------------------------------------------------")
    print("-----------------------Delete tail 1000-------------------------")
    print("----------------------------------------------------------------")
    # test delete tail
    print("static array       delete tail 1000: " + str(static_array.test_delete_tail(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      delete tail 1000: " + str(dynamic_array.test_delete_tail(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list delete tail 1000: " + str(singly_linked_list.test_delete_tail(insert_1000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list delete tail 1000: " + str(doubly_linked_list.test_delete_tail(insert_1000)))

# --------------------------10000 Elements---------------------------- #

def test_with_10000(data: datastructure) -> None:
    static_array = benchmark(data.static_array)
    dynamic_array = benchmark(data.dynamic_array)
    singly_linked_list = benchmark(data.singly_linked_list)
    doubly_linked_list = benchmark(data.doubly_linked_list)

    insert_10000 = [i for i in range(10000)]

    print("\n******************** TEST WITH 10000 ELEMENTS *******************")
    
    print("\n----------------------------------------------------------------")
    print("-----------------------Get 10000--------------------------------")
    print("----------------------------------------------------------------")
    # test get
    print("static array       get 10000: " + str(static_array.test_get(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      get 10000: " + str(dynamic_array.test_get(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list get 10000: " + str(singly_linked_list.test_get(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list get 10000: " + str(doubly_linked_list.test_get(insert_10000)))

    print("\n----------------------------------------------------------------")
    print("-----------------------Insert head 10000------------------------")
    print("----------------------------------------------------------------")
    # test insert head
    print("static array       insert head 10000: " + str(static_array.test_insert_head(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      insert head 10000: " + str(dynamic_array.test_insert_head(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list insert head 10000: " + str(singly_linked_list.test_insert_head(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list insert head 10000: " + str(doubly_linked_list.test_insert_head(insert_10000)))

    print("\n----------------------------------------------------------------")
    print("-----------------------Insert mid 10000-------------------------")
    print("----------------------------------------------------------------")
    # test insert mid
    print("static array       insert mid 10000: " + str(static_array.test_insert_mid(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      insert mid 10000: " + str(dynamic_array.test_insert_mid(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list insert mid 10000: " + str(singly_linked_list.test_insert_mid(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list insert mid 10000: " + str(doubly_linked_list.test_insert_mid(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")

    print("\n----------------------------------------------------------------")
    print("-----------------------Insert tail 10000------------------------")
    print("----------------------------------------------------------------")
    # test insert tail
    print("static array       insert tail 10000: " + str(static_array.test_insert_tail(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      insert tail 10000: " + str(dynamic_array.test_insert_tail(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list insert tail 10000: " + str(singly_linked_list.test_insert_tail(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list insert tail 10000: " + str(doubly_linked_list.test_insert_tail(insert_10000)))

    print("\n----------------------------------------------------------------")
    print("-----------------------Delete head 10000------------------------")
    print("----------------------------------------------------------------")
    # test delete head
    print("static array       delete head 10000: " + str(static_array.test_delete_head(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      delete head 10000: " + str(dynamic_array.test_delete_head(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list delete head 10000: " + str(singly_linked_list.test_delete_head(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list delete head 10000: " + str(doubly_linked_list.test_delete_head(insert_10000)))

    print("\n----------------------------------------------------------------")
    print("-----------------------Delete mid 10000-------------------------")
    print("----------------------------------------------------------------")
    # test delete mid
    print("static array       delete mid 10000: " + str(static_array.test_delete_mid(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      delete mid 10000: " + str(dynamic_array.test_delete_mid(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list delete mid 10000: " + str(singly_linked_list.test_delete_mid(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list delete mid 10000: " + str(doubly_linked_list.test_delete_mid(insert_10000)))

    print("\n----------------------------------------------------------------")
    print("-----------------------Delete tail 10000------------------------")
    print("----------------------------------------------------------------")
    # test delete tail
    print("static array       delete tail 10000: " + str(static_array.test_delete_tail(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      delete tail 10000: " + str(dynamic_array.test_delete_tail(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list delete tail 10000: " + str(singly_linked_list.test_delete_tail(insert_10000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list delete tail 10000: " + str(doubly_linked_list.test_delete_tail(insert_10000)))

# -------------------------100000 Elements---------------------------- #

def test_with_100000(data: datastructure) -> None:
    static_array = benchmark(data.static_array)
    dynamic_array = benchmark(data.dynamic_array)
    singly_linked_list = benchmark(data.singly_linked_list)
    doubly_linked_list = benchmark(data.doubly_linked_list)

    insert_100000 = [i for i in range(100000)]

    print("\n******************** TEST WITH 100000 ELEMENTS *******************")
    
    print("\n----------------------------------------------------------------")
    print("-----------------------Get 100000-------------------------------")
    print("----------------------------------------------------------------")
    # test get
    print("static array       get 100000: " + str(static_array.test_get(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      get 100000: " + str(dynamic_array.test_get(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list get 100000: " + str(singly_linked_list.test_get(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list get 100000: " + str(doubly_linked_list.test_get(insert_100000)))

    print("\n----------------------------------------------------------------")
    print("----------------------Insert head 100000------------------------")
    print("----------------------------------------------------------------")
    # test insert head
    print("static array       insert head 100000: " + str(static_array.test_insert_head(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      insert head 100000: " + str(dynamic_array.test_insert_head(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list insert head 100000: " + str(singly_linked_list.test_insert_head(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list insert head 100000: " + str(doubly_linked_list.test_insert_head(insert_100000)))

    print("\n----------------------------------------------------------------")
    print("----------------------Insert mid 100000-------------------------")
    print("----------------------------------------------------------------")
    # test insert mid
    print("static array       insert mid 100000: " + str(static_array.test_insert_mid(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      insert mid 100000: " + str(dynamic_array.test_insert_mid(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list insert mid 100000: " + str(singly_linked_list.test_insert_mid(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list insert mid 100000: " + str(doubly_linked_list.test_insert_mid(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")

    print("\n----------------------------------------------------------------")
    print("----------------------Insert tail 100000------------------------")
    print("----------------------------------------------------------------")
    # test insert tail
    print("static array       insert tail 100000: " + str(static_array.test_insert_tail(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      insert tail 100000: " + str(dynamic_array.test_insert_tail(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list insert tail 100000: " + str(singly_linked_list.test_insert_tail(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list insert tail 100000: " + str(doubly_linked_list.test_insert_tail(insert_100000)))

    print("\n----------------------------------------------------------------")
    print("----------------------Delete head 100000------------------------")
    print("----------------------------------------------------------------")
    # test delete head
    print("static array       delete head 100000: " + str(static_array.test_delete_head(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      delete head 100000: " + str(dynamic_array.test_delete_head(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list delete head 100000: " + str(singly_linked_list.test_delete_head(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list delete head 100000: " + str(doubly_linked_list.test_delete_head(insert_100000)))

    print("\n----------------------------------------------------------------")
    print("----------------------Delete mid 100000-------------------------")
    print("----------------------------------------------------------------")
    # test delete mid
    print("static array       delete mid 100000: " + str(static_array.test_delete_mid(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      delete mid 100000: " + str(dynamic_array.test_delete_mid(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list delete mid 100000: " + str(singly_linked_list.test_delete_mid(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list delete mid 100000: " + str(doubly_linked_list.test_delete_mid(insert_100000)))

    print("\n----------------------------------------------------------------")
    print("-----------------------Delete tail 10000------------------------")
    print("----------------------------------------------------------------")
    # test delete tail
    print("static array       delete tail 100000: " + str(static_array.test_delete_tail(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("dynamic array      delete tail 100000: " + str(dynamic_array.test_delete_tail(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("singly linked list delete tail 100000: " + str(singly_linked_list.test_delete_tail(insert_100000)))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("doubly linked list delete tail 100000: " + str(doubly_linked_list.test_delete_tail(insert_100000)))

if __name__ == "__main__":
    main()
