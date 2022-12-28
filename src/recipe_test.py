import unittest
import recipe as rp
import scheduler as sch
from datetime import timedelta


class MyTestCase(unittest.TestCase):
    def test_basic_recipe(self):
        r = rp.Recipe("test dish")
        r.add_ingredient(rp.Ingredient("tomato", 2, ""))
        r.add_ingredient(rp.Ingredient("flour", 400, "grams"))
        r.add_step(rp.Step(instruction="Cook tomato",
                           estimated_time=timedelta(minutes=3), is_hands_off=False, utensil="pot"))

        r.add_step(rp.Step(instruction="Cook flour",
                           estimated_time=timedelta(minutes=5), is_hands_off=False, utensil="pot"))

        r.print_recipe()

    def test_best_order(self):
        r1 = rp.Recipe("test dish")
        r1.add_ingredient(rp.Ingredient("tomato", 2, ""))
        r1.add_ingredient(rp.Ingredient("flour", 400, "grams"))
        r1.add_step(rp.Step(instruction="Cook tomato",
                           estimated_time=timedelta(minutes=3), is_hands_off=False, utensil="pot"))

        r1.add_step(rp.Step(instruction="Cook flour",
                           estimated_time=timedelta(minutes=5), is_hands_off=False, utensil="pot"))
        r1.add_dependency_by_index(2, 1)

        r2 = rp.Recipe("test dish")
        r2.add_ingredient(rp.Ingredient("tomato", 2, ""))
        r2.add_ingredient(rp.Ingredient("flour", 400, "grams"))
        r2.add_step(rp.Step(instruction="Cook tomato2",
                            estimated_time=timedelta(minutes=3), is_hands_off=False, utensil="pot"))

        r2.add_step(rp.Step(instruction="Cook flour2",
                            estimated_time=timedelta(minutes=5), is_hands_off=False, utensil="pot"))

        s = sch.Scheduler(dishes=[r1, r2], utensils={}, num_cooks=1)
        res = s.best_order()
        for r in res:
            print(r.instruction)



if __name__ == '__main__':
    unittest.main()
