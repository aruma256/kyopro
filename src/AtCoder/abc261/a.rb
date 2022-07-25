L1, R1, L2, R2 = gets.chomp.split.map(&:to_i)

puts (0..100).count {|i| (L1...R1).include?(i) && (L2...R2).include?(i) }
