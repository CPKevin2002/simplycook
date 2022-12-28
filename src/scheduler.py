from typing import List, Dict
from datetime import timedelta
import recipe as rp

class Scheduler:
    def __init__(self, dishes: List[rp.Recipe], utensils: Dict[str, int], num_cooks: int):
        self.dishes = dishes
        self.pointers = {}
        for d in self.dishes:
            self.pointers[d] = 0

        self.utensils = utensils
        self.num_cooks = num_cooks
        self.total_time = timedelta(minutes=0)
        self.hands_off_steps: Dict[rp.Step, timedelta] = {}  # (step, ending_time)

    def _rank_dish_by_handsoff_distance(self) -> List[(rp.Recipe, timedelta)]:
        res = []
        for d in self.dishes:
            res.append((d, d.shortest_distance_to_handsoff(self.pointers[d])))
        res.sort(key=lambda x: x[1])
        return res

    def best_order(self) -> List[(str, rp.Step)]:
        steps = []
        total_steps = sum(len(recipe.steps) for recipe in self.dishes)
        while len(steps) != total_steps or self.hands_off_steps:
            # delete hands off steps that are finished
            for s, t in list(self.hands_off_steps.items()):
                if self.total_time >= t:
                    del self.hands_off_steps[s]

            # rank dishes according to distance to handsoff step
            best_steps = self._rank_dish_by_handsoff_distance()
            scheduled = False
            for d, _ in best_steps:
                if self.pointers[d] < len(d.steps):
                    s: rp.Step = d.steps[self.pointers[d]]
                    steps.append((d.dish_name, s))
                    if s.is_hands_off:
                        self.hands_off_steps[s] = self.total_time + s.estimated_time
                    else:
                        self.total_time += s.estimated_time
                    scheduled = True
                    break

            # if nothing can be done at the moment, advance to the next event
            if not scheduled:
                self.total_time = min(self.hands_off_steps.values())

        return steps




