import re

def is_empty(data):
    if data:
        return False
    else:
        return True


def compare_keys(key_words, data):
    ret = True
    for process in data:
        for word in key_words:
            if word not in data[process].keys():
                print("Field " + word + " missing for process " + process)
                ret = False
    return (ret)


def match_process_name_to_cmd(data):
    for process in data:
        if process != data[process]["CMD"]:
            print ("Process name does not match process CMD. process name shoud be: " + data[process]["CMD"]
                   + " not " + process)


def compare_permission(perm, perm_values):
    if perm is perm_values[0]:
        return (4)
    if perm is perm_values[1]:
        return (2)
    if perm is perm_values[2]:
        return (1)
    return (-1)


def format_permissions(values, delm, types, data):
    error = False
    perm = 0
    new_perm_elem = "0"
    for process in data:
        for type in types:
            tmp = data[process][type]
            if tmp != "":
                tmp = tmp.split(delm)
                if len(tmp) < 1 or len(tmp) > 3:
                    error = True
                else:
                    for member in tmp:
                        perm += compare_permission(member, values)
                    if perm < 1 or perm > 7:
                        error = True
            if error:
                print(type + " of " + process + " might not be well formatted. Please make sure you are using " +
                      "R, W, and X to indicate " +
                      " read, write, and execute permissions, deleminated by commas without any spaces, as in \"R,W,X\"." +
                      "Alternativly you can leave blank this option blank if no permissions are required")
            else:
                new_perm_elem += str(perm)
                del data[process][type]
                perm = 0
        data[process]["PERM"] = new_perm_elem
        new_perm_elem = "0"
    return (not error)


def format_env_vars(delm, data):
    error = False
    for process in data:
        env_var_list = data[process]["ENV_VARS"]
        if env_var_list != "":
            check_format = re.compile("[A-Z_]{1,}\=[^=\s]{0,}$")
            env_var_list = env_var_list.split(delm)
            for var in env_var_list:
                if not check_format.match(var):
                    print ("ENV_VARS in " + process + " might not be well formatted, please make sure you are using " +
                           "the format: VAR=data with commas, and no spaces seperating each environment variable.")
                    error = True
                data[process]["ENV_VARS"] = env_var_list
    return (not error)


def compare_values(values, field, data):
    error = True
    file_error = False
    for process in data:
        for value in values:
            if str(data[process][field]) == value:
                error = False
        if error:
            print (field + " in " + process + " might not be well formatted, please make sure you are using " +
                   "one of these values:", "")
            for value in values:
                print (" " + value + ",", "")
            print("")
            file_error = True
        error = True
    return (not file_error)


def compare_dicts(diff_list, old_data, new_data):
    for process in old_data:
        if process in new_data.keys():
            for field in old_data[process]:
                if old_data[process][field] != new_data[process][field]:
                    diff_list.append(process)