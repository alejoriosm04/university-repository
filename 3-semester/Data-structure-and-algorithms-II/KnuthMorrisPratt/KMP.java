
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author htrefftz
 */

public class KMP {
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
            // Add a 0 to the pattern if no match is found
            if (j == 0) {
                pattern += "0";
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
        // Print message indicating that the search has ended
        System.out.println("Búsqueda terminada");
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
            String prefix = pattern.substring(0, i + 1);
            int max = 0;
            for (int j = 1; j < prefix.length(); j++) {
                String suffix = prefix.substring(j, prefix.length());
                if (prefix.startsWith(suffix)) {
                    max = Math.max(max, suffix.length());
                }
            }
            pi[i] = max;
        }
        return pi;
    }
}
