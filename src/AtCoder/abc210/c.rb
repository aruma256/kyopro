N, K = gets.chomp.split.map(&:to_i)
C = gets.chomp.split.map(&:to_i)

d = Hash.new(0)
v = 0
v_max = 0
C.each_with_index do |c, idx|
  v += 1 if d[c].zero?
  d[c] += 1
  if K <= idx
    v -= 1 if d[C[idx-K]] == 1
    d[C[idx-K]] -= 1
  end
  v_max = [v_max, v].max
end
puts v_max
