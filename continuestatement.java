public class continuestatement {
    public static void main (String [] args){
        for (int i = 1; i<=5;i++){
            for(int j = 1; j<=5; j++){
                if (i == 3 && j>=2 && j<4){
                    continue;
                }
                    System.out.println(j);
                }               
            }
           System.out.println(); 
    }

} 


