package interview;

import java.util.*;

/**
 * @author chen
 * @company 杭州尚尚签网络科技有限公司
 * @date 03/03/2017
 * @since 3.0
 */
public class Four {
    static boolean resolve(int[] A){
        return true;
    }

    public static void main(String[] args){
        ArrayList<Integer> inputs = new ArrayList<Integer>();
        Scanner in = new Scanner(System.in);
        String line = in.nextLine();
        while(line != null && !line.isEmpty()){
            int value = Integer.parseInt(line.trim());
            if (value == 0) break;
            inputs.add(value);
            line = in.nextLine();
        }
        int[] A = new int[inputs.size()];
        for (int i = 0; i < inputs.size(); i++) {
            A[i] = inputs.get(i).intValue();
        }

        Boolean res = resolve(A);

        System.out.println(String.valueOf(res));

    }

}
