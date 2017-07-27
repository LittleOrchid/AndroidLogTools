# -*- coding: utf-8 -*-


class LogOnOffPair:
    def __init__(self, key, on_features, off_features):
        self.key = key
        self.on_features = on_features
        self.off_features = off_features
        pass

    def get_pair_identify(self, origin_data):
        if not self.on_features or not self.off_features:
            return self.key
        find_result = False
        for feature in self.on_features:
            if origin_data.find(feature) >= 0:
                find_result = True
                break
        if find_result:
            return self.key, "on"
        for feature in self.off_features:
            if origin_data.find(feature) >= 0:
                find_result = True
                break
        if find_result:
            return self.key, "off"
        else:
            return None, None


class PairStack:
    # Pair对，但每个Pair其实是一个槽的stack，相同Pair只保留一个，不同的求差异后全部pop掉
    def __init__(self, plist=[]):
        self.pair_list = plist
        pass

    def get_length(self):
        return len(self.pair_list)

    def push(self, pair, diff_method):
        # 相同Pair只保留一个，不同的求差异后全部pop掉
        pair_index = self.index_pair(pair)
        if pair_index == -1:
            self.pair_list.append(pair)
            return None
        else:
            base_pair = self.pair_list[pair_index]
            self.pair_list.remove(base_pair)
            return pair[0], diff_method(base_pair, pair)

    def pop(self, in_pair=None):
        # in_pair == None, pop掉最后一个
        # pop掉list中与in_pair的一个元素相同的pair
        if not in_pair:
            self.pair_list.pop()
        pair_index = self.index_pair(in_pair)
        if pair_index != -1:
            self.pair_list.pop(pair_index)

    def index_pair(self, pair):
        if len(self.pair_list) == 0:
            return -1
        for index, item_pair in enumerate(self.pair_list):
            if cmp(item_pair[0], pair[0]) == 0:
                return index
