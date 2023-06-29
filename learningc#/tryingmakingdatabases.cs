///class table
///{
///    private string tablename;
///    private object[,] array = new object[,] {};
///    public table(params object[] strings)
///    {
///        tablename = strings[0,0];
///        for (int i=1; i<strings.Length; i++)
///        {
///            if (strings[i,1]=="string")
///            {
///                array[0].Add(strings[i,0]);
///                array.Add(new string[]);
///            } 
///            else if (strings[i,1]=="int")
///            {
///                array[0].Add(strings[i,0]);
///                array.Add(new int[]);
///            }
///            else if (strings[i,1]=="float")
///            {
///                array[0].Add(strings[i,0]);
///                array.Add(new int[]);
///            }
///        }
///
///    }
///    
///}

class date
{
    private int day;
    {
        get{return day;}
    }
    private int month;
    {
        get{return month;}
    }
    private int year;
    {
        get{return year;}
    }
    private int[12]normalDaysPerMonth = new int[12] {31,28,31,30,31,30,31,31,30,31,30,31};
    private int[12]leapDaysPerMonth = new int[12] {31,28,31,30,31,30,31,31,30,31,30,31};
    public date(int d = 0, int m = 0, int y = 0)
    {
        day=d;
        month=m;
        year=y;
    }
    private static int getDaysPerMonth(m)
    {
        if (year%4==0)
        {
            return leapDaysPerMonth[m];
        }
        else
        {
            return normalDaysPerMonth[m];
        }
    }
    public override date operator +(date x, date y)
    {
        int sumday=x.day+y.day;
        int summonth = x.month+y.month
        int sumyear = x.year+y.year
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
        while (sumday > getDaysPerMonth(summonth))
        {
            summonth++;
            if (summonth > 12)
            {
                summonth=1;
                sumyear++;
            }
            sumday-=getDaysPerMonth(summonth);
        }
        while (sumday<=0)
        {
            summonth--;
            if (summonth <= 0)
            {
                summonth=12;
                sumyear--;
            }
            sumday+=getDaysPerMonth(summonth);
        }
        return new date(sumday, summonth, sumyear);
    }
    public override date operator +(date x, int y)
    {
        int sumday=x.day+y;
        int summonth=x.month;
        int sumyear=x.year;
        while (sumday > getDaysPerMonth(summonth))
        {
            summonth++;
            if (summonth > 12)
            {
                summonth=1;
                sumyear++;
            }
            sumday-=getDaysPerMonth(summonth);
        }
        while (sumday<=0)
        {
            summonth--;
            if (summonth <= 0)
            {
                summonth=12;
                sumyear--;
            }
            sumday+=getDaysPerMonth(summonth);
        }
        return new date(sumday, summonth, sumyear);
    }
    public override void operator +(int x, date y)
    {
        throw new ArgumentException("You cannot add a type int and type date together in this order");
    }
    public override date operator -(date x, date y)
    {
        int sumday = x.day-y.day;
        int summonth = x.month-y.month
        int sumyear = x.year-y.year
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
        while (sumday > getDaysPerMonth(summonth))
        {
            summonth++;
            if (summonth > 12)
            {
                summonth=1;
                sumyear++;
            }
            sumday-=getDaysPerMonth(summonth);
        }
        while (sumday<=0)
        {
            summonth--;
            if (summonth <= 0)
            {
                summonth=12;
                sumyear--;
            }
            sumday+=getDaysPerMonth(summonth);
        }
        return new date(sumday, summonth, sumyear);
    }
    public override date operator -(date x, int y)
    {
        int sumday=x.day-y;
        int summonth=x.month;
        int sumyear=x.year;
        while (sumday > getDaysPerMonth(summonth))
        {
            summonth++;
            if (summonth > 12)
            {
                summonth=1;
                sumyear++;
            }
            sumday-=getDaysPerMonth(summonth);
        }
        while (sumday<=0)
        {
            summonth--;
            if (summonth <= 0)
            {
                summonth=12;
                sumyear--;
            }
            sumday+=getDaysPerMonth(summonth);
        }
        return new date(sumday, summonth, sumyear);
    }
    public override void operator -(int x, date y)
    {
        throw new ArgumentException("You cannot add a int type and date type together in this order");
    }
    public override void operator *(params object[])
    {
        throw new ArgumentException("You cannot multiply a date type");
    }
    public override void operator /(params object[])
    {
        throw new ArgumentException("You cannot divide a date type");
    }
    public override string ToString()
    {
        return (string)day + "/" + (string)month + "/" + (string)year
    }
}

class time
{
    private int hours;
    {
        get { return hours; }
    }
    private int minutes;
    {
        get { return minutes; }
    }
    private int seconds;
    {
        get { return seconds; }
    }
}

today = date(29/6/2023)
tomorrow =date(30/6/2023)
Console.WriteLine(today+tomorrow)