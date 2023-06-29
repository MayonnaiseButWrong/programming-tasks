class table
{
    private string tablename;
    private object[,] array = new object[,] {};
    public table(params object[] strings)
    {
        tablename = strings[0,0];
        for (int i=1; i<strings.Length; i++)
        {
            if (strings[i,1]=="string")
            {
                array[0].Add(strings[i,0]);
                array.Add(new string[]);
            } 
            else if (strings[i,1]=="int")
            {
                array[0].Add(strings[i,0]);
                array.Add(new int[]);
            }
            else if (strings[i,1]=="float")
            {
                array[0].Add(strings[i,0]);
                array.Add(new int[]);
            }
        }

    }
    
}