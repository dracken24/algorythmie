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

from tp_1.datastructure import datastructure 
from tp_1.tests_unitaires import test_with_capacity, generer_all_graphiques

# ------------------------------------------------------------------- #

def main() -> None:

    data = datastructure(int)

    test_with_capacity(data, 1000)
    test_with_capacity(data, 10000)
    test_with_capacity(data, 15000)
    test_with_capacity(data, 20000)
    test_with_capacity(data, 25000)
    test_with_capacity(data, 30000)

    generer_all_graphiques()

# ------------------------------------------------------------------- #

if __name__ == "__main__":
    main()
