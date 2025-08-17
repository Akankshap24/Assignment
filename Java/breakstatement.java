public class breakstatement{
    public static void main (String [] args){
        for (int i = 1; i<=5;i++){
            for(int j = 1; j<=5; j++){
                if (i == 3 && j>2){
                    break;
                }
                System.out.print("*");
            }
           System.out.println(); 
    }
}
}
