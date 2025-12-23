def double(x):
    return 2 * x

def square(x):
    return x * x

def triple(x):
    return 3 * x


def build_pipeline(operation_names):
    operations = {
        "double": double,
        "square": square,
        "triple": triple
    }

    # This must raise KeyError for unknown operations
    for name in operation_names:
        if name not in operations:
            raise KeyError(name)

    def pipeline(value):
        result = value
        for name in operation_names:
            result = operations[name](result)
        return result

    return pipeline
