import statistics


def calculate_statistics(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    mode = statistics.mode(data)
    std_dev = statistics.stdev(data)
    return mean, median, mode, std_dev
