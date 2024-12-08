


import random

def simulate_three_pointer(three_point_stat, rebound_stat, time_remaining, time_per_action):
    """
    Simulate a 3-point shot attempt. If missed, attempt an offensive rebound.
    """
    if time_remaining <= 0:
        return 0, time_remaining 

    shot_success = random.random() < three_point_stat
    time_remaining -= time_per_action 

    if shot_success:
        return 3, time_remaining 


    if random.random() < rebound_stat and time_remaining > time_per_action:
        return simulate_offense_play(time_remaining, time_per_action)

    return 0, time_remaining

def simulate_foul(free_throw_stat, rebound_stat, time_remaining, time_per_action):
    """
    Simulate fouling the opponent, leading to free throw attempts, and possibly an offensive play.
    """
    if time_remaining <= 0:
        return 0, time_remaining 

    free_throw_success = 0
    for _ in range(2):
        if time_remaining <= 0:
            break

        if random.random() < free_throw_stat:
            free_throw_success += 1
        time_remaining -= time_per_action
    points, time_remaining = simulate_offense_play(time_remaining, time_per_action)
    points += free_throw_success

    return points, time_remaining

def simulate_offense_play(time_remaining, time_per_action):
    """
    Simulate a 2-point shot attempt if there's enough time remaining.
    """
    if time_remaining <= 0:
        return 0, time_remaining

    shot_success = random.random() < 0.5  
    time_remaining -= time_per_action 

    return (2 if shot_success else 0), time_remaining

def simulate_overtime(overtime_win_prob):
    """
    Simulate winning in overtime if the score is tied.
    """
    return random.random() < overtime_win_prob  
