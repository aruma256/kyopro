N = gets.to_i
A = gets.chomp.split.map(&:to_i)

c = Hash.new(0)
A.each do |a|
  c[a] += 1
end
s = A.uniq.sort.reverse

(0...N).each do |i|
  puts c[s[i]]
end
