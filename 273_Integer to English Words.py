class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        zeroToNineteen = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        thousands = ["","Thousand","Million","Billion"]
        #make sure we have space after the function
        def buildLessThanThousand(num):
            if num == 0: return ""
            elif num < 20: return zeroToNineteen[num] + " "
            elif num < 100: return tens[num//10] + " " + buildLessThanThousand(num%10)
            else: return zeroToNineteen[num//100] + " Hundred " + buildLessThanThousand(num%100)
        
        if num == 0: return "Zero"
        res = ""
        for i in range(len(thousands)):
            # make sure it has remainder, else 1 million
            if num % 1000 != 0:
                res = buildLessThanThousand(num%1000) + thousands[i] + " " + res
            num //= 1000
        return res.strip()
            
