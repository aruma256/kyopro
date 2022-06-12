N, Q = gets.chomp.split.map(&:to_i)
A = gets.chomp.split.map(&:to_i).sort
S = [0]
A.each do |a|
  S << S[-1] + a
end

Q.times do
  x = gets.chomp.to_i
  idx = A.bsearch_index {|n| n >= x}
  idx ||= N
  puts x*idx - S[idx] + S[-1]-S[idx] - x*(N-idx)
end
