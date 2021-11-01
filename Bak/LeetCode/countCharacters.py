from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def judge(word: str, chars: str) -> bool:
            for character in set(word):
                if word.count(character) > chars.count(character):
                    return False

            return True

        def length(x):
            return len(x)

        result = list()

        for word in words:
            if judge(word, chars):
                result.append(word)

        return sum(list(map(length, result))) if len(result) > 0 else 0


solution = Solution()
result = solution.countCharacters(["pxlqovnbsgvqjzpfeidchzrodnbqfrccfydzjptukscjuatlsrcurepllxzyghhdepitqptlmfkhzxjgswaulxkfydhkilg","uqklvqnlhdkwryjawkqfajfpbcnhglxlwxlaskxlytr","jvgkxcdkxrvfahjkvhmfuyjzxtyxrsogbtsjybeaxugqymcr","rgxditmosplnqvodtis","jm","ruqjwejuanjtiizcmbieobesnjnadzqvqumggblzmkxilgfarnxwpcawtkzxlvugibpidvwtikloeziuxqoi","wxeyzrnbhlhwxecrgejsrawyulynvgtszwqqlihkcvckgcgtgpyqtkuwvjywmhpskaiwmpyarftqhnogxpith","vdpbykqlihtpvfnqbrcjpggojqbalerohyitktuikbffvfatcnneuvbanjihiaorrjcdthntnrxebfhvshmpodmzhtwnasbm","wgjstkoaojcesfdrllugmojwdmgeejyiqvshlowtktddattunarnohgvqsoskfmbrami","ecwqxbawirvnxvsjybbebclaturorlcbpf","gtjbaigvufrotlwfoqqolnjabnvtbcygtfcytinzpcjbvprdkdjawrcbthmxjrabimhhs","cvzlbrvppkyxtjxzeglzwoagmpjnfxddbwolxmwdohgtfktgftzzkwpianslkpldyfzubtjczse","neaw","mxhmvkajofnmdiiduactlemcvpztscmsnrdhuhquxnnzywsrzxyplgbppiypxwcfbsnyzblaeifo","krekecabfpufucjhqphjnibaeqdvdpmrfougdwugvoioqangdnxromwlxnfeydaneyazzclscqgdxlhhgnoqmslfflzqv","klutvchxsceihfmzitgqakytesfjykribjhjzdruuoycjkwaghmmqkfrhkrtawudtjyjwqbyspamlegqjlwlj","raykfkflqdzrpthdejetwolgciygwaktulkxemkdbbllkjxhnnafsms","os","xhchkcetmlprcdmrnalvkvgabxxnomphqpqhnddqhecogspbdebeoshvjgzvmqu","jqtdysnpskktynxwmsfaabglagnqcllptvuyyqjwrmqaftenusmsahhhqubkwxltpr","sulmwluiwvlroldpiyecaicwrawzwflokefqkdwmxejaovvpbflfdtviinbvvtlhhhefmgfsqs","sxyhcckvyl","vsaacsybcddxvuzkddjmuivsvtjyanpbydmkcwnkmxvsiantgkvkmqjysclsvd","sxcghypulvmfqfunxj","pozekufhlooosxpcggbi","xzaoxzllcixfqbupqozmzrnugj","j","tgslwp","ntrdkixexajlpjgmcbrqimwtqnzfrqjszeiuvrgzclerzmsnagzaxbredvlrmipzflrzusclckmxphc","ifdflsywdfizpodsehrrifsvejcxarrxmxyjgbbvqyqvywncphzfmnxhybxpdcozfnzablfx","uluhplzrsaehaqxfnbcmixueedevhirbwqdyztwaxnkogcauymxgcpabxekib","agtfkinbdccoemxetbryzpluzlpyzicnfopphrxriqm","pdympxpwvxwcqaxrvbvyqkrresrjgzgxuyfxtkgldtathokdbyfsqfmitmiyagtqgijaiazvsumeyutbbwxqdshquzrehn","rqe","sljsvenhhstnnngzqyo","dezrzpgldeimxfoqajuhjctgvalwkhkjemjaxumxqmifglbizusuqlttxirpbqbuvauwy","dkwpyezbmkcskoxxcgrxcewknqgdckjxfyzcmzqcbyeucxbqybxoldogtkmdknsrruvnlfqnpfx","sjeftmjkuperfynbreycwhuoyqybticswblbrrpugzhlrmiedjqufnehevzqwtaebwvdswsz","lolnfyliloqmhjmhhohdtgfajjfdjqpubslbsrwitbjmrcegdrdjzvonxaefdvdfcbqmaaks","qhcoaiocjhuzywkirlblajgeapzajqsoa","sxrmoqxqbtakuqwmrrkljmegbwbeqbywmlyuprwyhljzejbybxoumidpxdrohwdjoqycpxcmivaulnqzneydwqfsvcxgyyseuk","yrowy","dohrzkrzdjehpctnjrvhzojullsiucrhphshwxwicyzkvzbqrztic","rmshnxtbhsdgkiijrmwulocdzjzpgfyimkjdthuzkhoqgkeawgwincubrloknocxwzgqqcxafksxgzh","aymovnuhptozhkiyowbeguzlkmrwjnujgjbdne","abc","vxoigovwmqizmkwbkktqk","uokwktdempzloaglvvkqstztmwzcmhgxtoua","bzwjxqueazlzfojrkbqmhtwrvuwsnfcnylurnddpektekca","qgndjgvzcyajhgmrrnhdywwdbmkhtthwcfiueuxfldanyrmccwcy"]
,"figspbov")
print('end')
print(result)
