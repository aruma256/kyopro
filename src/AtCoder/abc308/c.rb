n = gets.to_i
e = n.times.map do |i|
  a, b = gets.split.map(&:to_i)
  [a, a+b, i]
end

e.sort!{|l, r| r[0]*l[1] <=> l[0]*r[1]}

puts e.map{|a, b, i| i+1}.join(" ")
