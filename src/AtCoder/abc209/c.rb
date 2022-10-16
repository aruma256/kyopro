N = gets.to_i
C = gets.chomp.split.map(&:to_i)
C.sort!

ans = 1
C.each_with_index  do |c, idx|
  ans = (ans * (c-idx)) % 1000000007
end

puts ans
