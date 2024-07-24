def input_error(function):
    def inner(args, contacts):
        try:
            return function(args, contacts)
        except ValueError:
            return "Give me name and phone please"
        except KeyError:
            return "This contact does not exist. Please enter a valid contact name."
        except IndexError:
            return "Give me name and phone please"
    return inner
