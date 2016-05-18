import sys
import importlib
if __name__ == '__main__':
    if (len(sys.argv) != 4):
        print("Usage: main.py <SRM> <CLASS> <METHOD>")
        exit(-1)

    srm = sys.argv[1]
    class_name = sys.argv[2]
    method_name = sys.argv[3]

    module = importlib.import_module(srm+"."+class_name)
    clazz = getattr(module, class_name)
    obj = clazz()
    method = getattr(obj, method_name)

    # Read test file
    file_obj = open(srm+"/"+class_name+"."+method_name+".bin")
    for line in file_obj:
        [input, output] = line.split('\t')
        cmd = "method("+input+")"
        real_output =  eval(cmd)
        if output[0] == "\"":
            output = output.strip("\n")
            real_output = "\"" + real_output + "\""
        else:
            output = eval(output)

        print("input:" + input + "\toutput:" + str(real_output))

        if real_output == output:
            print("\t\033[0;32;mPass\033[0m")
        else:
            print("\t\033[0;31;mFail\033[0m\texpected:" + str(output))
