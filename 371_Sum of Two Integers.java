class Solution {
    public int getSum(int a, int b) {
        // 3 + 2
        //         0011
        //         0010
        // ^       0001
        // & <<    0100
        // ^       0101
        
        // every << would add a 0 at the end, so no matter what a is, b would eventually be 0 after k iterations, k is the digits of the input
        int tmp;
        while (b != 0){
            // get all the carry bits
            tmp = a&b;
            // get the rest bit
            a = a^b;
            // move one level left
            b = tmp<<1;
        }
        return a;
    }
}
