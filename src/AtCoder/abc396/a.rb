N = gets.chomp.to_i
A = gets.chomp.split(" ").map(&:to_i)

puts A.each_cons(3).any? { _1.uniq.size == 1 } ? "Yes" : "No"
