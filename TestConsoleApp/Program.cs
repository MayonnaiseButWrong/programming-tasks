Console.WriteLine("start");
decimal x = 0;
int decimalPlaces = 7;
for (decimal n = 1;n<(decimal)Math.Pow(10,decimalPlaces);n++) 
{
    x+=4m*(n%2==0?-1m:1m)/(2*n-1m);
}
Console.WriteLine(x);