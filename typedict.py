from typing import TypedDict

class Pearson(TypedDict):
    name: str
    age: int

new_pearson: Pearson = {'name':'nitish', 'age':'35'}

print(new_pearson)