


import random
from config import THREE_POINT_STAT, TWO_POINT_STAT, FREE_THROW_STAT, REBOUND_STAT, OVERTIME_WIN_PROB, TIME_REMAINING, TIME_PER_ACTION, TRIALS
from simulation import simulate_three_pointer, simulate_foul, simulate_overtime, simulate_offense_play
from utils import print_stats

def run_trials():
    stats = {"three_point_wins": 0, "foul_wins": 0, "total_points_3": 0, "total_points_foul": 0 }

    for _ in range(TRIALS):
        time_remaining = TIME_REMAINING  
        down = 3  # The team is down by 3 points

        if random.choice([True, False]):
            # Simulate taking a 3-point shot
            points, time_remaining = simulate_three_pointer(THREE_POINT_STAT, REBOUND_STAT, time_remaining, TIME_PER_ACTION)
            stats["total_points_3"] += points

            if points > down:
                stats["three_point_wins"] += 1
            elif points == down:
                if simulate_overtime(OVERTIME_WIN_PROB):
                    stats["three_point_wins"] += 1
        else:
            # Simulate fouling and free throws
            points, time_remaining = simulate_foul(FREE_THROW_STAT, REBOUND_STAT, time_remaining, TIME_PER_ACTION)
            stats["total_points_foul"] += points

            if points > down:
                stats["foul_wins"] += 1
            elif points == down:
                if simulate_overtime(OVERTIME_WIN_PROB):
                    stats["foul_wins"] += 1

    # Print the results
    print_stats(stats, TRIALS)

if __name__ == "__main__":
    run_trials()
