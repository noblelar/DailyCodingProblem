function canFormPalindrome(str, k) {
   function isPalindrome(s, start, end) {
       while (start < end) {
           if (s[start] !== s[end]) {
               return false;
           }
           start++;
           end--;
       }
       return true;
   }

   function canMakePalindrome(s, start, end, k) {
       while (start < end) {
           if (s[start] !== s[end]) {
               if (k === 0) return false;
               // Try removing either the start or end character
               return canMakePalindrome(s, start + 1, end, k - 1) ||
                      canMakePalindrome(s, start, end - 1, k - 1);
           }
           start++;
           end--;
       }
       return true;
   }

   return canMakePalindrome(str, 0, str.length - 1, k);
}

// Test cases
console.log(canFormPalindrome('waterrfetawx', 2)); // true
console.log(canFormPalindrome('abcba', 0)); // true
console.log(canFormPalindrome('abcde', 2)); // false
console.log(canFormPalindrome('abxa', 1)); // true
