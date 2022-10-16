N, X = gets.chomp.split.map(&:to_i)
A = gets.chomp.split.map(&:to_i)

A.each_index { |i| A[i] -= 1 if (i+1).even? }

puts A.sum <= X ? 'Yes' : 'No'
