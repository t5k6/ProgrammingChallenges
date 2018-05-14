// https://www.codewars.com/kata/century-from-year/train/c/5ad8c0f832d79ebde20000e0
int centuryFromYear(int year) 
{
  return (year % 100 == 0) ? year / 100 : year/100 + 1;
}