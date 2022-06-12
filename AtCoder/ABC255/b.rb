require 'set'

N, K = gets.chomp.split.map(&:to_i)
A = Set[*gets.chomp.split.map(&:to_i)]

d = []
b = []

(1..N).each do |i|
  x, y = gets.chomp.split.map(&:to_i)
  if A.include? i
    b << [x, y]
  else
    d << [x, y]
  end
end

puts d.map{|dx, dy| b.map{|bx, by| ((dx-bx)**2 + (dy-by)**2)**0.5}.min}.max
