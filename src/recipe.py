import time
from datetime import timedelta
from typing import List


class Ingredient:
    def __init__(self, name: str, quantity: int | float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit


class Step:
    def __init__(self, instruction: str, estimated_time: timedelta, utensil: str, is_hands_off: bool):
        self.instruction = instruction
        self.estimated_time = estimated_time
        self.utensil = utensil
        self.is_hands_off = is_hands_off

    def __str__(self):
        return "{" + self.instruction + "}"


class Recipe:
    def __init__(self, dish_name: str):
        self.dish_name = dish_name
        self.ingredients = []
        self.steps: List[Step] = []
        self.prep_time = timedelta(minutes=0)
        self.dependency = {}

    def update_prep_time(self, delta: timedelta):
        self.prep_time += delta

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def add_step(self, step: Step):
        if step in self.dependency:
            print(f"AddStep: failed to add step {step}: an identical step already exists")
            return
        self.steps.append(step)
        self.dependency[step] = []
        self.update_prep_time(step.estimated_time)

    def add_dependency_by_step(self, child: Step, parent: Step):
        if parent not in self.steps:
            print("parent step doesn't exist")
            return
        if child not in self.steps:
            print("child step doesn't exist")
            return
        if parent not in self.dependency[child]:
            self.dependency[child].append(parent)

    def add_dependency_by_index(self, child_idx: int, parent_idx: int):
        if child_idx < 1 or child_idx > len(self.steps):
            print("AddDependencyByIndex: invalid step index for childIdx")
            return
        if parent_idx < 1 or parent_idx > len(self.steps):
            print("AddDependencyByIndex: invalid step index for parentIdx")
            return

        # offset to match the array indices
        child_idx -= 1
        parent_idx -= 1

        child_list = self.dependency[self.steps[child_idx]]
        if self.steps[parent_idx] not in child_list:
            child_list.append(self.steps[parent_idx])
            self.dependency[self.steps[child_idx]] = child_list

    def print_recipe(self):
        print(f"Recipe for {self.dish_name}")
        print("Ingredients:")
        for i, ingredient in enumerate(self.ingredients):
            print(f"{i}: {ingredient.name}, {ingredient.quantity} {ingredient.unit}")
        print("Steps:")
        for i, step in enumerate(self.steps):
            print(
                f"{i}: {step.instruction} ({step.estimated_time}), utensil: {step.utensil}, hands-off: {step.is_hands_off}")
        print(f"Total prep time: {self.prep_time}")

    def shortest_distance_to_handsoff(self, idx: int):
        t = timedelta(minutes=0)
        for i in range(idx, len(self.steps)):
            if self.steps[i].is_hands_off:
                return t
            else:
                t += self.steps[i].estimated_time
        return t

