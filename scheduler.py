from typing import List, Dict

import recipe as rp


"""
There are 3 states in the scheduler:
1. HOFF: one or more "handsoff" tasks are ongoing, looking for hands-on tasks to fill in the gap
2. HON: looking to proceed until a handsoff is found
3. WAIT: no more tasks to do
"""

class Scheduler:

    def __init__(self, dishes: List[rp.Recipe], utensils: Dict[str, int], num_cooks: int):
        self.dishes = dishes
        self.indices = [0] * len(dishes)
        self.utensils = utensils
        self.num_cooks = num_cooks
        self.total_time = 0

    def best_order(self) -> List[rp.Step]:
        steps = []

        # find the shortest path to handsoff step
        min_time, min_idx = float('inf'), -1
        for i, dish in enumerate(self.dishes):
            time_to_handsoff = dish.shortest_distance_to_handsoff(self.indices[i])
            if time_to_handsoff < min_time:
                min_idx = i
                min_time = time_to_handsoff

        # if there exists a handoff step
        if min_idx != -1:
            dish_steps = self.dishes[min_idx].steps
            while not dish_steps[min_idx].is_hands_off:
                steps.append(dish_steps[min_idx])
                min_idx += 1

        return steps




