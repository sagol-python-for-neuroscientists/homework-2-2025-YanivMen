from enum import Enum
from collections import namedtuple
from itertools import islice

# — your existing definitions —
Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent     = namedtuple("Agent", ("name", "category"))

# — helper functions for stepping categories up or down —
def improve(cat: Condition) -> Condition:
    """Move one step toward HEALTHY (lower enum value), but not below CURE."""
    if cat.value > Condition.CURE.value:
        return Condition(cat.value - 1)
    return cat

def worsen(cat: Condition) -> Condition:
    """Move one step toward DEAD (higher enum value), but not above DEAD."""
    if cat.value < Condition.DEAD.value:
        return Condition(cat.value + 1)
    return cat

def meet_pair(a_cat: Condition, b_cat: Condition):
    """
    Apply the meeting rules to two categories and return their new categories.
    """
    # Case 1: cure involved
    if a_cat == Condition.CURE and b_cat != Condition.CURE:
        # cure makes the other feel better; cure is unaffected
        return a_cat, improve(b_cat)
    if b_cat == Condition.CURE and a_cat != Condition.CURE:
        return improve(a_cat), b_cat
    if a_cat == Condition.CURE and b_cat == Condition.CURE:
        # two cures meet → nothing happens
        return a_cat, b_cat

    # Case 2: no cure → both worsen one step
    return worsen(a_cat), worsen(b_cat)

def meetup(agents):
    """
    Take a list of Agent, have them meet in sequential pairs,
    and return a new list of Agent with updated categories.
    
    * Healthy and Dead agents do not meet (they simply carry over unchanged).
    * All other agents (Cure, Sick, Dying) are paired off in order.
    * If there's an odd one out, they also carry over unchanged.
    """
    # split out those who never meet
    no_meet = [ag for ag in agents if ag.category in (Condition.HEALTHY, Condition.DEAD)]
    to_meet = [ag for ag in agents if ag.category not in (Condition.HEALTHY, Condition.DEAD)]
    
    # pair them off
    updated = []
    it = iter(to_meet)
    for a in it:
        try:
            b = next(it)
        except StopIteration:
            # odd-one-out: carries over unchanged
            updated.append(a)
            break
        
        # apply meeting rules
        new_a, new_b = meet_pair(a.category, b.category)
        updated.extend([
            Agent(a.name, new_a),
            Agent(b.name, new_b),
        ])
    
    # add in those who didn't meet
    updated.extend(no_meet)
    return updated