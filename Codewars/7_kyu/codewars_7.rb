# https://www.codewars.com/kata/list-filtering/train/ruby
def filter_list(l)
    l.select { |i| i*0==0 }.compact
  end