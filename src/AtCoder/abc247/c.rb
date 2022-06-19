N = gets.chomp.to_i

s = []
(1..N).each do |i|
  s = s + [i] + s
end

puts s.join(' ')
