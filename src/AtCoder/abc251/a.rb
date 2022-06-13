s = S = gets.chomp
until s.length >= 6 do
  s += S
end
puts s
