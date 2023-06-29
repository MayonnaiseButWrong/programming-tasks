class date
{
    private int Day;
    public int day
    {
        get{return Day;}
    }
    private int Month;
    public int month
    {
        get{return Month;}
    }
    private int Year;
    public int year
    {
        get{return Year;}
    }
    public override string ToString()
    {
        return Day.ToString() + "/" + Month.ToString() + "/" + Year.ToString();
    }
    public date(int d, int m, int y)
    {
        Day=d;
        Month=m;
        Year=y;
    }
    private static int getDaysPerMonth(int m,int y)
    {
        int[] normalDaysPerMonth = new int[12] {31,28,31,30,31,30,31,31,30,31,30,31};
        int[] leapDaysPerMonth = new int[12] {31,28,31,30,31,30,31,31,30,31,30,31};
        if (y%4==0)
        {
            return leapDaysPerMonth[m-1];
        }
        else
        {
            return normalDaysPerMonth[m-1];
        }
    }
    public static date operator +(date x, date y)
    {
        int sumday=x.day+y.day;
        int summonth = x.month+y.month;
        int sumyear = x.year+y.year;
        while (summonth > 12)
        {
            sumyear++;
            summonth-=12;
        }
        while (summonth<=0)
        {
            sumyear--;
            summonth+=12;
        }
        while (sumday > getDaysPerMonth(summonth,sumyear))
        {
            sumday-=getDaysPerMonth(summonth,sumyear);
            summonth++;
            if (summonth > 12)
            {
                summonth=1;
                sumyear++;
            }
        }
        while (sumday<=0)
        {
            sumday+=getDaysPerMonth(summonth,sumyear);
            summonth--;
            if (summonth <= 0)
            {
                summonth=12;
                sumyear--;
            }
        }
        return new date(sumday, summonth, sumyear);
    }
    public static date operator +(date x, int y)
    {
        int sumday=x.day+y;
        int summonth=x.month;
        int sumyear=x.year;
        while (sumday > getDaysPerMonth(summonth,sumyear))
        {
            sumday-=getDaysPerMonth(summonth,sumyear);
            summonth++;
            if (summonth > 12)
            {
                summonth=1;
                sumyear++;
            }
        }
        while (sumday<=0)
        {
            sumday+=getDaysPerMonth(summonth,sumyear);
            summonth--;
            if (summonth <= 0)
            {
                summonth=12;
                sumyear--;
            }
        }
        return new date(sumday, summonth, sumyear);
    }
    public static date operator +(int x, date y)
    {
        throw new ArgumentException("You cannot add a type int and type date together in this order");
    }
    public static date operator -(date x, date y)
    {
        int sumday = x.day-y.day;
        int summonth = x.month-y.month;
        int sumyear = x.year-y.year;
        while (summonth > 12)
        {
            sumyear++;
            summonth-=12;
        }
        while (summonth<=0)
        {
            sumyear--;
            summonth+=12;
        }
        while (sumday > getDaysPerMonth(summonth,sumyear))
        {
            sumday-=getDaysPerMonth(summonth,sumyear);
            summonth++;
            if (summonth > 12)
            {
                summonth=1;
                sumyear++;
            }
        }
        while (sumday<=0)
        {
            sumday+=getDaysPerMonth(summonth,sumyear);
            summonth--;
            if (summonth <= 0)
            {
                summonth=12;
                sumyear--;
            }
        }
        return new date(sumday, summonth, sumyear);
    }
    public static date operator -(date x, int y)
    {
        int sumday=x.day-y;
        int summonth=x.month;
        int sumyear=x.year;
        while (sumday > getDaysPerMonth(summonth,sumyear))
        {
            sumday-=getDaysPerMonth(summonth,sumyear);
            summonth++;
            if (summonth > 12)
            {
                summonth=1;
                sumyear++;
            }
        }
        while (sumday<=0)
        {
            sumday+=getDaysPerMonth(summonth,sumyear);
            summonth--;
            if (summonth <= 0)
            {
                summonth=12;
                sumyear--;
            }
        }
        return new date(sumday, summonth, sumyear);
    }
    public static date operator -(int x, date y)
    {
        throw new ArgumentException("You cannot add a int type and date type together in this order");
    }
}

class time
{
    private int Hours;
    public int hours
    {
        get { return Hours; }
    }
    private int Minutes;
    public int minutes
    {
        get { return Minutes; }
    }
    private int Seconds;
    public int seconds
    {
        get { return Seconds; }
    }
}

Console.WriteLine("HERE");
date today = new date(29,6,2023);
date tomorrow = new date(30,6,2023);
Console.WriteLine(today+new date(-11,-11,03));