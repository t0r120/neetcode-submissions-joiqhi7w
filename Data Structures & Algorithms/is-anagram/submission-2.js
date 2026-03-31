class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let splitted_s = s.split('').sort().join('');
        let splitted_t = t.split('').sort().join('');

        if(splitted_s == splitted_t){
            return true
        }
        return false


    }
}
