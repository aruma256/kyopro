n, m = gets.split.map(&:to_i)
w = Array.new(n) { Array.new(n, 0) }
m.times do
  a, b, c = gets.split.map(&:to_i)
  a -= 1
  b -= 1
  w[a][b] = c
  w[b][a] = c
end
#
max_dist = 0
[*0...n].to_a.permutation.each do |route|
  dist = 0
  # route.each_cons(2) do |a, b|
  #   d = w[a][b]
  #   break if d == 0
  #   dist += d
  # end
  (n - 1).times do |i|
    d = w[route[i]][route[i + 1]]
    break if d == 0
    dist += d
  end
  max_dist = dist if dist > max_dist
end
puts max_dist
