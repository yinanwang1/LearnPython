from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            values = email.split('@')
            address = values[0]
            address = address.replace('.', '')
            try:
                index = address.index('+')
                address = address[:index]
            except Exception as e:
                pass

            result.add(address + values[1])

        return len(result)




