require 'set'

N, M = gets.chomp.split.map(&:to_i)

w = Array.new(N+1) {[]}

M.times do
  a, b = gets.chomp.split.map(&:to_i)
  w[a] << b
  w[b] << a
end

Q = gets.chomp.to_i

Q.times do
  x, k = gets.chomp.split.map(&:to_i)
  q = [x]
  nq = []
  r = Set[x]
  while k > 0
    q.each do |p|
      w[p].each do |d|
        unless r.include?(d)
          nq.append(d)
          r.add(d)
        end
      end
    end
    q, nq = nq, q
    nq.clear
    k -= 1
  end
  puts r.sum
end
