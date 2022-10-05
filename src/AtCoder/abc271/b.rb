N, Q = gets.chomp.split.map(&:to_i)
AS = N.times.map{ gets.chomp.split.map(&:to_i)[1..] }
Q.times do
  s, t = gets.chomp.split.map(&:to_i).map{ |n| n-1 }
  puts AS[s][t]
end
