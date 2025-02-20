class d01:
    def __init__(self, data):
        """ 
        This Christmas we are missing the Chief Historian. 
            - Finding him we look at the historical locations he was checking out this year. 
                + Each of these locations will be marked by a star.
            - data is a list of pairs of values obtained by the 'input' file.
        """
        self.data = data
    def p1(self):
        """
        Given the data sort them from least to greatest and compare their absolute distance difference.
            - The answer is the accumulation of these distances.
        """
        total = 0
        right_list = []
        left_list = []
        for pair in self.data:
            left_list.append(pair[0])
            right_list.append(pair[1])
        left_list = sorted(left_list)
        right_list = sorted(right_list)
        for index in range(len(left_list)):
            total += abs(left_list[index] - right_list[index])
        return total

    def p2(self):
        """
        from part 1's answer the anaylsis confirmed that the two lists of location IDs are very different.
        - The new theory is to find out the similiary score of the lists.
            + by adding up each number in the left list by the number of times the number appears in the right list.
        """
        left_nums = {}
        right_nums = {}
        # 2.19, the answer is too low...
        for pair in self.data:
            try:
                left_nums[pair[0]] += 1
            except:
                left_nums[pair[0]] = 1
            try:
                right_nums[pair[1]] += 1
            except:
                right_nums[pair[1]] = 1
        
        total = 0
        for key, value in left_nums.items():
            try:
                print("\t", right_nums[key])
                print(key, value)
                total += value * right_nums[key]
            except KeyError:
                pass
        return total

if __name__ == '__main__':
    data = [tuple(map(int, i.split("   "))) for i in open("input").read().splitlines()]
    d = d01(data)
    p1_v = d.p1()
    print("answer to p1: {}".format(p1_v))
    p2_v = d.p2()
    print("answer to p2: {}".format(p2_v))
