require 'prime'

N = gets.chomp.to_i
ps = Prime.each.take_while{ |n| 2 * n**3 <= N }.to_a
ans = 0

until ps.empty?
  p = ps.shift
  ps.pop while !ps.empty? && p * ps.last ** 3 > N
  ans += ps.size
end

puts ans
