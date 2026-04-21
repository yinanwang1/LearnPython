from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dict = dict()

        for domain in cpdomains:
            num_domain = domain.split(' ')
            print('num_domain')
            print(num_domain)
            if len(num_domain) != 2:
                continue

            domain_list = num_domain[1].split('.')
            for index in range(len(domain_list)):
                domain_temp = '.'.join(domain_list[index:])
                if domain_temp in domain_dict.keys():
                    domain_dict[domain_temp] += int(num_domain[0])
                else:
                    domain_dict.setdefault(domain_temp, int(num_domain[0]))

        result = list()
        print('domain_dict')
        print(domain_dict)
        for key, value in domain_dict.items():
            print('key value')
            print(key)
            print(value)
            result.append(str(value) + ' ' + str(key))

        return result



# solution = Solution()
# result = solution.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
# print('END')
# print(result)

from collections import defaultdict
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print('\n',d)
a=sorted(d.items())
print('\n',a)




