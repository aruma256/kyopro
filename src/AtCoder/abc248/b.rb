a, b, k = gets.chomp.split.map(&:to_i)
ans = 0
until a >= b do
  a *= k
  ans += 1
end
puts ans
