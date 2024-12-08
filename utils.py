

def print_stats(stats, trials):
    """
    Print the results of the simulation, including win rates and average points.
    """
    print(f"\nAfter {trials} trials:")
    print(f"Total successful 3-point shot wins: {stats['three_point_wins']}")
    print(f"Total successful foul shot wins: {stats['foul_wins']}")
    print(f"3-point win rate: {stats['three_point_wins'] / trials * 100:.2f}%")
    print(f"Foul win rate: {stats['foul_wins'] / trials * 100:.2f}%")
    print(f"Average points of 3-point strategy: {stats['total_points_3'] / trials:.2f}")
    print(f"Average points of foul strategy: {stats['total_points_foul'] / trials:.2f}")
