'''
Subdomain Visit Count
<T> HashTable

domain: discuss.leetcode.com
        top _> com
        next -> leetcode.com
        next -> discuss.leetcode.com

When we visit a domain, we also visit the top domains.



Given arr<"string">  ["count domain"]
first split the string


'''


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        def parseItem(domain):
            parsed = domain.split(" ")
            return(parsed[0], parsed[1])
        
        hmap = {}
        
        for item in cpdomains:
            c, domain = parseItem(item)
            parsed = domain.split(".")
            for i in range(len(parsed)):
                subdomain = ".".join(parsed[i:])
                #print(c, subdomain)
                if subdomain in hmap:
                    hmap[subdomain] += int(c)
                else:
                    hmap[subdomain] = int(c)
        
        # Another string operation, ugly question
        return [str(hmap[k]) + " " + str(k) for k in hmap]