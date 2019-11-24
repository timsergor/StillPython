# 1268. Search Suggestions System. Medium. Contest.

# Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return list of lists of the suggested products after each character of searchWord is typed. 

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        
        def pref(a,b):
            if len(a) <= len(b):
                for i in range(len(a)):
                    if a[i] != b[i]:
                        return False
                return True
            return False
        
        answer = []
        for s in range(1, len(searchWord) + 1):
            new = []
            for i in range(len(products)):
                if pref(searchWord[:s], products[i]):
                    new.append(products[i])
                    if len(new) == 3:
                        break
            answer.append(new)
        return answer
