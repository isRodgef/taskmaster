import json
from ConfigDataHelperFunctions import *

class ConfigData:
    required_fields = ["CMD", "NUM", "AUTO_S", "RESTART", "RET_CODE", "LIVE_TIME", "RESTART_NUM", "SIGNAL", "IN", "OUT",
                "ERROR", "ENV_VARS", "DIR", "USER_PERM", "GROUP_PERM", "WORLD_PERM"]
    auto_s_values = ["true", "false"]
    restart_values = ["true", "false", "on_error"]
    permission_values = ["R", "W", "X"]
    permission_types = ["USER_PERM", "GROUP_PERM", "WORLD_PERM"]
    permission_deliminator = ","
    env_vars_deliminator = ","
    def check_data(self, d_new):
        test = compare_keys(self.required_fields, d_new)
        if test is True:
            test = format_permissions(self.permission_values, self.permission_deliminator, self.permission_types, d_new)
        if test is True:
            test = format_env_vars(self.env_vars_deliminator, d_new)
        if test is True:
            test = compare_values(self.auto_s_values, "AUTO_S", d_new)
        if test is True:
            test = compare_values(self.restart_values, "RESTART", d_new)
        return (test)
    def load_data(self, file):
        data_new = dict()
        try:
            f = open(file, "r")
            try:
                data_new = json.load(f)
                if self.check_data(data_new):
                    if self.data:
                        print("I remembered that config was initialized")
                        self.changed_processes = list((set(self.data) - set(data_new)) | (set(data_new) - set(self.data)))
                        compare_dicts(self.changed_processes, self.data, data_new)
                    self.data = data_new
                    print("Config initialization succeeded")
                else:
                    print("Config initialization failed")
            except json.JSONDecodeError as err:
                print("Could not pars file")
                print(err)
        except FileNotFoundError:
            print(file + " does not exist")
    def __init__(self, file):
        self.data = None
        self.changed_processes = []
        ConfigData.load_data(self, file)