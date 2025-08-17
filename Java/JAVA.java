class Launch{
    public static void main(String[] args)
    {
        int a = 5;
        int b = 3;
        int c = -1;
        int d = 0;
        int e = -5;
        int res;

        res = (--c)-(a--)+(++e)+(--b)-(d--)+(++d)-(a++)+(++b)+(c++)-(b--)+(--a);

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        System.out.println(res);

    }
}