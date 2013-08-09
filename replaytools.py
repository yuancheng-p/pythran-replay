import matplotlib.pyplot as plt


def plot_results(results, title):
    """Plot compile time and execute time.

    We only take the best time for the execute time as it is
    the most stable one.
    Other time data are keeped in log files.
    """
    compile_times = []
    best_times = []

    for commit, result in results.items():
        best_times.append(result['best_time'])
        compile_times.append(result['compile_time'])

    xcnts = range(len(results))
    plt.suptitle(title)

    #compile_ax configure
    plt.subplot(211)
    plt.plot(xcnts, compile_times, '--r*')
    plt.ylabel("Compile time")
    plt.grid(True)
    plt.xlim([0, xcnts[-1] + 1])

    #execute_ax configure
    plt.subplot(212)
    plt.plot(xcnts, best_times, '--g*', label='$BestTime$')
    plt.ylabel("Execute time")
    plt.xlabel("Commit")
    plt.grid(True)
    plt.xlim([0, xcnts[-1] + 1])

    plt.show()
