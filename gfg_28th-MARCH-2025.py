#!/usr/bin/python3


def activitySelection(start: list[int], finish: list[int]):
    # Check for bugs
    """
    Returns the maximum number of activities
    that a person can complete in a day
    """
    task_duration = sorted(zip(start, finish), key=lambda x: x[1])
    
    # Always select the first activity
    count = 1
    last_finish_time = task_duration[0][1]

    # Iterate through the rest of the activities
    for i in range(1, len(task_duration)):
        # Check if current activity starts after or at last selected finish time
        if (task_duration[i][0] >= last_finish_time 
                and task_duration[i][1] <= 24):
            count += 1
            last_finish_time = task_duration[i][1]  # Update the finish time

    return count


if __name__ == "__main__":
    print(activitySelection([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
    print(activitySelection([10, 12, 20], [20, 25, 30]))
    print(activitySelection([1, 3, 2, 5], [2, 4, 3, 6]))
