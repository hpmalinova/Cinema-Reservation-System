def get_input(msg):
    var = input(msg)
    while not var:
        var = input(msg)
    return var
