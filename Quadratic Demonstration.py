'''
This file describes the methods required to qualitatively evaluate a data set. These methods are inspired by the Qualitative Trajectory Calculus formulations.

Two sequential measurements can be described by their relative position and their movement towards or away from one another.

This code can be altered to use Numpy or Pandas, for small data sets however the standard Python3 List is just fine.

This sample requires MatPlotLib for demonstration purposes only.
'''


def to_qualitative_single_dimension(data):
    '''
    Converts a single dimensional list to a qualitative representation.
    '''
    # Check if we have been past a list.
    if not isinstance(data,list):
        raise Exception('Must be passed a list.')
    # Check we have been given more than one list entry.abs
    if not len(data) > 1:
        raise Exception('Must be passed a list containing more than one item.')

    # A variable to contain the results.
    # NB: This array is not the same size as the input array.
    _results = []
    # Now we are happy to continue.
    # Iterate over the length of the list.
    # This is important as we need to access the i-1 and i+1 variables.
    for i in range(len(data)):
        # First check if we can access i-1.
        if not i > 0:
            continue
        # Now check we can access i+1.
        if i == len(data) - 1:
            continue
        # Now store some temporary variables.
        # Can you reverse a linked list?
        _past = data[i-1]
        _present = data[i]
        _future = data[i+1]

        # Check we have been given the right types.
        # Local Import for clarity.
        import numbers
        if not isinstance(_past, numbers.Integral):
            raise Exception('List contains non numerical data type.')
        if not isinstance(_present, numbers.Integral):
            raise Exception('List contains non numerical data type.')
        if not isinstance(_present, numbers.Integral):
            raise Exception('List contains non numerical data type.')
        
        # Now to determine the relationships.
        # This block is spread out for clarity.
        if _past < _present:
            if _present < _future:
                # Data points are moving closer together.
                _results.append(-1)
            else:
                # A curve.
                _results.append(0)
        
        if _past > _present:
            if _present > _future:
                # Data points are moving further away from one another.
                _results.append(1)
            else:
                # A curve.
                _results.append(0)
    # All done. Return _results.
    return _results

def plot(_series1, _series2):
    '''Simple method to render data visually.'''
    import matplotlib.pyplot as plt
    x = range(100)
    y = range(100,200)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # Multiply the difference for qualatative by 100 to make it clearer.
    _series2 = [x * 100 for x in _series2]
    ax1.plot(range(len(_series1)), _series1, c='b', marker="s", linestyle='-', label='Original Data')
    ax1.plot(range(len(_series2)), _series2, c='r', marker="o", linestyle='-', label='Qualitative output')
    plt.legend(loc='lower left');
    plt.show()

def plot_histogram(_series):
    '''Simple method to render histograms visually.'''
    import matplotlib.pyplot as plt
    plt.bar(range(len(_series)), list(_series.values()), align='center')
    plt.xticks(range(len(_series)), list(_series.keys()))
    plt.show()

def enumerate(_series):
    '''Simple method to enumerate the entries within a data series.'''
    # Declare a return dictionary.
    _result = {}
    # Loop over _series.
    for item in _series:
        if not item in _result:
            # We just found one.
            _result[item] = 1
        else:
            # Increment.
            _result[item] += 1
    # All done. Return _result.
    return _result

if __name__ == '__main__':
    # Build a sample data set from x^2.
    QUADRATIC = [x**2 for x in range(-10, 11, 1)]
    QUALITATIVE_QUADRATIC = to_qualitative_single_dimension(QUADRATIC)
    # Print the output.
    for qual in QUALITATIVE_QUADRATIC:
        print(qual)
    print('The wide eyed amongst you will notice an alignment issue between the two series when representing them visually. This occurs because the qualitative representation of the list is one element shorter.')
    print('This method is useful as it reduces the complexity of the data from a number of readings, to a number of states. These states can be then modeled using markoff chains.')
    plot(QUADRATIC, QUALITATIVE_QUADRATIC)
    print('Enumerating the occurrence rate of the qualitative verbs can give an indication of changes between data points.')
    _occurances = enumerate(QUALITATIVE_QUADRATIC)
    plot_histogram(_occurances)

    
