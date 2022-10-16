x = gets.chomp.chars.map(&:to_i)
if x.uniq.length == 1
  puts 'Weak'
elsif x.each_cons(2).all? {|a, b| (a+1)%10 == b%10 }
  puts 'Weak'
else
  puts 'Strong'
end
