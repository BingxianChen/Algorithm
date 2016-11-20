package schoolPractice.binary;
/**
 * @author chen
 * @date 2016/11/20
 * @since 3.0
 */

public class BinarySolution {
    /**
     * 获得两个整形二进制表达位数不同的数量
     *
     * @param m 整数m
     * @param n 整数n
     * @return 整型
     */
    public int countBitDiff(int m, int n) {
        String binM = Integer.toBinaryString(m);
        String binN = Integer.toBinaryString(n);
        System.out.println(binM);
        System.out.println(binN);
        int lenM = binM.length();
        int lenN = binN.length();
        int count = 0;
        int dis = 0;
        if (lenM >= lenN){
            for (int i = lenN-1; i >= 0; i--) {
                if (Character.compare(binM.charAt(i + lenM - lenN), binN.charAt(i)) != 0) {
                    count++;
                }
            }

            for (int i = lenM - lenN - 1; i >= 0; i--){
                if (Character.compare(binM.charAt(i), '0') != 0){
                    dis ++;
                }
            }
        }else{
            for (int i = lenM-1; i >= 0; i--) {
                if (Character.compare(binM.charAt(i), binN.charAt(i + lenN - lenM)) != 0) {
                    count++;
                }
            }

            for (int i = lenN - lenM -1; i >= 0; i--){
                if (Character.compare(binN.charAt(i), '0') != 0){
                    dis ++;
                }
            }
        }


        return count + dis;
    }
    public static void main(String[] args){
        System.out.print(new BinarySolution().countBitDiff(253647,43345687));

    }

}
