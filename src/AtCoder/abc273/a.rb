N = gets.to_i

def f(n)
  return 1 if n.zero?
  return n * f(n-1)
end

puts f(N)
