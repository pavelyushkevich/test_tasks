class DictCompare():
    
    def compare(self, dict1, dict2):
        diff = {}
        for key in dict1.keys():
            if type(dict1[key]) == dict and type(dict2[key]) == dict:
                dict_diff = self.compare(dict1[key], dict2[key])
                if dict_diff != {}:
                    diff[key] = dict_diff
            elif dict1[key] != dict2[key]:
                diff[key] = dict2[key]
        return diff
