N, A, B = gets.chomp.split.map(&:to_i)

def sum(n)
  (1+n)*n/2
end

lcm = A.lcm(B)

puts sum(N) - sum(N/A)*A - sum(N/B)*B + sum(N/lcm)*lcm
