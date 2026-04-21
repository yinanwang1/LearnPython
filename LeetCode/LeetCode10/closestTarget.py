from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        times = 0
        length = len(words)
        while True:
            left = (startIndex - times + length) % length
            right = (startIndex + times) % length
            if left == right and 0 != times and  target != words[left]:
                break
            if target == words[left] or target == words[right]:
                return times
            times += 1

        return -1


if __name__ == '__main__':
    # print(Solution().closestTarget(["hello","i","am","leetcode"], "leetcode", 0))
    # print(Solution().closestTarget(["i", "eat", "leetcode"], "ate", 0))
    print(Solution().closestTarget(["lwgdugypkmsvxwhwbrccrbtemvudwhctnaaonednsbodptendi","lumylagwxpmmivpujfawgvdbtxpluwekdpeakrqelpvrflnsnr","lngqwiijizfzzhlvvszaownnachqunlktsnhgsjeluvcpmavuj","nabbqiyarxmzleesxrfaynypfxonyhvwhebfjsxyinepggxnns","oiqghjtvrhpgvsjlzmrwbwpmomqqliqytdzawhkwematskflgf","dtiwjpdgcsmhaiwxrgligxlibfmvclobjjhljrqlvpuiufskix","svqgvooghuqszkrmcrayqclotygdqnxfetdrfrfvbypgiizzdk","qzrmfzdiodkdbhwifsinmamljlztwqtaoivufkcyeydsvpmdzw","ihaekjyxvnmhvtanysybyqvrtmffpkgmnxisgmmhkhbtonlwgo","ucrvwdlifpckbimcvevgsniepuewjqpakwnxksumgvrnmhmtuk","lngqwiijizfzzhlvvszaownnachqunlktsnhgsjeluvcpmavuj","lngqwiijizfzzhlvvszaownnachqunlktsnhgsjeluvcpmavuj","vdtvcclyyraevotgikgojlbefpfmlzypychxehnglgettackoz","qxspwpzxfxyxalrjuliwtbyllamkifbknnhzyfeabavwvvdkzk","vdtvcclyyraevotgikgojlbefpfmlzypychxehnglgettackoz","ucrvwdlifpckbimcvevgsniepuewjqpakwnxksumgvrnmhmtuk","dtiwjpdgcsmhaiwxrgligxlibfmvclobjjhljrqlvpuiufskix","vtbfahotrkxwcfwzlijfoqdkrvdmavpllbcfvibrqeuntsmrcs","mfhqksxfeeltpiupaijavavbpphjxyuzqlqehirxnmviiaqnfv","oowbnwbktlmsawtbilyvksqkbuohhjxqbepxgklkrwpjzcvipe","mpnnvwuqbczvmrwhzvsmtuumwjczqehuumjvfbpgoxlurjbckq","byaschxhjcgnnodazzpisqriyszffaqqiwljbuigdvzzobrlmc","dmctcimgeztojrvqwyygmnzfwtsrmmbgednmytsludnrpjjjvk","qxspwpzxfxyxalrjuliwtbyllamkifbknnhzyfeabavwvvdkzk","cawzflwjjopbemxqazpsrsrlxljwqlvzpvjbjarqeqgythrsou","ydqjqvalipkkrcbdprgjjangclswdjpaajiwhxeupidxirlith","lwgdugypkmsvxwhwbrccrbtemvudwhctnaaonednsbodptendi","ejtkmbyqtwrlhwynnqggpjaaaydjqnczhtyphfgugpbardzlvj","cawzflwjjopbemxqazpsrsrlxljwqlvzpvjbjarqeqgythrsou","oowbnwbktlmsawtbilyvksqkbuohhjxqbepxgklkrwpjzcvipe","khhwlijglujhgimvfvuwgggigppichzscdtsiklalgqeqsencq","khhwlijglujhgimvfvuwgggigppichzscdtsiklalgqeqsencq","lngqwiijizfzzhlvvszaownnachqunlktsnhgsjeluvcpmavuj","frdsoraagsllmgtatzybegxotrtgsuwfzpzxkpegggvpodnhrr","ynuartuisymsqxxdqwndonpqhczqpuekwbayfidfisjpriqogx","shmpixycafoqskoegqfvsrvboiegqwlbrkiuoeetncdxqlqsov","oiqghjtvrhpgvsjlzmrwbwpmomqqliqytdzawhkwematskflgf","xjtatoefvpwwgsvmepltadmzngxtnahqypfxgjppbqsmqnjvxm","vtbfahotrkxwcfwzlijfoqdkrvdmavpllbcfvibrqeuntsmrcs","dmctcimgeztojrvqwyygmnzfwtsrmmbgednmytsludnrpjjjvk","dsohnrdxdqrbwdjhqpphwvlzfyizqyoedckthdlhmkxjxewubc","qriythowwswwwucgwmezpqqneatemdxfqzpeytlozzojguywby","lyhmqyjnztwzqotqkpmvpueyzjfroousgkkerqvmwjnjtmlkuf","qzrmfzdiodkdbhwifsinmamljlztwqtaoivufkcyeydsvpmdzw","qzrmfzdiodkdbhwifsinmamljlztwqtaoivufkcyeydsvpmdzw","gxrtwoayoosijaddrlbvxqsvbbvaziqemcpxgljlnexvjnnakk","mjftbskulmuztejkopyftjsdeoyuvhvqragbkqlfhgqqkafvau","mjftbskulmuztejkopyftjsdeoyuvhvqragbkqlfhgqqkafvau","qzrmfzdiodkdbhwifsinmamljlztwqtaoivufkcyeydsvpmdzw","qxspwpzxfxyxalrjuliwtbyllamkifbknnhzyfeabavwvvdkzk"], "ydqjqvalipkkrcbdprgjjangclswdjpaajiwhxeupidxirlith", 0))
