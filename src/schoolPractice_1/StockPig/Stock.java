package schoolPractice.StockPig;
/**
 * @author chen
 * @date 04/12/2016
 * @since 3.0
 */
public class Stock {
    /**
     * 计算你能获得的最大收益
     *
     * @param prices Prices[i]即第i天的股价
     * @return 整型
     */

    public int oneMax(int[] prices, int start, int stop){
        int max = 0;
        for (int i = start; i < stop - 1; i++){
            for (int j = i+1; j < stop; j ++){
                if (max < prices[j] - prices[i]){
                    max = prices[j] - prices[i];
                }
            }
        }
        return max;
    }

    public int calculateMax(int[] prices) {
        int maxOne = oneMax(prices,0,prices.length);
        int maxTwo =0;
        for (int i = 2;i < prices.length - 1; i ++){
            if (maxTwo < oneMax(prices,0,i) + oneMax(prices,i,prices.length)){
                maxTwo = oneMax(prices,0,i) + oneMax(prices,i,prices.length);
            }

        }
        if (maxOne > maxTwo){
            return maxOne;
        }else {
            return maxTwo;
        }

    }

    public static void main(String[] args){
        Stock st = new Stock();
        int[] prices = {31,41};
        System.out.println(st.calculateMax(prices));
    }
}
