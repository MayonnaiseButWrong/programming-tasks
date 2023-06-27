using System;

namespace pi
{
    class pi
    {
        static void Main() 
        {
            decimal x = 0;
            for (decimal n = 1;n<1000;n++) 
            {
                x+=(n%2==0?-1m:1m)/(2*n+1m);
            }
            Console.WriteLine(x);
        }
    }
}