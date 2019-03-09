def removeWhiteChar(string):
    return string.replace(' ', '').replace('\t', '').replace('\n', '')

def compare_proto(str_to_compare, function_ptr):
    import os, sys
    if 'histogram' in function_ptr.id(): 
        return  # numpy.histogram has slightly different between different version
    module_id = function_ptr.__class__.__module__
    functionName = function_ptr.id().split('.')[-1]
    test_file = os.path.realpath(sys.modules[module_id].__file__)
    expected_file = os.path.join(os.path.dirname(test_file),
                                    "expect",
                                    module_id.split('.')[-1] + '.' + functionName + ".expect")
    print(expected_file)
    assert os.path.exists(expected_file)
    with open(expected_file) as f:
        expected = f.read()
    str_to_compare = str(str_to_compare)
    print(removeWhiteChar(str_to_compare))
    print(removeWhiteChar(expected))
    assert removeWhiteChar(str_to_compare) == removeWhiteChar(expected)

def write_proto(str_to_compare, function_ptr):
    import os, sys
    module_id = function_ptr.__class__.__module__
    functionName = function_ptr.id().split('.')[-1]
    test_file = os.path.realpath(sys.modules[module_id].__file__)
    expected_file = os.path.join(os.path.dirname(test_file),
                                    "expect",
                                    module_id.split('.')[-1] + '.' + functionName + ".expect")
    print(expected_file)
    with open(expected_file, 'w') as f:
        f.write(str(str_to_compare))
