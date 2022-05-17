ans = []
(1..99).each do |i|
  ans.push i
  ans.push i * 1_00
  ans.push i * 1_00_00
end
puts ans.size
puts ans.sort.join(' ')
