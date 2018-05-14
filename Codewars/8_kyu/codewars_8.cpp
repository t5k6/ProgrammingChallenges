// http://www.codewars.com/kata/find-the-smallest-integer-in-the-array/train/cpp
int findSmallest(vector <int> list)
{
  int min = list.at(0);
  
  for (int i = 1; i < list.size(); i++) {
    if ( list.at(i) < min ) min = list.at(i);
  }
  return min;
}
// alternative: return *std::min_element(list.begin(),list.end())