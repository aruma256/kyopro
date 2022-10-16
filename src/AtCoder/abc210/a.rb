n, a, x, y = gets.chomp.split.map(&:to_i)

ans = 0
b = 0
while n.positive?
  b += 1
  ans += (b <= a ? x : y)
  n -= 1
end
puts ans
