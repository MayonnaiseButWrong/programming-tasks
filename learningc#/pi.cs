using System;
Console.WriteLine("start");
double x = 0;
int decimalPlaces = 10;
for (double n = 1;n<(double)Math.Pow(10,decimalPlaces);n++) 
{
    x+=(n%2==0?-4d:4d)/(2*n-1d);
}
Console.WriteLine(x);
