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
               FILE: benchmark.py                                                  */
              -------------------------------------------------                    */
---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---    */
===============================================================================    */
'''

import time
class benchmark:

    def __init__(self, container_to_test):
        self.container_to_test = container_to_test

# ........................................................................ #

    def test_get(self, value: list[any]) -> float:

        self.fill_array(value)

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage in : " + str(memory_usage))

        start_time = time.time()
        for v in value:
            self.container_to_test.get(v)
        end_time = time.time()

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage out: " + str(memory_usage))

        return end_time - start_time

# ........................................................................ #

    def test_insert_head(self, value: list[any]) -> float:

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage in : " + str(memory_usage))

        start_time = time.time()
        for v in value:
            self.container_to_test.insert_head(v)
        end_time = time.time()

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage out: " + str(memory_usage))

        return end_time - start_time

# ........................................................................ #

    def test_insert_mid(self, value: list[any]) -> float:

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage in : " + str(memory_usage))

        start_time = time.time()
        for v in value:
            self.container_to_test.insert_mid(v, v)
        end_time = time.time()

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage out: " + str(memory_usage))

        return end_time - start_time

# ........................................................................ #

    def test_insert_tail(self, value: list[any]) -> float:

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage in : " + str(memory_usage))

        start_time = time.time()
        for v in value:
            self.container_to_test.insert_tail(v)
        end_time = time.time()

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage out: " + str(memory_usage))

        return end_time - start_time

# ........................................................................ #

    def test_delete_head(self, value: list[any]) -> float:

        self.fill_array(value)

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage in : " + str(memory_usage))

        start_time = time.time()
        for v in value:
            self.container_to_test.delete_head()
        end_time = time.time()

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage out: " + str(memory_usage))

        return end_time - start_time
    
# ........................................................................ #

    def test_delete_mid(self, value: list[any]) -> float:

        self.fill_array(value)

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage in : " + str(memory_usage))

        start_time = time.time()
        for v in value:
            self.container_to_test.delete_mid((int)(len(value) / 2))
        end_time = time.time()

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage out: " + str(memory_usage))

        return end_time - start_time

# ........................................................................ #

    def test_delete_tail(self, value: list[any]) -> float:

        self.fill_array(value)

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage in : " + str(memory_usage))

        start_time = time.time()
        for v in value:
            self.container_to_test.delete_tail()
        end_time = time.time()

        memory_usage = self.container_to_test.memory_usage()
        print("memory usage out: " + str(memory_usage))

        return end_time - start_time

# ........................................................................ #

    def fill_array(self, value: list[any]) -> float:
        for v in value:
            self.container_to_test.insert_tail(v)
