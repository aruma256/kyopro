N, M = gets.chomp.split.map(&:to_i)
A = gets.chomp.split.map(&:to_i)
B = gets.chomp.split.map(&:to_i)

c = A.map {|v| [v, 'A'] } + B.map {|v| [v, 'B'] }
c.sort!

puts c.each_cons(2).filter{ _1.last != _2.last }.map{ _2.first - _1.first }.min
