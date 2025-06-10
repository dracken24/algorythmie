'''
===============================================================================    */
---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---~---    */
              -------------------------------------------------                    */
               PROJET: <React Learning2>          PAR: Dracken24                   */
              -------------------------------------------------                    */
               CREATED: 10-6th-2025                                                */
               MODIFIED BY: Dracken24                                              */
               LAST MODIFIED: 10-6th-2025                                          */
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

        start_time = time.time()
        for v in value:
            self.container_to_test.get(v)
        end_time = time.time()

        return end_time - start_time

# ........................................................................ #

    def test_insert_head(self, value: list[any]) -> float:

        start_time = time.time()
        for v in value:
            self.container_to_test.insert_head(v)
        end_time = time.time()

        return end_time - start_time

# ........................................................................ #

    def test_insert_mid(self, value: list[any]) -> float:

        start_time = time.time()
        for v in value:
            self.container_to_test.insert_mid(v)
        end_time = time.time()

        return end_time - start_time

# ........................................................................ #

    def test_insert_tail(self, value: list[any]) -> float:

        start_time = time.time()
        for v in value:
            self.container_to_test.insert_tail(v)
        end_time = time.time()

        return end_time - start_time

# ........................................................................ #

    def test_delete_head(self, value: list[any]) -> float:

        self.test_insert_tail(value)

        start_time = time.time()
        for v in value:
            self.container_to_test.delete_head(v)
        end_time = time.time()

        return end_time - start_time
    
# ........................................................................ #

    def test_delet_mid(self, value: list[any]) -> float:

        self.test_insert_tail(value)

        start_time = time.time()
        for v in value:
            self.container_to_test.delete_mid(v)
        end_time = time.time()

        return end_time - start_time

# ........................................................................ #

    def test_delet_tail(self, value: list[any]) -> float:

        self.test_insert_tail(value)

        start_time = time.time()
        for v in value:
            self.container_to_test.delete_tail(v)
        end_time = time.time()

        return end_time - start_time

# ........................................................................ #
