package Array;

import java.util.HashSet;

public class DuplicateElem {
    public static Boolean duplicate(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3 ,4  };

        HashSet<Integer> set = new HashSet<>();
        for (int i : arr) {
            set.add(i);
        }
        if(set.size() <arr.length){
            System.out.println(true);
        }else{
            System.out.println(false);
        }
    }
}
