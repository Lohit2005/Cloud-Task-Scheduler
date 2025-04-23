from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Task:
    """Represents a cloud task with basic properties."""
    id: int
    length: int
    filesize: int
    outputsize: int
    cpu_req: int
    ram_req: int
    bw_req: int

@dataclass
class VM:
    """Represents a virtual machine."""
    id: int
    cpu_cap: int
    ram_cap: int
    bw_cap: int
    storage: int
    cost: float

class Individual:
    """Represents an individual scheduling solution."""
    def __init__(self, schedule: List[int]):
        self.schedule = schedule  # list of VM indices for each task
        self.objs: Optional[tuple] = None  # (makespan, total_cost, load_balance)
        self.rank: Optional[int] = None
        self.crowding_distance: float = 0.0

    def copy(self):
        new_ind = Individual(self.schedule.copy())
        new_ind.objs = self.objs
        new_ind.rank = self.rank
        new_ind.crowding_distance = self.crowding_distance
        return new_ind
