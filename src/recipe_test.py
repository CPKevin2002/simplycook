import unittest
import recipe as rp
import scheduler as sch
from datetime import timedelta


def test_recipe1() -> rp.Recipe:
    r = rp.Recipe(dish_name="test dish 1")
    r.add_step(rp.Step("HandsOn1", timedelta(minutes=10), "pot", False))
    r.add_step(rp.Step("HandsOn2", timedelta(minutes=10), "pot", False))
    r.add_step(rp.Step("HandsOn3", timedelta(minutes=10), "pot", False))
    r.default_dependency()
    return r


def test_recipe2() -> rp.Recipe:
    r = rp.Recipe(dish_name="test dish 2")
    r.add_step(rp.Step("HandsOn1", timedelta(minutes=3), "pot", False))
    r.add_step(rp.Step("HandsOn2", timedelta(minutes=5), "pot", False))
    r.add_step(rp.Step("HandsOn3", timedelta(minutes=7), "pot", False))
    r.default_dependency()
    return r


def test_recipe3() -> rp.Recipe:
    r = rp.Recipe(dish_name="test dish 3")
    r.add_step(rp.Step("HandsOn1", timedelta(minutes=3), "pot", True))
    r.add_step(rp.Step("HandsOn2", timedelta(minutes=5), "pot", False))
    r.add_step(rp.Step("HandsOn3", timedelta(minutes=7), "pot", True))
    r.default_dependency()
    return r


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

    def test_rank_recipe_by_distance(self):
        r1 = test_recipe1()
        t = r1.shortest_distance_to_handsoff(0)
        self.assertEqual(t, timedelta(minutes=30), "Incorrect ranking of recipes by distance")
        r2 = test_recipe3()
        t = r2.shortest_distance_to_handsoff(0)
        self.assertEqual(t, timedelta(minutes=0), "Incorrect ranking of recipes by distance")
        t = r2.shortest_distance_to_handsoff(1)
        self.assertEqual(t, timedelta(minutes=5), "Incorrect ranking of recipes by distance")

    def test_best_order1(self):
        r1, r2 = test_recipe1(), test_recipe2()
        s = sch.Scheduler(dishes=[r1, r2], utensils={}, num_cooks=1)
        res = s.best_order()
        for src, step in res:
            print(f"from dish: {src}: {step.instruction}")

    def test_best_order2(self):
        r1, r2 = test_recipe2(), test_recipe3()
        s = sch.Scheduler(dishes=[r1, r2], utensils={}, num_cooks=1)
        res = s.best_order()
        for src, step in res:
            print(f"from dish: {src}: {step.instruction}")



if __name__ == '__main__':
    unittest.main()
