N = gets.chomp.to_i

a = []
na = []

N.times do
  (0...a.length).each do |i|
    na << (i-1>=0 ? a[i-1] : 0) + a[i]
  end
  na << 1
  a, na = na, a
  puts a.join(' ')
  na.clear
end
