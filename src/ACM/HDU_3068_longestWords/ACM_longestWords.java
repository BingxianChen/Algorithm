package ACM.HDU_3068_longestWords;
import java.util.ArrayList;
import java.util.Scanner;

public class ACM_longestWords {

    private String words;
    private ArrayList<Integer> doubList;

    public ACM_longestWords(String s) {
        words = s;
        doubList = new ArrayList<Integer>();
        findDoubList();
    }

    //从某个节点返回奇数的回文长度
    public int numOfOdd(int index) {
        for (int i = 1; i <= index && i < (words.length() - index); i++) {
            if (Character.compare(words.charAt(index - i), words.charAt(index + i)) != 0) {
                return (i - 1) * 2 + 1;
            }
        }
        if (index < words.length() - index){
            return (index - 1) * 2 + 1;
        }else{
            return (words.length() - index - 1) * 2 + 1;
        }

    }

    //遍历所有字符后的最大奇数回文长度
    public int maxOfOdd() {
        int max = 0;
        for (int index = 1; index < words.length() - 1; index++) {
            if (max < numOfOdd(index)) {
                max = numOfOdd(index);
            }
        }
        return max;

    }

    //查找符合要求的连续双元素
    public void findDoubList(){
        for (int i = 0; i < words.length() - 1; i++){
            if (Character.compare(words.charAt(i), words.charAt(i+1)) == 0){
                doubList.add(i);
            }
        }
    }

    //从某个节点返回偶数的回文长度
    public int numOfEven(int indexLeft) {
        for (int i = 1; i <= indexLeft && i < (words.length() - indexLeft - 1); i++) {
            if (Character.compare(words.charAt(indexLeft - i), words.charAt(indexLeft + i + 1)) != 0) {
                return (i - 1) * 2 + 2;
            }
        }
        return words.length();
    }

    //遍历所有字符后的最大偶数回文长度
    public int maxOfEven(){
        int max = 0;
        for (int index : doubList) {
            if (max < numOfEven(index)) {
                max = numOfEven(index);
            }
        }
        return max;

    }

    //混合奇数偶数两种情况快速得到结果
    public int maxLongWords(){
        int even = maxOfEven();
        int odd = maxOfOdd();
        if (even > odd){
            return even;
        }else{
            return odd;
        }
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {
            String a = in.next();
            if (a.length() == 0) {
                continue;
            }
            ACM_longestWords lw = new ACM_longestWords(a);
            System.out.println(lw.maxLongWords());
        }
    }
}








