N = gets.chomp.to_i
A = gets.chomp.split.map(&:to_i)

b = [0] * 3
ans = A.map do |a|
  b << 1
  (a-1).times { b << 0 }
  b.shift(a).sum
end.sum

puts ans
