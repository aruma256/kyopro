n, p, q, r, s = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)

p -= 1
q -= 1
r -= 1
s -= 1

(0..q-p).each do |d|
  A[p+d], A[r+d] = A[r+d], A[p+d]
end

puts A.join(' ')
