public class KMP1 {
   public void matcher(String text, String pattern) {
      int[] pi = computePrefixFunction(pattern);
      int j = 0; // j is the index within the pattern
      // Visit all characters in the text
      for (int i = 0; i < text.length(); i++) {
         // look for shorter prefixes until finding one that
         // ends with text[i] or j becomes 0
         while (j > 0 && text.charAt(i) != pattern.charAt(j)) {
            j = pi[j - 1];
         }
         // Characters of text and pattern are matching, go on
         if (text.charAt(i) == pattern.charAt(j)) {
            j++;
         }
         // Print pi array
         System.out.print("π: ");
         for (int k = 0; k < pi.length; k++) {
            System.out.print(pi[k] + " ");
         }
         System.out.println();
         // Print current state of pattern and text
         System.out.println("i = " + i + ", j = " + j + ", patrón = " + pattern.substring(0, j) + ", texto = "
               + text.substring(i - j + 1, i + 1));
         if (j == pattern.length()) {
            System.out.println("Se encontró el patrón en la posición: " + (i - pattern.length() + 1));
            j = pi[j - 1];
         }
      }
   }

   public int[] computePrefixFunction(String pattern) {
      int[] pi = new int[pattern.length()];
      int j = 0;
      // Visit al characters in the pattern
      // Note that i starts at 1 (suffix has to be proper)
      for (int i = 1; i < pattern.length(); i++) {
         while (j > 0 && pattern.charAt(i) != pattern.charAt(j)) {
            j = pi[j - 1];
         }
         // Characters are matching, go on
         if (pattern.charAt(i) == pattern.charAt(j)) {
            j++;
         }
         // Assign "j" to the array at position "i"
         pi[i] = j;
         // Print pi array
         System.out.print("π: ");
         for (int k = 0; k <= i; k++) {
            System.out.print(pi[k] + " ");
         }
         System.out.println();
         // Print current state of pattern
         System.out.println("i = " + i + ", j = " + j + ", patrón = " + pattern.substring(0, j));
      }
      return pi;
   }

   public int[] computePrefixFunctionInefficient(String pattern) {
      int[] pi = new int[pattern.length()];
      pi[0] = 0;
      for (int i = 1; i < pattern.length(); i++) {
         String s = pattern.substring(0, i + 1);
         int len = 1;
         String prefix = s.substring(0, len);
         while (len <= i && s.startsWith(prefix) && s.endsWith(prefix)) {
            len++;
            prefix = s.substring(0, len);
         }
         pi[i] = len - 1;
      }
      return pi;
   }
}
