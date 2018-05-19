# https://www.codewars.com/kata/list-filtering/train/ruby
def filter_list(l)
  l.select { |i| i*0==0 }.compact
end

# http://www.codewars.com/kata/friend-or-foe/train/ruby
def friend(friends)
  friends.select { |name| name.length == 4 }
end
