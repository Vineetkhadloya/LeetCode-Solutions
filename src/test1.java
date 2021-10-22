public class test1 {
    
    public String solution(String S){
        
        String[] lines = S.split("\n", -1);
        String newString = lines[0]+ "\n";

        for (int i=1; i<lines.length; i++){
            if (lines[i].contains("NULL"))
            {
                String[] check = lines[i].split(",");
                Boolean checkFlg = false;
                for (int j = 0; j <check.length; j++)
                {
                    System.out.println(check[j]);
                    if (check[j].equals("NULL"))
                    {
                        checkFlg = true;
                        break;
                    }
                }
                if (checkFlg == false)
                {
                    newString = newString + lines[i] + "\n";
                }
                
            }
            else
            {
                newString = newString + lines[i] + "\n";
            }
        }
        return (newString);
    }
    
    public static void main(String args[]) {
        String str = "header,header\nANNUL,ANNULLED\nnull,NILL\nNULL,NULL";
        System.out.println(str);
        System.out.println("========");
        test1 obj = new test1();
        String newStr = obj.solution(str);
        System.out.println(newStr);
    }
}